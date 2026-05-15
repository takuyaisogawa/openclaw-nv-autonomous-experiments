#!/usr/bin/env python3
"""Sequential measurement batch runner with explicit retry / stop / resume rules."""

from __future__ import annotations

import argparse
import copy
import fcntl
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_ROOT = Path(__file__).resolve().parent
if str(SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPT_ROOT))

try:
    from tools_mat_parse import (
        export_savedexperiment_mat_raw_files,
        materialize_savedexperiment_mat_raw_artifacts,
    )
except Exception:
    export_savedexperiment_mat_raw_files = None
    materialize_savedexperiment_mat_raw_artifacts = None

try:
    from design_nv_sequence import materialize_sequence_spec as materialize_staging_sequence_spec
except Exception:
    materialize_staging_sequence_spec = None

try:
    from nv_bridge_runtime_watch import probe_job as probe_runtime_job, wait_for_result as wait_for_runtime_result
except Exception:
    probe_runtime_job = None
    wait_for_runtime_result = None

from project_schema import (
    PROJECT_BRANCH_KEYS,
    PROJECT_BRANCH_RULE_EVENTS,
    PROJECT_BRANCH_RULE_WHEN_BOOL_KEYS,
    PROJECT_BRANCH_RULE_WHEN_LIST_KEYS,
    RUNTIME_ITEM_OVERRIDE_ALLOWED_KEYS,
    SEQUENCE_AUTHORING_DICT_KEYS,
    SEQUENCE_AUTHORING_LIST_KEYS,
    SEQUENCE_AUTHORING_STRING_KEYS,
    SUPPORTED_PLAN_ITEM_KEYS,
    item_identity_hint,
    normalize_batch_mode,
    normalize_item_spec,
    normalize_override_spec,
    normalize_sequence_authoring_spec,
    select_project_branch_items as select_project_branch_items_for_context,
    summarize_project_branches,
    summarize_sequence_authoring,
)
from submit_spec_utils import build_submit_spec_from_batch_item


WORKSPACE_ROOT = Path("<OPENCLAW_WORKSPACE>")
DEFAULT_BATCH_ROOT = WORKSPACE_ROOT / ".openclaw" / "batches"
DEFAULT_CONFIG_PATH = Path("<OPENCLAW_CONFIG>")
DEFAULT_GATEWAY_URL = "http://127.0.0.1:18789"
DEFAULT_AUX_STATE_PATH = WORKSPACE_ROOT / ".openclaw" / "nv_aux_state.json"
DEFAULT_RECOVERY_ROOT = WORKSPACE_ROOT / ".openclaw" / "recovery"
DEFAULT_RECOVERY_CASE_LIBRARY_ROOT = WORKSPACE_ROOT / ".openclaw" / "recovery_case_library"
DEFAULT_RECOVERY_HOOK_PATH = "/hooks/nv-recovery"
DEFAULT_RECOVERY_PLAN_TIMEOUT_SECONDS = 600.0
DEFAULT_MEASUREMENT_PLAN_ROOT = WORKSPACE_ROOT / ".openclaw" / "measurement_plan"
DEFAULT_MEASUREMENT_PLAN_HOOK_PATH = "/hooks/nv-measurement-plan"
DEFAULT_MEASUREMENT_PLAN_TIMEOUT_SECONDS = 45.0
DEFAULT_DAYTIME_MAX_UNTRACKED_WINDOW_SECONDS = 600
DEFAULT_NIGHTTIME_MAX_UNTRACKED_WINDOW_SECONDS = 900
DEFAULT_DAYTIME_START_HOUR_LOCAL = 9
DEFAULT_NIGHTTIME_START_HOUR_LOCAL = 21
DEFAULT_CALIBRATION_TOTAL_SHOTS_MIN = 200_000
DEFAULT_CALIBRATION_TOTAL_SHOTS_MAX = 300_000
DEFAULT_PUBLICATION_QUALITY_MIN_TOTAL_SHOTS = 1_500_000
DEFAULT_PUBLICATION_QUALITY_TARGET_SEM_NORMALIZED_SIGNAL = 0.05
DEFAULT_ANALYSIS_REVIEW_ROOT = WORKSPACE_ROOT / ".openclaw" / "analysis_review"
DEFAULT_ANALYSIS_REVIEW_HOOK_PATH = "/hooks/nv-analysis-review"
DEFAULT_ANALYSIS_PLAN_TIMEOUT_SECONDS = 600.0
DEFAULT_CASE_LIBRARY_MATCH_LIMIT = 5
STOPPED_EXIT_CODE = 3
DEFAULT_MAX_ATTEMPTS_PER_ITEM = 3
MAX_ANALYSIS_REVIEW_ROUNDS = 3
VALID_ANALYSIS_FIT_KINDS = {"None"}
DEFAULT_REFERENCE_DATA_ROOT = Path("<MATLAB_23C_ROOT>")
DEFAULT_CUSTOM_ANALYSIS_ROOT = DEFAULT_REFERENCE_DATA_ROOT / "claw" / "custom_fits"


def current_tracking_cadence_policy(now: datetime | None = None) -> dict[str, Any]:
    current = now or datetime.now()
    current_hour = current.hour + current.minute / 60.0 + current.second / 3600.0
    is_daytime = DEFAULT_DAYTIME_START_HOUR_LOCAL <= current_hour < DEFAULT_NIGHTTIME_START_HOUR_LOCAL
    effective_seconds = (
        DEFAULT_DAYTIME_MAX_UNTRACKED_WINDOW_SECONDS
        if is_daytime
        else DEFAULT_NIGHTTIME_MAX_UNTRACKED_WINDOW_SECONDS
    )
    return {
        "timezone": "local system time",
        "daytime_start_hour_local": DEFAULT_DAYTIME_START_HOUR_LOCAL,
        "nighttime_start_hour_local": DEFAULT_NIGHTTIME_START_HOUR_LOCAL,
        "daytime_max_untracked_window_seconds": DEFAULT_DAYTIME_MAX_UNTRACKED_WINDOW_SECONDS,
        "nighttime_max_untracked_window_seconds": DEFAULT_NIGHTTIME_MAX_UNTRACKED_WINDOW_SECONDS,
        "effective_period": "daytime" if is_daytime else "nighttime",
        "effective_max_untracked_window_seconds": effective_seconds,
        "applies_to": "pre_enqueue_advisory drift_planning_window_seconds / per_average_seconds",
        "does_not_change": "Imaging GUI or legacy Experiment tracking_period defaults",
    }


def default_shot_budget_policy() -> dict[str, Any]:
    return {
        "calibration_total_shots_range": [
            DEFAULT_CALIBRATION_TOTAL_SHOTS_MIN,
            DEFAULT_CALIBRATION_TOTAL_SHOTS_MAX,
        ],
        "calibration_acceptable_total_shots_description": "2e5-3e5 total shots is usually sufficient for calibration, scout, resonance, and pulse checks in this NV system.",
        "publication_quality_min_total_shots": DEFAULT_PUBLICATION_QUALITY_MIN_TOTAL_SHOTS,
        "publication_quality_target_sem_normalized_signal": DEFAULT_PUBLICATION_QUALITY_TARGET_SEM_NORMALIZED_SIGNAL,
        "publication_quality_description": "For publication-level data targeting about 5% SEM on normalized 0..1 signal, plan at least 1.5e6 total shots.",
        "normalized_signal_range": [0, 1],
        "total_shots_definition": "averages * repetitions",
        "preserve_total_shots_before_reducing_quality": True,
        "if_drift_limited": "Prefer reducing repetitions per average and increasing averages, or splitting into shorter jobs, before reducing total shots.",
        "claim_boundary": "If a science run has fewer than 1.5e6 total shots, do not call it publication quality without explicit justification.",
        "measurement_intents": {
            "calibration_or_scout": "Usually 2e5-3e5 total shots is enough.",
            "publication_quality": "Requires at least 1.5e6 total shots for the ~5% SEM target.",
            "science_or_unknown": "Do not make publication-quality claims unless the run reaches the publication-quality shot budget.",
        },
    }


def infer_measurement_intent_for_shot_budget(
    item_spec: dict[str, Any],
    rendered_item: dict[str, Any],
    batch_spec: dict[str, Any],
) -> str:
    chunks: list[str] = []
    for source in (item_spec, rendered_item):
        if not isinstance(source, dict):
            continue
        for key in ("id", "sequence_manifest_id", "sequence_file", "sequence", "recipe"):
            chunks.append(str(source.get(key, "") or ""))
        metadata = source.get("metadata", {}) if isinstance(source.get("metadata", {}), dict) else {}
        for key in ("measurement_intent", "intent", "purpose", "quality_tier", "claim_level"):
            chunks.append(str(metadata.get(key, "") or ""))
        analysis = source.get("analysis", {}) if isinstance(source.get("analysis", {}), dict) else {}
        chunks.append(str(analysis.get("aux_key", "") or ""))
    chunks.append(str(batch_spec.get("natural_language_request", "") or ""))
    text = " ".join(chunks).lower()

    if any(token in text for token in ("publication", "publish", "final data", "publication_quality", "pub_quality")):
        return "publication_quality"
    if any(token in text for token in ("calibration", "calib", "odmr", "rabi", "pi_pulse", "resonance", "scout", "pilot", "preview")):
        return "calibration_or_scout"
    return "science_or_unknown"


def summarize_current_shot_budget(
    item_spec: dict[str, Any],
    rendered_item: dict[str, Any],
    batch_spec: dict[str, Any],
    pre_enqueue_advisory: dict[str, Any],
    shot_budget_policy: dict[str, Any],
) -> dict[str, Any]:
    candidates: list[dict[str, Any]] = []
    advisory_acquisition = pre_enqueue_advisory.get("acquisition", {}) if isinstance(pre_enqueue_advisory, dict) else {}
    if isinstance(advisory_acquisition, dict) and advisory_acquisition:
        candidates.append(copy.deepcopy(advisory_acquisition))
    for source in (rendered_item, item_spec):
        acquisition = source.get("acquisition", {}) if isinstance(source, dict) else {}
        if isinstance(acquisition, dict) and acquisition:
            candidates.append(copy.deepcopy(acquisition))

    acquisition: dict[str, Any] = {}
    total_shots: int | None = None
    for candidate in candidates:
        candidate_total = total_acquisition_count(candidate)
        if candidate_total is not None:
            acquisition = candidate
            total_shots = candidate_total
            break

    publication_min = normalize_positive_int(shot_budget_policy.get("publication_quality_min_total_shots"))
    calibration_range = shot_budget_policy.get("calibration_total_shots_range", [])
    intent = infer_measurement_intent_for_shot_budget(item_spec, rendered_item, batch_spec)
    summary = {
        "measurement_intent_inferred": intent,
        "acquisition": summarize_acquisition_for_recovery(acquisition),
        "total_shots": total_shots,
        "total_shots_definition": str(shot_budget_policy.get("total_shots_definition", "averages * repetitions") or ""),
        "calibration_total_shots_range": calibration_range,
        "publication_quality_min_total_shots": publication_min,
        "publication_quality_target_sem_normalized_signal": shot_budget_policy.get("publication_quality_target_sem_normalized_signal"),
        "meets_publication_quality_min_total_shots": (
            None if total_shots is None or publication_min is None else total_shots >= publication_min
        ),
    }
    if total_shots is not None and publication_min is not None and total_shots < publication_min:
        summary["publication_quality_claim_allowed_without_extra_justification"] = False
    return summary
DEFAULT_SAVED_EXPERIMENTS_ROOT = DEFAULT_REFERENCE_DATA_ROOT / "savedexperiments" / "NV1"
DEFAULT_SEQUENCE_CATALOG_PATH = WORKSPACE_ROOT / "nv_sequences.json"
DEFAULT_SEQUENCE_MANIFEST_ROOT = DEFAULT_REFERENCE_DATA_ROOT / "claw" / "sequence_manifests"
DEFAULT_SEQUENCE_AUTHORING_ROOT = WORKSPACE_ROOT / ".openclaw" / "sequence_authoring"
DEFAULT_NV_BRIDGE_ROOT = Path(os.environ.get("NV_BRIDGE_ROOT", "<NV_BRIDGE_ROOT>"))
DEFAULT_NV_USAGE_SUMMARY_PATH = Path("<NV_BRIDGE_ROOT>/status/recent_nv_usage_summary.json")
DEFAULT_NV_POSITION_REGISTRY_PATH = Path("<NV_BRIDGE_ROOT>/status/nv_position_registry.json")
DEFAULT_SAVED_EXPERIMENT_FAMILY_MATCH_LIMIT = 40
DEFAULT_SAVED_EXPERIMENT_MAT_SUMMARY_LIMIT = 6
DEFAULT_NV_USAGE_CLUSTER_LIMIT = 4
INTERNAL_MEASUREMENT_PLAN_ENV = "OPENCLAW_INTERNAL_MEASUREMENT_PLAN_SUBMIT"
SUBMISSION_PATH_ENV = "OPENCLAW_SUBMISSION_PATH"
SUBMISSION_LOCK_WAIT_SECONDS = 30.0
SUBMISSION_LOCK_POLL_SECONDS = 0.25
SAVED_EXPERIMENT_FILENAME_RE = re.compile(
    r"^(?P<prefix>.+?)-seq-(?P<sequence>.+?)-vary-(?P<vary>.+?)-(?P<date>\d{4}-\d{2}-\d{2})-(?P<clock>\d{6})\.mat$",
    re.IGNORECASE,
)
SEQUENCE_LOOKUP_KEY_RE = re.compile(r"[^a-z0-9]+")

_SEQUENCE_CATALOG_CACHE: dict[str, Any] | None = None
_SEQUENCE_MANIFEST_CACHE: dict[str, dict[str, Any]] = {}
SUPPORTED_DYNAMIC_ITEM_KEYS = SUPPORTED_PLAN_ITEM_KEYS
MAX_DYNAMIC_INSERT_ITEMS_PER_PLAN = 12

HARD_STOP_ERROR_CODES = {
    "NVBridge:RunControlStopRequested",
    "NVBridge:RunExperimentAborted",
}

DEFAULT_STOP_ERROR_CODES = {
    "INVALID_SEQUENCE_MANIFEST_ID",
    "SCAN_NOT_ALLOWED_BY_MANIFEST",
    "FLOAT_VAR_OUT_OF_RANGE",
    "MISSING_DATA_PATH",
    "INVALID_SCAN",
    "INVALID_FLOAT_VARS",
    "INVALID_LIMITS",
    "BOOTSTRAP_PRECHECK_FAILED",
    "MODE_NOT_ALLOWED_BY_MANIFEST",
    "NVBridge:ExecuteNotVerified",
    # RunExperimentAborted often means a human/agent/watchdog requested a
    # stop through bridge control. Do not blindly re-run the same hardware
    # execute; let the project agent choose a grounded recovery step.
    "NVBridge:RunControlStopRequested",
    "NVBridge:RunExperimentAborted",
    "AUX_RESOLUTION_FAILED",
    "QUEUE_ROOT_UNAVAILABLE",
    "SUBMISSION_LOCK_TIMEOUT",
    "SUBMISSION_LOCK_UNAVAILABLE",
}

DEFAULT_RETRY_ERROR_CODES = {
    "TIMEOUT",
    "NVBridge:AlignNVFailed",
    "NVBridge:RunExperimentFailed",
}

DEFAULT_STOP_ERROR_PREFIXES = (
    "INVALID_",
    "MISSING_",
    "SCAN_",
    "MATLAB:",
)

DEFAULT_RETRY_ERROR_PREFIXES: tuple[str, ...] = ()

DEFAULT_STOP_ERROR_MESSAGE_SUBSTRINGS = (
    "matlab:serial:fwrite:opfailed",
    "instrument object obj is an invalid object",
)

DEFAULT_RETRY_ERROR_MESSAGE_SUBSTRINGS: tuple[str, ...] = ()

RECOVERY_METADATA_HINT_KEYS = (
    "auto_align_nv",
    "minimum_final_kcps",
    "require_landmark_match",
    "allow_seed_fallback",
    "allow_fine_search_accept_without_tracking",
    "search_scan_xy_points",
    "search_scan_half_span_um",
    "search_scan_z_offsets_um",
    "search_scan_dwell_seconds",
    "search_scan_stale_hours",
    "search_scan_landmark_match_radius_um",
    "search_scan_minimum_landmark_matches",
    "search_scan_on_tracking_failure",
    "local_fine_search_before_tracking",
    "local_fine_search_xy_points",
    "local_fine_search_half_span_um",
    "local_fine_search_z_offsets_um",
    "local_fine_search_dwell_seconds",
    "local_fine_search_promote_xy",
    "tracking_z_seed_offsets_um",
    "reference_data",
    "reference_data_source",
    "reference_data_registry_path",
)


class QueueRootUnavailableError(RuntimeError):
    def __init__(self, path: Path, operation: str, error: BaseException) -> None:
        self.path = path
        self.operation = operation
        self.error = error
        super().__init__(f"Queue root unavailable while {operation} at {path}: {error}")


def read_json(path: Path) -> dict[str, Any]:
    raw_bytes = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-16", "utf-16-le", "utf-16-be", "latin-1"):
        try:
            return json.loads(raw_bytes.decode(encoding))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise ValueError(f"Could not decode JSON file: {path}")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sanitize_lock_token(value: Any) -> str:
    token = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(value or "").strip()).strip("._")
    return token or "item"


def normalize_signature_scalar(value: Any) -> Any:
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return format(float(value), ".12g")
    text = str(value or "").strip()
    return text


def normalize_signature_value(value: Any) -> Any:
    if isinstance(value, dict):
        normalized: dict[str, Any] = {}
        for key in sorted(value):
            normalized_value = normalize_signature_value(value.get(key))
            if normalized_value in (None, "", [], {}):
                continue
            normalized[str(key)] = normalized_value
        return normalized
    if isinstance(value, (list, tuple)):
        normalized_list = [normalize_signature_value(item) for item in value]
        return [item for item in normalized_list if item not in (None, "", [], {})]
    return normalize_signature_scalar(value)


def normalize_scan_signature(scan: Any) -> dict[str, Any]:
    payload = scan if isinstance(scan, dict) else {}

    def as_list(raw: Any) -> list[Any]:
        if isinstance(raw, list):
            return raw
        if raw in (None, ""):
            return []
        return [raw]

    return {
        "vary_prop": [str(item).strip() for item in as_list(payload.get("vary_prop")) if str(item).strip()],
        "begin": [normalize_signature_scalar(item) for item in as_list(payload.get("begin")) if item not in (None, "")],
        "end": [normalize_signature_scalar(item) for item in as_list(payload.get("end")) if item not in (None, "")],
        "points": [normalize_signature_scalar(item) for item in as_list(payload.get("points")) if item not in (None, "")],
    }


def normalize_job_acquisition_signature(job_or_spec: Any) -> dict[str, Any]:
    payload = job_or_spec if isinstance(job_or_spec, dict) else {}
    acquisition = payload.get("acquisition", {}) if isinstance(payload.get("acquisition", {}), dict) else {}
    metadata = payload.get("metadata", {}) if isinstance(payload.get("metadata", {}), dict) else {}
    metadata_acquisition = metadata.get("acquisition", {}) if isinstance(metadata.get("acquisition", {}), dict) else {}
    if metadata_acquisition:
        acquisition = metadata_acquisition
    return normalize_signature_value(acquisition)


def normalize_job_metadata_signature(metadata: Any) -> dict[str, Any]:
    payload = metadata if isinstance(metadata, dict) else {}
    tracking_offsets = payload.get("tracking_z_seed_offsets_um")
    if isinstance(tracking_offsets, list) and len(tracking_offsets) == 1:
        tracking_offsets = tracking_offsets[0]
    signature = {
        "project_id": payload.get("project_id", ""),
        "approval_path": payload.get("approval_path", ""),
        "intent": payload.get("intent", ""),
        "batch_id": payload.get("batch_id", ""),
        "batch_item_id": payload.get("batch_item_id", ""),
        "requested_by": payload.get("requested_by", ""),
        "submission_path": payload.get("submission_path", ""),
        "measurement_plan_verified": payload.get("measurement_plan_verified", None),
        "queue_execute_opt_in": payload.get("queue_execute_opt_in", None),
        "auto_align_nv": payload.get("auto_align_nv", None),
        "require_landmark_match": payload.get("require_landmark_match", None),
        "local_fine_search_before_tracking": payload.get("local_fine_search_before_tracking", None),
        "tracking_z_seed_offsets_um": tracking_offsets,
    }
    return normalize_signature_value(signature)


def build_submit_spec_signature(submit_spec: dict[str, Any], *, batch_id: str = "", item_id: str = "") -> dict[str, Any]:
    metadata = copy.deepcopy(submit_spec.get("metadata", {})) if isinstance(submit_spec.get("metadata", {}), dict) else {}
    if batch_id:
        metadata.setdefault("batch_id", batch_id)
    if item_id:
        metadata.setdefault("batch_item_id", item_id)
    if "requested_by" not in metadata and submit_spec.get("requested_by") is not None:
        metadata["requested_by"] = submit_spec.get("requested_by")
    if "submission_path" not in metadata and submit_spec.get("submission_path") is not None:
        metadata["submission_path"] = submit_spec.get("submission_path")
    if "measurement_plan_verified" not in metadata and submit_spec.get("measurement_plan_verified") is not None:
        metadata["measurement_plan_verified"] = submit_spec.get("measurement_plan_verified")

    return {
        "mode": normalize_signature_scalar(submit_spec.get("mode", "")),
        "recipe": normalize_signature_scalar(submit_spec.get("recipe", "")),
        "sample_id": normalize_signature_scalar(submit_spec.get("sample_id", "")),
        "sequence_manifest_id": normalize_signature_scalar(submit_spec.get("sequence_manifest_id", "")),
        "sequence_file": normalize_signature_scalar(submit_spec.get("sequence_file", "")),
        "scan": normalize_scan_signature(submit_spec.get("scan", {})),
        "float_vars": normalize_signature_value(submit_spec.get("float_vars", {})),
        "acquisition": normalize_job_acquisition_signature(submit_spec),
        "metadata": normalize_job_metadata_signature(metadata),
    }


def build_existing_job_signature(job: dict[str, Any]) -> dict[str, Any]:
    metadata = copy.deepcopy(job.get("metadata", {})) if isinstance(job.get("metadata", {}), dict) else {}
    return {
        "mode": normalize_signature_scalar(job.get("mode", "")),
        "recipe": normalize_signature_scalar(job.get("recipe", "")),
        "sample_id": normalize_signature_scalar(job.get("sample_id", "")),
        "sequence_manifest_id": normalize_signature_scalar(job.get("sequence_manifest_id", "")),
        "sequence_file": normalize_signature_scalar(job.get("sequence_file", "")),
        "scan": normalize_scan_signature(job.get("scan", {})),
        "float_vars": normalize_signature_value(job.get("float_vars", {})),
        "acquisition": normalize_job_acquisition_signature(job),
        "metadata": normalize_job_metadata_signature(metadata),
    }


def submit_spec_matches_existing_job(submit_spec: dict[str, Any], job: dict[str, Any], *, batch_id: str = "", item_id: str = "") -> bool:
    expected = build_submit_spec_signature(submit_spec, batch_id=batch_id, item_id=item_id)
    observed = build_existing_job_signature(job)
    expected_metadata = expected.get("metadata", {}) if isinstance(expected.get("metadata", {}), dict) else {}
    observed_metadata = observed.get("metadata", {}) if isinstance(observed.get("metadata", {}), dict) else {}

    expected_batch_id = str(expected_metadata.get("batch_id", "") or "")
    expected_batch_item_id = str(expected_metadata.get("batch_item_id", "") or "")
    observed_batch_id = str(observed_metadata.get("batch_id", "") or "")
    observed_batch_item_id = str(observed_metadata.get("batch_item_id", "") or "")
    if expected_batch_id and expected_batch_item_id and observed_batch_id and observed_batch_item_id:
        if expected_batch_id != observed_batch_id or expected_batch_item_id != observed_batch_item_id:
            return False

    for key in ("mode", "recipe", "sample_id", "sequence_manifest_id"):
        expected_value = expected.get(key)
        if expected_value not in (None, "") and expected_value != observed.get(key):
            return False

    expected_sequence_file = expected.get("sequence_file")
    if expected_sequence_file not in (None, "") and expected_sequence_file != observed.get("sequence_file"):
        return False

    if expected.get("scan", {}) != observed.get("scan", {}):
        return False
    if expected.get("acquisition", {}) != observed.get("acquisition", {}):
        return False

    expected_float_vars = expected.get("float_vars", {}) if isinstance(expected.get("float_vars", {}), dict) else {}
    observed_float_vars = observed.get("float_vars", {}) if isinstance(observed.get("float_vars", {}), dict) else {}
    for key, value in expected_float_vars.items():
        if observed_float_vars.get(key) != value:
            return False

    for key, value in expected_metadata.items():
        if key in {"batch_id", "batch_item_id"} and not observed_metadata.get(key):
            continue
        if observed_metadata.get(key) != value:
            return False

    return True


def default_nv_bridge_root() -> Path:
    env_root = str(os.environ.get("NV_BRIDGE_ROOT", "") or "").strip()
    return Path(env_root).expanduser() if env_root else DEFAULT_NV_BRIDGE_ROOT


def infer_queue_root_for_item(item_state: dict[str, Any]) -> Path:
    for history_entry in reversed(item_state.get("history", [])):
        queue_root = infer_queue_root_from_history_entry(history_entry)
        if queue_root is not None:
            return queue_root
    return default_nv_bridge_root()


def submission_lock_path(state_path: Path, item_id: str) -> Path:
    token = sanitize_lock_token(item_id)
    return state_path.parent / f"{state_path.stem}__{token}.submit.lock"


def acquire_submission_lock(lock_path: Path, *, timeout_seconds: float) -> Any:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+", encoding="utf-8")
    deadline = time.monotonic() + max(float(timeout_seconds), 0.0)
    while True:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            return handle
        except BlockingIOError:
            if time.monotonic() >= deadline:
                handle.close()
                raise TimeoutError(f"Timed out waiting for submission lock: {lock_path}")
            time.sleep(SUBMISSION_LOCK_POLL_SECONDS)


def write_submission_lock_metadata(handle: Any, payload: dict[str, Any]) -> None:
    handle.seek(0)
    handle.truncate()
    handle.write(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    handle.flush()


def find_equivalent_inflight_job(queue_root: Path, submit_spec: dict[str, Any], *, batch_id: str = "", item_id: str = "") -> dict[str, Any]:
    matches: list[dict[str, Any]] = []
    for state_name, rank in (("done", 0), ("running", 1), ("queued", 2)):
        state_root = queue_root / state_name
        if not guarded_is_dir(state_root, operation=f"checking {state_name} queue directory"):
            continue
        for job_dir in guarded_iterdir(state_root, operation=f"listing {state_name} queue directory"):
            if not guarded_is_dir(job_dir, operation=f"checking {state_name} job directory"):
                continue
            job_path = job_dir / "job.json"
            job = read_json_dict_if_exists_guarded(job_path, operation=f"reading {state_name} job payload")
            if not job:
                continue
            if not submit_spec_matches_existing_job(submit_spec, job, batch_id=batch_id, item_id=item_id):
                continue
            result_path = job_dir / "result.json"
            result_payload: dict[str, Any] = {}
            if state_name == "done":
                result_payload = read_json_dict_if_exists_guarded(result_path, operation="reading completed job result")
                if str(result_payload.get("status", "") or "") != "completed":
                    continue
            status_path = job_dir / "status.json"
            status_payload = read_json_dict_if_exists_guarded(status_path, operation=f"reading {state_name} job status")
            started_at = str(status_payload.get("started_at", "") or "")
            matches.append(
                {
                    "state": state_name,
                    "state_rank": rank,
                    "job_id": str(job.get("job_id", job_dir.name) or job_dir.name),
                    "job": job,
                    "job_dir": str(job_dir),
                    "job_path": str(job_path),
                    "status_path": str(status_path) if guarded_is_file(status_path, operation=f"checking {state_name} status path") else "",
                    "result_path": str(result_path) if state_name == "done" else "",
                    "result": copy.deepcopy(result_payload),
                    "started_at": started_at,
                    "queue_root": str(queue_root),
                }
            )
    if not matches:
        return {}
    matches.sort(key=lambda entry: (int(entry.get("state_rank", 9)), str(entry.get("started_at", "") or "~"), str(entry.get("job_id", "") or "~")))
    return matches[0]


def wait_for_existing_job_attachment(match: dict[str, Any], args: argparse.Namespace, submit_spec: dict[str, Any]) -> dict[str, Any]:
    queue_root = Path(str(match.get("queue_root", "") or default_nv_bridge_root()))
    job_id = str(match.get("job_id", "") or "")
    job = copy.deepcopy(match.get("job", {})) if isinstance(match.get("job", {}), dict) else {}
    cached_result = copy.deepcopy(match.get("result", {})) if isinstance(match.get("result", {}), dict) else {}
    if str(match.get("state", "") or "") == "done" and str(cached_result.get("status", "") or "") == "completed":
        result_path = str(match.get("result_path", "") or "")
        wait_response = {
            "timed_out": False,
            "final_state": "done",
            "job_dir": str(match.get("job_dir", "") or ""),
            "result_path": result_path,
            "result": cached_result,
            "outcome_summary": summarize_result_for_recovery(cached_result),
            "elapsed_seconds": 0.0,
            "error_code": str(cached_result.get("error_code", "") or ""),
            "error_message": str(cached_result.get("error_message", "") or ""),
            "runtime_watch": {},
        }
    else:
        if not callable(wait_for_runtime_result):
            raise RuntimeError("nv_bridge_runtime_watch.wait_for_result is unavailable; cannot attach to existing job safely.")
        try:
            wait_response = wait_for_runtime_result(
                queue_root,
                job_id,
                float(args.timeout_seconds),
                float(args.poll_seconds),
                job=job,
                config={"requested_by": str((job.get("metadata", {}) if isinstance(job.get("metadata", {}), dict) else {}).get("requested_by", "") or "openclaw-batch-run")},
            )
        except OSError as exc:
            raise QueueRootUnavailableError(queue_root, f"waiting for existing job {job_id}", exc) from exc
    response = {
        "ok": True,
        "mode": str(submit_spec.get("mode", "") or ""),
        "job_id": job_id,
        "job_dir": str(match.get("job_dir", "") or ""),
        "job_path": str(match.get("job_path", "") or ""),
        "queue_root": str(queue_root),
        "wait_for_result": True,
        "submit_spec": copy.deepcopy(submit_spec),
        "job": job,
        "submission_path": str(submit_spec.get("submission_path", "") or ""),
        "measurement_plan_verified": bool(submit_spec.get("measurement_plan_verified", False)),
        "attached_existing": {
            "job_id": job_id,
            "state": str(match.get("state", "") or ""),
            "job_path": str(match.get("job_path", "") or ""),
        },
    }
    response.update(wait_response if isinstance(wait_response, dict) else {})
    return response


def merge_enqueue_wait_response(initial_response: dict[str, Any], wait_response: dict[str, Any]) -> dict[str, Any]:
    response = copy.deepcopy(initial_response) if isinstance(initial_response, dict) else {}
    if isinstance(wait_response, dict):
        response.update(wait_response)
    return response


def submission_guard_failure_response(
    *,
    action: str,
    error_code: str,
    error_message: str,
    requested_mode: str,
    queue_root: Path,
    lock_path: Path,
    submit_spec: dict[str, Any],
    batch_id: str,
    item_id: str,
    stderr: str = "",
) -> tuple[int, dict[str, Any], str, str, dict[str, Any]]:
    guard = {
        "action": action,
        "lock_path": str(lock_path),
        "queue_root": str(queue_root),
        "error_code": error_code,
        "error_message": error_message,
        "submit_spec_signature": build_submit_spec_signature(submit_spec, batch_id=batch_id, item_id=item_id),
    }
    response = {
        "ok": False,
        "mode": requested_mode,
        "queue_root": str(queue_root),
        "error_code": error_code,
        "error_message": error_message,
        "submission_guard": copy.deepcopy(guard),
    }
    stdout = json.dumps(
        {
            "ok": False,
            "error_code": error_code,
            "error_message": error_message,
            "submission_guard": guard,
        },
        ensure_ascii=False,
    )
    return 2, response, stdout, stderr or error_message, guard


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def truncate_text(value: Any, max_chars: int = 4000) -> str:
    text = str(value or "").strip()
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 15].rstrip() + " ...[truncated]"


def normalize_path_for_agent(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    if len(text) >= 3 and text[1:3] in (":\\", ":/"):
        drive = text[0].lower()
        rest = text[2:].replace("\\", "/").lstrip("/")
        return f"/mnt/{drive}/{rest}"
    return text


def resolve_sequence_path(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    normalized = normalize_path_for_agent(text)
    path = Path(normalized)
    if path.is_absolute():
        return normalized
    relative_text = normalized.replace("\\", "/").lstrip("/")
    candidate = (DEFAULT_REFERENCE_DATA_ROOT / relative_text).resolve(strict=False)
    return str(candidate)


def normalize_sequence_lookup_key(value: Any) -> str:
    return SEQUENCE_LOOKUP_KEY_RE.sub("_", str(value or "").strip().lower()).strip("_")


def read_json_dict_if_exists(path: Path) -> dict[str, Any]:
    try:
        if not path.is_file():
            return {}
        raw = path.read_text(encoding="utf-8")
    except OSError:
        return {}
    if raw.startswith("\ufeff"):
        raw = raw[1:]
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def guarded_is_dir(path: Path, *, operation: str) -> bool:
    try:
        return path.is_dir()
    except OSError as exc:
        raise QueueRootUnavailableError(path, operation, exc) from exc


def guarded_is_file(path: Path, *, operation: str) -> bool:
    try:
        return path.is_file()
    except OSError as exc:
        raise QueueRootUnavailableError(path, operation, exc) from exc


def guarded_iterdir(path: Path, *, operation: str) -> list[Path]:
    try:
        return sorted(path.iterdir())
    except OSError as exc:
        raise QueueRootUnavailableError(path, operation, exc) from exc


def read_json_dict_if_exists_guarded(path: Path, *, operation: str) -> dict[str, Any]:
    try:
        if not path.is_file():
            return {}
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise QueueRootUnavailableError(path, operation, exc) from exc
    if raw.startswith("\ufeff"):
        raw = raw[1:]
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def load_sequence_catalog_entries() -> dict[str, Any]:
    global _SEQUENCE_CATALOG_CACHE
    if _SEQUENCE_CATALOG_CACHE is not None:
        return _SEQUENCE_CATALOG_CACHE
    payload = read_json_dict_if_exists(DEFAULT_SEQUENCE_CATALOG_PATH)
    sequences = payload.get("sequences", {})
    _SEQUENCE_CATALOG_CACHE = sequences if isinstance(sequences, dict) else {}
    return _SEQUENCE_CATALOG_CACHE


def lookup_sequence_catalog_entry(sequence_name: Any) -> dict[str, Any]:
    lookup_key = normalize_sequence_lookup_key(sequence_name)
    if not lookup_key:
        return {}
    for name, entry in load_sequence_catalog_entries().items():
        if not isinstance(entry, dict):
            continue
        if normalize_sequence_lookup_key(name) == lookup_key:
            return entry
        aliases = entry.get("aliases", [])
        if isinstance(aliases, list) and any(normalize_sequence_lookup_key(alias) == lookup_key for alias in aliases):
            return entry
    return {}


def load_sequence_manifest_entry(manifest_id: Any) -> dict[str, Any]:
    manifest_key = str(manifest_id or "").strip()
    if not manifest_key:
        return {}
    cached = _SEQUENCE_MANIFEST_CACHE.get(manifest_key)
    if cached is not None:
        return cached
    file_name = manifest_key if manifest_key.endswith(".json") else f"{manifest_key}.json"
    for candidate in (
        DEFAULT_SEQUENCE_MANIFEST_ROOT / "validated" / file_name,
        DEFAULT_SEQUENCE_MANIFEST_ROOT / "staging" / file_name,
    ):
        payload = read_json_dict_if_exists(candidate)
        if payload:
            _SEQUENCE_MANIFEST_CACHE[manifest_key] = payload
            return payload
    _SEQUENCE_MANIFEST_CACHE[manifest_key] = {}
    return {}


def list_available_sequences_for_agent() -> list[dict[str, Any]]:
    sequences = load_sequence_catalog_entries()
    summarized: list[dict[str, Any]] = []
    for name in sorted(sequences):
        entry = sequences.get(name, {})
        if not isinstance(entry, dict):
            continue
        summarized.append(
            {
                "name": name,
                "enabled": bool(entry.get("enabled", True)),
                "aliases": copy.deepcopy(entry.get("aliases", [])) if isinstance(entry.get("aliases", []), list) else [],
                "description": str(entry.get("description", "") or ""),
                "sequence_manifest_id": str(entry.get("sequence_manifest_id", "") or ""),
                "default_scan": copy.deepcopy(entry.get("scan", {})) if isinstance(entry.get("scan", {}), dict) else {},
                "metadata_defaults": copy.deepcopy(entry.get("metadata_defaults", {})) if isinstance(entry.get("metadata_defaults", {}), dict) else {},
            }
        )
    return summarized


def list_available_sequence_manifests_for_agent() -> list[dict[str, Any]]:
    manifests: list[dict[str, Any]] = []
    for source in ("validated", "staging"):
        root = DEFAULT_SEQUENCE_MANIFEST_ROOT / source
        if not root.is_dir():
            continue
        for path in sorted(root.glob("*.json")):
            payload = read_json_dict_if_exists(path)
            if not payload:
                continue
            manifests.append(
                {
                    "id": str(payload.get("id", path.stem) or path.stem),
                    "source": source,
                    "sample_id": str(payload.get("sample_id", "") or ""),
                    "allowed_modes": copy.deepcopy(payload.get("allowed_modes", [])) if isinstance(payload.get("allowed_modes", []), list) else [],
                    "sequence_file": str(payload.get("sequence_file", "") or ""),
                    "catalog_key": str(payload.get("catalog_key", "") or ""),
                    "description": str(payload.get("description", "") or ""),
                }
            )
    return manifests


def summarize_sequence_authoring_for_agent(item_spec: dict[str, Any]) -> dict[str, Any]:
    return summarize_sequence_authoring(item_spec)


def summarize_project_branches_for_agent(item_spec: dict[str, Any]) -> dict[str, Any]:
    return summarize_project_branches(item_spec)


def build_sequence_authoring_contract() -> dict[str, Any]:
    return {
        "supported": materialize_staging_sequence_spec is not None,
        "supported_item_field": "sequence_authoring",
        "supported_keys": sorted(SEQUENCE_AUTHORING_STRING_KEYS | SEQUENCE_AUTHORING_DICT_KEYS | SEQUENCE_AUTHORING_LIST_KEYS),
        "available_base_manifests": list_available_sequence_manifests_for_agent(),
        "default_runtime_manifest_overrides": {
            "allowed_modes": ["validate", "dry_run", "execute"],
            "requires": {},
        },
    }


def build_dynamic_item_contract(batch_spec: dict[str, Any], default_mode: str, default_sample_id: str) -> dict[str, Any]:
    return {
        "default_mode": str(default_mode or batch_spec.get("mode", "") or ""),
        "default_sample_id": str(default_sample_id or batch_spec.get("requested_sample_id", "") or ""),
        "supported_item_keys": copy.deepcopy(SUPPORTED_DYNAMIC_ITEM_KEYS),
        "available_sequences": list_available_sequences_for_agent(),
        "available_sequence_manifests": list_available_sequence_manifests_for_agent(),
        "project_branch_support": {
            "legacy_keys": list(PROJECT_BRANCH_KEYS),
            "rule_events": list(PROJECT_BRANCH_RULE_EVENTS),
            "rule_condition_keys": sorted(PROJECT_BRANCH_RULE_WHEN_LIST_KEYS | PROJECT_BRANCH_RULE_WHEN_BOOL_KEYS),
        },
        "sequence_authoring_support": build_sequence_authoring_contract(),
        "max_items_per_plan": MAX_DYNAMIC_INSERT_ITEMS_PER_PLAN,
        "preferred_sequence_field": "sequence_manifest_id",
    }


def resolve_item_sequence_context(item_spec: dict[str, Any]) -> dict[str, str]:
    item = item_spec if isinstance(item_spec, dict) else {}
    sequence = str(item.get("sequence", "") or "").strip()
    sequence_manifest_id = str(item.get("sequence_manifest_id", "") or "").strip()
    raw_sequence_file = str(item.get("sequence_file", "") or item.get("sequence_path", "") or "").strip()
    generated_sequence = item.get("generated_sequence", {}) if isinstance(item.get("generated_sequence"), dict) else {}
    if not sequence_manifest_id:
        sequence_manifest_id = str(((item.get("sequence_authoring") or {}) if isinstance(item.get("sequence_authoring"), dict) else {}).get("new_id", "") or "").strip()
    if not raw_sequence_file and isinstance(generated_sequence, dict):
        raw_sequence_file = str(generated_sequence.get("sequence_path", "") or "").strip()
    catalog_entry = lookup_sequence_catalog_entry(sequence)
    if not sequence_manifest_id and catalog_entry:
        sequence_manifest_id = str(catalog_entry.get("sequence_manifest_id", "") or "").strip()
    if not raw_sequence_file and catalog_entry:
        raw_sequence_file = str(catalog_entry.get("sequence_file", "") or "").strip()
    manifest_entry = load_sequence_manifest_entry(sequence_manifest_id)
    if not raw_sequence_file and manifest_entry:
        raw_sequence_file = str(manifest_entry.get("sequence_file", "") or "").strip()
    return {
        "sequence": sequence,
        "sequence_manifest_id": sequence_manifest_id,
        "sequence_file": normalize_path_for_agent(raw_sequence_file),
        "sequence_path": resolve_sequence_path(raw_sequence_file),
    }


def summarize_axis(values: Any) -> Any:
    if isinstance(values, (list, tuple)) and values and all(isinstance(v, (int, float)) for v in values):
        return {
            "start": float(values[0]),
            "end": float(values[-1]),
            "count": len(values),
        }
    return copy.deepcopy(values)


def summarize_metadata_for_recovery(metadata: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(metadata, dict):
        return {}
    summary: dict[str, Any] = {}
    for key in RECOVERY_METADATA_HINT_KEYS:
        if key in metadata:
            summary[key] = copy.deepcopy(metadata[key])
    return summary


def summarize_scan_for_recovery(scan: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(scan, dict):
        return {}
    summary: dict[str, Any] = {}
    for key in ("vary_prop", "begin", "end", "points"):
        if key in scan:
            summary[key] = copy.deepcopy(scan[key])
    return summary


def summarize_acquisition_for_recovery(acquisition: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(acquisition, dict):
        return {}
    summary: dict[str, Any] = {}
    for key in ("average_continuously", "averages", "repetitions"):
        if key in acquisition:
            summary[key] = copy.deepcopy(acquisition[key])
    return summary


def normalize_positive_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value if value > 0 else None
    if isinstance(value, float):
        if not value.is_integer():
            return None
        normalized = int(value)
        return normalized if normalized > 0 else None
    text = str(value or "").strip()
    if not text:
        return None
    try:
        if any(token in text.lower() for token in (".", "e")):
            numeric = float(text)
            if not numeric.is_integer():
                return None
            normalized = int(numeric)
        else:
            normalized = int(text)
    except (TypeError, ValueError):
        return None
    return normalized if normalized > 0 else None


def format_acquisition_count(acquisition: dict[str, Any]) -> str:
    if not isinstance(acquisition, dict):
        return "unknown acquisition"
    averages = normalize_positive_int(acquisition.get("averages"))
    repetitions = normalize_positive_int(acquisition.get("repetitions"))
    if averages is None or repetitions is None:
        return json.dumps(summarize_acquisition_for_recovery(acquisition), ensure_ascii=False, sort_keys=True)
    return f"{averages} averages x {repetitions} repetitions"


def total_acquisition_count(acquisition: dict[str, Any]) -> int | None:
    if not isinstance(acquisition, dict):
        return None
    averages = normalize_positive_int(acquisition.get("averages"))
    repetitions = normalize_positive_int(acquisition.get("repetitions"))
    if averages is None or repetitions is None:
        return None
    return averages * repetitions


def summarize_analysis_for_recovery(analysis: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(analysis, dict):
        return {}
    summary: dict[str, Any] = {}
    for key in ("fit_kind", "aux_key", "aux_slot", "discard_first_average"):
        if key in analysis:
            summary[key] = copy.deepcopy(analysis[key])
    return summary


def compact_history_entry(entry: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(entry, dict):
        return {}
    summary: dict[str, Any] = {}
    for key in (
        "at",
        "event",
        "message",
        "job_id",
        "queue_root",
        "final_state",
        "result_path",
        "request_path",
        "plan_path",
        "hook_ok",
    ):
        if key in entry and entry.get(key) not in ("", None, []):
            summary[key] = copy.deepcopy(entry[key])
    retry_rule = entry.get("retry_rule", {})
    if isinstance(retry_rule, dict):
        summary["retry_rule"] = {
            "action": retry_rule.get("action", ""),
            "reason": retry_rule.get("reason", ""),
            "rule_source": retry_rule.get("rule_source", ""),
            "error_code": retry_rule.get("error_code", ""),
            "error_message": truncate_text(retry_rule.get("error_message", ""), 600),
        }
    plan = entry.get("plan", {})
    if isinstance(plan, dict) and plan:
        summary["plan"] = {
            "action": plan.get("action", ""),
            "reason": truncate_text(plan.get("reason", ""), 600),
            "operator_message": truncate_text(plan.get("operator_message", ""), 600),
        }
    raw_export = entry.get("savedexperiment_raw_export", {})
    if not isinstance(raw_export, dict) or not raw_export:
        runtime_watch = entry.get("runtime_watch", {})
        if isinstance(runtime_watch, dict):
            raw_export = runtime_watch.get("savedexperiment_raw_export", {})
    if isinstance(raw_export, dict) and raw_export:
        summary["savedexperiment_raw_export"] = copy.deepcopy(raw_export)
    return summary


def slugify_filename(value: Any, default: str = "case") -> str:
    text = str(value or "").strip().lower()
    if not text:
        return default
    chunks: list[str] = []
    last_was_sep = False
    for char in text:
        if char.isalnum():
            chunks.append(char)
            last_was_sep = False
            continue
        if not last_was_sep:
            chunks.append("-")
            last_was_sep = True
    slug = "".join(chunks).strip("-")
    return slug[:80] or default


def response_from_history_entry(entry: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(entry, dict):
        return {}
    payload: dict[str, Any] = {}
    stdout = str(entry.get("stdout", "") or "").strip()
    if stdout:
        try:
            decoded = json.loads(stdout)
            if isinstance(decoded, dict):
                payload = decoded
        except json.JSONDecodeError:
            payload = {}
    for key in ("job_id", "queue_root", "final_state", "result_path", "job_dir"):
        if key not in payload or payload.get(key) in ("", None):
            value = entry.get(key, "")
            if value not in ("", None):
                payload[key] = copy.deepcopy(value)
    if ("outcome_summary" not in payload or not isinstance(payload.get("outcome_summary"), dict)) and isinstance(entry.get("outcome_summary"), dict):
        payload["outcome_summary"] = copy.deepcopy(entry.get("outcome_summary", {}))
    if ("runtime_watch" not in payload or not isinstance(payload.get("runtime_watch"), dict)) and isinstance(entry.get("runtime_watch"), dict):
        payload["runtime_watch"] = copy.deepcopy(entry.get("runtime_watch", {}))
    if (
        "savedexperiment_raw_export" not in payload
        or not isinstance(payload.get("savedexperiment_raw_export"), dict)
        or not payload.get("savedexperiment_raw_export")
    ) and isinstance(entry.get("savedexperiment_raw_export"), dict):
        payload["savedexperiment_raw_export"] = copy.deepcopy(entry.get("savedexperiment_raw_export", {}))
    if not payload.get("job_dir") and payload.get("result_path"):
        try:
            payload["job_dir"] = str(Path(str(payload["result_path"])).parent)
        except Exception:
            pass
    return payload


def latest_history_event(item_state: dict[str, Any], *event_names: str) -> dict[str, Any]:
    wanted = {str(name or "").strip() for name in event_names if str(name or "").strip()}
    if not wanted:
        return {}
    history = item_state.get("history", []) if isinstance(item_state, dict) else []
    if not isinstance(history, list):
        return {}
    for entry in reversed(history):
        if isinstance(entry, dict) and str(entry.get("event", "") or "").strip() in wanted:
            return entry
    return {}


def latest_failed_queue_submit(item_state: dict[str, Any]) -> dict[str, Any]:
    history = item_state.get("history", []) if isinstance(item_state, dict) else []
    if not isinstance(history, list):
        return {}
    for entry in reversed(history):
        if not isinstance(entry, dict) or str(entry.get("event", "") or "").strip() != "queue_submit":
            continue
        retry_rule = entry.get("retry_rule", {})
        action = str(retry_rule.get("action", "") or "").strip().lower() if isinstance(retry_rule, dict) else ""
        if action and action != "complete":
            return entry
        if str(entry.get("final_state", "") or "").strip().lower() == "failed":
            return entry
    return {}


def summarize_landmark_match_for_recovery(landmark: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(landmark, dict):
        return {}
    summary = {
        "ok": bool(landmark.get("ok", False)),
        "matched_count": landmark.get("matched_count", []),
        "mean_residual_um": landmark.get("mean_residual_um", []),
        "match_radius_um": landmark.get("match_radius_um", []),
        "minimum_matches": landmark.get("minimum_matches", []),
        "refined_position": copy.deepcopy(landmark.get("refined_position", [])),
        "warnings": copy.deepcopy((landmark.get("warnings") or [])[:8]),
        "notes": copy.deepcopy((landmark.get("notes") or [])[:8]),
        "blockers": copy.deepcopy((landmark.get("blockers") or [])[:8]),
    }
    current_detection = landmark.get("current_detection", {})
    if isinstance(current_detection, dict) and current_detection:
        summary["current_detection"] = {
            "ok": bool(current_detection.get("ok", False)),
            "image_datetime": current_detection.get("image_datetime", ""),
            "range_x": summarize_axis(current_detection.get("range_x", [])),
            "range_y": summarize_axis(current_detection.get("range_y", [])),
            "range_z": summarize_axis(current_detection.get("range_z", [])),
            "detected_landmarks_count": len(current_detection.get("landmarks_xy", []) or []),
            "warnings": copy.deepcopy((current_detection.get("warnings") or [])[:6]),
            "notes": copy.deepcopy((current_detection.get("notes") or [])[:6]),
            "blockers": copy.deepcopy((current_detection.get("blockers") or [])[:6]),
        }
    current_scan_artifacts = landmark.get("current_scan_artifacts", {})
    if isinstance(current_scan_artifacts, dict) and current_scan_artifacts:
        summary["current_scan_artifacts"] = {
            "ok": bool(current_scan_artifacts.get("ok", False)),
            "mat_path": normalize_path_for_agent(current_scan_artifacts.get("mat_path", "")),
            "preview_png_path": normalize_path_for_agent(current_scan_artifacts.get("preview_png_path", "")),
            "downsampled_png_path": normalize_path_for_agent(current_scan_artifacts.get("downsampled_png_path", "")),
            "selected_slice_index": current_scan_artifacts.get("selected_slice_index", []),
            "selected_slice_count": current_scan_artifacts.get("selected_slice_count", []),
            "image_size": copy.deepcopy(current_scan_artifacts.get("image_size", [])),
            "warnings": copy.deepcopy((current_scan_artifacts.get("warnings") or [])[:6]),
        }
    return summary


def summarize_search_scan_for_recovery(search_scan: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(search_scan, dict):
        return {}
    summary = {
        "requested": bool(search_scan.get("requested", False)),
        "ran": bool(search_scan.get("ran", False)),
        "ok": bool(search_scan.get("ok", False)),
        "source": search_scan.get("source", ""),
        "trigger_reason": search_scan.get("trigger_reason", ""),
        "points": copy.deepcopy(search_scan.get("points", [])),
        "dwell_seconds": search_scan.get("dwell_seconds", []),
        "seed_position": copy.deepcopy(search_scan.get("seed_position", [])),
        "range_x": summarize_axis(search_scan.get("range_x", [])),
        "range_y": summarize_axis(search_scan.get("range_y", [])),
        "range_z": summarize_axis(search_scan.get("range_z", [])),
        "warnings": copy.deepcopy((search_scan.get("warnings") or [])[:8]),
        "notes": copy.deepcopy((search_scan.get("notes") or [])[:8]),
        "blockers": copy.deepcopy((search_scan.get("blockers") or [])[:8]),
    }
    landmark_match = search_scan.get("landmark_match", {})
    if isinstance(landmark_match, dict) and landmark_match:
        summary["landmark_match"] = summarize_landmark_match_for_recovery(landmark_match)
    artifacts = search_scan.get("artifacts", {})
    if isinstance(artifacts, dict) and artifacts:
        summary["artifacts"] = {
            "ok": bool(artifacts.get("ok", False)),
            "mat_path": normalize_path_for_agent(artifacts.get("mat_path", "")),
            "preview_png_path": normalize_path_for_agent(artifacts.get("preview_png_path", "")),
            "downsampled_png_path": normalize_path_for_agent(artifacts.get("downsampled_png_path", "")),
            "selected_slice_index": artifacts.get("selected_slice_index", []),
            "selected_slice_count": artifacts.get("selected_slice_count", []),
            "image_size": copy.deepcopy(artifacts.get("image_size", [])),
            "warnings": copy.deepcopy((artifacts.get("warnings") or [])[:6]),
        }
    return summary


def summarize_local_fine_search_for_recovery(fine_search: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(fine_search, dict):
        return {}
    summary = {
        "requested": bool(fine_search.get("requested", False)),
        "ran": bool(fine_search.get("ran", False)),
        "ok": bool(fine_search.get("ok", False)),
        "seed_position": copy.deepcopy(fine_search.get("seed_position", [])),
        "applied_seed_position": copy.deepcopy(fine_search.get("applied_seed_position", [])),
        "brightest_position": copy.deepcopy(fine_search.get("brightest_position", [])),
        "brightest_value": fine_search.get("brightest_value", []),
        "selected_slice_index": fine_search.get("selected_slice_index", []),
        "selected_slice_count": fine_search.get("selected_slice_count", []),
        "accepted_without_tracking": bool(fine_search.get("accepted_without_tracking", False)),
        "fallback_reason": fine_search.get("fallback_reason", ""),
        "points": copy.deepcopy(fine_search.get("points", [])),
        "dwell_seconds": fine_search.get("dwell_seconds", []),
        "range_x": summarize_axis(fine_search.get("range_x", [])),
        "range_y": summarize_axis(fine_search.get("range_y", [])),
        "range_z": summarize_axis(fine_search.get("range_z", [])),
        "warnings": copy.deepcopy((fine_search.get("warnings") or [])[:8]),
        "notes": copy.deepcopy((fine_search.get("notes") or [])[:8]),
        "blockers": copy.deepcopy((fine_search.get("blockers") or [])[:8]),
    }
    artifacts = fine_search.get("artifacts", {})
    if isinstance(artifacts, dict) and artifacts:
        summary["artifacts"] = {
            "ok": bool(artifacts.get("ok", False)),
            "mat_path": normalize_path_for_agent(artifacts.get("mat_path", "")),
            "preview_png_path": normalize_path_for_agent(artifacts.get("preview_png_path", "")),
            "downsampled_png_path": normalize_path_for_agent(artifacts.get("downsampled_png_path", "")),
            "selected_slice_index": artifacts.get("selected_slice_index", []),
            "selected_slice_count": artifacts.get("selected_slice_count", []),
            "image_size": copy.deepcopy(artifacts.get("image_size", [])),
            "warnings": copy.deepcopy((artifacts.get("warnings") or [])[:6]),
        }
    return summary


def summarize_z_tracking_attempts_for_recovery(attempts: Any) -> list[dict[str, Any]]:
    if not isinstance(attempts, list):
        return []
    summary: list[dict[str, Any]] = []
    for attempt in attempts[:8]:
        if not isinstance(attempt, dict):
            continue
        summary.append(
            {
                "ok": bool(attempt.get("ok", False)),
                "requested_seed_position": copy.deepcopy(attempt.get("requested_seed_position", [])),
                "tracked_position": copy.deepcopy(attempt.get("tracked_position", [])),
                "final_counts_text": attempt.get("final_counts_text", ""),
                "final_counts_kcps": attempt.get("final_counts_kcps", []),
                "tracker_aborted": bool(attempt.get("tracker_aborted", False)),
                "blockers": copy.deepcopy((attempt.get("blockers") or [])[:6]),
            }
        )
    return summary


def summarize_align_nv_for_recovery(align_nv: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(align_nv, dict):
        return {}
    summary = {
        "ok": bool(align_nv.get("ok", False)),
        "aligned": bool(align_nv.get("aligned", False)),
        "requested_name": align_nv.get("requested_name", ""),
        "source": align_nv.get("source", ""),
        "seed_position": copy.deepcopy(align_nv.get("seed_position", [])),
        "target_position": copy.deepcopy(align_nv.get("target_position", [])),
        "tracking_seed_position": copy.deepcopy(align_nv.get("tracking_seed_position", [])),
        "tracked_position": copy.deepcopy(align_nv.get("tracked_position", [])),
        "current_imaging_seed_position": copy.deepcopy(align_nv.get("current_imaging_seed_position", [])),
        "gui_tracking_attempted": bool(align_nv.get("gui_tracking_attempted", False)),
        "agent_seed_selection_required": bool(align_nv.get("agent_seed_selection_required", False)),
        "final_counts_text": align_nv.get("final_counts_text", ""),
        "final_counts_kcps": align_nv.get("final_counts_kcps", []),
        "tracker_aborted": bool(align_nv.get("tracker_aborted", False)),
        "selected_z_tracking_attempt_index": align_nv.get("selected_z_tracking_attempt_index", []),
        "warnings": copy.deepcopy((align_nv.get("warnings") or [])[:10]),
        "notes": copy.deepcopy((align_nv.get("notes") or [])[:10]),
        "blockers": copy.deepcopy((align_nv.get("blockers") or [])[:10]),
    }
    registry_lookup = align_nv.get("registry_lookup", {})
    if isinstance(registry_lookup, dict) and registry_lookup:
        entry = registry_lookup.get("entry", {})
        if not isinstance(entry, dict):
            entry = {}
        summary["registry_lookup"] = {
            "found": bool(registry_lookup.get("found", False)),
            "registry_path": str(registry_lookup.get("registry_path", "") or ""),
            "entry": {
                "sample_id": str(entry.get("sample_id", "") or ""),
                "nv_name": str(entry.get("nv_name", "") or ""),
                "position": normalize_position_triplet(entry.get("position", [])),
                "updated_at": str(entry.get("updated_at", "") or ""),
                "final_counts_kcps": entry.get("final_counts_kcps", []),
                "source": str(entry.get("source", "") or ""),
                "reference_data": str(entry.get("reference_data", "") or ""),
            },
            "warnings": copy.deepcopy((registry_lookup.get("warnings") or [])[:6]),
            "notes": copy.deepcopy((registry_lookup.get("notes") or [])[:6]),
        }
    landmark_match = align_nv.get("landmark_match", {})
    if isinstance(landmark_match, dict) and landmark_match:
        summary["landmark_match"] = summarize_landmark_match_for_recovery(landmark_match)
    search_scan = align_nv.get("search_scan", {})
    if isinstance(search_scan, dict) and search_scan:
        summary["search_scan"] = summarize_search_scan_for_recovery(search_scan)
    local_fine_search = align_nv.get("local_fine_search", {})
    if isinstance(local_fine_search, dict) and local_fine_search:
        summary["local_fine_search"] = summarize_local_fine_search_for_recovery(local_fine_search)
    summary["z_tracking_attempts"] = summarize_z_tracking_attempts_for_recovery(align_nv.get("z_tracking_attempts", []))
    return summary


def summarize_configure_experiment_for_recovery(configure: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(configure, dict):
        return {}
    return {
        "ok": bool(configure.get("ok", False)),
        "applied": bool(configure.get("applied", False)),
        "setscan_ok": bool(configure.get("setscan_ok", False)),
        "sequence_path": configure.get("sequence_path", ""),
        "sequence_name": configure.get("sequence_name", ""),
        "derived_scan": copy.deepcopy(configure.get("derived_scan", {})),
        "warnings": copy.deepcopy((configure.get("warnings") or [])[:6]),
        "notes": copy.deepcopy((configure.get("notes") or [])[:8]),
        "blockers": copy.deepcopy((configure.get("blockers") or [])[:8]),
    }


def summarize_run_experiment_for_recovery(run_experiment: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(run_experiment, dict):
        return {}
    return {
        "called": bool(run_experiment.get("called", False)),
        "returned": bool(run_experiment.get("returned", False)),
        "has_aborted": bool(run_experiment.get("has_aborted", False)),
        "started_at": run_experiment.get("started_at", ""),
        "finished_at": run_experiment.get("finished_at", ""),
        "incomplete": bool(run_experiment.get("incomplete", False)),
        "incomplete_reason": run_experiment.get("incomplete_reason", ""),
        "notes": copy.deepcopy((run_experiment.get("notes") or [])[:8]),
    }


def summarize_result_for_recovery(result: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(result, dict):
        return {}
    summary: dict[str, Any] = {
        "status": result.get("status", ""),
        "mode": result.get("mode", ""),
        "started_at": result.get("started_at", ""),
        "finished_at": result.get("finished_at", ""),
        "run_id": result.get("run_id", ""),
        "data_path": normalize_path_for_agent(result.get("data_path", "")),
        "error_code": result.get("error_code", ""),
        "error_message": truncate_text(result.get("error_message", ""), 1200),
        "warnings": copy.deepcopy((result.get("warnings") or [])[:12]),
    }
    inner = result.get("summary", {})
    if isinstance(inner, dict):
        summary["sequence_label"] = inner.get("sequence_label", "")
        summary["sequence_path"] = normalize_path_for_agent(inner.get("sequence_path", ""))
        summary["sequence_name"] = inner.get("sequence_name", "")
        prepare_session = inner.get("prepare_session")
        if isinstance(prepare_session, dict) and prepare_session:
            summary["prepare_session"] = {
                "ok": bool(prepare_session.get("ok", False)),
                "prepared": bool(prepare_session.get("prepared", False)),
                "attached": copy.deepcopy(prepare_session.get("attached", [])),
                "blockers": copy.deepcopy((prepare_session.get("blockers") or [])[:8]),
            }
        align_nv = inner.get("align_nv")
        if isinstance(align_nv, dict) and align_nv:
            summary["align_nv"] = summarize_align_nv_for_recovery(align_nv)
        configure_experiment = inner.get("configure_experiment")
        if isinstance(configure_experiment, dict) and configure_experiment:
            summary["configure_experiment"] = summarize_configure_experiment_for_recovery(configure_experiment)
        run_experiment = inner.get("run_experiment")
        if isinstance(run_experiment, dict) and run_experiment:
            summary["run_experiment"] = summarize_run_experiment_for_recovery(run_experiment)
    metadata = result.get("metadata", {})
    if isinstance(metadata, dict) and metadata:
        summary["result_metadata"] = {
            "auto_align_nv": metadata.get("auto_align_nv", []),
            "require_landmark_match": metadata.get("require_landmark_match", []),
            "allow_seed_fallback": metadata.get("allow_seed_fallback", []),
            "acquisition": summarize_acquisition_for_recovery(metadata.get("acquisition", {})),
            "reference_data": normalize_path_for_agent(metadata.get("reference_data", "")),
        }
    return summary


def summarize_float_vars_for_recovery(float_vars: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(float_vars, dict):
        return {}
    summary: dict[str, Any] = {}
    for key, value in float_vars.items():
        if isinstance(value, (int, float, str, bool)):
            summary[key] = copy.deepcopy(value)
        elif isinstance(value, dict):
            summary[key] = copy.deepcopy(value)
    return summary


def summarize_item_context_for_recovery(item_spec: dict[str, Any], item_state: dict[str, Any]) -> dict[str, Any]:
    metadata = item_spec.get("metadata", {}) if isinstance(item_spec, dict) else {}
    retry_overrides = item_state.get("retry_overrides", {}) if isinstance(item_state, dict) else {}
    retry_metadata = retry_overrides.get("metadata", {}) if isinstance(retry_overrides, dict) else {}
    sequence_context = resolve_item_sequence_context(item_spec)
    return {
        "id": str(item_state.get("id", "") or ""),
        "mode": str(item_spec.get("mode", "") or ""),
        "sequence": sequence_context.get("sequence", ""),
        "sequence_manifest_id": sequence_context.get("sequence_manifest_id", ""),
        "sequence_file": sequence_context.get("sequence_file", ""),
        "sequence_path": sequence_context.get("sequence_path", ""),
        "sample_id": str(item_spec.get("sample_id", "") or ""),
        "scan": summarize_scan_for_recovery(item_spec.get("scan", {})),
        "float_vars": summarize_float_vars_for_recovery(item_spec.get("float_vars", {})),
        "analysis": summarize_analysis_for_recovery(item_spec.get("analysis", {})),
        "acquisition": summarize_acquisition_for_recovery(item_spec.get("acquisition", {})),
        "metadata": summarize_metadata_for_recovery(metadata if isinstance(metadata, dict) else {}),
        "sequence_authoring": summarize_sequence_authoring_for_agent(item_spec),
        "project_branches": summarize_project_branches_for_agent(item_spec),
        "retry_overrides": {
            "scan": summarize_scan_for_recovery(retry_overrides.get("scan", {})) if isinstance(retry_overrides, dict) else {},
            "float_vars": summarize_float_vars_for_recovery(retry_overrides.get("float_vars", {})) if isinstance(retry_overrides, dict) else {},
            "acquisition": summarize_acquisition_for_recovery(retry_overrides.get("acquisition", {})) if isinstance(retry_overrides, dict) else {},
            "metadata": summarize_metadata_for_recovery(retry_metadata if isinstance(retry_metadata, dict) else {}),
            "analysis": summarize_analysis_for_recovery(retry_overrides.get("analysis", {})) if isinstance(retry_overrides, dict) else {},
            "sequence_authoring": summarize_sequence_authoring_for_agent(retry_overrides),
            "project_branches": summarize_project_branches_for_agent(retry_overrides),
        },
        "override_hints": {
            "supported_metadata_keys": list(RECOVERY_METADATA_HINT_KEYS),
            "top_level_keys": ["scan", "float_vars", "acquisition", "metadata", "analysis", "allow_seed_fallback", "sequence_authoring", "project_branches"],
        },
    }


def summarize_job_for_recovery(job_payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(job_payload, dict):
        return {}
    metadata = job_payload.get("metadata", {})
    acquisition = {}
    if isinstance(metadata, dict):
        acquisition = metadata.get("acquisition", {})
    sequence_context = resolve_item_sequence_context(job_payload)
    return {
        "job_id": str(job_payload.get("job_id", "") or ""),
        "mode": str(job_payload.get("mode", "") or ""),
        "recipe": str(job_payload.get("recipe", "") or ""),
        "sample_id": str(job_payload.get("sample_id", "") or ""),
        "sequence_manifest_id": sequence_context.get("sequence_manifest_id", ""),
        "sequence_file": sequence_context.get("sequence_file", ""),
        "sequence_path": sequence_context.get("sequence_path", ""),
        "scan": summarize_scan_for_recovery(job_payload.get("scan", {})),
        "float_vars": summarize_float_vars_for_recovery(job_payload.get("float_vars", {})),
        "acquisition": summarize_acquisition_for_recovery(acquisition if isinstance(acquisition, dict) else {}),
        "metadata": summarize_metadata_for_recovery(metadata if isinstance(metadata, dict) else {}),
    }


def resolve_reference_data_path(value: Any) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    path = Path(text)
    if path.is_absolute():
        return normalize_path_for_agent(path)
    candidate = (DEFAULT_REFERENCE_DATA_ROOT / text).resolve()
    if candidate.exists():
        return str(candidate)
    return normalize_path_for_agent(text)


def enrich_rendered_item_sequence_context(rendered_item: dict[str, Any], item_spec: dict[str, Any]) -> dict[str, Any]:
    enriched = copy.deepcopy(rendered_item) if isinstance(rendered_item, dict) else {}
    item_context = item_spec if isinstance(item_spec, dict) else {}
    sequence_source = copy.deepcopy(item_context)
    for key in ("sequence", "sequence_manifest_id", "sequence_file", "sequence_path"):
        value = enriched.get(key, "")
        if value:
            sequence_source[key] = value
    sequence_context = resolve_item_sequence_context(sequence_source)
    enriched["sequence"] = sequence_context.get("sequence", "")
    enriched["sequence_manifest_id"] = sequence_context.get("sequence_manifest_id", "")
    enriched["sequence_file"] = sequence_context.get("sequence_file", "")
    enriched["sequence_path"] = sequence_context.get("sequence_path", "")
    return enriched


def summarize_aux_state_entries(entries: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(entries, dict):
        return {}
    summary: dict[str, Any] = {}
    for key, entry in entries.items():
        if not isinstance(entry, dict):
            continue
        summary[str(key)] = {
            "value": copy.deepcopy(entry.get("value")),
            "label": str(entry.get("label", "") or ""),
            "source": str(entry.get("source", "") or ""),
            "updated_at": str(entry.get("updated_at", "") or ""),
            "result_path": normalize_path_for_agent(entry.get("result_path", "")),
            "data_path": normalize_path_for_agent(entry.get("data_path", "")),
            "fit_kind": str(entry.get("fit_kind", "") or ""),
        }
    return summary


def normalize_text_list(value: Any) -> list[str]:
    if isinstance(value, (list, tuple, set)):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def normalize_position_triplet(value: Any) -> list[float]:
    if isinstance(value, (list, tuple)) and len(value) >= 3:
        triplet: list[float] = []
        for item in value[:3]:
            try:
                triplet.append(float(item))
            except (TypeError, ValueError):
                return []
        return triplet
    return []


def iso_age_hours(value: Any) -> float | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        timestamp = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if timestamp.tzinfo is None:
        timestamp = timestamp.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - timestamp.astimezone(timezone.utc)).total_seconds() / 3600.0


def family_token(value: Any) -> str:
    text = str(value or "").strip().lower()
    if text.endswith(".xml"):
        text = text[:-4]
    return re.sub(r"[^a-z0-9]+", "", text)


def parse_savedexperiment_filename(path_value: Any) -> dict[str, Any]:
    path = Path(str(path_value or "").strip())
    match = SAVED_EXPERIMENT_FILENAME_RE.match(path.name)
    if not match:
        return {}
    clock = match.group("clock")
    return {
        "path": normalize_path_for_agent(str(path)),
        "name": path.name,
        "sequence_hint": match.group("sequence"),
        "vary_hint": match.group("vary"),
        "time_iso": f"{match.group('date')}T{clock[0:2]}:{clock[2:4]}:{clock[4:6]}",
        "family_token": family_token(match.group("sequence")),
        "vary_token": family_token(match.group("vary")),
    }


def lookup_registry_entry_for_past_data(rendered_item: dict[str, Any], metadata: dict[str, Any]) -> dict[str, Any]:
    sample_id = str(rendered_item.get("sample_id", "") or "").strip()
    nv_name = str(metadata.get("nv_name", "") or "").strip()
    registry_path_text = str(metadata.get("reference_data_registry_path", "") or "").strip()
    registry_path = Path(normalize_path_for_agent(registry_path_text)) if registry_path_text else DEFAULT_NV_POSITION_REGISTRY_PATH
    payload = try_read_json(registry_path)
    raw_entries = payload.get("entries", {})
    if isinstance(raw_entries, dict):
        entries = [raw_entries]
    elif isinstance(raw_entries, list):
        entries = [entry for entry in raw_entries if isinstance(entry, dict)]
    else:
        entries = []

    selected_entry: dict[str, Any] = {}
    match_field = ""
    sample_id_key = sample_id.lower()
    nv_name_key = nv_name.lower()
    for entry in reversed(entries):
        entry_sample = str(entry.get("sample_id", "") or "").strip().lower()
        entry_nv_name = str(entry.get("nv_name", "") or "").strip().lower()
        if sample_id_key and entry_sample == sample_id_key:
            selected_entry = entry
            match_field = "sample_id"
            break
        if nv_name_key and entry_nv_name == nv_name_key:
            selected_entry = entry
            match_field = "nv_name"
            break

    entry_reference = str(selected_entry.get("reference_data", "") or "").strip() if selected_entry else ""
    entry_data_path = str(selected_entry.get("data_path", "") or "").strip() if selected_entry else ""
    return {
        "query": {
            "sample_id": sample_id,
            "nv_name": nv_name,
        },
        "registry_path": normalize_path_for_agent(str(registry_path)),
        "found": bool(selected_entry),
        "match_field": match_field,
        "entry": {
            "sample_id": str(selected_entry.get("sample_id", "") or ""),
            "nv_name": str(selected_entry.get("nv_name", "") or ""),
            "position": normalize_position_triplet(selected_entry.get("position", [])),
            "updated_at": str(selected_entry.get("updated_at", "") or ""),
            "age_hours": iso_age_hours(selected_entry.get("updated_at", "")),
            "final_counts_kcps": selected_entry.get("final_counts_kcps", []),
            "source": str(selected_entry.get("source", "") or ""),
            "reference_data": normalize_path_for_agent(entry_reference),
            "reference_data_resolved_path": resolve_reference_data_path(entry_reference),
            "data_path": normalize_path_for_agent(entry_data_path),
        },
    }


def select_recent_usage_clusters(reference_data_path: str, registry_context: dict[str, Any]) -> dict[str, Any]:
    payload = try_read_json(DEFAULT_NV_USAGE_SUMMARY_PATH)
    if not payload:
        return {
            "summary_path": normalize_path_for_agent(str(DEFAULT_NV_USAGE_SUMMARY_PATH)),
            "exists": False,
            "generated_at": "",
            "age_hours": [],
            "matched_clusters": [],
        }

    clusters = payload.get("clusters", [])
    if not isinstance(clusters, list):
        clusters = []
    registry_entry = registry_context.get("entry", {}) if isinstance(registry_context, dict) else {}
    registry_position = normalize_position_triplet(registry_entry.get("position", []))
    reference_compare = str(reference_data_path or "").strip()

    matched_clusters: list[dict[str, Any]] = []
    nearest_candidates: list[tuple[float, dict[str, Any]]] = []
    for cluster in clusters:
        if not isinstance(cluster, dict):
            continue
        experiment_paths = [normalize_path_for_agent(path) for path in cluster.get("experiment_paths", []) if str(path or "").strip()]
        centroid_position = normalize_position_triplet(cluster.get("centroid_position", []))
        match_reasons: list[str] = []
        xy_distance = []
        z_distance = []
        centroid_distance = []

        if reference_compare and reference_compare in experiment_paths:
            match_reasons.append("contains_reference_data")
        if registry_position and centroid_position:
            xy = ((registry_position[0] - centroid_position[0]) ** 2 + (registry_position[1] - centroid_position[1]) ** 2) ** 0.5
            z = abs(registry_position[2] - centroid_position[2])
            xyz = ((registry_position[0] - centroid_position[0]) ** 2 + (registry_position[1] - centroid_position[1]) ** 2 + (registry_position[2] - centroid_position[2]) ** 2) ** 0.5
            xy_distance = round(xy, 3)
            z_distance = round(z, 3)
            centroid_distance = round(xyz, 3)
            nearest_candidates.append((xyz, cluster))
            if xy <= 2.5 and z <= 3.5:
                match_reasons.append("near_registry_position")

        if not match_reasons:
            continue
        matched_clusters.append(
            {
                "cluster_id": cluster.get("cluster_id", []),
                "count": int(cluster.get("count", 0) or 0),
                "centroid_position": centroid_position,
                "first_time": str(cluster.get("first_time", "") or ""),
                "last_time": str(cluster.get("last_time", "") or ""),
                "sequence_names": copy.deepcopy(cluster.get("sequence_names", [])),
                "vary_props": copy.deepcopy(cluster.get("vary_props", [])),
                "experiment_paths": experiment_paths,
                "representative_image": normalize_path_for_agent(cluster.get("representative_image", "")),
                "match_reasons": match_reasons,
                "registry_xy_distance_um": xy_distance,
                "registry_z_distance_um": z_distance,
                "registry_xyz_distance_um": centroid_distance,
            }
        )

    if matched_clusters:
        def cluster_sort_key(cluster: dict[str, Any]) -> tuple[int, int, float, int]:
            reasons = set(cluster.get("match_reasons", []))
            distance = cluster.get("registry_xyz_distance_um", [])
            try:
                distance_value = float(distance)
            except (TypeError, ValueError):
                distance_value = float("inf")
            return (
                0 if "contains_reference_data" in reasons else 1,
                0 if "near_registry_position" in reasons else 1,
                distance_value,
                -int(cluster.get("count", 0) or 0),
            )

        matched_clusters = sorted(matched_clusters, key=cluster_sort_key)
    if not matched_clusters and nearest_candidates:
        for _, cluster in sorted(nearest_candidates, key=lambda item: item[0])[:DEFAULT_NV_USAGE_CLUSTER_LIMIT]:
            centroid_position = normalize_position_triplet(cluster.get("centroid_position", []))
            xyz = []
            if registry_position and centroid_position:
                xyz = round(
                    ((registry_position[0] - centroid_position[0]) ** 2 + (registry_position[1] - centroid_position[1]) ** 2 + (registry_position[2] - centroid_position[2]) ** 2) ** 0.5,
                    3,
                )
            matched_clusters.append(
                {
                    "cluster_id": cluster.get("cluster_id", []),
                    "count": int(cluster.get("count", 0) or 0),
                    "centroid_position": centroid_position,
                    "first_time": str(cluster.get("first_time", "") or ""),
                    "last_time": str(cluster.get("last_time", "") or ""),
                    "sequence_names": copy.deepcopy(cluster.get("sequence_names", [])),
                    "vary_props": copy.deepcopy(cluster.get("vary_props", [])),
                    "experiment_paths": [normalize_path_for_agent(path) for path in cluster.get("experiment_paths", []) if str(path or "").strip()],
                    "representative_image": normalize_path_for_agent(cluster.get("representative_image", "")),
                    "match_reasons": ["nearest_registry_cluster"],
                    "registry_xyz_distance_um": xyz,
                }
            )

    return {
        "summary_path": normalize_path_for_agent(str(DEFAULT_NV_USAGE_SUMMARY_PATH)),
        "exists": True,
        "generated_at": str(payload.get("generated_at", "") or ""),
        "age_hours": iso_age_hours(payload.get("generated_at", "")),
        "matched_clusters": matched_clusters,
        "likely_nv": copy.deepcopy(payload.get("likely_nv", {})) if isinstance(payload.get("likely_nv", {}), dict) else {},
    }


def summarize_savedexperiment_family_history(
    rendered_item: dict[str, Any],
    reference_data_path: str,
    registry_context: dict[str, Any],
) -> dict[str, Any]:
    root = DEFAULT_SAVED_EXPERIMENTS_ROOT
    scan = rendered_item.get("scan", {}) if isinstance(rendered_item, dict) else {}
    current_sequence = str(rendered_item.get("sequence", "") or "").strip()
    current_sequence_token = family_token(current_sequence)
    scan_vary_props = [family_token(item) for item in normalize_text_list(scan.get("vary_prop", [])) if family_token(item)]

    reference_family = parse_savedexperiment_filename(reference_data_path)
    reference_sequence_token = str(reference_family.get("family_token", "") or "")
    reference_vary_token = str(reference_family.get("vary_token", "") or "")

    exact_family_matches: list[dict[str, Any]] = []
    same_vary_matches: list[dict[str, Any]] = []
    same_sequence_matches: list[dict[str, Any]] = []
    if root.is_dir():
        for path in sorted(root.glob("*.mat"), reverse=True):
            parsed = parse_savedexperiment_filename(path)
            if not parsed:
                continue
            reasons: list[str] = []
            if reference_sequence_token and reference_vary_token:
                if parsed["family_token"] == reference_sequence_token and parsed["vary_token"] == reference_vary_token:
                    reasons.append("exact_reference_family")
            if scan_vary_props and parsed["vary_token"] in scan_vary_props:
                reasons.append("matching_scan_vary_prop")
            if current_sequence_token and (
                current_sequence_token.startswith(parsed["family_token"]) or parsed["family_token"].startswith(current_sequence_token)
            ):
                reasons.append("matching_current_sequence")
            parsed["match_reasons"] = sorted(set(reasons))
            if "exact_reference_family" in parsed["match_reasons"]:
                exact_family_matches.append(parsed)
            elif "matching_scan_vary_prop" in parsed["match_reasons"]:
                same_vary_matches.append(parsed)
            elif "matching_current_sequence" in parsed["match_reasons"]:
                same_sequence_matches.append(parsed)

    return {
        "root": normalize_path_for_agent(str(root)),
        "reference_family": {
            "path": reference_family.get("path", ""),
            "sequence_hint": reference_family.get("sequence_hint", ""),
            "vary_hint": reference_family.get("vary_hint", ""),
        },
        "query_hints": {
            "current_sequence": current_sequence,
            "scan_vary_prop": normalize_text_list(scan.get("vary_prop", [])),
            "registry_sample_id": str(registry_context.get("query", {}).get("sample_id", "") or ""),
        },
        "exact_reference_family_total_count": len(exact_family_matches),
        "matching_scan_vary_prop_total_count": len(same_vary_matches),
        "matching_current_sequence_total_count": len(same_sequence_matches),
        "recent_exact_reference_family": exact_family_matches[:DEFAULT_SAVED_EXPERIMENT_FAMILY_MATCH_LIMIT],
        "recent_matching_scan_vary_prop": same_vary_matches[:DEFAULT_SAVED_EXPERIMENT_FAMILY_MATCH_LIMIT],
        "recent_matching_current_sequence": same_sequence_matches[:DEFAULT_SAVED_EXPERIMENT_FAMILY_MATCH_LIMIT],
        "note": "These entries come directly from savedexperiments/NV1 filenames, so they include human-run and bridge-run data but are not sample-name aware on their own.",
    }


def select_savedexperiment_entries_for_mat_summary(
    savedexperiment_history: dict[str, Any],
    reference_data: dict[str, Any],
    selection_order: list[str] | None = None,
    limit: int = DEFAULT_SAVED_EXPERIMENT_MAT_SUMMARY_LIMIT,
) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    seen_paths: set[str] = set()

    def maybe_add(entry: dict[str, Any], bucket: str) -> None:
        if not isinstance(entry, dict):
            return
        path_value = normalize_path_for_agent(entry.get("path", ""))
        if not path_value or path_value in seen_paths:
            return
        candidate = copy.deepcopy(entry)
        candidate["path"] = path_value
        match_reasons = normalize_text_list(candidate.get("match_reasons", []))
        if bucket and bucket not in match_reasons:
            match_reasons = [bucket] + [reason for reason in match_reasons if reason != bucket]
        candidate["match_reasons"] = match_reasons
        candidate["selection_bucket"] = bucket
        selected.append(candidate)
        seen_paths.add(path_value)

    reference_path = normalize_path_for_agent(reference_data.get("resolved_path", "") or reference_data.get("raw_path", ""))
    reference_family = savedexperiment_history.get("reference_family", {}) if isinstance(savedexperiment_history, dict) else {}
    selection_order = list(selection_order or [])
    if not selection_order:
        selection_order = [
            "reference_data",
            "recent_exact_reference_family",
            "recent_matching_scan_vary_prop",
            "recent_matching_current_sequence",
        ]

    for bucket in selection_order:
        if bucket == "reference_data":
            if reference_path:
                maybe_add(
                    {
                        "path": reference_path,
                        "name": Path(reference_path).name,
                        "sequence_hint": str(reference_family.get("sequence_hint", "") or ""),
                        "vary_hint": str(reference_family.get("vary_hint", "") or ""),
                        "time_iso": "",
                        "match_reasons": ["reference_data"],
                    },
                    "reference_data",
                )
            if len(selected) >= int(limit):
                return selected
            continue
        entries = savedexperiment_history.get(bucket, []) if isinstance(savedexperiment_history, dict) else []
        for entry in entries:
            maybe_add(entry, bucket)
            if len(selected) >= int(limit):
                return selected
    return selected


def determine_savedexperiment_mat_selection_order(
    savedexperiment_history: dict[str, Any],
    rendered_item: dict[str, Any],
) -> list[str]:
    default_order = [
        "reference_data",
        "recent_exact_reference_family",
        "recent_matching_scan_vary_prop",
        "recent_matching_current_sequence",
    ]

    reference_family = savedexperiment_history.get("reference_family", {}) if isinstance(savedexperiment_history, dict) else {}
    current_sequence_token = family_token(rendered_item.get("sequence", "") or "")
    current_scan = rendered_item.get("scan", {}) if isinstance(rendered_item.get("scan", {}), dict) else {}
    current_vary_tokens = [family_token(item) for item in normalize_text_list(current_scan.get("vary_prop", [])) if family_token(item)]
    reference_sequence_token = family_token(reference_family.get("sequence_hint", "") or "")
    reference_vary_token = family_token(reference_family.get("vary_hint", "") or "")

    prefer_current_sequence = False
    if current_sequence_token and reference_sequence_token and current_sequence_token != reference_sequence_token:
        prefer_current_sequence = True
    elif current_vary_tokens and reference_vary_token and reference_vary_token not in current_vary_tokens:
        prefer_current_sequence = True

    if prefer_current_sequence:
        return [
            "recent_matching_current_sequence",
            "recent_matching_scan_vary_prop",
            "reference_data",
            "recent_exact_reference_family",
        ]
    return default_order


def prepare_savedexperiment_mat_selection(
    savedexperiment_history: dict[str, Any],
    reference_data: dict[str, Any],
    rendered_item: dict[str, Any],
    limit: int = DEFAULT_SAVED_EXPERIMENT_MAT_SUMMARY_LIMIT,
) -> dict[str, Any]:
    selection_order = determine_savedexperiment_mat_selection_order(savedexperiment_history, rendered_item)
    selected_entries = select_savedexperiment_entries_for_mat_summary(
        savedexperiment_history,
        reference_data,
        selection_order=selection_order,
        limit=limit,
    )
    selected_paths = [str(entry.get("path", "") or "") for entry in selected_entries if str(entry.get("path", "") or "").strip()]
    return {
        "selection_order": selection_order,
        "selected_entries": selected_entries,
        "selected_paths": selected_paths,
    }


def summarize_savedexperiment_mat_history(
    savedexperiment_history: dict[str, Any],
    reference_data: dict[str, Any],
    rendered_item: dict[str, Any],
) -> dict[str, Any]:
    context = {
        "available": False,
        "limit": int(DEFAULT_SAVED_EXPERIMENT_MAT_SUMMARY_LIMIT),
        "selection_order": [],
        "selected_paths": [],
        "raw_exports": [],
        "warnings": [],
    }

    selection = prepare_savedexperiment_mat_selection(
        savedexperiment_history,
        reference_data,
        rendered_item,
        limit=DEFAULT_SAVED_EXPERIMENT_MAT_SUMMARY_LIMIT,
    )
    context["selection_order"] = copy.deepcopy(selection.get("selection_order", []))
    selected_entries = selection.get("selected_entries", [])
    selected_paths = selection.get("selected_paths", [])
    if not selected_entries:
        return context

    context["selected_paths"] = selected_paths
    if export_savedexperiment_mat_raw_files is None:
        context["warnings"].append("savedexperiment .mat raw export tool was unavailable, so only filename-level history is present.")
        return context

    try:
        raw_exports = export_savedexperiment_mat_raw_files(selected_paths)
    except Exception as exc:
        context["warnings"].append(f"savedexperiment .mat raw export failed: {exc}")
        return context

    merged_exports: list[dict[str, Any]] = []
    for entry, raw_export in zip(selected_entries, raw_exports):
        merged = copy.deepcopy(raw_export) if isinstance(raw_export, dict) else {}
        merged["history_match_reasons"] = copy.deepcopy(entry.get("match_reasons", []))
        merged["history_time_iso"] = str(entry.get("time_iso", "") or "")
        merged["history_sequence_hint"] = str(entry.get("sequence_hint", "") or "")
        merged["history_vary_hint"] = str(entry.get("vary_hint", "") or "")
        merged["selection_bucket"] = str(entry.get("selection_bucket", "") or "")
        merged["source_priority"] = "savedexperiment_mat_raw_export"
        merged_exports.append(merged)

    context["available"] = bool(merged_exports)
    context["raw_exports"] = merged_exports
    return context


def build_savedexperiment_mat_artifact_context(
    savedexperiment_history: dict[str, Any],
    reference_data: dict[str, Any],
    rendered_item: dict[str, Any],
) -> dict[str, Any]:
    context = {
        "available": False,
        "limit": int(DEFAULT_SAVED_EXPERIMENT_MAT_SUMMARY_LIMIT),
        "selection_order": [],
        "selected_paths": [],
        "artifacts": [],
        "warnings": [],
    }

    selection = prepare_savedexperiment_mat_selection(
        savedexperiment_history,
        reference_data,
        rendered_item,
        limit=DEFAULT_SAVED_EXPERIMENT_MAT_SUMMARY_LIMIT,
    )
    context["selection_order"] = copy.deepcopy(selection.get("selection_order", []))
    selected_entries = selection.get("selected_entries", [])
    selected_paths = selection.get("selected_paths", [])
    if not selected_entries:
        return context

    context["selected_paths"] = selected_paths
    if materialize_savedexperiment_mat_raw_artifacts is None:
        context["warnings"].append("savedexperiment .mat artifact tool was unavailable, so direct parsed artifacts were not prepared.")
        return context

    try:
        raw_artifacts = materialize_savedexperiment_mat_raw_artifacts(selected_paths)
    except Exception as exc:
        context["warnings"].append(f"savedexperiment .mat artifact extraction failed: {exc}")
        return context

    merged_artifacts: list[dict[str, Any]] = []
    for entry, artifact in zip(selected_entries, raw_artifacts):
        merged = copy.deepcopy(artifact) if isinstance(artifact, dict) else {}
        merged["history_match_reasons"] = copy.deepcopy(entry.get("match_reasons", []))
        merged["history_time_iso"] = str(entry.get("time_iso", "") or "")
        merged["history_sequence_hint"] = str(entry.get("sequence_hint", "") or "")
        merged["history_vary_hint"] = str(entry.get("vary_hint", "") or "")
        merged["selection_bucket"] = str(entry.get("selection_bucket", "") or "")
        merged["source_priority"] = "savedexperiment_raw_mat_artifact"
        merged_artifacts.append(merged)

    context["available"] = bool(merged_artifacts)
    context["artifacts"] = merged_artifacts
    return context


def latest_result_path_from_history(item_state: dict[str, Any]) -> str:
    for history_entry in reversed(item_state.get("history", [])):
        result_path = str(history_entry.get("result_path", "") or "").strip()
        if result_path:
            return result_path
    return ""


def summarize_completed_items_for_planning(
    batch_spec: dict[str, Any],
    state: dict[str, Any],
    current_index: int,
    aux_entries: dict[str, Any],
) -> list[dict[str, Any]]:
    summary: list[dict[str, Any]] = []
    batch_items = list(batch_spec.get("items", []))
    state_items = list(state.get("items", []))
    for index in range(min(current_index, len(batch_items), len(state_items))):
        item_spec = batch_items[index]
        item_state = state_items[index]
        if str(item_state.get("status", "") or "").strip().lower() != "completed":
            continue
        result_path = latest_result_path_from_history(item_state)
        result_payload = try_read_json(Path(result_path)) if result_path else {}
        data_path = ""
        run_id = ""
        outcome_summary = {}
        if isinstance(result_payload, dict):
            data_path = normalize_path_for_agent(result_payload.get("data_path", ""))
            run_id = str(result_payload.get("run_id", "") or "")
            outcome_summary = copy.deepcopy(result_payload.get("outcome_summary", {}))
        aux_keys_updated = [
            key
            for key, entry in aux_entries.items()
            if isinstance(entry, dict) and str(entry.get("result_path", "") or "").strip() == result_path
        ]
        summary.append(
            {
                "item_id": str(item_state.get("id", "") or ""),
                "sequence": str(item_spec.get("sequence", "") or ""),
                "sequence_manifest_id": str(item_spec.get("sequence_manifest_id", "") or ""),
                "status": str(item_state.get("status", "") or ""),
                "attempts": int(item_state.get("attempts", 0)),
                "result_path": normalize_path_for_agent(result_path),
                "data_path": data_path,
                "run_id": run_id,
                "analysis_final_action": str(item_state.get("analysis", {}).get("final_action", "") or ""),
                "aux_keys_updated": sorted(aux_keys_updated),
                "outcome_summary": outcome_summary,
            }
        )
    return summary


def try_read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = read_json(path)
    except ValueError:
        return {}
    return payload if isinstance(payload, dict) else {}


def tail_text_file(path: Path, max_lines: int = 80, max_chars: int = 6000) -> str:
    if not path.is_file():
        return ""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""
    lines = text.splitlines()
    tail = "\n".join(lines[-max_lines:])
    return truncate_text(tail, max_chars)


def default_control_path(state_path: Path) -> Path:
    name = state_path.name
    if name.endswith(".state.json"):
        return state_path.with_name(name[: -len(".state.json")] + ".control.json")
    return state_path.with_name(state_path.stem + ".control.json")


def resolve_hook_token(config_path: Path) -> str:
    env_token = os.environ.get("OPENCLAW_HOOKS_TOKEN")
    if env_token:
        return env_token
    if config_path.is_file():
        cfg = read_json(config_path)
        hooks_token = cfg.get("hooks", {}).get("token")
        if hooks_token:
            return hooks_token
        gateway_token = cfg.get("gateway", {}).get("auth", {}).get("token")
        if gateway_token:
            return gateway_token
    return ""


def post_hook(gateway_url: str, hook_token: str, hook_path: str, payload: dict[str, Any]) -> bool:
    if not hook_token:
        return False
    req = urllib.request.Request(
        gateway_url.rstrip("/") + "/" + hook_path.lstrip("/"),
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {hook_token}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20):
            return True
    except urllib.error.URLError:
        return False


def send_hook(gateway_url: str, hook_token: str, text: str) -> None:
    post_hook(gateway_url, hook_token, "/hooks/wake", {"text": text, "mode": "now"})


def load_aux_state(path: Path) -> dict[str, Any]:
    if path.is_file():
        return read_json(path)
    return {"updated_at": "", "entries": {}}


def build_custom_analysis_contract() -> dict[str, Any]:
    return {
        "fit_kind": "CustomFunction",
        "supported_fields": [
            "fit_kind",
            "aux_key",
            "aux_slot",
            "discard_first_average",
            "custom_fit_function",
            "custom_fit_path",
            "custom_fit_args",
            "fit_label",
        ],
        "function_signature": "function fit = my_fit(x, y, scan, request)",
        "supported_return_shapes": [
            "numeric scalar",
            {
                "ok": True,
                "value": 0.0,
                "name": "label",
                "error": "",
                "warnings": [],
            },
        ],
        "recommended_repo_dir": normalize_path_for_agent(str(DEFAULT_CUSTOM_ANALYSIS_ROOT)),
        "guidance": "Agents may author a new MATLAB .m fit helper and then reference it from analysis.custom_fit_function. custom_fit_function may be either a function name already on the MATLAB path or a path to a .m file. custom_fit_path may point to an additional directory to add to the MATLAB path before feval.",
    }


def load_control(path: Path) -> dict[str, Any]:
    if path.is_file():
        payload = read_json(path)
    else:
        payload = {}
    return {
        "stop_requested": bool(payload.get("stop_requested", False)),
        "stop_reason": str(payload.get("stop_reason", "") or ""),
        "requested_by": str(payload.get("requested_by", "") or ""),
        "updated_at": str(payload.get("updated_at", "") or ""),
    }


def write_control(path: Path, control: dict[str, Any]) -> None:
    write_json(
        path,
        {
            "stop_requested": bool(control.get("stop_requested", False)),
            "stop_reason": str(control.get("stop_reason", "") or ""),
            "requested_by": str(control.get("requested_by", "") or ""),
            "updated_at": str(control.get("updated_at", "") or now_iso()),
        },
    )


def sync_control_into_state(state: dict[str, Any], control_path: Path, control: dict[str, Any]) -> None:
    state["control"] = {
        "path": str(control_path),
        "stop_requested": bool(control.get("stop_requested", False)),
        "stop_reason": str(control.get("stop_reason", "") or ""),
        "requested_by": str(control.get("requested_by", "") or ""),
        "updated_at": str(control.get("updated_at", "") or ""),
    }


def resolve_aux_reference(value: Any, aux_entries: dict[str, Any]) -> Any:
    if isinstance(value, str) and value.startswith("aux:"):
        key = value.split(":", 1)[1].strip()
        if key not in aux_entries:
            raise ValueError(f"Aux value '{key}' is not available yet.")
        return aux_entries[key].get("value")

    if isinstance(value, dict) and "aux" in value:
        key = str(value.get("aux", "")).strip()
        if key not in aux_entries:
            raise ValueError(f"Aux value '{key}' is not available yet.")
        base = aux_entries[key].get("value")
        scale = float(value.get("scale", 1.0))
        offset = float(value.get("offset", 0.0))
        return base * scale + offset

    if isinstance(value, list):
        return [resolve_aux_reference(item, aux_entries) for item in value]

    if isinstance(value, dict):
        return {k: resolve_aux_reference(v, aux_entries) for k, v in value.items()}

    return value


def render_item(item: dict[str, Any], aux_entries: dict[str, Any]) -> dict[str, Any]:
    rendered = copy.deepcopy(item)
    if "scan" in rendered:
        rendered["scan"] = resolve_aux_reference(rendered["scan"], aux_entries)
    if "float_vars" in rendered:
        rendered["float_vars"] = resolve_aux_reference(rendered["float_vars"], aux_entries)
    if "acquisition" in rendered:
        rendered["acquisition"] = resolve_aux_reference(rendered["acquisition"], aux_entries)
    if "metadata" in rendered:
        rendered["metadata"] = resolve_aux_reference(rendered["metadata"], aux_entries)
    return rendered


def select_analysis_branch_items(
    item_spec: dict[str, Any],
    *,
    action: str,
    rendered_item: dict[str, Any],
    aux_entry: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    analysis = rendered_item.get("analysis", {}) if isinstance(rendered_item, dict) else {}
    if not isinstance(analysis, dict):
        analysis = {}
    return select_project_branch_items_for_context(
        item_spec,
        event="analysis",
        action=action,
        aux_key=str((aux_entry or {}).get("key", "") or analysis.get("aux_key", "") or ""),
        aux_applied=bool(aux_entry),
        fit_kind=str(analysis.get("fit_kind", "") or ""),
    )


def select_recovery_branch_items(item_spec: dict[str, Any], *, action: str, error_code: str = "") -> list[dict[str, Any]]:
    return select_project_branch_items_for_context(
        item_spec,
        event="recovery",
        action=action,
        error_code=error_code,
    )


def prepare_runtime_sequence_authoring_spec(item_spec: dict[str, Any], batch_spec: dict[str, Any]) -> dict[str, Any]:
    sample_id = str(item_spec.get("sample_id", "") or batch_spec.get("requested_sample_id", "") or "").strip().upper()
    authoring = normalize_sequence_authoring_spec(item_spec.get("sequence_authoring"), sample_id)
    if not authoring:
        return {}
    manifest_overrides = deep_merge_dicts(
        {
            "allowed_modes": ["validate", "dry_run", "execute"],
            "requires": {},
        },
        authoring.get("manifest_overrides", {}) if isinstance(authoring.get("manifest_overrides"), dict) else {},
    )
    authoring["manifest_overrides"] = manifest_overrides
    if sample_id and not authoring.get("sample_id"):
        authoring["sample_id"] = sample_id
    return authoring


def materialize_sequence_authoring_for_item(
    *,
    batch_id: str,
    batch_spec: dict[str, Any],
    batch_spec_path: Path,
    state: dict[str, Any],
    state_path: Path,
    item_index: int,
    item_state: dict[str, Any],
    item_spec: dict[str, Any],
    aux_entries: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    if item_spec.get("sequence_manifest_id"):
        return item_spec, {}

    authoring = prepare_runtime_sequence_authoring_spec(item_spec, batch_spec)
    if not authoring:
        return item_spec, {}
    if materialize_staging_sequence_spec is None:
        raise ValueError("Runtime sequence authoring is unavailable because design_nv_sequence.py could not be imported.")

    rendered_authoring = resolve_aux_reference(copy.deepcopy(authoring), aux_entries)
    authoring_root = DEFAULT_SEQUENCE_AUTHORING_ROOT / batch_id / str(item_state.get("id", "item"))
    authoring_root.mkdir(parents=True, exist_ok=True)
    attempt_tag = f"attempt_{int(item_state.get('attempts', 0)) + 1:02d}"
    spec_path = authoring_root / f"{attempt_tag}.spec.json"
    write_json(spec_path, rendered_authoring)

    response = materialize_staging_sequence_spec(
        rendered_authoring,
        repo_root=DEFAULT_REFERENCE_DATA_ROOT,
        manifest_root=DEFAULT_SEQUENCE_MANIFEST_ROOT,
        staging_sequence_dir=DEFAULT_REFERENCE_DATA_ROOT / "SavedSequences" / "SavedSequences-AWG" / "_openclaw_staging",
        staging_manifest_dir=DEFAULT_SEQUENCE_MANIFEST_ROOT / "staging",
        dry_run=False,
    )
    manifest_id = str(((response.get("staging_manifest") or {}) if isinstance(response.get("staging_manifest"), dict) else {}).get("id", "") or rendered_authoring.get("new_id", "")).strip()
    if not manifest_id:
        raise ValueError("Runtime sequence authoring did not produce a staging manifest id.")

    materialized_update = {
        "sequence_manifest_id": manifest_id,
        "generated_sequence": {
            "materialized_at": now_iso(),
            "spec_path": str(spec_path),
            "manifest_path": str(response.get("manifest_output_path", "") or ""),
            "sequence_path": str(response.get("sequence_output_path", "") or ""),
            "base_manifest_id": str(rendered_authoring.get("base_manifest_id", "") or ""),
            "new_id": str(rendered_authoring.get("new_id", "") or ""),
            "xml_source": str(response.get("xml_source", "") or ""),
        },
    }
    if rendered_authoring.get("sample_id") and not item_spec.get("sample_id"):
        materialized_update["sample_id"] = str(rendered_authoring.get("sample_id", "") or "")

    batch_spec["items"][item_index] = deep_merge_dicts(batch_spec.get("items", [])[item_index], materialized_update)
    item_state.setdefault("history", []).append(
        {
            "at": now_iso(),
            "event": "sequence_authored",
            "message": f"Materialized runtime staging sequence `{manifest_id}` for this batch item.",
            "manifest_id": manifest_id,
            "spec_path": str(spec_path),
            "manifest_path": str(response.get("manifest_output_path", "") or ""),
            "sequence_path": str(response.get("sequence_output_path", "") or ""),
        }
    )
    write_json(batch_spec_path, batch_spec)
    write_json(state_path, state)
    return deep_merge_dicts(item_spec, materialized_update), materialized_update


def deep_merge_dicts(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge_dicts(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def validate_measurement_plan_acquisition_override(
    item_spec: dict[str, Any],
    rendered_item: dict[str, Any],
    pre_enqueue_advisory: dict[str, Any],
    planning_plan: dict[str, Any],
) -> str:
    item_overrides = planning_plan.get("item_overrides", {}) if isinstance(planning_plan, dict) else {}
    if not isinstance(item_overrides, dict):
        return ""
    acquisition_override = item_overrides.get("acquisition", {})
    if not isinstance(acquisition_override, dict) or not acquisition_override:
        return ""

    baseline_candidates: list[dict[str, Any]] = []
    advisory_acquisition = pre_enqueue_advisory.get("acquisition", {}) if isinstance(pre_enqueue_advisory, dict) else {}
    if isinstance(advisory_acquisition, dict) and advisory_acquisition:
        baseline_candidates.append(copy.deepcopy(advisory_acquisition))
    for candidate in (
        rendered_item.get("acquisition", {}) if isinstance(rendered_item, dict) else {},
        item_spec.get("acquisition", {}) if isinstance(item_spec, dict) else {},
    ):
        if isinstance(candidate, dict) and candidate:
            baseline_candidates.append(copy.deepcopy(candidate))

    baseline_acquisition: dict[str, Any] = {}
    baseline_total: int | None = None
    for candidate in baseline_candidates:
        candidate_total = total_acquisition_count(candidate)
        if candidate_total is not None:
            baseline_acquisition = candidate
            baseline_total = candidate_total
            break

    if baseline_total is None:
        return (
            "Measurement plan attempted to override acquisition, but OpenClaw could not verify the "
            "baseline total acquisition count from the current item/advisory. Refusing the override so "
            "the planner cannot silently change total shots."
        )

    planned_acquisition = deep_merge_dicts(baseline_acquisition, acquisition_override)
    planned_total = total_acquisition_count(planned_acquisition)
    if planned_total is None:
        return (
            "Measurement plan attempted to override acquisition, but the resulting acquisition no longer "
            f"has a verifiable total shot count. Baseline: {format_acquisition_count(baseline_acquisition)}. "
            "Refusing the override."
        )
    if planned_total != baseline_total:
        return (
            "Measurement plan attempted to change total acquisition count from "
            f"{baseline_total} ({format_acquisition_count(baseline_acquisition)}) to "
            f"{planned_total} ({format_acquisition_count(planned_acquisition)}). "
            "Total acquisition count must stay fixed; change scan/span/points instead if runtime or drift "
            "needs adjustment."
        )
    return ""


def validate_measurement_plan_current_item_overrides(planning_plan: dict[str, Any], policy: dict[str, Any]) -> str:
    if bool(policy.get("measurement_plan_allow_current_item_overrides", False)):
        return ""
    item_overrides = planning_plan.get("item_overrides", {}) if isinstance(planning_plan, dict) else {}
    if not isinstance(item_overrides, dict) or not item_overrides:
        return ""
    override_keys = sorted(item_overrides.keys())
    return (
        "Pre-run measurement planning proposed direct current-item overrides "
        f"({', '.join(override_keys)}), but this path now runs in advisory/stop mode. "
        "Proceed as requested, insert prerequisite items with prepend_items, or stop for operator review instead "
        "of silently rewriting the current item."
    )


def join_measurement_plan_messages(*parts: str) -> str:
    cleaned: list[str] = []
    for part in parts:
        text = str(part or "").strip()
        if text and text not in cleaned:
            cleaned.append(text)
    return " ".join(cleaned)


def run_json_command(command: list[str], extra_env: dict[str, str] | None = None) -> tuple[int, dict[str, Any], str, str]:
    env = None
    if extra_env:
        env = os.environ.copy()
        env.update({str(key): str(value) for key, value in extra_env.items()})
    completed = subprocess.run(command, capture_output=True, text=True, env=env)
    stdout = completed.stdout.strip()
    payload: dict[str, Any] = {}
    if stdout:
        try:
            payload = json.loads(stdout)
        except json.JSONDecodeError:
            payload = {}
    return completed.returncode, payload, completed.stdout, completed.stderr


def build_submit_spec(
    item: dict[str, Any],
    batch_spec: dict[str, Any],
    args: argparse.Namespace,
    *,
    submission_path: str = "single_item_measurement_plan",
    measurement_plan_verified: bool | None = None,
) -> dict[str, Any]:
    requested_mode = str(item.get("mode", batch_spec.get("mode", "execute")) or "").strip().lower()
    submit_spec = build_submit_spec_from_batch_item(
        item,
        batch_spec,
        submission_path=submission_path,
        measurement_plan_verified=((requested_mode == "execute") if measurement_plan_verified is None else measurement_plan_verified),
    )
    metadata = submit_spec.get("metadata", {}) if isinstance(submit_spec.get("metadata", {}), dict) else {}
    metadata = copy.deepcopy(metadata)
    batch_id = str(batch_spec.get("batch_id", "") or "").strip()
    item_id = str(item.get("id", "") or "").strip()
    if batch_id:
        metadata.setdefault("batch_id", batch_id)
    if item_id:
        metadata.setdefault("batch_item_id", item_id)
    if submit_spec.get("requested_by") is not None:
        metadata.setdefault("requested_by", submit_spec.get("requested_by"))
    if submit_spec.get("submission_path") is not None:
        metadata.setdefault("submission_path", submit_spec.get("submission_path"))
    if submit_spec.get("measurement_plan_verified") is not None:
        metadata.setdefault("measurement_plan_verified", submit_spec.get("measurement_plan_verified"))
    submit_spec["metadata"] = metadata
    return submit_spec


def build_queue_command_from_submit_spec(
    submit_spec: dict[str, Any],
    args: argparse.Namespace,
    *,
    wait_for_result: bool = True,
) -> list[str]:
    helper_path = Path(args.queue_helper).expanduser().resolve() if args.queue_helper else (WORKSPACE_ROOT / "enqueue_nv_sequence_direct.py")
    command = [
        sys.executable,
        str(helper_path),
        "--skip-measurement-plan",
        "--submit-spec-json",
        json.dumps(submit_spec, ensure_ascii=False),
        "--timeout-seconds",
        str(args.timeout_seconds),
        "--poll-seconds",
        str(args.poll_seconds),
        "--no-runtime-watch",
    ]
    if wait_for_result:
        command.append("--wait-for-result")
    else:
        command.append("--no-wait-for-result")

    return command


def build_queue_command(
    item: dict[str, Any],
    batch_spec: dict[str, Any],
    args: argparse.Namespace,
    *,
    submission_path: str = "single_item_measurement_plan",
    measurement_plan_verified: bool | None = None,
    wait_for_result: bool = True,
) -> list[str]:
    submit_spec = build_submit_spec(
        item,
        batch_spec,
        args,
        submission_path=submission_path,
        measurement_plan_verified=measurement_plan_verified,
    )
    return build_queue_command_from_submit_spec(submit_spec, args, wait_for_result=wait_for_result)


def build_preview_advisory_command(item: dict[str, Any], batch_spec: dict[str, Any], args: argparse.Namespace) -> list[str]:
    command = build_queue_command(
        item,
        batch_spec,
        args,
        submission_path="pre_enqueue_advisory_preview",
        measurement_plan_verified=False,
    )
    command.append("--preview-job-advisory-only")
    return command


def submit_item_with_idempotence_guard(
    item: dict[str, Any],
    batch_spec: dict[str, Any],
    args: argparse.Namespace,
    *,
    batch_id: str,
    item_state: dict[str, Any],
    state_path: Path,
    extra_env: dict[str, str] | None = None,
) -> tuple[int, dict[str, Any], str, str, dict[str, Any]]:
    submit_spec = build_submit_spec(
        item,
        batch_spec,
        args,
        submission_path="single_item_measurement_plan",
        measurement_plan_verified=True,
    )
    requested_mode = str(submit_spec.get("mode", "") or "").strip().lower()
    item_id = str(item_state.get("id", item.get("id", "item")) or "item")
    if requested_mode != "execute":
        queue_command = build_queue_command_from_submit_spec(submit_spec, args, wait_for_result=True)
        returncode, response, stdout, stderr = run_json_command(queue_command, extra_env=extra_env)
        return returncode, response, stdout, stderr, {
            "action": "direct_submit",
            "mode": requested_mode,
            "submit_spec_signature": build_submit_spec_signature(submit_spec, batch_id=batch_id, item_id=item_id),
        }

    queue_root = infer_queue_root_for_item(item_state)
    lock_path = submission_lock_path(state_path, item_id)
    try:
        lock_handle = acquire_submission_lock(lock_path, timeout_seconds=SUBMISSION_LOCK_WAIT_SECONDS)
        write_submission_lock_metadata(
            lock_handle,
            {
                "batch_id": batch_id,
                "item_id": item_id,
                "mode": requested_mode,
                "queue_root": str(queue_root),
                "pid": os.getpid(),
                "acquired_at": now_iso(),
            },
        )
    except TimeoutError as exc:
        return submission_guard_failure_response(
            action="submission_lock_timeout",
            error_code="SUBMISSION_LOCK_TIMEOUT",
            error_message=str(exc),
            requested_mode=requested_mode,
            queue_root=queue_root,
            lock_path=lock_path,
            submit_spec=submit_spec,
            batch_id=batch_id,
            item_id=item_id,
        )
    except OSError as exc:
        return submission_guard_failure_response(
            action="submission_lock_unavailable",
            error_code="SUBMISSION_LOCK_UNAVAILABLE",
            error_message=f"Could not acquire or write submission lock {lock_path}: {exc}",
            requested_mode=requested_mode,
            queue_root=queue_root,
            lock_path=lock_path,
            submit_spec=submit_spec,
            batch_id=batch_id,
            item_id=item_id,
        )

    attach_match: dict[str, Any] = {}
    attach_action = ""
    attach_stderr = ""
    returncode = 0
    enqueue_response: dict[str, Any] = {}
    stdout = ""
    stderr = ""
    try:
        try:
            match = find_equivalent_inflight_job(queue_root, submit_spec, batch_id=batch_id, item_id=item_id)
        except QueueRootUnavailableError as exc:
            return submission_guard_failure_response(
                action="idempotence_guard_failed_closed",
                error_code="QUEUE_ROOT_UNAVAILABLE",
                error_message=str(exc),
                requested_mode=requested_mode,
                queue_root=queue_root,
                lock_path=lock_path,
                submit_spec=submit_spec,
                batch_id=batch_id,
                item_id=item_id,
            )
        if match:
            attach_match = match
            attach_action = "attached_existing"
        else:
            queue_command = build_queue_command_from_submit_spec(submit_spec, args, wait_for_result=False)
            returncode, enqueue_response, stdout, stderr = run_json_command(queue_command, extra_env=extra_env)
            if returncode != 0:
                try:
                    fallback_match = find_equivalent_inflight_job(queue_root, submit_spec, batch_id=batch_id, item_id=item_id)
                except QueueRootUnavailableError as exc:
                    return submission_guard_failure_response(
                        action="idempotence_guard_failed_closed_after_submit_error",
                        error_code="QUEUE_ROOT_UNAVAILABLE",
                        error_message=str(exc),
                        requested_mode=requested_mode,
                        queue_root=queue_root,
                        lock_path=lock_path,
                        submit_spec=submit_spec,
                        batch_id=batch_id,
                        item_id=item_id,
                        stderr=stderr,
                    )
                if fallback_match:
                    attach_match = fallback_match
                    attach_action = "attached_existing_after_submit_error"
                    attach_stderr = stderr
                else:
                    return returncode, enqueue_response, stdout, stderr, {
                        "action": "submit_failed_before_attach",
                        "lock_path": str(lock_path),
                        "queue_root": str(queue_root),
                        "submit_spec_signature": build_submit_spec_signature(submit_spec, batch_id=batch_id, item_id=item_id),
                    }
    finally:
        try:
            lock_handle.close()
        except Exception:
            pass

    if attach_match:
        try:
            response = wait_for_existing_job_attachment(attach_match, args, submit_spec)
        except QueueRootUnavailableError as exc:
            return submission_guard_failure_response(
                action=f"{attach_action}_wait_failed_closed",
                error_code="QUEUE_ROOT_UNAVAILABLE",
                error_message=str(exc),
                requested_mode=requested_mode,
                queue_root=queue_root,
                lock_path=lock_path,
                submit_spec=submit_spec,
                batch_id=batch_id,
                item_id=item_id,
                stderr=attach_stderr,
            )
        attach_stdout = {
            "ok": True,
            "job_id": response.get("job_id", ""),
            "queue_root": response.get("queue_root", ""),
            "attached_existing": response.get("attached_existing", {}),
        }
        if stdout:
            attach_stdout["submit_stdout"] = stdout
        return 0, response, json.dumps(attach_stdout, ensure_ascii=False), attach_stderr, {
            "action": attach_action,
            "lock_path": str(lock_path),
            "matched_job_id": str(attach_match.get("job_id", "") or ""),
            "matched_state": str(attach_match.get("state", "") or ""),
            "matched_job_path": str(attach_match.get("job_path", "") or ""),
            "queue_root": str(queue_root),
            "submit_spec_signature": build_submit_spec_signature(submit_spec, batch_id=batch_id, item_id=item_id),
        }

    job_id = str(enqueue_response.get("job_id", "") or "").strip()
    response_queue_root = str(enqueue_response.get("queue_root", "") or "").strip()
    if response_queue_root:
        queue_root = Path(response_queue_root)
    if not job_id:
        return returncode, enqueue_response, stdout, stderr, {
            "action": "submit_missing_job_id",
            "lock_path": str(lock_path),
            "queue_root": str(queue_root),
            "submit_spec_signature": build_submit_spec_signature(submit_spec, batch_id=batch_id, item_id=item_id),
        }
    if not callable(wait_for_runtime_result):
        raise RuntimeError("nv_bridge_runtime_watch.wait_for_result is unavailable; cannot wait for submitted execute job safely.")
    enqueue_job = copy.deepcopy(enqueue_response.get("job", {})) if isinstance(enqueue_response.get("job", {}), dict) else {}
    enqueue_metadata = enqueue_job.get("metadata", {}) if isinstance(enqueue_job.get("metadata", {}), dict) else {}
    requested_by = str(enqueue_metadata.get("requested_by", "") or "openclaw-batch-run")
    try:
        wait_response = wait_for_runtime_result(
            queue_root,
            job_id,
            float(args.timeout_seconds),
            float(args.poll_seconds),
            job=enqueue_job or None,
            config={"requested_by": requested_by},
        )
    except OSError as exc:
        return submission_guard_failure_response(
            action="submitted_new_wait_failed_closed",
            error_code="QUEUE_ROOT_UNAVAILABLE",
            error_message=str(QueueRootUnavailableError(queue_root, f"waiting for submitted job {job_id}", exc)),
            requested_mode=requested_mode,
            queue_root=queue_root,
            lock_path=lock_path,
            submit_spec=submit_spec,
            batch_id=batch_id,
            item_id=item_id,
            stderr=stderr,
        )
    response = merge_enqueue_wait_response(enqueue_response, wait_response)
    response["submission_guard"] = {
        "action": "submitted_new",
        "lock_path": str(lock_path),
    }
    return 0, response, stdout, stderr, {
        "action": "submitted_new",
        "lock_path": str(lock_path),
        "job_id": job_id,
        "queue_root": str(queue_root),
        "submit_spec_signature": build_submit_spec_signature(submit_spec, batch_id=batch_id, item_id=item_id),
    }


def summarize_pre_enqueue_advisory(payload: dict[str, Any], returncode: int, stdout: str, stderr: str) -> dict[str, Any]:
    advisory = payload.get("job_advisory", {}) if isinstance(payload, dict) else {}
    if not isinstance(advisory, dict):
        advisory = {}

    warnings = advisory.get("warnings", [])
    blockers = advisory.get("blockers", [])
    notes = advisory.get("notes", [])
    runner = payload.get("job_advisory_runner", {}) if isinstance(payload, dict) else {}
    if not isinstance(runner, dict):
        runner = {}

    acquisition = copy.deepcopy(advisory.get("acquisition", {})) if isinstance(advisory.get("acquisition", {}), dict) else {}
    estimated_runtime = copy.deepcopy(advisory.get("estimated_runtime", {})) if isinstance(advisory.get("estimated_runtime", {}), dict) else {}
    recent_nv_drift = copy.deepcopy(advisory.get("recent_nv_drift", {})) if isinstance(advisory.get("recent_nv_drift", {}), dict) else {}
    guidance = copy.deepcopy(advisory.get("guidance", {})) if isinstance(advisory.get("guidance", {}), dict) else {}
    runtime_available = bool(estimated_runtime)
    drift_available = bool(recent_nv_drift)

    error_code = str(advisory.get("error_code", "") or "")
    error_message = str(advisory.get("error_message", "") or "")
    if not advisory.get("ok", False) and not error_code:
        if not runtime_available and drift_available:
            error_code = "PRE_ENQUEUE_RUNTIME_UNAVAILABLE"
        elif not runtime_available and not drift_available:
            error_code = "PRE_ENQUEUE_ADVISORY_INCOMPLETE"
        else:
            error_code = "PRE_ENQUEUE_ADVISORY_WARNING"
    if not error_message and not advisory.get("ok", False):
        fallback_message = ""
        candidate_lists = []
        if isinstance(blockers, list):
            candidate_lists.append(blockers)
        if isinstance(warnings, list):
            candidate_lists.append(warnings)
        if isinstance(notes, list):
            candidate_lists.append(notes)

        preferred_tokens = ("missing", "unavailable", "failed", "cannot", "could not", "blocked", "required")
        candidates = [str(value or "") for group in candidate_lists for value in group if str(value or "").strip()]
        for candidate in candidates:
            lowered = candidate.lower()
            if any(token in lowered for token in preferred_tokens):
                fallback_message = candidate
                break
        if not fallback_message and candidates:
            fallback_message = candidates[0]
        error_message = truncate_text(fallback_message or stderr or stdout, 1200)

    return {
        "requested": True,
        "ok": bool(advisory.get("ok", False)),
        "source": "claw_preview_job_advisory",
        "job_id": str(payload.get("job_id", "") or ""),
        "sequence": str(payload.get("sequence", "") or ""),
        "sequence_name": str(advisory.get("sequence_name", "") or ""),
        "acquisition": acquisition,
        "estimated_runtime": estimated_runtime,
        "recent_nv_drift": recent_nv_drift,
        "guidance": guidance,
        "runtime_available": runtime_available,
        "drift_available": drift_available,
        "warnings": copy.deepcopy(warnings[:8]) if isinstance(warnings, list) else [],
        "notes": copy.deepcopy(notes[:6]) if isinstance(notes, list) else [],
        "blockers": copy.deepcopy(blockers[:6]) if isinstance(blockers, list) else [],
        "error_code": error_code,
        "error_message": error_message,
        "runner": {
            "returncode": int(returncode),
            "timed_out": bool(runner.get("timed_out", False)),
            "stdout": truncate_text(stdout, 1200),
            "stderr": truncate_text(stderr, 1200),
        },
    }


def fetch_pre_enqueue_advisory(item: dict[str, Any], batch_spec: dict[str, Any], args: argparse.Namespace, policy: dict[str, Any]) -> dict[str, Any]:
    if not bool(policy.get("pre_enqueue_advisory_enabled", True)):
        return {
            "requested": False,
            "ok": False,
            "reason": "pre_enqueue_advisory_disabled",
        }

    requested_mode = str(item.get("mode", batch_spec.get("mode", "execute")) or "").strip().lower()
    if requested_mode != "execute":
        return {
            "requested": False,
            "ok": False,
            "reason": "mode_not_execute",
        }

    command = build_preview_advisory_command(item, batch_spec, args)
    returncode, payload, stdout, stderr = run_json_command(
        command,
        extra_env={
            INTERNAL_MEASUREMENT_PLAN_ENV: "1",
            SUBMISSION_PATH_ENV: "pre_enqueue_advisory_preview",
        },
    )
    summary = summarize_pre_enqueue_advisory(payload, returncode, stdout, stderr)
    if returncode != 0 and not summary.get("error_code"):
        summary["error_code"] = "PRE_ENQUEUE_ADVISORY_HELPER_FAILED"
    if returncode != 0 and not summary.get("error_message"):
        summary["error_message"] = truncate_text(stderr or stdout, 1200)
    return summary


def normalize_analysis_spec(analysis: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(analysis, dict):
        return {}
    fit_kind = str(analysis.get("fit_kind", "None") or "None").strip()
    if fit_kind not in VALID_ANALYSIS_FIT_KINDS:
        fit_kind = "None"
    normalized: dict[str, Any] = {"fit_kind": fit_kind}
    aux_key = str(analysis.get("aux_key", "") or "").strip()
    if aux_key:
        normalized["aux_key"] = aux_key
    aux_slot = analysis.get("aux_slot")
    if aux_slot is not None:
        try:
            normalized["aux_slot"] = int(aux_slot)
        except (TypeError, ValueError):
            pass
    if analysis.get("discard_first_average"):
        normalized["discard_first_average"] = True
    if fit_kind == "CustomFunction":
        custom_fit_function = str(analysis.get("custom_fit_function", "") or "").strip()
        if custom_fit_function:
            normalized["custom_fit_function"] = custom_fit_function
        custom_fit_path = str(analysis.get("custom_fit_path", "") or "").strip()
        if custom_fit_path:
            normalized["custom_fit_path"] = custom_fit_path
        if "custom_fit_args" in analysis:
            normalized["custom_fit_args"] = copy.deepcopy(analysis.get("custom_fit_args"))
        fit_label = str(analysis.get("fit_label", "") or "").strip()
        if fit_label:
            normalized["fit_label"] = fit_label
    if normalized.get("aux_key"):
        persist_aux_update = analysis.get("persist_aux_update")
        if isinstance(persist_aux_update, bool):
            normalized["persist_aux_update"] = persist_aux_update
        else:
            normalized["persist_aux_update"] = False
    return normalized


def build_analysis_command(analysis_spec: dict[str, Any], result_path: str) -> list[str]:
    raise RuntimeError(
        "Legacy nv_result_analyze.py auto-analysis is disabled; use raw export "
        "and transparent task-specific analysis instead."
    )


def build_analysis_evidence_only_result(
    analysis_attempts: list[dict[str, Any]],
    *,
    message: str = "",
) -> dict[str, Any]:
    latest_response: dict[str, Any] = {}
    if analysis_attempts:
        candidate = analysis_attempts[-1].get("response", {})
        if isinstance(candidate, dict):
            latest_response = candidate
    aux_candidate = latest_response.get("aux_update", {})
    if not (isinstance(aux_candidate, dict) and aux_candidate.get("ok")):
        aux_candidate = {}
    if not message:
        message = "Analysis saved as evidence; Aux adoption and follow-up decisions are deferred to the main project agent."
    return {
        "action": "evidence_only",
        "message": message,
        "analysis_record": {
            "attempts": analysis_attempts,
            "final_action": "evidence_only",
            "review_hook_used": False,
            "aux_adoption": "deferred_to_main_project_agent",
            "aux_candidate": copy.deepcopy(aux_candidate),
        },
        "aux_entry": {},
        "item_overrides": {},
        "insert_items_after": [],
        "insert_items_before_rerun": [],
    }


def normalize_dynamic_insert_item(raw_item: Any, default_mode: str, default_sample_id: str) -> dict[str, Any]:
    return normalize_item_spec(
        raw_item,
        require_sequence=True,
        default_mode=default_mode,
        default_sample_id=default_sample_id,
        allow_id=True,
        normalize_analysis=normalize_analysis_spec,
        use_default_mode=True,
        max_branch_items=MAX_DYNAMIC_INSERT_ITEMS_PER_PLAN,
    )


def normalize_dynamic_insert_items(raw_items: Any, default_mode: str, default_sample_id: str) -> list[dict[str, Any]]:
    if not isinstance(raw_items, list):
        return []
    normalized: list[dict[str, Any]] = []
    for raw_item in raw_items[:MAX_DYNAMIC_INSERT_ITEMS_PER_PLAN]:
        item = normalize_dynamic_insert_item(raw_item, default_mode, default_sample_id)
        if item:
            normalized.append(item)
    return normalized


def normalize_runtime_item_overrides(raw_overrides: Any, default_mode: str, default_sample_id: str) -> dict[str, Any]:
    return normalize_override_spec(
        raw_overrides,
        default_mode=default_mode,
        default_sample_id=default_sample_id,
        allowed_keys=RUNTIME_ITEM_OVERRIDE_ALLOWED_KEYS,
        normalize_analysis=normalize_analysis_spec,
        use_default_mode=True,
        max_branch_items=MAX_DYNAMIC_INSERT_ITEMS_PER_PLAN,
    )


def make_item_state(item_spec: dict[str, Any], inserted_event: dict[str, Any] | None = None) -> dict[str, Any]:
    item_id = str(item_spec.get("id", "") or item_identity_hint(item_spec))
    state = {
        "id": item_id,
        "status": "pending",
        "attempts": 0,
        "last_error_code": "",
        "last_error_message": "",
        "history": [],
        "analysis": {},
    }
    if isinstance(inserted_event, dict) and inserted_event:
        state["history"].append(copy.deepcopy(inserted_event))
    return state


def assign_unique_dynamic_item_id(candidate: str, existing_ids: set[str]) -> str:
    proposed = str(candidate or "").strip()
    if not proposed:
        proposed = "inserted_item"
    normalized = re.sub(r"[^A-Za-z0-9_]+", "_", proposed).strip("_") or "inserted_item"
    if normalized not in existing_ids:
        existing_ids.add(normalized)
        return normalized
    for index in range(2, 10000):
        trial = f"{normalized}__dyn{index}"
        if trial not in existing_ids:
            existing_ids.add(trial)
            return trial
    fallback = f"{normalized}__dyn{int(time.time())}"
    existing_ids.add(fallback)
    return fallback


def insert_dynamic_items(
    batch_spec: dict[str, Any],
    state: dict[str, Any],
    batch_spec_path: Path,
    state_path: Path,
    insert_index: int,
    items_to_insert: list[dict[str, Any]],
    *,
    source_event: str,
    source_item_id: str,
    source_message: str,
) -> list[dict[str, Any]]:
    if not items_to_insert:
        return []

    existing_ids = {
        str(item.get("id", "") or "").strip()
        for item in list(batch_spec.get("items", [])) + list(state.get("items", []))
        if isinstance(item, dict) and str(item.get("id", "") or "").strip()
    }
    inserted_specs: list[dict[str, Any]] = []
    inserted_states: list[dict[str, Any]] = []
    for ordinal, raw_item in enumerate(items_to_insert, start=1):
        item = copy.deepcopy(raw_item)
        if not isinstance(item, dict):
            continue
        candidate_id = str(
            item.get("id", "")
            or item.get("sequence_manifest_id", "")
            or item.get("sequence", "")
            or ((item.get("sequence_authoring") or {}) if isinstance(item.get("sequence_authoring"), dict) else {}).get("new_id", "")
            or f"{source_event}_{ordinal}"
        )
        item["id"] = assign_unique_dynamic_item_id(candidate_id, existing_ids)
        inserted_specs.append(item)
        inserted_states.append(
            make_item_state(
                item,
                inserted_event={
                    "at": now_iso(),
                    "event": "dynamically_inserted",
                    "message": source_message,
                    "source_event": source_event,
                    "source_item_id": source_item_id,
                },
            )
        )

    if not inserted_specs:
        return []

    batch_spec.setdefault("items", [])
    state.setdefault("items", [])
    batch_spec["items"][insert_index:insert_index] = inserted_specs
    state["items"][insert_index:insert_index] = inserted_states
    append_batch_event(
        state,
        "items_inserted",
        source_message,
        source_event=source_event,
        source_item_id=source_item_id,
        item_ids=[item.get("id", "") for item in inserted_specs],
        insert_index=int(insert_index),
    )
    update_progress(state)
    write_json(batch_spec_path, batch_spec)
    write_json(state_path, state)
    return inserted_specs


def savedexperiment_raw_export_from_response(response: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(response, dict):
        return {}
    raw_export = response.get("savedexperiment_raw_export", {})
    if isinstance(raw_export, dict) and raw_export:
        return copy.deepcopy(raw_export)
    runtime_watch = response.get("runtime_watch", {})
    if isinstance(runtime_watch, dict):
        raw_export = runtime_watch.get("savedexperiment_raw_export", {})
        if isinstance(raw_export, dict) and raw_export:
            return copy.deepcopy(raw_export)
    return {}


def result_data_path_from_response(response: dict[str, Any]) -> str:
    if not isinstance(response, dict):
        return ""
    result = response.get("result", {})
    if not isinstance(result, dict):
        result = {}
    candidates = [
        result.get("data_path", ""),
        response.get("data_path", ""),
    ]
    summary = result.get("summary", {})
    if isinstance(summary, dict):
        saved_artifact = summary.get("saved_artifact", {})
        if isinstance(saved_artifact, dict):
            candidates.append(saved_artifact.get("path", ""))
    for candidate in candidates:
        text = normalize_path_for_agent(candidate)
        if text:
            return text
    return ""


def ensure_response_savedexperiment_raw_export(response: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(response, dict):
        return {}
    existing = savedexperiment_raw_export_from_response(response)
    if existing:
        response["savedexperiment_raw_export"] = copy.deepcopy(existing)
        runtime_watch = response.get("runtime_watch", {})
        if isinstance(runtime_watch, dict):
            runtime_watch.setdefault("savedexperiment_path", existing.get("data_path", ""))
            runtime_watch["savedexperiment_raw_export"] = copy.deepcopy(existing)
            response["runtime_watch"] = runtime_watch
        return existing
    data_path = result_data_path_from_response(response)
    if not data_path or not callable(export_savedexperiment_mat_raw_files):
        return {}
    try:
        payloads = export_savedexperiment_mat_raw_files([data_path])
        raw_export = payloads[0] if payloads and isinstance(payloads[0], dict) else {}
    except Exception as exc:
        raw_export = {
            "ok": False,
            "source": "savedexperiment_mat_raw_export",
            "data_path": data_path,
            "error_code": "SAVEDEXPERIMENT_RAW_EXPORT_FAILED",
            "error_message": str(exc),
            "scan": {},
            "extra_variables": {},
            "diagnostic_figures": {},
            "warnings": [],
        }
    if not raw_export:
        return {}
    response["savedexperiment_raw_export"] = copy.deepcopy(raw_export)
    runtime_watch = response.get("runtime_watch", {})
    if not isinstance(runtime_watch, dict):
        runtime_watch = {}
    runtime_watch.setdefault("savedexperiment_path", raw_export.get("data_path", data_path))
    runtime_watch["savedexperiment_raw_export"] = copy.deepcopy(raw_export)
    response["runtime_watch"] = runtime_watch
    return copy.deepcopy(raw_export)


def should_run_analysis(item: dict[str, Any], response: dict[str, Any], policy: dict[str, Any] | None = None) -> bool:
    # Legacy nv_result_analyze.py auto-analysis is disabled. Project agents
    # should review raw exports and write transparent task-specific analysis.
    return False
    if not (isinstance(policy, dict) and bool(policy.get("analysis_auto_run_enabled", False))):
        return False
    analysis = item.get("analysis", {})
    if not isinstance(analysis, dict) or not analysis.get("fit_kind"):
        return False
    mode = str(item.get("mode", "") or "").strip().lower()
    if mode and mode != "execute":
        return False
    result = response.get("result", {})
    data_path = str(result.get("data_path", "")).strip()
    return bool(data_path)


def is_success(response: dict[str, Any]) -> bool:
    return bool(response.get("result", {}).get("status") == "completed" or response.get("final_state") == "done")


def normalize_policy_rules(policy: dict[str, Any], key: str, defaults: set[str] | tuple[str, ...]) -> list[str]:
    value = policy.get(key, defaults)
    if isinstance(value, (list, tuple, set)):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return [str(item).strip() for item in defaults if str(item).strip()]


def classify_error(error_code: str, error_message: str, policy: dict[str, Any]) -> tuple[str, str]:
    error_code = str(error_code or "").strip()
    normalized_message = str(error_message or "").strip().lower()
    if error_code in HARD_STOP_ERROR_CODES:
        return "stop", "hard_stop_error_codes"

    retry_message_substrings = tuple(
        rule.lower() for rule in normalize_policy_rules(policy, "retry_error_message_substrings", DEFAULT_RETRY_ERROR_MESSAGE_SUBSTRINGS)
    )
    stop_message_substrings = tuple(
        rule.lower() for rule in normalize_policy_rules(policy, "stop_error_message_substrings", DEFAULT_STOP_ERROR_MESSAGE_SUBSTRINGS)
    )

    if normalized_message:
        if any(rule and rule in normalized_message for rule in retry_message_substrings):
            return "retry", "retry_error_message_substrings"
        if any(rule and rule in normalized_message for rule in stop_message_substrings):
            return "stop", "stop_error_message_substrings"

    if not error_code:
        default_action = str(policy.get("default_unknown_error_action", "retry") or "retry").strip().lower()
        return default_action, "default_unknown_error_action"

    retry_codes = set(normalize_policy_rules(policy, "retry_error_codes", DEFAULT_RETRY_ERROR_CODES))
    stop_codes = set(normalize_policy_rules(policy, "stop_error_codes", DEFAULT_STOP_ERROR_CODES))
    retry_prefixes = tuple(normalize_policy_rules(policy, "retry_error_prefixes", DEFAULT_RETRY_ERROR_PREFIXES))
    stop_prefixes = tuple(normalize_policy_rules(policy, "stop_error_prefixes", DEFAULT_STOP_ERROR_PREFIXES))

    if error_code in retry_codes:
        return "retry", "retry_error_codes"
    if error_code in stop_codes:
        return "stop", "stop_error_codes"
    if any(error_code.startswith(prefix) for prefix in retry_prefixes):
        return "retry", "retry_error_prefixes"
    if any(error_code.startswith(prefix) for prefix in stop_prefixes):
        return "stop", "stop_error_prefixes"

    default_action = str(policy.get("default_unknown_error_action", "retry") or "retry").strip().lower()
    return default_action, "default_unknown_error_action"


def classify_attempt(response: dict[str, Any], returncode: int, policy: dict[str, Any]) -> dict[str, Any]:
    result = response.get("result", {}) if isinstance(response, dict) else {}
    error_code = str(result.get("error_code", "") or response.get("error_code", "")).strip()
    error_message = str(result.get("error_message", "") or response.get("error_message", "")).strip()
    timed_out = bool(response.get("timed_out", False))
    runtime_watch = response.get("runtime_watch", {}) if isinstance(response, dict) else {}
    runtime_watch_anomaly = runtime_watch.get("anomaly", {}) if isinstance(runtime_watch, dict) else {}

    if not error_code and isinstance(runtime_watch_anomaly, dict) and bool(runtime_watch_anomaly.get("detected", False)):
        error_code = str(runtime_watch_anomaly.get("error_code", "") or "").strip()
    if not error_message and isinstance(runtime_watch_anomaly, dict) and bool(runtime_watch_anomaly.get("detected", False)):
        error_message = str(runtime_watch_anomaly.get("message", "") or "").strip()

    if returncode == 0 and is_success(response):
        return {
            "action": "complete",
            "reason": "completed",
            "error_code": error_code,
            "error_message": error_message,
            "rule_source": "success",
        }
    if isinstance(runtime_watch_anomaly, dict) and bool(runtime_watch_anomaly.get("detected", False)):
        if not error_code:
            error_code = "RUNTIME_WATCH_TRIGGERED"
        if not error_message:
            error_message = "Runtime watch detected an anomaly."
        if not bool(runtime_watch_anomaly.get("retry_recommended", False)):
            return {
                "action": "stop",
                "reason": "runtime_watch",
                "error_code": error_code,
                "error_message": error_message,
                "rule_source": "runtime_watch",
            }
        return {
            "action": "retry",
            "reason": "runtime_watch",
            "error_code": error_code,
            "error_message": error_message,
            "rule_source": "runtime_watch",
        }
    if timed_out:
        return {
            "action": "retry",
            "reason": "timeout",
            "error_code": "TIMEOUT",
            "error_message": error_message or "Queue helper timed out while waiting for the result.",
            "rule_source": "timeout",
        }
    if returncode != 0 and not response:
        return {
            "action": "stop",
            "reason": "empty_error_response",
            "error_code": error_code or "COMMAND_FAILED",
            "error_message": error_message or "Queue helper returned a non-zero exit code without a JSON response.",
            "rule_source": "empty_error_response",
        }
    action, rule_source = classify_error(error_code, error_message, policy)
    return {
        "action": action,
        "reason": "classified_error_code",
        "error_code": error_code,
        "error_message": error_message,
        "rule_source": rule_source,
    }


def default_policy(batch_spec: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    spec_policy = copy.deepcopy(batch_spec.get("policy", {}))
    if not isinstance(spec_policy, dict):
        spec_policy = {}

    max_attempts = spec_policy.get("max_attempts_per_item")
    if args.max_attempts_per_item is not None:
        max_attempts = int(args.max_attempts_per_item)
    elif max_attempts is None:
        max_attempts = DEFAULT_MAX_ATTEMPTS_PER_ITEM

    policy = {
        "max_attempts_per_item": max_attempts,
        "retry_delay_seconds": float(args.retry_delay_seconds),
        "stop_on_aux_resolution_failure": True,
        "stop_on_fatal_failure": True,
        "continue_on_analysis_failure": True,
        "measurement_plan_enabled": False,
        "measurement_plan_required": False,
        "measurement_plan_advisory_only": True,
        "measurement_plan_allow_current_item_overrides": False,
        "measurement_plan_timeout_seconds": float(args.measurement_plan_timeout_seconds),
        "pre_enqueue_advisory_enabled": True,
        "pre_enqueue_advisory_required": False,
        "analysis_review_enabled": False,
        "analysis_review_required": False,
        "analysis_evidence_only": True,
        "analysis_auto_run_enabled": False,
        "analysis_auto_adopt_aux": False,
        "resume_incomplete_items": True,
        "agent_recovery_enabled": True,
        "agent_recovery_required_for_retry": False,
        "retry_error_codes": sorted(DEFAULT_RETRY_ERROR_CODES),
        "stop_error_codes": sorted(DEFAULT_STOP_ERROR_CODES),
        "retry_error_prefixes": list(DEFAULT_RETRY_ERROR_PREFIXES),
        "stop_error_prefixes": list(DEFAULT_STOP_ERROR_PREFIXES),
        "retry_error_message_substrings": list(DEFAULT_RETRY_ERROR_MESSAGE_SUBSTRINGS),
        "stop_error_message_substrings": list(DEFAULT_STOP_ERROR_MESSAGE_SUBSTRINGS),
        "default_unknown_error_action": "retry",
    }
    policy.update(spec_policy)
    return policy


def infer_queue_root_from_value(raw_value: str) -> Path | None:
    value = str(raw_value or "").strip()
    if not value:
        return None
    path = Path(value)
    parts = path.parts
    for marker in ("queued", "running", "done", "failed"):
        if marker in parts:
            return Path(*parts[: parts.index(marker)])
    return None


def infer_queue_root_from_history_entry(history_entry: dict[str, Any]) -> Path | None:
    for key in ("queue_root", "job_dir", "job_path", "result_path"):
        queue_root = infer_queue_root_from_value(history_entry.get(key, ""))
        if queue_root is not None:
            return queue_root

    pre_enqueue_advisory = history_entry.get("pre_enqueue_advisory", {}) if isinstance(history_entry.get("pre_enqueue_advisory", {}), dict) else {}
    advisory_runner = pre_enqueue_advisory.get("runner", {}) if isinstance(pre_enqueue_advisory.get("runner", {}), dict) else {}
    for key in ("queue_root", "job_dir", "job_path", "result_path"):
        queue_root = infer_queue_root_from_value(pre_enqueue_advisory.get(key, ""))
        if queue_root is not None:
            return queue_root
        queue_root = infer_queue_root_from_value(advisory_runner.get(key, ""))
        if queue_root is not None:
            return queue_root

    stdout = str(history_entry.get("stdout", "") or "").strip()
    if stdout:
        try:
            payload = json.loads(stdout)
        except json.JSONDecodeError:
            payload = {}
        if isinstance(payload, dict):
            for key in ("queue_root", "job_dir", "job_path", "result_path"):
                queue_root = infer_queue_root_from_value(payload.get(key, ""))
                if queue_root is not None:
                    return queue_root

    advisory_stdout = str(advisory_runner.get("stdout", "") or "").strip()
    if advisory_stdout:
        try:
            advisory_payload = json.loads(advisory_stdout)
        except json.JSONDecodeError:
            advisory_payload = {}
        if isinstance(advisory_payload, dict):
            for key in ("queue_root", "job_dir", "job_path", "result_path"):
                queue_root = infer_queue_root_from_value(advisory_payload.get(key, ""))
                if queue_root is not None:
                    return queue_root
    return None


def find_prior_completed_attempt(item_state: dict[str, Any]) -> dict[str, Any] | None:
    ignored_job_ids = {
        str(job_id).strip()
        for job_id in item_state.get("ignored_prior_success_job_ids", [])
        if str(job_id).strip()
    }
    for history_entry in reversed(item_state.get("history", [])):
        job_id = str(history_entry.get("job_id", "") or "").strip()
        if not job_id:
            continue
        if job_id in ignored_job_ids:
            continue

        explicit_result_path = str(history_entry.get("result_path", "") or "").strip()
        if explicit_result_path:
            result_path = Path(explicit_result_path)
            if result_path.is_file():
                try:
                    result_payload = read_json(result_path)
                except ValueError:
                    result_payload = {}
                if str(result_payload.get("status", "") or "") == "completed":
                    return {
                        "job_id": job_id,
                        "result_path": str(result_path),
                        "result": result_payload,
                    }

        queue_root = infer_queue_root_from_history_entry(history_entry)
        if queue_root is None:
            continue

        result_path = queue_root / "done" / job_id / "result.json"
        if not result_path.is_file():
            continue

        try:
            result_payload = read_json(result_path)
        except ValueError:
            continue

        if str(result_payload.get("status", "") or "") == "completed":
            return {
                "job_id": job_id,
                "result_path": str(result_path),
                "result": result_payload,
            }
    return None


def latest_failure_artifacts(response: dict[str, Any]) -> dict[str, str]:
    artifacts = {
        "job_id": str(response.get("job_id", "") or "").strip(),
        "result_path": str(response.get("result_path", "") or "").strip(),
        "job_dir": str(response.get("job_dir", "") or "").strip(),
        "bridge_log_path": "",
        "job_json_path": "",
    }
    job_dir = artifacts["job_dir"]
    if job_dir:
        artifacts["bridge_log_path"] = str(Path(job_dir) / "bridge.log")
        artifacts["job_json_path"] = str(Path(job_dir) / "job.json")
    return artifacts


def summarize_failure_history_entry(entry: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(entry, dict) or not entry:
        return {}
    response = response_from_history_entry(entry)
    artifacts = latest_failure_artifacts(response)
    result_payload = try_read_json(Path(artifacts["result_path"])) if artifacts.get("result_path") else {}
    job_payload = try_read_json(Path(artifacts["job_json_path"])) if artifacts.get("job_json_path") else {}
    bridge_log_tail = tail_text_file(Path(artifacts["bridge_log_path"])) if artifacts.get("bridge_log_path") else ""
    retry_rule = entry.get("retry_rule", {}) if isinstance(entry.get("retry_rule"), dict) else {}
    return {
        "at": str(entry.get("at", "") or ""),
        "job_id": str(response.get("job_id", "") or ""),
        "final_state": str(response.get("final_state", "") or ""),
        "result_path": normalize_path_for_agent(response.get("result_path", "")),
        "error_code": str(retry_rule.get("error_code", "") or ""),
        "error_message": truncate_text(retry_rule.get("error_message", ""), 1200),
        "rule_action": str(retry_rule.get("action", "") or ""),
        "rule_reason": str(retry_rule.get("reason", "") or ""),
        "rule_source": str(retry_rule.get("rule_source", "") or ""),
        "outcome_summary": copy.deepcopy(response.get("outcome_summary", {})),
        "result_summary": summarize_result_for_recovery(result_payload),
        "job_summary": summarize_job_for_recovery(job_payload),
        "bridge_log_tail": bridge_log_tail,
    }


def summarize_plan_history_entry(entry: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(entry, dict) or not entry:
        return {}
    plan = entry.get("plan", {}) if isinstance(entry.get("plan"), dict) else {}
    return {
        "at": str(entry.get("at", "") or ""),
        "event": str(entry.get("event", "") or ""),
        "message": str(entry.get("message", "") or ""),
        "plan_path": str(entry.get("plan_path", "") or ""),
        "plan": copy.deepcopy(plan),
    }


def build_attempt_context_for_planning(item_state: dict[str, Any]) -> dict[str, Any]:
    attempts = int(item_state.get("attempts", 0)) if isinstance(item_state, dict) else 0
    status = str(item_state.get("status", "") or "") if isinstance(item_state, dict) else ""
    last_failure = summarize_failure_history_entry(latest_failed_queue_submit(item_state))
    last_recovery_plan = summarize_plan_history_entry(latest_history_event(item_state, "recovery_plan_received", "agent_recovery_plan"))
    last_retry_adjustment = compact_history_entry(latest_history_event(item_state, "retry_adjusted"))
    return {
        "is_retry": bool(attempts > 0 or status == "retrying"),
        "next_attempt": attempts + 1,
        "status_before_attempt": status,
        "current_retry_overrides": copy.deepcopy(item_state.get("retry_overrides", {})) if isinstance(item_state, dict) else {},
        "last_failure": last_failure,
        "last_recovery_plan": last_recovery_plan,
        "last_retry_adjustment": last_retry_adjustment,
    }


def load_recovery_case_library_matches(
    case_library_root: Path,
    rendered_item: dict[str, Any],
    error_code: str = "",
    max_matches: int = DEFAULT_CASE_LIBRARY_MATCH_LIMIT,
) -> list[dict[str, Any]]:
    if not case_library_root.is_dir():
        return []

    sample_id = str(rendered_item.get("sample_id", "") or "").strip()
    sequence = str(rendered_item.get("sequence", "") or "").strip()
    sequence_manifest_id = str(rendered_item.get("sequence_manifest_id", "") or "").strip()
    wanted_error = str(error_code or "").strip()
    scored_matches: list[tuple[int, float, dict[str, Any]]] = []

    for path in case_library_root.rglob("*.json"):
        try:
            case = read_json(path)
        except ValueError:
            continue
        if not isinstance(case, dict):
            continue

        case_sample = str(case.get("sample_id", "") or "").strip()
        case_sequence = str(case.get("sequence", "") or "").strip()
        case_manifest = str(case.get("sequence_manifest_id", "") or "").strip()
        failure = case.get("failure", {}) if isinstance(case.get("failure"), dict) else {}
        case_error = str(failure.get("error_code", "") or "").strip()

        score = 0
        matched_fields: list[str] = []
        if sample_id and case_sample == sample_id:
            score += 3
            matched_fields.append("sample_id")
        if sequence_manifest_id and case_manifest == sequence_manifest_id:
            score += 4
            matched_fields.append("sequence_manifest_id")
        elif sequence and case_sequence == sequence:
            score += 3
            matched_fields.append("sequence")
        if wanted_error and case_error == wanted_error:
            score += 4
            matched_fields.append("error_code")

        if score <= 0:
            continue

        success = case.get("success", {}) if isinstance(case.get("success"), dict) else {}
        recovery_plan = case.get("recovery_plan", {}) if isinstance(case.get("recovery_plan"), dict) else {}
        match = {
            "case_path": str(path),
            "saved_at": str(case.get("saved_at", "") or ""),
            "batch_id": str(case.get("batch_id", "") or ""),
            "item_id": str(case.get("item_id", "") or ""),
            "sample_id": case_sample,
            "sequence": case_sequence,
            "sequence_manifest_id": case_manifest,
            "failure": {
                "error_code": case_error,
                "error_message": truncate_text(failure.get("error_message", ""), 800),
                "rule_reason": str(failure.get("rule_reason", "") or ""),
                "rule_source": str(failure.get("rule_source", "") or ""),
            },
            "recovery_plan": {
                "action": str(recovery_plan.get("action", "") or ""),
                "reason": truncate_text(recovery_plan.get("reason", ""), 800),
                "operator_message": truncate_text(recovery_plan.get("operator_message", ""), 800),
                "item_overrides": copy.deepcopy(recovery_plan.get("item_overrides", {})) if isinstance(recovery_plan.get("item_overrides"), dict) else {},
            },
            "success": {
                "result_path": normalize_path_for_agent(success.get("result_path", "")),
                "data_path": normalize_path_for_agent(success.get("data_path", "")),
                "run_id": str(success.get("run_id", "") or ""),
                "status": str(success.get("status", "") or ""),
            },
            "similarity": {
                "score": score,
                "matched_fields": matched_fields,
            },
        }
        try:
            mtime = path.stat().st_mtime
        except OSError:
            mtime = 0.0
        scored_matches.append((score, mtime, match))

    scored_matches.sort(key=lambda item: (-item[0], -item[1]))
    return [match for _, _, match in scored_matches[:max_matches]]


def build_recovery_case_record(
    batch_id: str,
    item_spec: dict[str, Any],
    rendered_item: dict[str, Any],
    item_state: dict[str, Any],
    response: dict[str, Any],
) -> dict[str, Any]:
    latest_plan_entry = latest_history_event(item_state, "recovery_plan_received", "agent_recovery_plan")
    if not latest_plan_entry:
        return {}

    failure_entry = latest_failed_queue_submit(item_state)
    failure_summary = summarize_failure_history_entry(failure_entry)
    if not failure_summary:
        return {}

    result_path = str(response.get("result_path", "") or "").strip()
    result_payload = try_read_json(Path(result_path)) if result_path else {}
    success_summary = summarize_result_for_recovery(result_payload)
    return {
        "saved_at": now_iso(),
        "batch_id": batch_id,
        "item_id": str(item_state.get("id", "") or ""),
        "sample_id": str(rendered_item.get("sample_id", "") or item_spec.get("sample_id", "") or ""),
        "sequence": str(rendered_item.get("sequence", "") or item_spec.get("sequence", "") or ""),
        "sequence_manifest_id": str(rendered_item.get("sequence_manifest_id", "") or item_spec.get("sequence_manifest_id", "") or ""),
        "attempts_before_success": int(item_state.get("attempts", 0)),
        "failure": failure_summary,
        "recovery_plan": summarize_plan_history_entry(latest_plan_entry),
        "applied_retry_overrides": copy.deepcopy(item_state.get("retry_overrides", {})),
        "success": {
            "result_path": normalize_path_for_agent(result_path),
            "data_path": success_summary.get("data_path", ""),
            "run_id": str(success_summary.get("run_id", "") or ""),
            "status": str(success_summary.get("status", "") or ""),
            "result_summary": success_summary,
            "analysis_record": copy.deepcopy(item_state.get("analysis", {})),
        },
    }


def maybe_save_successful_recovery_case(
    case_library_root: Path,
    batch_id: str,
    item_spec: dict[str, Any],
    rendered_item: dict[str, Any],
    item_state: dict[str, Any],
    response: dict[str, Any],
) -> str:
    if not isinstance(item_state, dict):
        return ""
    existing = str(item_state.get("successful_recovery_case_path", "") or "").strip()
    if existing:
        return existing

    case_record = build_recovery_case_record(batch_id, item_spec, rendered_item, item_state, response)
    if not case_record:
        return ""

    case_library_root.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")
    sample_slug = slugify_filename(case_record.get("sample_id", ""), "sample")
    sequence_slug = slugify_filename(case_record.get("sequence", "") or case_record.get("sequence_manifest_id", ""), "sequence")
    error_slug = slugify_filename(case_record.get("failure", {}).get("error_code", ""), "error")
    case_path = case_library_root / sample_slug / sequence_slug / f"{timestamp}_{error_slug}.json"
    write_json(case_path, case_record)
    item_state["successful_recovery_case_path"] = str(case_path)
    item_state.setdefault("history", []).append(
        {
            "at": now_iso(),
            "event": "recovery_case_saved",
            "message": "Saved a successful recovery case for future planning and retries.",
            "case_path": str(case_path),
        }
    )
    return str(case_path)


def build_recovery_request_payload(
    batch_id: str,
    state_path: Path,
    batch_spec: dict[str, Any],
    item_spec: dict[str, Any],
    rendered_item: dict[str, Any],
    item_state: dict[str, Any],
    outcome: dict[str, Any],
    response: dict[str, Any],
    request_path: Path,
    plan_path: Path,
    case_library_root: Path,
) -> dict[str, Any]:
    history = list(item_state.get("history", []))
    recent_history = history[-5:] if len(history) > 5 else history
    artifacts = latest_failure_artifacts(response)
    result_payload = try_read_json(Path(artifacts["result_path"])) if artifacts.get("result_path") else {}
    job_payload = try_read_json(Path(artifacts["job_json_path"])) if artifacts.get("job_json_path") else {}
    bridge_log_tail = tail_text_file(Path(artifacts["bridge_log_path"])) if artifacts.get("bridge_log_path") else ""
    case_library_matches = load_recovery_case_library_matches(
        case_library_root,
        rendered_item,
        str(outcome.get("error_code", "") or ""),
    )
    return {
        "batch_id": batch_id,
        "state_path": str(state_path),
        "item_id": str(item_state.get("id", "") or ""),
        "attempt": int(item_state.get("attempts", 0)),
        "requested_at": now_iso(),
        "request_path": str(request_path),
        "plan_path": str(plan_path),
        "current_item_spec": copy.deepcopy(item_spec),
        "current_item_context": summarize_item_context_for_recovery(rendered_item, item_state),
        "item_state": {
            "status": item_state.get("status", ""),
            "attempts": int(item_state.get("attempts", 0)),
            "last_error_code": str(item_state.get("last_error_code", "") or ""),
            "last_error_message": str(item_state.get("last_error_message", "") or ""),
            "retry_overrides": copy.deepcopy(item_state.get("retry_overrides", {})),
            "recent_history": [compact_history_entry(entry) for entry in recent_history],
        },
        "case_library_matches": case_library_matches,
        "failure": {
            "action": str(outcome.get("action", "") or ""),
            "reason": str(outcome.get("reason", "") or ""),
            "rule_source": str(outcome.get("rule_source", "") or ""),
            "error_code": str(outcome.get("error_code", "") or ""),
            "error_message": str(outcome.get("error_message", "") or ""),
            "response_summary": {
                "job_id": str(response.get("job_id", "") or ""),
                "final_state": str(response.get("final_state", "") or ""),
                "timed_out": bool(response.get("timed_out", False)),
                "result_path": str(response.get("result_path", "") or ""),
                "outcome_summary": copy.deepcopy(response.get("outcome_summary", {})),
            },
            "artifacts": artifacts,
            "job_summary": summarize_job_for_recovery(job_payload),
            "result_summary": summarize_result_for_recovery(result_payload),
            "bridge_log_tail": bridge_log_tail,
        },
        "dynamic_item_support": build_dynamic_item_contract(
            batch_spec,
            str(item_spec.get("mode", batch_spec.get("mode", "execute")) or ""),
            str(item_spec.get("sample_id", batch_spec.get("requested_sample_id", "")) or ""),
        ),
        "instructions": {
            "valid_actions": ["retry", "stop", "complete"],
            "can_insert_items_before_retry": True,
            "supported_insert_item_keys": copy.deepcopy(SUPPORTED_DYNAMIC_ITEM_KEYS),
        },
    }


def wait_for_recovery_plan(plan_path: Path, timeout_seconds: float, poll_seconds: float = 2.0) -> dict[str, Any] | None:
    started = time.monotonic()
    while time.monotonic() - started < timeout_seconds:
        if plan_path.is_file():
            try:
                return read_json(plan_path)
            except ValueError:
                return None
        time.sleep(poll_seconds)
    return None


def normalize_agent_recovery_plan(
    plan: dict[str, Any],
    default_mode: str = "execute",
    default_sample_id: str = "NV23",
) -> dict[str, Any]:
    if not isinstance(plan, dict):
        return {}
    default_mode = str(default_mode or "execute").strip() or "execute"
    default_sample_id = str(default_sample_id or "NV23").strip() or "NV23"
    action = str(plan.get("action", "") or "").strip().lower()
    if action not in {"retry", "stop", "complete"}:
        return {}
    normalized = {
        "action": action,
        "reason": str(plan.get("reason", "") or "").strip(),
        "operator_message": str(plan.get("operator_message", "") or "").strip(),
        "item_overrides": normalize_runtime_item_overrides(plan.get("item_overrides", {}), default_mode, default_sample_id),
        "insert_items_before_retry": normalize_dynamic_insert_items(plan.get("insert_items_before_retry", []), default_mode, default_sample_id),
        "raw": copy.deepcopy(plan),
    }
    return normalized


def find_aux_references(value: Any) -> set[str]:
    references: set[str] = set()
    if isinstance(value, str) and value.startswith("aux:"):
        key = value.split(":", 1)[1].strip()
        if key:
            references.add(key)
        return references

    if isinstance(value, dict):
        aux_key = str(value.get("aux", "") or "").strip() if "aux" in value else ""
        if aux_key:
            references.add(aux_key)
        for inner_value in value.values():
            references.update(find_aux_references(inner_value))
        return references

    if isinstance(value, list):
        for inner_value in value:
            references.update(find_aux_references(inner_value))
    return references


def summarize_future_aux_dependencies(future_items: list[dict[str, Any]], focus_aux_key: str) -> list[dict[str, Any]]:
    summary: list[dict[str, Any]] = []
    focus = str(focus_aux_key or "").strip()
    for item in future_items:
        refs: set[str] = set()
        for key in ("scan", "float_vars", "acquisition", "metadata"):
            refs.update(find_aux_references(item.get(key)))
        if not refs:
            continue
        entry = {
            "item_id": str(item.get("id", "") or ""),
            "sequence": str(item.get("sequence", "") or ""),
            "sequence_manifest_id": str(item.get("sequence_manifest_id", "") or ""),
            "aux_keys": sorted(refs),
            "depends_on_current_aux": bool(focus and focus in refs),
        }
        summary.append(entry)
    return summary


def summarize_analysis_response_for_review(analysis: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(analysis, dict):
        return {}
    summary = {
        "ok": bool(analysis.get("ok", False)),
        "fit_kind": str(analysis.get("fit_kind", "") or ""),
        "result_path": normalize_path_for_agent(analysis.get("result_path", "")),
        "data_path": normalize_path_for_agent(analysis.get("data_path", "")),
        "sequence_name": str(analysis.get("sequence_name", "") or ""),
        "error_code": str(analysis.get("error_code", "") or ""),
        "error_message": truncate_text(analysis.get("error_message", ""), 1200),
        "warnings": copy.deepcopy((analysis.get("warnings") or [])[:10]),
    }
    fit = analysis.get("fit", {})
    if isinstance(fit, dict) and fit:
        summary["fit"] = {
            "ok": bool(fit.get("ok", False)),
            "value": fit.get("value", []),
            "name": str(fit.get("name", "") or ""),
            "error": truncate_text(fit.get("error", ""), 800),
        }
    aux_update = analysis.get("aux_update", {})
    if isinstance(aux_update, dict) and aux_update:
        summary["aux_update"] = {
            "ok": bool(aux_update.get("ok", False)),
            "key": str(aux_update.get("key", "") or ""),
            "value": aux_update.get("value", []),
            "label": str(aux_update.get("label", "") or ""),
            "source": str(aux_update.get("source", "") or ""),
        }
    signal = analysis.get("signal", {})
    if isinstance(signal, dict) and signal:
        summary["signal"] = {
            "source": str(signal.get("source", "") or ""),
            "readout_count": signal.get("readout_count", []),
            "discard_first_average": bool(signal.get("discard_first_average", False)),
            "averages_used": signal.get("averages_used", []),
            "num_points": signal.get("num_points", []),
            "x_begin": signal.get("x_begin", []),
            "x_end": signal.get("x_end", []),
            "y_min": signal.get("y_min", []),
            "y_max": signal.get("y_max", []),
            "x_values": copy.deepcopy(signal.get("x_values", [])),
            "x_preview": copy.deepcopy(signal.get("x_preview", [])),
        }
    request = analysis.get("request", {})
    if isinstance(request, dict) and request:
        summary["request"] = copy.deepcopy(request)
    if analysis.get("analysis_request_path"):
        summary["analysis_request_path"] = normalize_path_for_agent(analysis.get("analysis_request_path", ""))
    if analysis.get("analysis_output_path"):
        summary["analysis_output_path"] = normalize_path_for_agent(analysis.get("analysis_output_path", ""))
    return summary


def build_savedexperiment_mat_tool_context() -> dict[str, Any]:
    script_path = SCRIPT_ROOT / "tools_mat_parse.py"
    normalized_script_path = normalize_path_for_agent(str(script_path))
    return {
        "available": script_path.is_file(),
        "script_path": normalized_script_path,
        "read_single_command": f"python3 {normalized_script_path} --pretty <savedexperiment_mat_path>",
        "read_multiple_command": f"python3 {normalized_script_path} --pretty <savedexperiment_mat_path_1> <savedexperiment_mat_path_2> ...",
        "output_format": "raw_export_plus_plot",
        "selection_guidance": "Start from savedexperiment_history filenames and reference_data, then read only the most relevant .mat files. The default output is raw MATLAB data plus raw-readout plot paths, not a scientific summary or verdict.",
    }


def build_past_data_context(
    batch_spec: dict[str, Any],
    state: dict[str, Any],
    current_index: int,
    rendered_item: dict[str, Any],
    aux_entries: dict[str, Any],
) -> dict[str, Any]:
    metadata = rendered_item.get("metadata", {}) if isinstance(rendered_item, dict) else {}
    if not isinstance(metadata, dict):
        metadata = {}
    registry_context = lookup_registry_entry_for_past_data(rendered_item, metadata)
    registry_entry = registry_context.get("entry", {}) if isinstance(registry_context, dict) else {}
    reference_data = str(metadata.get("reference_data", "") or "").strip()
    reference_data_source = str(metadata.get("reference_data_source", "") or "").strip()
    if not reference_data:
        reference_data = str(registry_entry.get("reference_data", "") or "").strip()
        if reference_data and not reference_data_source:
            reference_data_source = "nv_position_registry"
    resolved_reference_data = resolve_reference_data_path(reference_data)
    reference_exists = bool(resolved_reference_data and Path(resolved_reference_data).exists())
    reference_context = {
        "raw_path": reference_data,
        "resolved_path": resolved_reference_data,
        "exists": reference_exists,
        "source": reference_data_source,
        "registry_path": normalize_path_for_agent(metadata.get("reference_data_registry_path", "") or registry_context.get("registry_path", "")),
    }
    savedexperiment_history = summarize_savedexperiment_family_history(rendered_item, resolved_reference_data, registry_context)
    return {
        "reference_data": reference_context,
        "registry_entry": registry_context,
        "recent_nv_usage": select_recent_usage_clusters(resolved_reference_data, registry_context),
        "savedexperiment_mat_tool": build_savedexperiment_mat_tool_context(),
        "savedexperiment_history": savedexperiment_history,
        "completed_items": summarize_completed_items_for_planning(batch_spec, state, current_index, aux_entries),
        "aux_state": summarize_aux_state_entries(aux_entries),
    }


def build_measurement_plan_request_payload(
    batch_id: str,
    state_path: Path,
    batch_spec: dict[str, Any],
    state: dict[str, Any],
    current_index: int,
    item_state: dict[str, Any],
    item_spec: dict[str, Any],
    rendered_item: dict[str, Any],
    request_path: Path,
    plan_path: Path,
    future_items: list[dict[str, Any]],
    aux_entries: dict[str, Any],
    case_library_root: Path,
    pre_enqueue_advisory: dict[str, Any],
    policy: dict[str, Any],
) -> dict[str, Any]:
    analysis_aux_key = str(rendered_item.get("analysis", {}).get("aux_key", "") or "").strip()
    attempt_context = build_attempt_context_for_planning(item_state)
    failure_error_code = str(attempt_context.get("last_failure", {}).get("error_code", "") or "")
    case_library_matches = load_recovery_case_library_matches(case_library_root, rendered_item, failure_error_code)
    rendered_item_with_sequence = enrich_rendered_item_sequence_context(rendered_item, item_spec)
    advisory_only = bool(policy.get("measurement_plan_advisory_only", False))
    allow_current_item_overrides = bool(policy.get("measurement_plan_allow_current_item_overrides", False)) and not advisory_only
    planner_timeout_seconds = float(policy.get("measurement_plan_timeout_seconds", DEFAULT_MEASUREMENT_PLAN_TIMEOUT_SECONDS))
    tracking_cadence_policy = current_tracking_cadence_policy()
    shot_budget_policy = default_shot_budget_policy()
    current_shot_budget = summarize_current_shot_budget(
        item_spec,
        rendered_item_with_sequence,
        batch_spec,
        pre_enqueue_advisory,
        shot_budget_policy,
    )
    return {
        "batch_id": batch_id,
        "state_path": str(state_path),
        "item_id": str(item_state.get("id", "") or ""),
        "attempt": int(item_state.get("attempts", 0)) + 1,
        "request_path": str(request_path),
        "plan_path": str(plan_path),
        "batch_context": {
            "mode": str(batch_spec.get("mode", "") or ""),
            "requested_sample_id": str(batch_spec.get("requested_sample_id", "") or ""),
            "natural_language_request": str(batch_spec.get("natural_language_request", "") or ""),
        },
        "current_item_context": summarize_item_context_for_recovery(item_spec, item_state),
        "current_rendered_item": rendered_item_with_sequence,
        "pre_enqueue_advisory": copy.deepcopy(pre_enqueue_advisory) if isinstance(pre_enqueue_advisory, dict) else {},
        "shot_budget_policy": shot_budget_policy,
        "current_shot_budget": current_shot_budget,
        "attempt_context": attempt_context,
        "future_aux_dependencies": summarize_future_aux_dependencies(future_items, analysis_aux_key),
        "past_data_context": build_past_data_context(batch_spec, state, current_index, rendered_item_with_sequence, aux_entries),
        "case_library_matches": case_library_matches,
        "custom_analysis_support": build_custom_analysis_contract(),
        "dynamic_item_support": build_dynamic_item_contract(
            batch_spec,
            str(item_spec.get("mode", batch_spec.get("mode", "execute")) or ""),
            str(item_spec.get("sample_id", batch_spec.get("requested_sample_id", "")) or ""),
        ),
        "instructions": {
            "agent_must_consult_past_data": True,
            "agent_must_consult_savedexperiment_history": True,
            "agent_must_start_from_savedexperiment_filenames": True,
            "agent_must_use_savedexperiment_mat_tool_when_relevant": not advisory_only,
            "agent_should_not_do_deep_evidence_analysis_when_advisory_only": advisory_only,
            "agent_must_open_sequence_xml_when_available": True,
            "agent_must_read_sequence_xml_before_parameter_changes": True,
            "agent_must_consider_pre_enqueue_advisory": bool(isinstance(pre_enqueue_advisory, dict) and pre_enqueue_advisory.get("requested", False)),
            "agent_should_use_estimated_runtime_and_recent_nv_drift_to_choose_acquisition": True,
            "agent_must_preserve_total_acquisition_count": True,
            "agent_must_treat_total_acquisition_count_as_averages_times_repetitions": True,
            "agent_should_change_scan_or_stop_instead_of_reducing_total_acquisition_count": True,
            "agent_must_apply_shot_budget_policy": True,
            "agent_should_distinguish_calibration_from_publication_quality_data": True,
            "agent_should_treat_calibration_2e5_to_3e5_shots_as_usually_sufficient": True,
            "agent_must_not_call_science_data_publication_quality_below_1p5e6_shots_without_explicit_justification": True,
            "agent_should_preserve_or_split_publication_quality_total_shots_before_reducing_quality": True,
            "tracking_cadence_policy": tracking_cadence_policy,
            "agent_should_use_day_night_tracking_cadence_policy": True,
            "agent_should_keep_default_untracked_window_seconds_in_mind": tracking_cadence_policy["effective_max_untracked_window_seconds"],
            "agent_should_compare_tracking_window_to_suggested_window": True,
            "measurement_plan_is_advisory_only": advisory_only,
            "agent_must_not_expect_automatic_stop_or_mutation": advisory_only,
            "agent_should_put_recommendations_in_reason_or_operator_message_when_advisory_only": advisory_only,
            "agent_must_not_directly_override_current_item": not allow_current_item_overrides,
            "current_item_overrides_allowed": allow_current_item_overrides,
            "planner_timeout_seconds": planner_timeout_seconds,
            "agent_should_return_before_timeout": True,
            "agent_should_keep_response_short": True,
            "valid_actions": ["proceed", "stop"],
            "supported_override_keys": (
                ["scan", "float_vars", "acquisition", "metadata", "analysis", "allow_seed_fallback", "sequence_authoring", "project_branches"]
                if allow_current_item_overrides
                else []
            ),
            "can_prepend_items": not advisory_only,
            "supported_insert_item_keys": copy.deepcopy(SUPPORTED_DYNAMIC_ITEM_KEYS),
            "return_concrete_values_when_possible": True,
        },
    }


def normalize_measurement_plan(plan: dict[str, Any], default_mode: str, default_sample_id: str) -> dict[str, Any]:
    if not isinstance(plan, dict):
        return {}
    action = str(plan.get("action", "") or "").strip().lower()
    if action not in {"proceed", "stop"}:
        return {}
    item_overrides = normalize_runtime_item_overrides(plan.get("item_overrides", {}), default_mode, default_sample_id)
    return {
        "action": action,
        "reason": str(plan.get("reason", "") or "").strip(),
        "operator_message": str(plan.get("operator_message", "") or "").strip(),
        "item_overrides": item_overrides,
        "prepend_items": normalize_dynamic_insert_items(plan.get("prepend_items", []), default_mode, default_sample_id),
        "raw": copy.deepcopy(plan),
    }


def build_analysis_review_request_payload(
    batch_id: str,
    state_path: Path,
    batch_spec: dict[str, Any],
    state: dict[str, Any],
    current_index: int,
    item_spec: dict[str, Any],
    item_state: dict[str, Any],
    rendered_item: dict[str, Any],
    response: dict[str, Any],
    analysis_spec: dict[str, Any],
    analysis_response: dict[str, Any],
    request_path: Path,
    plan_path: Path,
    future_items: list[dict[str, Any]],
    aux_entries: dict[str, Any],
) -> dict[str, Any]:
    artifacts = latest_failure_artifacts(response)
    result_payload = try_read_json(Path(artifacts["result_path"])) if artifacts.get("result_path") else {}
    job_payload = try_read_json(Path(artifacts["job_json_path"])) if artifacts.get("job_json_path") else {}
    review_aux_key = str(analysis_response.get("aux_update", {}).get("key", "") or analysis_spec.get("aux_key", "") or "").strip()
    history = list(item_state.get("history", []))
    recent_history = history[-5:] if len(history) > 5 else history
    rendered_item_with_sequence = enrich_rendered_item_sequence_context(rendered_item, item_spec)
    return {
        "batch_id": batch_id,
        "state_path": str(state_path),
        "item_id": str(item_state.get("id", "") or ""),
        "attempt": int(item_state.get("attempts", 0)),
        "request_path": str(request_path),
        "plan_path": str(plan_path),
        "current_item_context": summarize_item_context_for_recovery(rendered_item_with_sequence, item_state),
        "analysis_context": {
            "requested_analysis": normalize_analysis_spec(analysis_spec),
            "analysis_response": summarize_analysis_response_for_review(analysis_response),
            "candidate_fit_kinds": sorted(VALID_ANALYSIS_FIT_KINDS),
            "custom_analysis_support": build_custom_analysis_contract(),
            "future_aux_dependencies": summarize_future_aux_dependencies(future_items, review_aux_key),
        },
        "past_data_context": build_past_data_context(batch_spec, state, current_index, rendered_item_with_sequence, aux_entries),
        "result_summary": summarize_result_for_recovery(result_payload),
        "job_summary": summarize_job_for_recovery(job_payload),
        "recent_history": [compact_history_entry(entry) for entry in recent_history],
        "dynamic_item_support": build_dynamic_item_contract(
            batch_spec,
            str(rendered_item.get("mode", batch_spec.get("mode", "execute")) or ""),
            str(rendered_item.get("sample_id", batch_spec.get("requested_sample_id", "")) or ""),
        ),
        "instructions": {
            "agent_must_choose_action": True,
            "agent_must_consult_savedexperiment_history": True,
            "agent_must_start_from_savedexperiment_filenames": True,
            "agent_must_use_savedexperiment_mat_tool_when_relevant": True,
            "agent_must_open_sequence_xml_when_available": True,
            "agent_must_read_sequence_xml_before_fit_judgment": True,
            "valid_actions": ["accept", "continue", "reanalyze", "rerun_item", "stop"],
            "can_override_analysis": True,
            "can_override_next_attempt": True,
            "can_insert_items_after_accept_or_continue": True,
            "can_insert_items_before_rerun": True,
            "supported_insert_item_keys": copy.deepcopy(SUPPORTED_DYNAMIC_ITEM_KEYS),
        },
    }


def normalize_analysis_review_plan(plan: dict[str, Any], default_mode: str, default_sample_id: str) -> dict[str, Any]:
    if not isinstance(plan, dict):
        return {}
    action = str(plan.get("action", "") or "").strip().lower()
    if action not in {"accept", "continue", "reanalyze", "rerun_item", "stop"}:
        return {}
    analysis_overrides = normalize_analysis_spec(plan.get("analysis_overrides", {}))
    normalized = {
        "action": action,
        "reason": str(plan.get("reason", "") or "").strip(),
        "operator_message": str(plan.get("operator_message", "") or "").strip(),
        "analysis_overrides": analysis_overrides,
        "item_overrides": normalize_runtime_item_overrides(plan.get("item_overrides", {}), default_mode, default_sample_id),
        "apply_aux_update": bool(plan.get("apply_aux_update", action == "accept")),
        "insert_items_after": normalize_dynamic_insert_items(plan.get("insert_items_after", []), default_mode, default_sample_id),
        "insert_items_before_rerun": normalize_dynamic_insert_items(plan.get("insert_items_before_rerun", []), default_mode, default_sample_id),
        "raw": copy.deepcopy(plan),
    }
    return normalized


def merge_analysis_spec(base_spec: dict[str, Any], override_spec: dict[str, Any]) -> dict[str, Any]:
    merged = normalize_analysis_spec(base_spec)
    override = normalize_analysis_spec(override_spec)
    if override:
        merged.update(override)
    return merged


def run_measurement_plan_with_agent(
    batch_id: str,
    state_path: Path,
    batch_spec: dict[str, Any],
    state: dict[str, Any],
    current_index: int,
    item_spec: dict[str, Any],
    item_state: dict[str, Any],
    rendered_item: dict[str, Any],
    future_items: list[dict[str, Any]],
    aux_entries: dict[str, Any],
    policy: dict[str, Any],
    args: argparse.Namespace,
    hook_token: str,
) -> dict[str, Any]:
    planning_enabled = bool(policy.get("measurement_plan_enabled", False))
    planning_required = bool(policy.get("measurement_plan_required", False))
    advisory_only = bool(policy.get("measurement_plan_advisory_only", False))
    advisory_required = bool(policy.get("pre_enqueue_advisory_required", False))
    pre_enqueue_advisory = fetch_pre_enqueue_advisory(rendered_item, batch_spec, args, policy)
    if advisory_required and pre_enqueue_advisory.get("requested", False) and not pre_enqueue_advisory.get("ok", False):
        return {
            "action": "stop",
            "message": pre_enqueue_advisory.get("error_message", "") or "Pre-enqueue advisory was required, but runtime/drift context could not be built safely.",
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": {
                "request_path": "",
                "plan_path": "",
                "hook_ok": False,
                "timeout_seconds": 0,
                "plan": {},
                "pre_enqueue_advisory": copy.deepcopy(pre_enqueue_advisory),
            },
            "prepend_items": [],
        }

    if not planning_enabled:
        planning_record = {}
        if isinstance(pre_enqueue_advisory, dict) and pre_enqueue_advisory.get("requested", False):
            planning_record = {
                "request_path": "",
                "plan_path": "",
                "hook_ok": False,
                "timeout_seconds": 0,
                "plan": {},
                "pre_enqueue_advisory": copy.deepcopy(pre_enqueue_advisory),
            }
        return {
            "action": "proceed",
            "message": "Measurement planning disabled; deterministic pre-enqueue advisory recorded." if planning_record else "",
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": planning_record,
            "prepend_items": [],
        }

    if not hook_token and planning_required and not advisory_only:
        return {
            "action": "stop",
            "message": "Pre-run measurement planning was required, but no OpenClaw hooks token was available.",
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": {},
            "prepend_items": [],
        }

    planning_root = Path(os.path.expanduser(args.measurement_plan_root)).resolve()
    case_library_root = Path(os.path.expanduser(args.recovery_case_library_root)).resolve()
    planning_root.mkdir(parents=True, exist_ok=True)
    item_plan_root = planning_root / batch_id / str(item_state.get("id", "item"))
    item_plan_root.mkdir(parents=True, exist_ok=True)
    request_path = item_plan_root / f"attempt_{int(item_state.get('attempts', 0)) + 1:02d}.request.json"
    plan_path = item_plan_root / f"attempt_{int(item_state.get('attempts', 0)) + 1:02d}.plan.json"
    request_payload = build_measurement_plan_request_payload(
        batch_id=batch_id,
        state_path=state_path,
        batch_spec=batch_spec,
        state=state,
        current_index=current_index,
        item_state=item_state,
        item_spec=item_spec,
        rendered_item=rendered_item,
        request_path=request_path,
        plan_path=plan_path,
        future_items=future_items,
        aux_entries=aux_entries,
        case_library_root=case_library_root,
        pre_enqueue_advisory=pre_enqueue_advisory,
        policy=policy,
    )
    write_json(request_path, request_payload)
    hook_payload = {
        "batchId": batch_id,
        "itemId": str(item_state.get("id", "") or ""),
        "attempt": int(item_state.get("attempts", 0)) + 1,
        "requestPath": str(request_path),
        "planPath": str(plan_path),
    }
    hook_ok = post_hook(args.gateway_url, hook_token, args.measurement_plan_hook_path, hook_payload) if hook_token else False
    measurement_plan_timeout_seconds = float(
        policy.get("measurement_plan_timeout_seconds", args.measurement_plan_timeout_seconds)
    )
    planned = wait_for_recovery_plan(plan_path, measurement_plan_timeout_seconds) if hook_ok else {}
    planning_plan = normalize_measurement_plan(
        planned or {},
        str(item_spec.get("mode", batch_spec.get("mode", "execute")) or ""),
        str(item_spec.get("sample_id", batch_spec.get("requested_sample_id", "")) or ""),
    )
    planning_record = {
        "request_path": str(request_path),
        "plan_path": str(plan_path),
        "hook_ok": hook_ok,
        "timeout_seconds": measurement_plan_timeout_seconds,
        "plan": copy.deepcopy(planning_plan.get("raw", {})),
        "pre_enqueue_advisory": copy.deepcopy(pre_enqueue_advisory),
    }

    if not planning_plan:
        if planning_required and not advisory_only:
            message = "Pre-run measurement planning was required, but no valid plan was returned before the timeout."
            if not hook_ok:
                message = "Pre-run measurement planning hook request failed, so the batch cannot choose parameters safely."
            return {
                "action": "stop",
                "message": message,
                "item_spec": item_spec,
                "rendered_item": rendered_item,
                "planning_record": planning_record,
                "prepend_items": [],
            }
        advisory_message = ""
        if advisory_only:
            advisory_message = "Measurement planner did not return a valid advisory before the timeout; executing the requested item unchanged."
            if not hook_ok:
                advisory_message = "Measurement planning hook request failed; executing the requested item unchanged."
        return {
            "action": "proceed",
            "message": advisory_message,
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": planning_record,
            "prepend_items": [],
        }

    if advisory_only:
        advisory_notes: list[str] = []
        if planning_plan["action"] == "stop":
            advisory_notes.append("Planner recommended operator review, but advisory-only mode is enabled.")
        if planning_plan.get("prepend_items"):
            advisory_notes.append("Planner suggested prerequisite items, but advisory-only mode executes the requested item unchanged.")
        if planning_plan.get("item_overrides"):
            advisory_notes.append("Planner suggested current-item changes, but advisory-only mode ignores them.")
        return {
            "action": "proceed",
            "message": join_measurement_plan_messages(
                planning_plan.get("operator_message", "") or planning_plan.get("reason", ""),
                " ".join(advisory_notes),
            ),
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": planning_record,
            "prepend_items": [],
        }

    if planning_plan["action"] == "stop":
        return {
            "action": "stop",
            "message": planning_plan.get("operator_message", "") or planning_plan.get("reason", "") or "Pre-run planning requested operator review.",
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": planning_record,
            "prepend_items": [],
        }

    current_item_override_error = validate_measurement_plan_current_item_overrides(planning_plan, policy)
    if current_item_override_error:
        return {
            "action": "stop",
            "message": current_item_override_error,
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": planning_record,
            "prepend_items": [],
        }

    acquisition_override_error = validate_measurement_plan_acquisition_override(
        item_spec=item_spec,
        rendered_item=rendered_item,
        pre_enqueue_advisory=pre_enqueue_advisory,
        planning_plan=planning_plan,
    )
    if acquisition_override_error:
        return {
            "action": "stop",
            "message": acquisition_override_error,
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": planning_record,
            "prepend_items": [],
        }

    planned_item_spec = deep_merge_dicts(item_spec, planning_plan.get("item_overrides", {}))
    try:
        planned_rendered_item = render_item(planned_item_spec, aux_entries)
    except ValueError as exc:
        return {
            "action": "stop",
            "message": f"Pre-run planning produced unresolved overrides: {exc}",
            "item_spec": item_spec,
            "rendered_item": rendered_item,
            "planning_record": planning_record,
            "prepend_items": [],
        }

    return {
        "action": "proceed",
        "message": planning_plan.get("operator_message", "") or planning_plan.get("reason", ""),
        "item_spec": planned_item_spec,
        "rendered_item": planned_rendered_item,
        "planning_record": planning_record,
        "prepend_items": copy.deepcopy(planning_plan.get("prepend_items", [])),
    }


def run_analysis_with_agent_review(
    batch_id: str,
    state_path: Path,
    batch_spec: dict[str, Any],
    state: dict[str, Any],
    current_index: int,
    item_spec: dict[str, Any],
    item_state: dict[str, Any],
    rendered_item: dict[str, Any],
    response: dict[str, Any],
    future_items: list[dict[str, Any]],
    aux_entries: dict[str, Any],
    policy: dict[str, Any],
    args: argparse.Namespace,
    hook_token: str,
) -> dict[str, Any]:
    analysis_spec = normalize_analysis_spec(rendered_item.get("analysis", {}))
    if not analysis_spec:
        return {
            "action": "none",
            "message": "",
            "analysis_record": {},
            "aux_entry": {},
            "item_overrides": {},
            "insert_items_after": [],
            "insert_items_before_rerun": [],
        }

    result_path = str(response.get("result_path", "") or "").strip()
    analysis_attempts: list[dict[str, Any]] = []
    analysis_review_root = Path(os.path.expanduser(args.analysis_review_root)).resolve()
    analysis_review_root.mkdir(parents=True, exist_ok=True)
    require_review_plan = bool(policy.get("analysis_review_required", False))
    review_enabled = bool(policy.get("analysis_review_enabled", False))
    evidence_only = bool(policy.get("analysis_evidence_only", True))
    if evidence_only:
        review_enabled = False
        require_review_plan = False
    auto_adopt_aux = bool(policy.get("analysis_auto_adopt_aux", False))

    for review_round in range(1, MAX_ANALYSIS_REVIEW_ROUNDS + 1):
        command = build_analysis_command(analysis_spec, result_path)
        a_code, a_response, a_stdout, a_stderr = run_json_command(command)
        attempt_record = {
            "review_round": review_round,
            "analysis_spec": copy.deepcopy(analysis_spec),
            "returncode": a_code,
            "stdout": a_stdout,
            "stderr": a_stderr,
            "response": a_response,
        }
        analysis_attempts.append(attempt_record)

        if not review_enabled:
            return build_analysis_evidence_only_result(analysis_attempts)

        if not hook_token and require_review_plan:
            return {
                "action": "stop",
                "message": "Analysis review was required, but no OpenClaw hooks token was available.",
                "analysis_record": {"attempts": analysis_attempts, "final_action": "stop"},
                "aux_entry": {},
                "item_overrides": {},
                "insert_items_after": [],
                "insert_items_before_rerun": [],
            }

        if not hook_token:
            return build_analysis_evidence_only_result(
                analysis_attempts,
                message="Analysis saved as evidence because no analysis-review hook token was available.",
            )

        item_review_root = analysis_review_root / batch_id / str(item_state.get("id", "item"))
        item_review_root.mkdir(parents=True, exist_ok=True)
        request_path = item_review_root / f"attempt_{int(item_state.get('attempts', 0)):02d}_review_{review_round:02d}.request.json"
        plan_path = item_review_root / f"attempt_{int(item_state.get('attempts', 0)):02d}_review_{review_round:02d}.plan.json"
        review_request = build_analysis_review_request_payload(
            batch_id=batch_id,
            state_path=state_path,
            batch_spec=batch_spec,
            state=state,
            current_index=current_index,
            item_spec=item_spec,
            item_state=item_state,
            rendered_item=rendered_item,
            response=response,
            analysis_spec=analysis_spec,
            analysis_response=a_response,
            request_path=request_path,
            plan_path=plan_path,
            future_items=future_items,
            aux_entries=aux_entries,
        )
        write_json(request_path, review_request)
        hook_payload = {
            "batchId": batch_id,
            "itemId": str(item_state.get("id", "") or ""),
            "attempt": int(item_state.get("attempts", 0)),
            "reviewRound": review_round,
            "fitKind": str(analysis_spec.get("fit_kind", "") or ""),
            "auxKey": str(analysis_spec.get("aux_key", "") or ""),
            "requestPath": str(request_path),
            "planPath": str(plan_path),
        }
        hook_ok = post_hook(args.gateway_url, hook_token, args.analysis_review_hook_path, hook_payload)
        attempt_record["review_request_path"] = str(request_path)
        attempt_record["review_plan_path"] = str(plan_path)
        attempt_record["review_hook_ok"] = hook_ok

        if not hook_ok and require_review_plan:
            return {
                "action": "stop",
                "message": "Analysis review hook request failed, so the batch cannot safely decide how to use this fit.",
                "analysis_record": {"attempts": analysis_attempts, "final_action": "stop"},
                "aux_entry": {},
                "item_overrides": {},
                "insert_items_after": [],
                "insert_items_before_rerun": [],
            }

        if not hook_ok:
            return build_analysis_evidence_only_result(
                analysis_attempts,
                message="Analysis saved as evidence because the optional analysis-review hook did not accept the request.",
            )

        planned = wait_for_recovery_plan(plan_path, float(args.analysis_plan_timeout_seconds)) if hook_ok else {}
        review_plan = normalize_analysis_review_plan(
            planned or {},
            str(rendered_item.get("mode", batch_spec.get("mode", "execute")) or ""),
            str(rendered_item.get("sample_id", batch_spec.get("requested_sample_id", "")) or ""),
        )
        attempt_record["review_plan"] = copy.deepcopy(review_plan.get("raw", {}))

        if not review_plan:
            if require_review_plan:
                return {
                    "action": "stop",
                    "message": "Analysis review was required, but no valid review plan was returned before the timeout.",
                    "analysis_record": {"attempts": analysis_attempts, "final_action": "stop"},
                    "aux_entry": {},
                    "item_overrides": {},
                    "insert_items_after": [],
                    "insert_items_before_rerun": [],
                }
            return build_analysis_evidence_only_result(
                analysis_attempts,
                message="Analysis saved as evidence because optional analysis review returned no valid plan.",
            )

        action = str(review_plan.get("action", "") or "").strip().lower()
        operator_message = review_plan.get("operator_message", "") or review_plan.get("reason", "")
        aux_update = a_response.get("aux_update", {})
        accepted_aux = (
            aux_update
            if auto_adopt_aux
            and isinstance(aux_update, dict)
            and aux_update.get("ok")
            and review_plan.get("apply_aux_update", action == "accept")
            else {}
        )

        if action in {"accept", "continue"}:
            return {
                "action": action,
                "message": operator_message,
                "analysis_record": {"attempts": analysis_attempts, "final_action": action},
                "aux_entry": accepted_aux,
                "item_overrides": {},
                "insert_items_after": copy.deepcopy(review_plan.get("insert_items_after", [])),
                "insert_items_before_rerun": [],
            }
        if action == "stop":
            return {
                "action": "stop",
                "message": operator_message or "Analysis review requested operator review.",
                "analysis_record": {"attempts": analysis_attempts, "final_action": "stop"},
                "aux_entry": {},
                "item_overrides": {},
                "insert_items_after": [],
                "insert_items_before_rerun": [],
            }
        if action == "rerun_item":
            item_overrides = copy.deepcopy(review_plan.get("item_overrides", {}))
            if review_plan.get("analysis_overrides"):
                item_overrides = deep_merge_dicts(item_overrides, {"analysis": review_plan["analysis_overrides"]})
            return {
                "action": "rerun_item",
                "message": operator_message or "Analysis review requested a rerun with modified conditions.",
                "analysis_record": {"attempts": analysis_attempts, "final_action": "rerun_item"},
                "aux_entry": {},
                "item_overrides": item_overrides,
                "insert_items_after": [],
                "insert_items_before_rerun": copy.deepcopy(review_plan.get("insert_items_before_rerun", [])),
            }
        if action == "reanalyze":
            if review_round >= MAX_ANALYSIS_REVIEW_ROUNDS:
                return {
                    "action": "stop",
                    "message": operator_message or "Analysis review exceeded the maximum reanalysis rounds.",
                    "analysis_record": {"attempts": analysis_attempts, "final_action": "stop"},
                    "aux_entry": {},
                    "item_overrides": {},
                    "insert_items_after": [],
                    "insert_items_before_rerun": [],
                }
            next_spec = merge_analysis_spec(analysis_spec, review_plan.get("analysis_overrides", {}))
            if next_spec == analysis_spec:
                return {
                    "action": "stop",
                    "message": operator_message or "Analysis review requested reanalysis but did not provide a meaningful override.",
                    "analysis_record": {"attempts": analysis_attempts, "final_action": "stop"},
                    "aux_entry": {},
                    "item_overrides": {},
                    "insert_items_after": [],
                    "insert_items_before_rerun": [],
                }
            analysis_spec = next_spec
            continue

    return {
        "action": "stop",
        "message": "Analysis review exceeded the maximum review rounds.",
        "analysis_record": {"attempts": analysis_attempts, "final_action": "stop"},
        "aux_entry": {},
        "item_overrides": {},
        "insert_items_after": [],
        "insert_items_before_rerun": [],
    }


def plan_retry_adjustments(item_spec: dict[str, Any], item_state: dict[str, Any], outcome: dict[str, Any]) -> tuple[dict[str, Any], str]:
    error_code = str(outcome.get("error_code", "") or "").strip()
    attempt_count = int(item_state.get("attempts", 0))
    existing = copy.deepcopy(item_state.get("retry_overrides", {}))
    metadata = copy.deepcopy(existing.get("metadata", {}))

    if error_code != "NVBridge:AlignNVFailed":
        return existing, ""

    metadata["local_fine_search_before_tracking"] = True
    metadata["require_landmark_match"] = False
    metadata["allow_seed_fallback"] = True
    metadata["legacy_landmark_map_requested"] = True

    if attempt_count <= 1:
        metadata["local_fine_search_xy_points"] = 31
        metadata["local_fine_search_half_span_um"] = [2.0, 2.0]
        metadata["local_fine_search_z_offsets_um"] = [-0.75, -0.25, 0.0, 0.25, 0.75]
        metadata["local_fine_search_dwell_seconds"] = 0.005
        metadata["tracking_z_seed_offsets_um"] = [0.0, -0.5, 0.5, -1.0, 1.0]
        note = "Retrying without legacy landmark-map matching, using denser local fine search and additional z seeds around the best available seed."
    else:
        metadata["local_fine_search_xy_points"] = 31
        metadata["local_fine_search_half_span_um"] = [2.5, 2.5]
        metadata["local_fine_search_z_offsets_um"] = [-1.0, -0.5, 0.0, 0.5, 1.0]
        metadata["local_fine_search_dwell_seconds"] = 0.005
        metadata["tracking_z_seed_offsets_um"] = [0.0, -0.5, 0.5, -1.0, 1.0]
        note = "Retrying without legacy landmark-map matching, using a wider local fine search and additional z seeds around the best available seed."

    existing["metadata"] = metadata
    return existing, note


def should_request_agent_recovery(outcome: dict[str, Any], policy: dict[str, Any]) -> bool:
    if not bool(policy.get("agent_recovery_enabled", True)):
        return False
    action = str(outcome.get("action", "") or "").strip().lower()
    if action != "retry":
        return False
    if str(outcome.get("rule_source", "") or "").strip() == "analysis_review_plan":
        return False
    error_code = str(outcome.get("error_code", "") or "").strip()
    stop_codes = set(normalize_policy_rules(policy, "stop_error_codes", DEFAULT_STOP_ERROR_CODES))
    return error_code not in stop_codes


def update_progress(state: dict[str, Any]) -> None:
    items = list(state.get("items", []))
    state["progress"] = {
        "completed": sum(1 for item in items if item.get("status") == "completed"),
        "total": len(items),
        "pending": sum(1 for item in items if item.get("status") == "pending"),
        "running": sum(1 for item in items if item.get("status") == "running"),
        "retrying": sum(1 for item in items if item.get("status") == "retrying"),
        "failed": sum(1 for item in items if item.get("status") == "failed"),
        "blocked": sum(1 for item in items if item.get("status") == "blocked"),
        "stopped": sum(1 for item in items if item.get("status") == "stopped"),
    }


def append_batch_event(state: dict[str, Any], event: str, message: str, **extra: Any) -> None:
    events = state.setdefault("events", [])
    record = {"at": now_iso(), "event": event, "message": message}
    record.update(extra)
    events.append(record)


def ensure_state(batch_spec: dict[str, Any], state_path: Path, args: argparse.Namespace, control_path: Path) -> tuple[dict[str, Any], bool]:
    if state_path.is_file():
        state = read_json(state_path)
        state.setdefault("batch_id", batch_spec.get("batch_id", state_path.stem))
        state.setdefault("started_at", "")
        state.setdefault("finished_at", "")
        state.setdefault("aux_state", {})
        state.setdefault("items", [])
        state.setdefault("resume_count", 0)
        state.setdefault("events", [])
        state["policy"] = default_policy(batch_spec, args)
        control = load_control(control_path)
        sync_control_into_state(state, control_path, control)
        update_progress(state)
        write_json(state_path, state)
        return state, False

    items_state = []
    for item in batch_spec.get("items", []):
        items_state.append(make_item_state(item))

    control = load_control(control_path)
    write_control(control_path, control)
    state = {
        "batch_id": batch_spec.get("batch_id", state_path.stem),
        "batch_spec_path": "",
        "status": "pending",
        "started_at": "",
        "finished_at": "",
        "resume_count": 0,
        "current_item_id": "",
        "aux_state": {},
        "items": items_state,
        "events": [],
        "policy": default_policy(batch_spec, args),
    }
    sync_control_into_state(state, control_path, control)
    update_progress(state)
    write_json(state_path, state)
    return state, True


def normalize_state_for_resume(state: dict[str, Any], allow_resume_failed: bool) -> tuple[dict[str, Any], str]:
    batch_status = str(state.get("status", "pending") or "pending")
    if batch_status == "completed":
        return state, "completed"
    if batch_status == "failed" and not allow_resume_failed:
        return state, "failed_requires_override"

    reset_statuses = {"running", "retrying", "stopped"}
    if allow_resume_failed:
        reset_statuses.update({"failed", "blocked"})

    changed = False
    for item in state.get("items", []):
        item_status = str(item.get("status", "") or "")
        if item_status in reset_statuses:
            item.setdefault("history", []).append(
                {
                    "at": now_iso(),
                    "event": "resume_reset",
                    "from_status": item_status,
                    "message": "Reset incomplete item to pending while resuming the batch runner.",
                }
            )
            item["status"] = "pending"
            changed = True

    if changed:
        state["resume_count"] = int(state.get("resume_count", 0)) + 1
        append_batch_event(state, "resume", "Resumed batch runner and reset incomplete items to pending.")

    state["status"] = "pending"
    state["finished_at"] = ""
    update_progress(state)
    return state, "resumed" if changed else "no_change"


def find_next_item_index(state: dict[str, Any]) -> int | None:
    for idx, item_state in enumerate(state.get("items", [])):
        if item_state.get("status") != "completed":
            return idx
    return None


def progress_text(batch_id: str, state: dict[str, Any], item_state: dict[str, Any], extra: str) -> str:
    update_progress(state)
    completed = state.get("progress", {}).get("completed", 0)
    total = state.get("progress", {}).get("total", 0)
    item_id = item_state.get("id", "item")
    return f"Batch `{batch_id}`: {completed}/{total} completed. Current item `{item_id}`. {extra}"


def latest_analysis_response(analysis_record: dict[str, Any]) -> dict[str, Any]:
    attempts = analysis_record.get("attempts", []) if isinstance(analysis_record, dict) else []
    if not isinstance(attempts, list):
        return {}
    for attempt in reversed(attempts):
        if not isinstance(attempt, dict):
            continue
        response = attempt.get("response", {})
        if isinstance(response, dict):
            return response
    return {}


def build_aux_entry(aux_update: dict[str, Any], result_path: str, analysis_record: dict[str, Any]) -> dict[str, Any]:
    response = latest_analysis_response(analysis_record)
    entry = {
        "value": aux_update.get("value"),
        "label": aux_update.get("label", ""),
        "source": aux_update.get("source", ""),
        "updated_at": now_iso(),
        "result_path": result_path,
        "data_path": str(response.get("data_path", "") or ""),
        "fit_kind": str(response.get("fit_kind", "") or aux_update.get("source", "") or ""),
    }
    sequence_name = str(response.get("sequence_name", "") or "").strip()
    if sequence_name:
        entry["sequence_name"] = sequence_name
    return entry


def persist_aux_update(aux_state_path: Path, key: str, entry: dict[str, Any]) -> None:
    aux_state = load_aux_state(aux_state_path)
    entries = aux_state.setdefault("entries", {})
    entries[key] = copy.deepcopy(entry)
    aux_state["updated_at"] = str(entry.get("updated_at", "") or now_iso())
    write_json(aux_state_path, aux_state)


def record_aux_update(state: dict[str, Any], aux_update: dict[str, Any], result_path: str, analysis_record: dict[str, Any] | None = None) -> None:
    if not isinstance(aux_update, dict) or not aux_update.get("ok"):
        return
    key = str(aux_update.get("key", "") or "").strip()
    if not key:
        return
    entry = build_aux_entry(aux_update, result_path, analysis_record or {})
    state["aux_state"][key] = entry
    persist_aux_update(DEFAULT_AUX_STATE_PATH, key, entry)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a measurement batch sequentially with retry / stop / resume rules.")
    parser.add_argument("--batch-spec", required=True)
    parser.add_argument("--state-path", default="")
    parser.add_argument("--control-path", default="")
    parser.add_argument("--queue-helper", default="")
    parser.add_argument("--timeout-seconds", type=float, default=7200.0)
    parser.add_argument("--poll-seconds", type=float, default=2.0)
    parser.add_argument("--retry-delay-seconds", type=float, default=5.0)
    parser.add_argument("--max-attempts-per-item", type=int)
    parser.add_argument("--restart", action="store_true")
    parser.add_argument("--resume-failed", action="store_true")
    parser.add_argument("--config-path", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--gateway-url", default=DEFAULT_GATEWAY_URL)
    parser.add_argument("--recovery-root", default=str(DEFAULT_RECOVERY_ROOT))
    parser.add_argument("--recovery-case-library-root", default=str(DEFAULT_RECOVERY_CASE_LIBRARY_ROOT))
    parser.add_argument("--recovery-hook-path", default=DEFAULT_RECOVERY_HOOK_PATH)
    parser.add_argument("--recovery-plan-timeout-seconds", type=float, default=DEFAULT_RECOVERY_PLAN_TIMEOUT_SECONDS)
    parser.add_argument("--measurement-plan-root", default=str(DEFAULT_MEASUREMENT_PLAN_ROOT))
    parser.add_argument("--measurement-plan-hook-path", default=DEFAULT_MEASUREMENT_PLAN_HOOK_PATH)
    parser.add_argument("--measurement-plan-timeout-seconds", type=float, default=DEFAULT_MEASUREMENT_PLAN_TIMEOUT_SECONDS)
    parser.add_argument("--analysis-review-root", default=str(DEFAULT_ANALYSIS_REVIEW_ROOT))
    parser.add_argument("--analysis-review-hook-path", default=DEFAULT_ANALYSIS_REVIEW_HOOK_PATH)
    parser.add_argument("--analysis-plan-timeout-seconds", type=float, default=DEFAULT_ANALYSIS_PLAN_TIMEOUT_SECONDS)
    parser.add_argument("--no-progress-hooks", dest="progress_hooks", action="store_false")
    parser.set_defaults(progress_hooks=True)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    config_path = Path(os.path.expanduser(args.config_path)).resolve()

    batch_spec_path = Path(os.path.expanduser(args.batch_spec)).resolve()
    batch_spec = read_json(batch_spec_path)
    batch_id = str(batch_spec.get("batch_id", batch_spec_path.stem))
    state_path = Path(os.path.expanduser(args.state_path)).resolve() if args.state_path else (DEFAULT_BATCH_ROOT / f"{batch_id}.state.json")
    control_path = Path(os.path.expanduser(args.control_path)).resolve() if args.control_path else default_control_path(state_path)
    recovery_root = Path(os.path.expanduser(args.recovery_root)).resolve()
    hook_token = resolve_hook_token(config_path)
    if args.restart:
        if state_path.exists():
            state_path.unlink()
        if control_path.exists():
            control_path.unlink()

    state, created_state = ensure_state(batch_spec, state_path, args, control_path)
    state["batch_spec_path"] = str(batch_spec_path)
    state["policy"] = default_policy(batch_spec, args)
    state, resume_status = normalize_state_for_resume(state, allow_resume_failed=args.resume_failed)
    if resume_status == "completed":
        write_json(state_path, state)
        print(json.dumps(state, ensure_ascii=False))
        return 0
    if resume_status == "failed_requires_override":
        write_json(state_path, state)
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "batch_failed_requires_resume_override",
                    "message": "Batch state is failed. Use --resume-failed to resume after addressing the underlying issue.",
                    "state_path": str(state_path),
                    "control_path": str(control_path),
                },
                ensure_ascii=False,
            ),
            file=sys.stderr,
        )
        return 1

    state["status"] = "running"
    if not state.get("started_at"):
        state["started_at"] = now_iso()
    state["finished_at"] = ""
    update_progress(state)
    write_json(state_path, state)

    if args.progress_hooks:
        if created_state:
            send_hook(args.gateway_url, hook_token, f"Batch `{batch_id}` started with {len(state.get('items', []))} items.")
        elif resume_status == "resumed":
            send_hook(args.gateway_url, hook_token, f"Batch `{batch_id}` resumed from existing state.")

    while True:
        next_index = find_next_item_index(state)
        if next_index is None:
            state["status"] = "completed"
            state["finished_at"] = now_iso()
            state["current_item_id"] = ""
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                send_hook(args.gateway_url, hook_token, f"Batch `{batch_id}` completed successfully ({len(state.get('items', []))}/{len(state.get('items', []))} items).")
            print(json.dumps(state, ensure_ascii=False))
            return 0

        control = load_control(control_path)
        sync_control_into_state(state, control_path, control)
        if control.get("stop_requested"):
            current_item = state["items"][next_index]
            current_item["status"] = "stopped"
            current_item.setdefault("history", []).append(
                {
                    "at": now_iso(),
                    "event": "stop_requested",
                    "message": str(control.get("stop_reason", "") or "Stop requested before starting the next item."),
                }
            )
            state["status"] = "stopped"
            state["finished_at"] = now_iso()
            state["current_item_id"] = current_item.get("id", "")
            append_batch_event(state, "stopped", "Stopped due to control request.", stop_reason=control.get("stop_reason", ""))
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                stop_reason = str(control.get("stop_reason", "") or "manual stop request")
                send_hook(args.gateway_url, hook_token, progress_text(batch_id, state, current_item, f"Stopped. reason=`{stop_reason}`"))
            print(json.dumps(state, ensure_ascii=False))
            return STOPPED_EXIT_CODE

        item_state = state["items"][next_index]
        base_item_spec = batch_spec["items"][next_index]
        item_spec = deep_merge_dicts(base_item_spec, item_state.get("retry_overrides", {}))
        future_items = list(batch_spec.get("items", []))[next_index + 1 :]
        aux_entries = load_aux_state(DEFAULT_AUX_STATE_PATH).get("entries", {})
        aux_entries.update(state.get("aux_state", {}))

        try:
            item_spec, materialized_update = materialize_sequence_authoring_for_item(
                batch_id=batch_id,
                batch_spec=batch_spec,
                batch_spec_path=batch_spec_path,
                state=state,
                state_path=state_path,
                item_index=next_index,
                item_state=item_state,
                item_spec=item_spec,
                aux_entries=aux_entries,
            )
            if materialized_update:
                base_item_spec = batch_spec["items"][next_index]
                if args.progress_hooks:
                    manifest_id = str(materialized_update.get("sequence_manifest_id", "") or "")
                    send_hook(
                        args.gateway_url,
                        hook_token,
                        progress_text(batch_id, state, item_state, f"Authored runtime staging sequence `{manifest_id}` for the current item."),
                    )
        except ValueError as exc:
            item_state["status"] = "failed"
            item_state["last_error_code"] = "SEQUENCE_AUTHORING_FAILED"
            item_state["last_error_message"] = str(exc)
            item_state.setdefault("history", []).append({"at": now_iso(), "event": "sequence_authoring_failed", "message": str(exc)})
            state["status"] = "failed"
            state["finished_at"] = now_iso()
            state["current_item_id"] = item_state.get("id", "")
            append_batch_event(state, "failed", "Runtime sequence authoring failed; batch stopped.", item_id=item_state.get("id", ""), error_code="SEQUENCE_AUTHORING_FAILED")
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                send_hook(args.gateway_url, hook_token, progress_text(batch_id, state, item_state, f"Runtime sequence authoring failed: {exc}"))
            print(json.dumps(state, ensure_ascii=False))
            return 2

        try:
            rendered_item = render_item(item_spec, aux_entries)
        except ValueError as exc:
            item_state["status"] = "blocked"
            item_state["last_error_code"] = "AUX_RESOLUTION_FAILED"
            item_state["last_error_message"] = str(exc)
            item_state.setdefault("history", []).append({"at": now_iso(), "event": "aux_resolution_failed", "message": str(exc)})
            state["status"] = "failed"
            state["finished_at"] = now_iso()
            state["current_item_id"] = item_state.get("id", "")
            append_batch_event(state, "failed", "AUX resolution failed; batch stopped.", item_id=item_state.get("id", ""), error_code="AUX_RESOLUTION_FAILED")
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                send_hook(args.gateway_url, hook_token, progress_text(batch_id, state, item_state, f"AUX resolution failed: {exc}"))
            print(json.dumps(state, ensure_ascii=False))
            return 2

        prior_success = find_prior_completed_attempt(item_state)
        if prior_success is not None:
            item_state.setdefault("history", []).append(
                {
                    "at": now_iso(),
                    "event": "late_success_detected",
                    "job_id": prior_success.get("job_id", ""),
                    "result_path": prior_success.get("result_path", ""),
                    "message": "Detected a previously completed attempt for this item and skipped a duplicate retry.",
                }
            )
            synthetic_response = {
                "job_id": prior_success.get("job_id", ""),
                "final_state": "done",
                "result_path": prior_success.get("result_path", ""),
                "result": prior_success.get("result", {}),
            }
            analysis_review = {
                "action": "none",
                "message": "",
                "analysis_record": {},
                "aux_entry": {},
                "item_overrides": {},
                "insert_items_after": [],
                "insert_items_before_rerun": [],
            }
            ensure_response_savedexperiment_raw_export(synthetic_response)
            if should_run_analysis(rendered_item, synthetic_response, state.get("policy", {})):
                analysis_review = run_analysis_with_agent_review(
                    batch_id=batch_id,
                    state_path=state_path,
                    batch_spec=batch_spec,
                    state=state,
                    current_index=next_index,
                    item_spec=item_spec,
                    item_state=item_state,
                    rendered_item=rendered_item,
                    response=synthetic_response,
                    future_items=future_items,
                    aux_entries=aux_entries,
                    policy=state.get("policy", {}),
                    args=args,
                    hook_token=hook_token,
                )
                item_state["analysis"] = copy.deepcopy(analysis_review.get("analysis_record", {}))

            if analysis_review.get("action") == "stop":
                item_state["status"] = "failed"
                item_state["last_error_code"] = "ANALYSIS_REVIEW_STOP"
                item_state["last_error_message"] = str(analysis_review.get("message", "") or "Analysis review rejected the completed attempt.")
                state["status"] = "failed"
                state["finished_at"] = now_iso()
                state["current_item_id"] = item_state.get("id", "")
                append_batch_event(state, "failed", "Stopped batch after analysis review rejected a reused completed attempt.", item_id=item_state.get("id", ""), error_code=item_state.get("last_error_code", ""))
                update_progress(state)
                write_json(state_path, state)
                if args.progress_hooks:
                    send_hook(args.gateway_url, hook_token, progress_text(batch_id, state, item_state, item_state["last_error_message"]))
                print(json.dumps(state, ensure_ascii=False))
                return 1

            if analysis_review.get("action") == "rerun_item":
                ignored = list(item_state.get("ignored_prior_success_job_ids", []))
                ignored.append(prior_success.get("job_id", ""))
                item_state["ignored_prior_success_job_ids"] = [job_id for job_id in ignored if str(job_id).strip()]
                item_state["retry_overrides"] = deep_merge_dicts(item_state.get("retry_overrides", {}), analysis_review.get("item_overrides", {}))
                item_state.setdefault("history", []).append(
                    {
                        "at": now_iso(),
                        "event": "analysis_review_requested_rerun",
                        "message": analysis_review.get("message", "") or "Analysis review requested a fresh rerun instead of reusing the prior completed attempt.",
                        "retry_overrides": copy.deepcopy(item_state.get("retry_overrides", {})),
                    }
                )
                item_state["status"] = "pending"
                item_state["last_error_code"] = ""
                item_state["last_error_message"] = ""
                items_before_rerun = select_analysis_branch_items(
                    item_spec,
                    action="rerun_item",
                    rendered_item=rendered_item,
                ) + list(analysis_review.get("insert_items_before_rerun", []))
                if items_before_rerun:
                    inserted_specs = insert_dynamic_items(
                        batch_spec,
                        state,
                        batch_spec_path,
                        state_path,
                        next_index,
                        items_before_rerun,
                        source_event="analysis_review_insert_before_rerun",
                        source_item_id=str(item_state.get("id", "") or ""),
                        source_message=analysis_review.get("message", "") or "Inserted new calibration/follow-up items before rerunning the current item.",
                    )
                    if inserted_specs:
                        item_state.setdefault("history", []).append(
                            {
                                "at": now_iso(),
                                "event": "analysis_review_inserted_items_before_rerun",
                                "message": analysis_review.get("message", "") or "Inserted new items before rerunning the current item.",
                                "item_ids": [item.get("id", "") for item in inserted_specs],
                            }
                        )
                        if args.progress_hooks:
                            send_hook(
                                args.gateway_url,
                                hook_token,
                                progress_text(
                                    batch_id,
                                    state,
                                    item_state,
                                    f"Inserted {len(inserted_specs)} item(s) before rerunning the current item.",
                                ),
                            )
                        continue
                update_progress(state)
                write_json(state_path, state)
                continue

            item_state["status"] = "completed"
            item_state["last_error_code"] = ""
            item_state["last_error_message"] = ""
            record_aux_update(
                state,
                analysis_review.get("aux_entry", {}),
                synthetic_response.get("result_path", ""),
                analysis_review.get("analysis_record", {}),
            )
            maybe_save_successful_recovery_case(
                Path(os.path.expanduser(args.recovery_case_library_root)).resolve(),
                batch_id,
                item_spec,
                rendered_item,
                item_state,
                synthetic_response,
            )

            append_batch_event(
                state,
                "late_success_completed",
                "Completed item using a previously successful attempt result.",
                item_id=item_state.get("id", ""),
                job_id=prior_success.get("job_id", ""),
            )
            review_action = str(analysis_review.get("action", "") or "none").strip().lower()
            inserted_after = select_analysis_branch_items(
                item_spec,
                action=review_action,
                rendered_item=rendered_item,
                aux_entry=analysis_review.get("aux_entry", {}),
            ) + list(analysis_review.get("insert_items_after", []))
            if inserted_after:
                inserted_specs = insert_dynamic_items(
                    batch_spec,
                    state,
                    batch_spec_path,
                    state_path,
                    next_index + 1,
                    inserted_after,
                    source_event="analysis_review_insert_after_completion",
                    source_item_id=str(item_state.get("id", "") or ""),
                    source_message=analysis_review.get("message", "") or "Inserted new items after completing the current item.",
                )
                if inserted_specs:
                    item_state.setdefault("history", []).append(
                        {
                            "at": now_iso(),
                            "event": "analysis_review_inserted_items_after",
                            "message": analysis_review.get("message", "") or "Inserted new items after completion.",
                            "item_ids": [item.get("id", "") for item in inserted_specs],
                        }
                    )
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                completion_message = analysis_review.get("message", "") or "Recovered from an earlier timeout/failure by reusing a completed prior attempt."
                if inserted_after:
                    completion_message = f"{completion_message} Inserted {len(inserted_after)} follow-up item(s)."
                send_hook(
                    args.gateway_url,
                    hook_token,
                    progress_text(batch_id, state, item_state, completion_message),
                )
            continue

        measurement_plan = run_measurement_plan_with_agent(
            batch_id=batch_id,
            state_path=state_path,
            batch_spec=batch_spec,
            state=state,
            current_index=next_index,
            item_spec=item_spec,
            item_state=item_state,
            rendered_item=rendered_item,
            future_items=future_items,
            aux_entries=aux_entries,
            policy=state.get("policy", {}),
            args=args,
            hook_token=hook_token,
        )
        planning_record = measurement_plan.get("planning_record", {})
        if planning_record:
            item_state.setdefault("history", []).append(
                {
                    "at": now_iso(),
                    "event": "measurement_plan",
                    "message": measurement_plan.get("message", "") or "Applied pre-run measurement planning.",
                    "request_path": planning_record.get("request_path", ""),
                    "plan_path": planning_record.get("plan_path", ""),
                    "hook_ok": planning_record.get("hook_ok", False),
                    "timeout_seconds": planning_record.get("timeout_seconds", ""),
                    "pre_enqueue_advisory": copy.deepcopy(planning_record.get("pre_enqueue_advisory", {})),
                    "plan": copy.deepcopy(planning_record.get("plan", {})),
                }
            )
        if measurement_plan.get("action") == "stop":
            item_state["status"] = "failed"
            item_state["last_error_code"] = "MEASUREMENT_PLAN_STOP"
            item_state["last_error_message"] = str(measurement_plan.get("message", "") or "Pre-run measurement planning rejected this item.")
            state["status"] = "failed"
            state["finished_at"] = now_iso()
            state["current_item_id"] = item_state.get("id", "")
            append_batch_event(state, "failed", "Stopped batch before execution because measurement planning requested operator review.", item_id=item_state.get("id", ""), error_code=item_state.get("last_error_code", ""))
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                send_hook(args.gateway_url, hook_token, progress_text(batch_id, state, item_state, item_state["last_error_message"]))
            print(json.dumps(state, ensure_ascii=False))
            return 1
        prepend_items = list(measurement_plan.get("prepend_items", []))
        if prepend_items:
            inserted_specs = insert_dynamic_items(
                batch_spec,
                state,
                batch_spec_path,
                state_path,
                next_index,
                prepend_items,
                source_event="measurement_plan_prepend_items",
                source_item_id=str(item_state.get("id", "") or ""),
                source_message=measurement_plan.get("message", "") or "Inserted new items before executing the current item.",
            )
            if inserted_specs:
                item_state.setdefault("history", []).append(
                    {
                        "at": now_iso(),
                        "event": "measurement_plan_inserted_items_before_current",
                        "message": measurement_plan.get("message", "") or "Inserted new items before the current item.",
                        "item_ids": [item.get("id", "") for item in inserted_specs],
                    }
                )
                if args.progress_hooks:
                    send_hook(
                        args.gateway_url,
                        hook_token,
                        progress_text(
                            batch_id,
                            state,
                            item_state,
                            f"Inserted {len(inserted_specs)} item(s) before the current item.",
                        ),
                    )
                continue
        item_spec = copy.deepcopy(measurement_plan.get("item_spec", item_spec))
        rendered_item = copy.deepcopy(measurement_plan.get("rendered_item", rendered_item))

        item_state["status"] = "running"
        item_state["attempts"] = int(item_state.get("attempts", 0)) + 1
        item_state["last_attempt_at"] = now_iso()
        item_state["last_error_code"] = ""
        item_state["last_error_message"] = ""
        state["current_item_id"] = item_state.get("id", "")
        update_progress(state)
        write_json(state_path, state)

        if args.progress_hooks:
            send_hook(
                args.gateway_url,
                hook_token,
                progress_text(batch_id, state, item_state, f"Starting attempt {item_state['attempts']}."),
            )

        returncode, response, stdout, stderr, submission_guard = submit_item_with_idempotence_guard(
            rendered_item,
            batch_spec,
            args,
            batch_id=batch_id,
            item_state=item_state,
            state_path=state_path,
            extra_env={
                INTERNAL_MEASUREMENT_PLAN_ENV: "1",
                SUBMISSION_PATH_ENV: "single_item_measurement_plan",
            },
        )
        if str(submission_guard.get("action", "") or "").startswith("attached_existing") and int(item_state.get("attempts", 0)) > 1:
            item_state["attempts"] = int(item_state.get("attempts", 0)) - 1
        terminal_raw_export = ensure_response_savedexperiment_raw_export(response)
        outcome = classify_attempt(response, returncode, state.get("policy", {}))
        history_entry = {
            "at": now_iso(),
            "event": "queue_submit",
            "returncode": returncode,
            "stdout": stdout,
            "stderr": stderr,
            "job_id": response.get("job_id", ""),
            "queue_root": response.get("queue_root", ""),
            "final_state": response.get("final_state", ""),
            "result_path": response.get("result_path", ""),
            "outcome_summary": response.get("outcome_summary", {}),
            "savedexperiment_raw_export": copy.deepcopy(terminal_raw_export),
            "runtime_watch": copy.deepcopy(response.get("runtime_watch", {})),
            "agent_recovery": copy.deepcopy(response.get("agent_recovery", {})),
            "submission_guard": copy.deepcopy(submission_guard),
            "retry_rule": outcome,
        }
        item_state.setdefault("history", []).append(history_entry)
        item_state["last_error_code"] = outcome.get("error_code", "")
        item_state["last_error_message"] = outcome.get("error_message", "")

        if outcome["action"] == "complete":
            analysis_review = {
                "action": "none",
                "message": "",
                "analysis_record": {},
                "aux_entry": {},
                "item_overrides": {},
                "insert_items_after": [],
                "insert_items_before_rerun": [],
            }
            if should_run_analysis(rendered_item, response, state.get("policy", {})):
                analysis_review = run_analysis_with_agent_review(
                    batch_id=batch_id,
                    state_path=state_path,
                    batch_spec=batch_spec,
                    state=state,
                    current_index=next_index,
                    item_spec=item_spec,
                    item_state=item_state,
                    rendered_item=rendered_item,
                    response=response,
                    future_items=future_items,
                    aux_entries=aux_entries,
                    policy=state.get("policy", {}),
                    args=args,
                    hook_token=hook_token,
                )
                item_state["analysis"] = copy.deepcopy(analysis_review.get("analysis_record", {}))

            if analysis_review.get("action") == "stop":
                item_state["status"] = "failed"
                item_state["last_error_code"] = "ANALYSIS_REVIEW_STOP"
                item_state["last_error_message"] = str(analysis_review.get("message", "") or "Analysis review rejected the completed run.")
                state["status"] = "failed"
                state["finished_at"] = now_iso()
                state["current_item_id"] = item_state.get("id", "")
                append_batch_event(state, "failed", "Stopped batch after analysis review rejected the completed run.", item_id=item_state.get("id", ""), error_code=item_state.get("last_error_code", ""))
                update_progress(state)
                write_json(state_path, state)
                if args.progress_hooks:
                    send_hook(args.gateway_url, hook_token, progress_text(batch_id, state, item_state, item_state["last_error_message"]))
                print(json.dumps(state, ensure_ascii=False))
                return 1

            if analysis_review.get("action") == "rerun_item":
                item_state["status"] = "retrying"
                item_state["last_error_code"] = "ANALYSIS_RERUN_REQUESTED"
                item_state["last_error_message"] = str(analysis_review.get("message", "") or "Analysis review requested another measurement run.")
                item_state["retry_overrides"] = deep_merge_dicts(item_state.get("retry_overrides", {}), analysis_review.get("item_overrides", {}))
                item_state.setdefault("history", []).append(
                    {
                        "at": now_iso(),
                        "event": "analysis_review_requested_rerun",
                        "message": item_state["last_error_message"],
                        "retry_overrides": copy.deepcopy(item_state.get("retry_overrides", {})),
                    }
                )
                items_before_rerun = select_analysis_branch_items(
                    item_spec,
                    action="rerun_item",
                    rendered_item=rendered_item,
                ) + list(analysis_review.get("insert_items_before_rerun", []))
                if items_before_rerun:
                    inserted_specs = insert_dynamic_items(
                        batch_spec,
                        state,
                        batch_spec_path,
                        state_path,
                        next_index,
                        items_before_rerun,
                        source_event="analysis_review_insert_before_rerun",
                        source_item_id=str(item_state.get("id", "") or ""),
                        source_message=analysis_review.get("message", "") or "Inserted new items before rerunning the current item.",
                    )
                    if inserted_specs:
                        item_state.setdefault("history", []).append(
                            {
                                "at": now_iso(),
                                "event": "analysis_review_inserted_items_before_rerun",
                                "message": analysis_review.get("message", "") or "Inserted new items before rerunning the current item.",
                                "item_ids": [item.get("id", "") for item in inserted_specs],
                            }
                        )
                        if args.progress_hooks:
                            send_hook(
                                args.gateway_url,
                                hook_token,
                                progress_text(
                                    batch_id,
                                    state,
                                    item_state,
                                    f"Inserted {len(inserted_specs)} item(s) before rerunning the current item.",
                                ),
                            )
                        continue
                outcome = {
                    "action": "retry",
                    "reason": "analysis_review_rerun_item",
                    "error_code": item_state["last_error_code"],
                    "error_message": item_state["last_error_message"],
                    "rule_source": "analysis_review_plan",
                }
            else:
                item_state["status"] = "completed"
                item_state["last_error_code"] = ""
                item_state["last_error_message"] = ""
                record_aux_update(
                    state,
                    analysis_review.get("aux_entry", {}),
                    response.get("result_path", ""),
                    analysis_review.get("analysis_record", {}),
                )
                maybe_save_successful_recovery_case(
                    Path(os.path.expanduser(args.recovery_case_library_root)).resolve(),
                    batch_id,
                    item_spec,
                    rendered_item,
                    item_state,
                    response,
                )

                append_batch_event(state, "item_completed", "Completed item successfully.", item_id=item_state.get("id", ""))
                review_action = str(analysis_review.get("action", "") or "none").strip().lower()
                inserted_after = select_analysis_branch_items(
                    item_spec,
                    action=review_action,
                    rendered_item=rendered_item,
                    aux_entry=analysis_review.get("aux_entry", {}),
                ) + list(analysis_review.get("insert_items_after", []))
                if inserted_after:
                    inserted_specs = insert_dynamic_items(
                        batch_spec,
                        state,
                        batch_spec_path,
                        state_path,
                        next_index + 1,
                        inserted_after,
                        source_event="analysis_review_insert_after_completion",
                        source_item_id=str(item_state.get("id", "") or ""),
                        source_message=analysis_review.get("message", "") or "Inserted new items after completing the current item.",
                    )
                    if inserted_specs:
                        item_state.setdefault("history", []).append(
                            {
                                "at": now_iso(),
                                "event": "analysis_review_inserted_items_after",
                                "message": analysis_review.get("message", "") or "Inserted new items after completion.",
                                "item_ids": [item.get("id", "") for item in inserted_specs],
                            }
                        )
                update_progress(state)
                write_json(state_path, state)
                if args.progress_hooks:
                    extra = analysis_review.get("message", "") or "Completed successfully."
                    aux_update = analysis_review.get("aux_entry", {})
                    if isinstance(aux_update, dict) and aux_update.get("ok"):
                        extra = f"{extra} Updated aux `{aux_update.get('key')}` = `{aux_update.get('value')}`."
                    if inserted_after:
                        extra = f"{extra} Inserted {len(inserted_after)} follow-up item(s)."
                    send_hook(args.gateway_url, hook_token, progress_text(batch_id, state, item_state, extra.strip()))
                continue

        max_attempts = rendered_item.get("max_attempts", state.get("policy", {}).get("max_attempts_per_item"))
        reached_max_attempts = max_attempts is not None and item_state["attempts"] >= int(max_attempts)
        if outcome["action"] == "stop" or reached_max_attempts:
            item_state["status"] = "failed"
            state["status"] = "failed"
            state["finished_at"] = now_iso()
            state["current_item_id"] = item_state.get("id", "")
            stop_reason = outcome.get("reason", "fatal_failure")
            if reached_max_attempts and outcome["action"] != "stop":
                stop_reason = "max_attempts_exceeded"
                item_state["last_error_code"] = item_state["last_error_code"] or "MAX_ATTEMPTS_EXCEEDED"
                item_state["last_error_message"] = item_state["last_error_message"] or f"Reached max_attempts={int(max_attempts)} for this item."
            append_batch_event(
                state,
                "failed",
                "Stopped batch after item failure.",
                item_id=item_state.get("id", ""),
                stop_reason=stop_reason,
                error_code=item_state.get("last_error_code", ""),
            )
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                send_hook(
                    args.gateway_url,
                    hook_token,
                    progress_text(batch_id, state, item_state, f"Stopping after failure. error_code=`{item_state.get('last_error_code', '')}`"),
                )
            print(json.dumps(state, ensure_ascii=False))
            return 1

        item_state["status"] = "retrying"
        policy = state.get("policy", {})
        require_agent_plan = bool(policy.get("agent_recovery_required_for_retry", True))
        agent_plan_requested = should_request_agent_recovery(outcome, policy)
        agent_plan = {}
        agent_plan_failure_message = ""
        if agent_plan_requested and not hook_token and require_agent_plan:
            agent_plan_failure_message = "Recovery plan required for retry, but no OpenClaw hooks token was available."
            item_state.setdefault("history", []).append(
                {
                    "at": now_iso(),
                    "event": "agent_recovery_missing_token",
                    "message": agent_plan_failure_message,
                }
            )
        elif agent_plan_requested and hook_token:
            item_recovery_root = recovery_root / batch_id / str(item_state.get("id", "item"))
            item_recovery_root.mkdir(parents=True, exist_ok=True)
            request_path = item_recovery_root / f"attempt_{int(item_state.get('attempts', 0)):02d}.request.json"
            plan_path = item_recovery_root / f"attempt_{int(item_state.get('attempts', 0)):02d}.plan.json"
            recovery_request = build_recovery_request_payload(
                batch_id,
                state_path,
                batch_spec,
                item_spec,
                rendered_item,
                item_state,
                outcome,
                response,
                request_path,
                plan_path,
                Path(os.path.expanduser(args.recovery_case_library_root)).resolve(),
            )
            write_json(request_path, recovery_request)
            hook_payload = {
                "batchId": batch_id,
                "itemId": str(item_state.get("id", "") or ""),
                "attempt": int(item_state.get("attempts", 0)),
                "errorCode": str(outcome.get("error_code", "") or ""),
                "errorMessage": str(outcome.get("error_message", "") or ""),
                "requestPath": str(request_path),
                "planPath": str(plan_path),
            }
            hook_ok = post_hook(args.gateway_url, hook_token, args.recovery_hook_path, hook_payload)
            item_state.setdefault("history", []).append(
                {
                    "at": now_iso(),
                    "event": "recovery_plan_requested",
                    "message": "Requested a recovery plan for the failed item.",
                    "hook_ok": hook_ok,
                    "request_path": str(request_path),
                    "plan_path": str(plan_path),
                }
            )
            if hook_ok:
                planned = wait_for_recovery_plan(plan_path, float(args.recovery_plan_timeout_seconds))
                agent_plan = normalize_agent_recovery_plan(
                    planned or {},
                    str(item_spec.get("mode", batch_spec.get("mode", "execute")) or ""),
                    str(item_spec.get("sample_id", batch_spec.get("requested_sample_id", "")) or ""),
                )
                if agent_plan:
                    item_state.setdefault("history", []).append(
                        {
                            "at": now_iso(),
                            "event": "recovery_plan_received",
                            "message": agent_plan.get("operator_message", "") or agent_plan.get("reason", "") or "Received a recovery plan.",
                            "plan_path": str(plan_path),
                            "plan": copy.deepcopy(agent_plan.get("raw", {})),
                        }
                    )
                elif require_agent_plan:
                    agent_plan_failure_message = "Recovery plan was requested, but no valid plan was returned before the timeout."
                    item_state.setdefault("history", []).append(
                        {
                            "at": now_iso(),
                            "event": "agent_recovery_missing_plan",
                            "message": agent_plan_failure_message,
                            "plan_path": str(plan_path),
                        }
                    )
            elif require_agent_plan:
                agent_plan_failure_message = "Recovery plan hook request failed, so the batch cannot retry safely."
                item_state.setdefault("history", []).append(
                    {
                        "at": now_iso(),
                        "event": "agent_recovery_hook_failed",
                        "message": agent_plan_failure_message,
                        "plan_path": str(plan_path),
                    }
                )

        retry_overrides = copy.deepcopy(item_state.get("retry_overrides", {}))
        retry_note = ""
        if agent_plan_requested and require_agent_plan and not agent_plan:
            outcome = {
                "action": "stop",
                "reason": "recovery_plan_required",
                "error_code": str(outcome.get("error_code", "") or ""),
                    "error_message": agent_plan_failure_message or "Recovery plan was required but unavailable.",
                "rule_source": "agent_recovery_required",
            }
        elif agent_plan:
            action = str(agent_plan.get("action", "") or "").strip().lower()
            if action == "stop":
                outcome = {
                    "action": "stop",
                    "reason": "recovery_plan_stop",
                    "error_code": str(outcome.get("error_code", "") or ""),
                    "error_message": agent_plan.get("operator_message", "") or agent_plan.get("reason", "") or str(outcome.get("error_message", "") or ""),
                    "rule_source": "recovery_plan",
                }
            elif action == "retry":
                retry_overrides = deep_merge_dicts(retry_overrides, agent_plan.get("item_overrides", {}))
                retry_note = agent_plan.get("operator_message", "") or agent_plan.get("reason", "") or retry_note
                items_before_retry = select_recovery_branch_items(
                    item_spec,
                    action="retry",
                    error_code=str(outcome.get("error_code", "") or ""),
                ) + list(agent_plan.get("insert_items_before_retry", []))
                if items_before_retry:
                    if retry_overrides != item_state.get("retry_overrides", {}):
                        item_state["retry_overrides"] = retry_overrides
                    inserted_specs = insert_dynamic_items(
                        batch_spec,
                        state,
                        batch_spec_path,
                        state_path,
                        next_index,
                        items_before_retry,
                        source_event="agent_recovery_insert_before_retry",
                        source_item_id=str(item_state.get("id", "") or ""),
                        source_message=retry_note or "Inserted new items before retrying the failed item.",
                    )
                    if inserted_specs:
                        item_state.setdefault("history", []).append(
                            {
                                "at": now_iso(),
                                "event": "agent_recovery_inserted_items_before_retry",
                                "message": retry_note or "Inserted new items before retrying the failed item.",
                                "item_ids": [item.get("id", "") for item in inserted_specs],
                                "retry_overrides": copy.deepcopy(item_state.get("retry_overrides", {})),
                            }
                        )
                        if args.progress_hooks:
                            send_hook(
                                args.gateway_url,
                                hook_token,
                                progress_text(
                                    batch_id,
                                    state,
                                    item_state,
                                    f"Inserted {len(inserted_specs)} item(s) before retrying the failed item.",
                                ),
                            )
                        continue
            elif action == "complete":
                item_state["status"] = "completed"
                item_state["last_error_code"] = ""
                item_state["last_error_message"] = ""
                item_state.setdefault("history", []).append(
                    {
                        "at": now_iso(),
                        "event": "recovery_plan_completed",
                        "message": agent_plan.get("operator_message", "") or agent_plan.get("reason", "") or "Marked item complete from a recovery plan.",
                        "plan": copy.deepcopy(agent_plan.get("raw", {})),
                    }
                )
                append_batch_event(
                    state,
                    "item_completed",
                    "Completed item from agent recovery plan.",
                    item_id=item_state.get("id", ""),
                )
                update_progress(state)
                write_json(state_path, state)
                if args.progress_hooks:
                    send_hook(
                        args.gateway_url,
                        hook_token,
                        progress_text(batch_id, state, item_state, agent_plan.get("operator_message", "") or "Marked complete from recovery plan."),
                    )
                continue
        elif not agent_plan_requested:
            retry_overrides, retry_note = plan_retry_adjustments(item_spec, item_state, outcome)

        if retry_overrides != item_state.get("retry_overrides", {}):
            item_state["retry_overrides"] = retry_overrides
        if retry_note:
            item_state.setdefault("history", []).append(
                {
                    "at": now_iso(),
                    "event": "retry_adjusted",
                    "message": retry_note,
                    "retry_overrides": copy.deepcopy(item_state.get("retry_overrides", {})),
                }
            )

        fallback_retry_branch_items = []
        if outcome.get("action") == "retry" and not agent_plan:
            fallback_retry_branch_items = select_recovery_branch_items(
                item_spec,
                action="retry",
                error_code=str(outcome.get("error_code", "") or ""),
            )
        if fallback_retry_branch_items:
            inserted_specs = insert_dynamic_items(
                batch_spec,
                state,
                batch_spec_path,
                state_path,
                next_index,
                fallback_retry_branch_items,
                source_event="project_branch_insert_before_retry",
                source_item_id=str(item_state.get("id", "") or ""),
                source_message=retry_note or "Inserted project-planned items before retrying the failed item.",
            )
            if inserted_specs:
                item_state.setdefault("history", []).append(
                    {
                        "at": now_iso(),
                        "event": "project_branch_inserted_items_before_retry",
                        "message": retry_note or "Inserted project-planned items before retrying the failed item.",
                        "item_ids": [item.get("id", "") for item in inserted_specs],
                        "retry_overrides": copy.deepcopy(item_state.get("retry_overrides", {})),
                    }
                )
                if args.progress_hooks:
                    send_hook(
                        args.gateway_url,
                        hook_token,
                        progress_text(
                            batch_id,
                            state,
                            item_state,
                            f"Inserted {len(inserted_specs)} project-planned item(s) before retrying the failed item.",
                        ),
                    )
                continue

        if outcome["action"] == "stop":
            item_state["status"] = "failed"
            state["status"] = "failed"
            state["finished_at"] = now_iso()
            state["current_item_id"] = item_state.get("id", "")
            append_batch_event(
                state,
                "failed",
                "Stopped batch because agent recovery did not authorize a retry.",
                item_id=item_state.get("id", ""),
                stop_reason=outcome.get("reason", "recovery_plan_stop"),
                error_code=item_state.get("last_error_code", ""),
            )
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                send_hook(
                    args.gateway_url,
                    hook_token,
                    progress_text(batch_id, state, item_state, f"Stopping after failure. {item_state.get('last_error_message', '')}"),
                )
            print(json.dumps(state, ensure_ascii=False))
            return 1

        append_batch_event(
            state,
            "retrying",
            "Retrying item after a retryable failure.",
            item_id=item_state.get("id", ""),
            error_code=item_state.get("last_error_code", ""),
        )
        update_progress(state)
        write_json(state_path, state)
        if args.progress_hooks:
            extra = f"Retrying after failure. error_code=`{item_state.get('last_error_code', '')}`"
            if retry_note:
                extra += f" {retry_note}"
            send_hook(
                args.gateway_url,
                hook_token,
                progress_text(batch_id, state, item_state, extra),
            )

        control = load_control(control_path)
        sync_control_into_state(state, control_path, control)
        if control.get("stop_requested"):
            item_state["status"] = "stopped"
            item_state.setdefault("history", []).append(
                {
                    "at": now_iso(),
                    "event": "stop_requested",
                    "message": str(control.get("stop_reason", "") or "Stop requested before retrying the item."),
                }
            )
            state["status"] = "stopped"
            state["finished_at"] = now_iso()
            state["current_item_id"] = item_state.get("id", "")
            append_batch_event(state, "stopped", "Stopped before retry because a control request was present.", item_id=item_state.get("id", ""))
            update_progress(state)
            write_json(state_path, state)
            if args.progress_hooks:
                stop_reason = str(control.get("stop_reason", "") or "manual stop request")
                send_hook(args.gateway_url, hook_token, progress_text(batch_id, state, item_state, f"Stopped before retry. reason=`{stop_reason}`"))
            print(json.dumps(state, ensure_ascii=False))
            return STOPPED_EXIT_CODE

        state["status"] = "retry_wait"
        update_progress(state)
        write_json(state_path, state)
        time.sleep(float(state.get("policy", {}).get("retry_delay_seconds", args.retry_delay_seconds)))
        state["status"] = "running"
        update_progress(state)
        write_json(state_path, state)


if __name__ == "__main__":
    raise SystemExit("Direct execution of this execution-source file is disabled in the public release.")
