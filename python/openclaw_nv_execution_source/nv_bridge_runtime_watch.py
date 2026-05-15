#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import os
import re
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools_mat_parse import analyze_savedexperiment_average_drift_mat_files, export_savedexperiment_mat_raw_files, normalize_agent_path
except Exception:
    analyze_savedexperiment_average_drift_mat_files = None
    export_savedexperiment_mat_raw_files = None
    normalize_agent_path = lambda value: str(value or "").strip()  # type: ignore


DEFAULT_SAVED_EXPERIMENTS_ROOT = Path("<MATLAB_23C_ROOT>/savedexperiments/NV1")
DEFAULT_REQUESTED_BY = "openclaw-runtime-watch"
FINAL_QUEUE_STATES = {"done", "failed"}
RECENT_OBSERVATION_LIMIT = 24
FINAL_COUNTS_RE = re.compile(r"([-+]?\d+(?:\.\d+)?)")
NON_SAVEDEXPERIMENT_RECIPES = {"imaging_scan_v1", "track_center_v1"}
MATLAB_COMMAND_LOG_FILENAME = "matlab_command_window.log"
MATLAB_COMMAND_LOG_TAIL_BYTES = 32768
MATLAB_COMMAND_LOG_TAIL_LINES = 16
MATLAB_FATAL_LOG_PATTERNS = [
    re.compile(r"^\s*Error using\b", re.IGNORECASE),
    re.compile(r"^\s*Undefined function\b", re.IGNORECASE),
    re.compile(r"^\s*Unrecognized function or variable\b", re.IGNORECASE),
    re.compile(r"\bIndex exceeds\b", re.IGNORECASE),
    re.compile(r"\bArray indices must be\b", re.IGNORECASE),
    re.compile(r"\bSubscript indices must\b", re.IGNORECASE),
    re.compile(r"\bReference to non-existent field\b", re.IGNORECASE),
    re.compile(r"\bDot indexing is not supported\b", re.IGNORECASE),
    re.compile(r"\bInvalid or deleted object\b", re.IGNORECASE),
    re.compile(r"\bCell contents reference from a non-cell array object\b", re.IGNORECASE),
]
PRE_RUN_PHASES = {
    "",
    "job_initialized",
    "job_loaded",
    "job_validated",
    "dry_run_bootstrapped",
    "execute_bootstrapped",
    "execute_gate_opened",
    "sequence_wrapper_started",
    "prepare_session_complete",
    "scheduled_tracking_prepared",
    "align_nv_active",
    "align_nv_complete",
    "configure_experiment_active",
    "configure_experiment_complete",
    "run_experiment_ready",
    "run_experiment_starting",
    "run_experiment_monitor_start_failed",
}
FINALIZING_PHASES = {
    "run_experiment_returned",
    "run_experiment_failed",
    "execute_finished",
    "result_ready",
    "safe_shutdown_complete",
    "writing_result",
    "result_written",
    "moving_finalized_job",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_path_for_agent(value: Any) -> str:
    return normalize_agent_path(value) if callable(normalize_agent_path) else str(value or "").strip()


def normalize_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        return float(value)
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def normalize_int(value: Any) -> int | None:
    number = normalize_float(value)
    if number is None:
        return None
    try:
        return int(round(number))
    except (TypeError, ValueError):
        return None


def parse_iso_datetime(text: Any) -> datetime | None:
    raw = str(text or "").strip()
    if not raw:
        return None
    try:
        if raw.endswith("Z"):
            return datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return datetime.fromisoformat(raw)
    except ValueError:
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d-%H%M%S"):
            try:
                return datetime.strptime(raw, fmt)
            except ValueError:
                continue
    return None


def seconds_since_datetime(text: Any) -> float | None:
    parsed = parse_iso_datetime(text)
    if parsed is None:
        return None
    if parsed.tzinfo is None:
        delta = datetime.now() - parsed
    else:
        delta = datetime.now(parsed.tzinfo) - parsed
    return max(0.0, delta.total_seconds())


def clamp_float(value: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, value))


def phase_group(phase: Any) -> str:
    text = str(phase or "").strip()
    if text in PRE_RUN_PHASES:
        return "pre_run"
    if text in FINALIZING_PHASES:
        return "finalizing"
    if text.startswith("run_experiment"):
        return "in_run"
    return "pre_run"


def latest_status_activity_age_seconds(status: dict[str, Any], status_path: Path) -> float | None:
    timestamps: list[float] = []
    if isinstance(status, dict):
        updated_at = parse_iso_datetime(status.get("updated_at", ""))
        if updated_at is not None:
            timestamps.append(updated_at.timestamp())
        monitor = status.get("monitor", {}) if isinstance(status.get("monitor"), dict) else {}
        last_tick_at = parse_iso_datetime(monitor.get("last_tick_at", ""))
        if last_tick_at is not None:
            timestamps.append(last_tick_at.timestamp())
    if not timestamps and status_path.is_file():
        timestamps.append(status_path.stat().st_mtime)
    if not timestamps:
        return None
    return max(0.0, time.time() - max(timestamps))


def normalize_expected_runtime_summary(expected_runtime: Any) -> dict[str, Any]:
    if isinstance(expected_runtime, dict):
        return expected_runtime
    if not isinstance(expected_runtime, list):
        return {}

    entries = [entry for entry in expected_runtime if isinstance(entry, dict)]
    if not entries:
        return {}

    merged = copy.deepcopy(entries[0])
    numeric_fields = (
        "total_seconds",
        "per_average_seconds",
        "tracking_window_seconds",
        "averages",
        "repetitions",
        "num_scan_points",
    )
    for field in numeric_fields:
        numeric_values = [normalize_float(entry.get(field)) for entry in entries]
        numeric_values = [value for value in numeric_values if value is not None]
        if numeric_values:
            merged[field] = max(numeric_values)

    if "ok" not in merged:
        merged["ok"] = any(bool(entry.get("ok", False)) for entry in entries)

    for field in ("estimator_mode", "notes"):
        if merged.get(field) not in (None, "", []):
            continue
        for entry in entries[1:]:
            value = entry.get(field)
            if value not in (None, "", []):
                merged[field] = copy.deepcopy(value)
                break

    return merged


def runtime_watch_thresholds(status: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    group = phase_group(status.get("phase", ""))
    expected = normalize_expected_runtime_summary(status.get("expected_runtime"))

    warn_after = normalize_float(config.get("warn_after_seconds"))
    max_stale = normalize_float(config.get("max_stale_seconds"))
    basis_seconds = None

    if group == "pre_run":
        warn_after = normalize_float(config.get("pre_run_warn_after_seconds")) if config.get("pre_run_warn_after_seconds") is not None else warn_after
        max_stale = normalize_float(config.get("pre_run_max_stale_seconds")) if config.get("pre_run_max_stale_seconds") is not None else max_stale
        if warn_after is None:
            warn_after = 300.0
        if max_stale is None:
            max_stale = 600.0
    elif group == "in_run":
        basis_seconds = (
            normalize_float(expected.get("tracking_window_seconds"))
            or normalize_float(expected.get("per_average_seconds"))
            or normalize_float(expected.get("total_seconds"))
            or 300.0
        )
        if max_stale is None:
            max_stale = normalize_float(config.get("in_run_max_stale_seconds"))
        if max_stale is None:
            multiplier = normalize_float(config.get("in_run_stale_runtime_multiplier")) or 1.5
            grace = normalize_float(config.get("in_run_stale_grace_seconds")) or 120.0
            minimum = normalize_float(config.get("in_run_min_max_stale_seconds")) or 300.0
            maximum = normalize_float(config.get("in_run_max_max_stale_seconds")) or 7200.0
            max_stale = clamp_float(round(multiplier * basis_seconds + grace), minimum, maximum)
        if warn_after is None:
            warn_after = normalize_float(config.get("in_run_warn_after_seconds"))
        if warn_after is None:
            warn_after = min(max_stale - 60.0, max(120.0, round(0.5 * max_stale)))
    else:
        warn_after = normalize_float(config.get("finalizing_warn_after_seconds")) if config.get("finalizing_warn_after_seconds") is not None else warn_after
        max_stale = normalize_float(config.get("finalizing_max_stale_seconds")) if config.get("finalizing_max_stale_seconds") is not None else max_stale
        if warn_after is None:
            warn_after = 30.0
        if max_stale is None:
            max_stale = 120.0

    warn_after = max(0.0, float(warn_after))
    max_stale = max(warn_after, float(max_stale))
    return {
        "phase_group": group,
        "warn_after_seconds": warn_after,
        "max_stale_seconds": max_stale,
        "basis_seconds": basis_seconds,
    }


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_json_dict_if_exists(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = read_json(path)
    except (OSError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def file_age_seconds(path: Path) -> float | None:
    try:
        return max(0.0, time.time() - path.stat().st_mtime)
    except OSError:
        return None


def read_text_tail(path: Path, max_bytes: int) -> str:
    if max_bytes <= 0:
        max_bytes = MATLAB_COMMAND_LOG_TAIL_BYTES
    with path.open("rb") as handle:
        try:
            handle.seek(0, os.SEEK_END)
            size = handle.tell()
            handle.seek(max(0, size - max_bytes), os.SEEK_SET)
        except OSError:
            handle.seek(0)
        data = handle.read(max_bytes)
    return data.decode("utf-8", errors="replace")


def resolve_matlab_command_log_path(
    probe: dict[str, Any],
    status: dict[str, Any],
    config: dict[str, Any],
) -> Path | None:
    paths = status.get("paths", {}) if isinstance(status.get("paths"), dict) else {}
    configured_name = str(config.get("matlab_command_log_name", MATLAB_COMMAND_LOG_FILENAME) or MATLAB_COMMAND_LOG_FILENAME)
    candidates = [
        paths.get("matlab_command_log_path", ""),
        paths.get("matlab_log_path", ""),
    ]
    job_dir = probe.get("job_dir")
    if isinstance(job_dir, Path) and job_dir:
        candidates.append(str(job_dir / configured_name))
    resolved: list[Path] = []
    for candidate in candidates:
        text = str(candidate or "").strip()
        if not text:
            continue
        path = Path(normalize_path_for_agent(text)).expanduser()
        resolved.append(path)
        if path.is_file():
            return path
    return resolved[0] if resolved else None


def classify_matlab_log_tail(text: str) -> dict[str, Any]:
    lines = text.splitlines()
    latest_line = ""
    for line in reversed(lines):
        if line.strip():
            latest_line = line.strip()
            break

    fatal_line = ""
    fatal_pattern = ""
    for line in reversed(lines):
        stripped = line.strip()
        if not stripped or stripped.lower().startswith("warning:"):
            continue
        for pattern in MATLAB_FATAL_LOG_PATTERNS:
            if pattern.search(stripped):
                fatal_line = stripped
                fatal_pattern = pattern.pattern
                break
        if fatal_line:
            break

    return {
        "latest_line": latest_line,
        "tail_lines": lines[-MATLAB_COMMAND_LOG_TAIL_LINES:],
        "fatal_detected": bool(fatal_line),
        "fatal_line": fatal_line,
        "fatal_pattern": fatal_pattern,
    }


def analyze_matlab_command_log(
    probe: dict[str, Any],
    status: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    if not bool(config.get("matlab_command_log_enabled", True)):
        return {"enabled": False, "available": False}

    path = resolve_matlab_command_log_path(probe, status, config)
    if path is None:
        return {"enabled": True, "available": False, "path": ""}
    payload: dict[str, Any] = {
        "enabled": True,
        "available": path.is_file(),
        "path": str(path),
        "size_bytes": 0,
        "mtime_age_seconds": None,
        "latest_line": "",
        "tail_lines": [],
        "fatal_detected": False,
        "fatal_line": "",
        "fatal_pattern": "",
        "read_error": "",
    }
    if not path.is_file():
        return payload

    try:
        stat = path.stat()
        payload["size_bytes"] = int(stat.st_size)
        payload["mtime_age_seconds"] = max(0.0, time.time() - stat.st_mtime)
        tail_bytes = int(normalize_float(config.get("matlab_command_log_tail_bytes")) or MATLAB_COMMAND_LOG_TAIL_BYTES)
        tail = read_text_tail(path, tail_bytes)
        payload.update(classify_matlab_log_tail(tail))
    except Exception as exc:
        payload["read_error"] = str(exc)
    return payload


def matlab_log_recent(log_analysis: dict[str, Any], config: dict[str, Any], thresholds: dict[str, Any]) -> bool:
    if not isinstance(log_analysis, dict) or not bool(log_analysis.get("available", False)):
        return False
    age = normalize_float(log_analysis.get("mtime_age_seconds"))
    if age is None:
        return False
    configured = normalize_float(config.get("matlab_command_log_activity_fresh_seconds"))
    warn_after = normalize_float(thresholds.get("warn_after_seconds")) or 0.0
    fresh_seconds = max(configured or 0.0, min(900.0, max(120.0, warn_after)))
    return age <= fresh_seconds


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(serialized)
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except OSError:
            pass
        raise


def summarize_result(result: dict[str, Any]) -> dict[str, Any]:
    summary = result.get("summary", {}) if isinstance(result, dict) else {}
    align = summary.get("align_nv", {}) if isinstance(summary, dict) else {}
    landmark = align.get("landmark_match", {}) if isinstance(align, dict) else {}
    search_scan = align.get("search_scan", {}) if isinstance(align, dict) else {}
    return {
        "status": result.get("status", ""),
        "error_code": result.get("error_code", ""),
        "run_id": result.get("run_id", ""),
        "data_path": result.get("data_path", ""),
        "align_source": align.get("source", ""),
        "final_counts_kcps": align.get("final_counts_kcps"),
        "landmark_match_ok": landmark.get("ok"),
        "used_search_scan": search_scan.get("ran"),
    }


def probe_job(queue_root: Path, job_id: str) -> dict[str, Any]:
    for state in ["done", "failed", "running", "queued"]:
        job_dir = queue_root / state / job_id
        if job_dir.is_dir():
            return {
                "state": state,
                "job_dir": job_dir,
                "result_path": job_dir / "result.json",
                "status_path": job_dir / "status.json",
                "control_path": job_dir / "control.json",
            }
    return {
        "state": "missing",
        "job_dir": Path(),
        "result_path": Path(),
        "status_path": Path(),
        "control_path": Path(),
    }


def default_watch_config(job: dict[str, Any] | None = None, overrides: dict[str, Any] | None = None) -> dict[str, Any]:
    metadata = job.get("metadata", {}) if isinstance(job, dict) else {}
    runtime_watch = metadata.get("runtime_watch", {}) if isinstance(metadata, dict) else {}
    recipe = str(job.get("recipe", "") or "").strip().lower() if isinstance(job, dict) else ""
    standalone_non_savedexperiment = bool(
        isinstance(job, dict)
        and (
            recipe in NON_SAVEDEXPERIMENT_RECIPES
            or (recipe == "" and ("imaging" in job or "tracking" in job) and "sequence_manifest_id" not in job)
        )
    )
    config: dict[str, Any] = {
        "enabled": True,
        "requested_by": DEFAULT_REQUESTED_BY,
        "savedexperiments_root": str(DEFAULT_SAVED_EXPERIMENTS_ROOT),
        "warn_after_seconds": None,
        "max_stale_seconds": None,
        "pre_run_warn_after_seconds": 900.0 if standalone_non_savedexperiment else 300.0,
        "pre_run_max_stale_seconds": 1800.0 if standalone_non_savedexperiment else 600.0,
        "in_run_warn_after_seconds": None,
        "in_run_max_stale_seconds": None,
        "in_run_stale_runtime_multiplier": 1.5,
        "in_run_stale_grace_seconds": 600.0,
        "in_run_min_max_stale_seconds": 300.0,
        "in_run_max_max_stale_seconds": 7200.0,
        "finalizing_warn_after_seconds": 30.0,
        "finalizing_max_stale_seconds": 120.0,
        "disable_auto_stop_during_run": False,
        "stale_multiplier": 6.0,
        "stale_floor_seconds": 60.0,
        "pre_active_stale_floor_seconds": 900.0,
        "expected_runtime_multiplier": 2.0,
        "expected_runtime_grace_seconds": 900.0,
        "expected_runtime_overrun_action": "advisory",
        "average_stall_multiplier": 8.0,
        "average_stall_floor_seconds": 1800.0,
        "matlab_command_log_enabled": True,
        "matlab_command_log_name": MATLAB_COMMAND_LOG_FILENAME,
        "matlab_command_log_tail_bytes": MATLAB_COMMAND_LOG_TAIL_BYTES,
        "matlab_command_log_activity_fresh_seconds": 300.0,
        "recent_average_drift_decision_enabled": False,
        "recent_average_drift_required_count": 3,
        "recent_average_drift_threshold": 0.15,
        "recent_average_drift_slice_index": 1,
        "recent_average_drift_min_averages_for_reference": 3,
        "recent_average_drift_analysis_timeout_seconds": 240.0,
        "stop_confirm_seconds": 180.0,
        "minimum_final_kcps": None,
        "observation_limit": RECENT_OBSERVATION_LIMIT,
    }
    if isinstance(runtime_watch, dict):
        config.update(copy.deepcopy(runtime_watch))
    if isinstance(metadata, dict) and metadata.get("minimum_final_kcps") is not None:
        config["minimum_final_kcps"] = metadata.get("minimum_final_kcps")
    if isinstance(overrides, dict):
        config.update(copy.deepcopy(overrides))
    config["enabled"] = bool(config.get("enabled", True))
    config["requested_by"] = str(config.get("requested_by", DEFAULT_REQUESTED_BY) or DEFAULT_REQUESTED_BY)
    config["savedexperiments_root"] = normalize_path_for_agent(config.get("savedexperiments_root", DEFAULT_SAVED_EXPERIMENTS_ROOT))
    return config


def initial_watch_session(job_id: str, config: dict[str, Any]) -> dict[str, Any]:
    return {
        "enabled": bool(config.get("enabled", True)),
        "job_id": job_id,
        "started_at": now_iso(),
        "savedexperiment_path": "",
        "savedexperiment_raw_export": {},
        "last_savedexperiment_count": 0,
        "last_savedexperiment_progress_at": None,
        "last_runtime_average_index": None,
        "last_progress_value": 0,
        "last_progress_at": None,
        "first_active_at": None,
        "recent_observations": [],
        "drift_decision": {
            "enabled": bool(config.get("recent_average_drift_decision_enabled", False)),
            "decision_required": False,
            "reason": "",
        },
        "advisory": {
            "detected": False,
            "code": "",
            "message": "",
            "detected_at": "",
            "agent_review_recommended": False,
        },
        "matlab_command_log": {},
        "anomaly": {
            "detected": False,
            "error_code": "",
            "message": "",
            "detected_at": "",
            "retry_recommended": False,
            "requested_stop": False,
            "request_written": False,
        },
        "stop_request": {
            "requested": False,
            "requested_at": "",
            "requested_by": "",
            "reason": "",
            "request_written": False,
        },
        "stop_confirmation": {
            "confirmed": False,
            "confirmed_at": "",
            "final_state": "",
            "stop_applied": False,
            "stop_apply_error": "",
            "wait_seconds": 0.0,
            "overdue": False,
        },
    }


def sequence_token_candidates(status: dict[str, Any], job: dict[str, Any] | None) -> list[str]:
    tokens: list[str] = []
    runtime = status.get("runtime", {}) if isinstance(status, dict) else {}
    summary = status.get("summary", {}) if isinstance(status, dict) else {}
    candidates = [
        runtime.get("sequence_name", ""),
        summary.get("sequence_name", ""),
    ]
    if isinstance(job, dict):
        candidates.extend(
            [
                job.get("sequence_file", ""),
                job.get("sequence_manifest_id", ""),
            ]
        )
    for candidate in candidates:
        text = str(candidate or "").strip()
        if not text:
            continue
        base = Path(text).stem.lower()
        if base and base not in tokens:
            tokens.append(base)
    return tokens


def derive_datetime_hint(status: dict[str, Any]) -> str:
    runtime = status.get("runtime", {}) if isinstance(status, dict) else {}
    summary = status.get("summary", {}) if isinstance(status, dict) else {}
    for candidate in [runtime.get("date_time", ""), summary.get("date_time", "")]:
        text = str(candidate or "").strip()
        if text:
            return text
    return ""


def job_uses_savedexperiment_raw_export(job: dict[str, Any] | None) -> bool:
    if not isinstance(job, dict):
        return True
    recipe = str(job.get("recipe", "") or "").strip().lower()
    if recipe in NON_SAVEDEXPERIMENT_RECIPES:
        return False
    if recipe == "" and ("imaging" in job or "tracking" in job) and "sequence_manifest_id" not in job:
        return False
    return True


job_uses_savedexperiment_summary = job_uses_savedexperiment_raw_export


def select_savedexperiment_path(
    status: dict[str, Any],
    job: dict[str, Any] | None,
    config: dict[str, Any],
    cached_path: str = "",
) -> str:
    if cached_path:
        cached = Path(cached_path)
        if cached.is_file():
            return normalize_path_for_agent(str(cached))

    root = Path(str(config.get("savedexperiments_root", DEFAULT_SAVED_EXPERIMENTS_ROOT))).expanduser()
    if not root.is_dir():
        return ""

    datetime_hint = derive_datetime_hint(status)
    sequence_tokens = sequence_token_candidates(status, job)
    started_at = parse_iso_datetime(status.get("started_at", ""))
    started_epoch = None if started_at is None else started_at.timestamp()

    candidates: list[Path] = []
    if datetime_hint:
        candidates.extend(sorted(root.glob(f"*{datetime_hint}.mat")))

    if not candidates:
        recent = sorted(root.glob("*.mat"), key=lambda path: path.stat().st_mtime, reverse=True)[:80]
        for path in recent:
            if started_epoch is not None and path.stat().st_mtime < started_epoch - 300:
                continue
            candidates.append(path)

    scored: list[tuple[int, float, Path]] = []
    for path in candidates:
        name = path.name.lower()
        score = 0
        if datetime_hint and datetime_hint.lower() in name:
            score += 100
        for token in sequence_tokens:
            if token and token in name:
                score += 20
        if started_epoch is not None and path.stat().st_mtime >= started_epoch - 60:
            score += 10
        scored.append((score, path.stat().st_mtime, path))

    if not scored:
        return ""

    scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return normalize_path_for_agent(str(scored[0][2]))


def compact_signal_summary(signal: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(signal, dict):
        return {}
    return {
        "source": str(signal.get("source", "") or ""),
        "readout_count": normalize_int(signal.get("readout_count")),
        "discard_first_average": bool(signal.get("discard_first_average", False)),
        "averages_used": normalize_int(signal.get("averages_used")),
        "num_points": normalize_int(signal.get("num_points")),
        "x_begin": normalize_float(signal.get("x_begin")),
        "x_end": normalize_float(signal.get("x_end")),
        "x_preview": copy.deepcopy(signal.get("x_preview", [])) if isinstance(signal.get("x_preview"), list) else [],
        "derived_signal_hidden": True,
        "hidden_derived_fields": ["y_values", "y_preview", "y_min", "y_max"],
    }


def compact_average_signal_summary(average_signal: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(average_signal, dict):
        return {}
    recent_entries: list[dict[str, Any]] = []
    raw_entries = average_signal.get("recent_entries", [])
    if isinstance(raw_entries, list):
        for entry in raw_entries[-4:]:
            if not isinstance(entry, dict):
                continue
            compact_entry = {
                "average_index": normalize_int(entry.get("average_index")),
                "source": str(entry.get("source", "") or ""),
                "readout_count": normalize_int(entry.get("readout_count")),
                "num_points": normalize_int(entry.get("num_points")),
                "contains_nan": bool(entry.get("contains_nan", False)),
                "readout_means": copy.deepcopy(entry.get("readout_means", [])) if isinstance(entry.get("readout_means"), list) else [],
                "derived_signal_hidden": True,
                "hidden_derived_fields": ["y_values", "y_preview", "y_min", "y_max", "y_mean", "y_std"],
            }
            recent_entries.append(compact_entry)
    return {
        "available": bool(average_signal.get("available", False)),
        "scan_index": normalize_int(average_signal.get("scan_index")),
        "total_averages": normalize_int(average_signal.get("total_averages")),
        "recent_limit": normalize_int(average_signal.get("recent_limit")),
        "readout_count": normalize_int(average_signal.get("readout_count")),
        "warnings": copy.deepcopy(average_signal.get("warnings", [])) if isinstance(average_signal.get("warnings"), list) else [],
        "derived_signal_hidden": True,
        "hidden_derived_fields": ["latest_mean_delta", "latest_max_abs_delta"],
        "recent_entries": recent_entries,
    }


def compact_readout_series(readouts: Any) -> list[dict[str, Any]]:
    compact: list[dict[str, Any]] = []
    if not isinstance(readouts, list):
        return compact
    for item in readouts:
        if not isinstance(item, dict):
            continue
        values = item.get("values", [])
        entry = {
            "readout_index": normalize_int(item.get("readout_index")),
            "num_points": normalize_int(item.get("num_points")),
            "mean": normalize_float(item.get("mean")),
            "std": normalize_float(item.get("std")),
            "min": normalize_float(item.get("min")),
            "max": normalize_float(item.get("max")),
            "preview": copy.deepcopy(item.get("preview", [])) if isinstance(item.get("preview"), list) else [],
        }
        if isinstance(values, list) and len(values) <= 128:
            entry["values"] = copy.deepcopy(values)
        compact.append(entry)
    return compact


def compact_raw_readouts_summary(raw_readouts: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(raw_readouts, dict):
        return {}
    recent_entries: list[dict[str, Any]] = []
    raw_entries = raw_readouts.get("recent_average_entries", [])
    if isinstance(raw_entries, list):
        for entry in raw_entries[-4:]:
            if not isinstance(entry, dict):
                continue
            recent_entries.append({
                "average_index": normalize_int(entry.get("average_index")),
                "readout_count": normalize_int(entry.get("readout_count")),
                "num_points": normalize_int(entry.get("num_points")),
                "readouts": compact_readout_series(entry.get("readouts", [])),
            })
    return {
        "available": bool(raw_readouts.get("available", False)),
        "scan_index": normalize_int(raw_readouts.get("scan_index")),
        "readout_count": normalize_int(raw_readouts.get("readout_count")),
        "num_points": normalize_int(raw_readouts.get("num_points")),
        "x_values": copy.deepcopy(raw_readouts.get("x_values", [])) if isinstance(raw_readouts.get("x_values"), list) else [],
        "combined": compact_readout_series(raw_readouts.get("combined", [])),
        "total_averages": normalize_int(raw_readouts.get("total_averages")),
        "recent_average_limit": normalize_int(raw_readouts.get("recent_average_limit")),
        "recent_average_entries": recent_entries,
        "warnings": copy.deepcopy(raw_readouts.get("warnings", [])) if isinstance(raw_readouts.get("warnings"), list) else [],
    }


def compact_savedexperiment_raw_export(raw_export: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(raw_export, dict):
        return {}
    return {
        "ok": bool(raw_export.get("ok", False)),
        "source": str(raw_export.get("source", "") or ""),
        "data_path": normalize_path_for_agent(raw_export.get("data_path", "")),
        "mat_variables": copy.deepcopy(raw_export.get("mat_variables", [])) if isinstance(raw_export.get("mat_variables"), list) else [],
        "scan": copy.deepcopy(raw_export.get("scan", {})) if isinstance(raw_export.get("scan"), dict) else {},
        "extra_variables": copy.deepcopy(raw_export.get("extra_variables", {}))
        if isinstance(raw_export.get("extra_variables"), dict)
        else {},
        "diagnostic_figures": copy.deepcopy(raw_export.get("diagnostic_figures", {}))
        if isinstance(raw_export.get("diagnostic_figures"), dict)
        else {},
        "warnings": copy.deepcopy(raw_export.get("warnings", [])) if isinstance(raw_export.get("warnings"), list) else [],
        "error_code": str(raw_export.get("error_code", "") or ""),
        "error_message": str(raw_export.get("error_message", "") or ""),
    }


def is_number_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, (int, float)) or item is None for item in value
    )


def looks_like_average_entry(value: Any) -> bool:
    return isinstance(value, list) and any(is_number_list(item) for item in value)


def find_average_entry_container(value: Any) -> list[Any]:
    if not isinstance(value, list) or not value:
        return []
    if any(looks_like_average_entry(item) for item in value):
        return value
    for item in value:
        found = find_average_entry_container(item)
        if found:
            return found
    return []


def savedexperiment_average_entries_from_raw_export(raw_export: dict[str, Any]) -> list[Any]:
    if not isinstance(raw_export, dict):
        return []
    scan = raw_export.get("scan", {}) if isinstance(raw_export.get("scan"), dict) else {}
    return find_average_entry_container(scan.get("ExperimentDataEachAvg", []))


def savedexperiment_average_count_from_raw_export(raw_export: dict[str, Any]) -> int:
    return len(savedexperiment_average_entries_from_raw_export(raw_export))


def savedexperiment_latest_average_entry_from_raw_export(raw_export: dict[str, Any]) -> Any:
    entries = savedexperiment_average_entries_from_raw_export(raw_export)
    return entries[-1] if entries else None


def nested_contains_nonfinite(value: Any) -> bool:
    if isinstance(value, float):
        return not (value == value and value not in {float("inf"), float("-inf")})
    if isinstance(value, int) or value is None:
        return False
    if isinstance(value, list):
        return any(nested_contains_nonfinite(item) for item in value)
    if isinstance(value, dict):
        return any(nested_contains_nonfinite(item) for item in value.values())
    return False


def average_entry_has_raw_points(value: Any) -> bool:
    if is_number_list(value):
        return True
    if isinstance(value, list):
        return any(average_entry_has_raw_points(item) for item in value)
    return False


def maybe_collect_savedexperiment_raw_export(
    status: dict[str, Any],
    job: dict[str, Any] | None,
    config: dict[str, Any],
    session: dict[str, Any],
) -> dict[str, Any]:
    if not callable(export_savedexperiment_mat_raw_files):
        return {}
    if not job_uses_savedexperiment_raw_export(job):
        return {}
    if str(status.get("state", "")).lower() not in {"running", "completed", "failed"}:
        return {}
    if phase_group(status.get("phase", "")) == "pre_run" and not derive_datetime_hint(status):
        return {}

    candidate = select_savedexperiment_path(status, job, config, session.get("savedexperiment_path", ""))
    if not candidate:
        return {}

    session["savedexperiment_path"] = candidate
    try:
        payloads = export_savedexperiment_mat_raw_files([candidate])
    except Exception as exc:
        return {
            "ok": False,
            "data_path": candidate,
            "error_code": "SAVEDEXPERIMENT_RAW_EXPORT_FAILED",
            "error_message": str(exc),
            "scan": {},
            "diagnostic_figures": {},
            "warnings": [],
        }
    if not payloads:
        return {}
    return compact_savedexperiment_raw_export(payloads[0] if isinstance(payloads[0], dict) else {})


def parse_final_counts_kcps(status: dict[str, Any]) -> float | None:
    runtime = status.get("runtime", {}) if isinstance(status, dict) else {}
    raw_text = str(runtime.get("final_counts_text", "") or "").strip()
    if not raw_text:
        return None
    match = FINAL_COUNTS_RE.search(raw_text)
    if match is None:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None


def observation_record(
    probe: dict[str, Any],
    status: dict[str, Any],
    control: dict[str, Any],
    saved_summary: dict[str, Any],
    matlab_log: dict[str, Any] | None = None,
) -> dict[str, Any]:
    runtime = status.get("runtime", {}) if isinstance(status.get("runtime"), dict) else {}
    expected = normalize_expected_runtime_summary(status.get("expected_runtime"))
    log_summary = matlab_log if isinstance(matlab_log, dict) else {}
    return {
        "at": now_iso(),
        "queue_state": str(probe.get("state", "") or ""),
        "phase": str(status.get("phase", "") or ""),
        "state": str(status.get("state", "") or ""),
        "elapsed_seconds": normalize_float(status.get("elapsed_seconds")),
        "average_index": normalize_int(runtime.get("average_index")),
        "averages_total": normalize_int(runtime.get("averages_total")),
        "savedexperiment_average_count": savedexperiment_average_count_from_raw_export(saved_summary),
        "expected_total_seconds": normalize_float(expected.get("total_seconds")),
        "expected_per_average_seconds": normalize_float(expected.get("per_average_seconds")),
        "status_age_seconds": normalize_float(seconds_since_datetime(status.get("updated_at"))),
        "stop_requested": bool(control.get("stop_requested", False)),
        "stop_applied": bool(control.get("stop_applied", False)),
        "final_counts_kcps": parse_final_counts_kcps(status),
        "savedexperiment_path": str(saved_summary.get("data_path", "") or ""),
        "matlab_command_log_age_seconds": normalize_float(log_summary.get("mtime_age_seconds")),
        "matlab_command_log_fatal_detected": bool(log_summary.get("fatal_detected", False)),
    }


def update_progress_tracking(
    session: dict[str, Any],
    status: dict[str, Any],
    saved_summary: dict[str, Any],
    now_monotonic: float,
) -> None:
    runtime = status.get("runtime", {}) if isinstance(status.get("runtime"), dict) else {}

    runtime_average_index = normalize_int(runtime.get("average_index"))
    saved_average_count = savedexperiment_average_count_from_raw_export(saved_summary)

    if str(status.get("phase", "")).startswith("run_experiment") and session.get("first_active_at") is None:
        session["first_active_at"] = now_monotonic

    effective_progress = max(runtime_average_index or 0, saved_average_count)
    if effective_progress > int(session.get("last_progress_value", 0) or 0):
        session["last_progress_value"] = effective_progress
        session["last_progress_at"] = now_monotonic

    if runtime_average_index is not None:
        previous_runtime_average = session.get("last_runtime_average_index")
        if previous_runtime_average is None or runtime_average_index > int(previous_runtime_average):
            session["last_runtime_average_index"] = runtime_average_index
            session["last_progress_at"] = now_monotonic

    if saved_average_count > int(session.get("last_savedexperiment_count", 0) or 0):
        session["last_savedexperiment_count"] = saved_average_count
        session["last_savedexperiment_progress_at"] = now_monotonic
        session["last_progress_at"] = now_monotonic


def build_anomaly(error_code: str, message: str, *, retry_recommended: bool = True, **details: Any) -> dict[str, Any]:
    payload = {
        "detected": True,
        "error_code": str(error_code or ""),
        "message": str(message or ""),
        "detected_at": now_iso(),
        "retry_recommended": bool(retry_recommended),
        "requested_stop": False,
        "request_written": False,
    }
    for key, value in details.items():
        payload[key] = copy.deepcopy(value)
    return payload


def maybe_collect_savedexperiment_average_drift(
    session: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    if not callable(analyze_savedexperiment_average_drift_mat_files):
        return {
            "ok": False,
            "source": "analyze_savedexperiment_average_drift.m",
            "reason": "drift_analysis_helper_unavailable",
            "entries": [],
        }
    data_path = str(session.get("savedexperiment_path", "") or "").strip()
    if not data_path:
        return {
            "ok": False,
            "source": "analyze_savedexperiment_average_drift.m",
            "reason": "savedexperiment_path_unavailable",
            "entries": [],
        }

    drop_threshold = normalize_float(config.get("recent_average_drift_threshold"))
    if drop_threshold is None:
        drop_threshold = 0.15
    slice_index = normalize_int(config.get("recent_average_drift_slice_index")) or 1
    min_reference = normalize_int(config.get("recent_average_drift_min_averages_for_reference")) or 3
    timeout_seconds = normalize_float(config.get("recent_average_drift_analysis_timeout_seconds")) or 240.0

    try:
        payloads = analyze_savedexperiment_average_drift_mat_files(
            [data_path],
            timeout_seconds=timeout_seconds,
            drop_threshold=float(drop_threshold),
            slice_index=int(slice_index),
            min_averages_for_reference=int(min_reference),
        )
    except Exception as exc:
        return {
            "ok": False,
            "source": "analyze_savedexperiment_average_drift.m",
            "data_path": data_path,
            "reason": "drift_analysis_failed",
            "entries": [],
            "error_code": "AVERAGE_DRIFT_ANALYSIS_FAILED",
            "error_message": str(exc),
        }
    if not payloads:
        return {
            "ok": False,
            "source": "analyze_savedexperiment_average_drift.m",
            "data_path": data_path,
            "reason": "drift_analysis_empty",
            "entries": [],
        }
    payload = payloads[0] if isinstance(payloads[0], dict) else {}
    payload.setdefault("source", "analyze_savedexperiment_average_drift.m")
    payload.setdefault("data_path", data_path)
    return payload


def evaluate_recent_average_drift(drift_analysis: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    enabled = bool(config.get("recent_average_drift_decision_enabled", False))
    required_count = max(1, normalize_int(config.get("recent_average_drift_required_count")) or 3)
    threshold = normalize_float(drift_analysis.get("drop_threshold"))
    if threshold is None:
        threshold = normalize_float(config.get("recent_average_drift_threshold"))
    if threshold is None:
        threshold = 0.15
    base = {
        "enabled": enabled,
        "decision_required": False,
        "reason": "",
        "source": "analyze_savedexperiment_average_drift.m",
        "data_path": normalize_path_for_agent(drift_analysis.get("data_path", "")),
        "analysis_ok": bool(drift_analysis.get("ok", False)),
        "basis": "analyze_savedexperiment_average_drift.common_mode_raw_brightness_flagged",
        "threshold": float(threshold),
        "required_count": int(required_count),
        "window_average_indices": [],
        "latest_average_index": None,
        "worst_score": None,
        "reference_method": "",
        "scan_order_source": "",
        "scan_order_mode": "",
        "data_order_for_score": "",
        "scan_order_used_count": 0,
        "scan_order_warnings": [],
        "entries": [],
        "decision_key": "",
        "recommended_agent_decision": "",
    }
    if not enabled:
        base["reason"] = "advisory_only"
        return base
    if not isinstance(drift_analysis, dict) or not bool(drift_analysis.get("ok", False)):
        base["reason"] = str(drift_analysis.get("reason", "") or "drift_analysis_unavailable")
        if drift_analysis.get("error_code") or drift_analysis.get("error_message"):
            base["error_code"] = str(drift_analysis.get("error_code", "") or "")
            base["error_message"] = str(drift_analysis.get("error_message", "") or "")
        return base

    raw_entries = drift_analysis.get("entries", [])
    entries = [entry for entry in raw_entries if isinstance(entry, dict)] if isinstance(raw_entries, list) else []
    if len(entries) < required_count:
        base["reason"] = "too_few_recent_entries"
        return base

    window = entries[-required_count:]
    scored_entries: list[dict[str, Any]] = []
    for entry in window:
        score = normalize_float(entry.get("drift_score"))
        scored_entries.append(
            {
                "average_index": normalize_int(entry.get("average_index")),
                "drift_score": score,
                "flagged": bool(entry.get("flagged", False)),
                "scan_order_used": bool(entry.get("scan_order_used", False)),
                "common_mode_end_minus_start_fraction": normalize_float(entry.get("common_mode_end_minus_start_fraction")),
                "common_mode_edge_end_minus_start_fraction": normalize_float(entry.get("common_mode_edge_end_minus_start_fraction")),
                "worst_drop_score": normalize_float(entry.get("worst_drop_score")),
                "worst_trace_index": normalize_int(entry.get("worst_trace_index")),
                "worst_trace_end_minus_start_fraction": normalize_float(entry.get("worst_trace_end_minus_start_fraction")),
                "worst_residual_end_minus_start_fraction": normalize_float(entry.get("worst_residual_end_minus_start_fraction")),
                "worst_edge_end_minus_start_fraction": normalize_float(entry.get("worst_edge_end_minus_start_fraction")),
            }
        )

    flagged_count = sum(1 for entry in scored_entries if bool(entry.get("flagged", False)))
    indices = [entry.get("average_index") for entry in scored_entries]
    latest_index = indices[-1] if indices else None
    worst_score = max((float(entry.get("drift_score") or 0.0) for entry in scored_entries if entry.get("drift_score") is not None), default=0.0)
    decision_required = flagged_count >= required_count
    index_text = ",".join(str(index) for index in indices if index is not None)
    decision_key = (
        f"recent_average_drift:{index_text or 'unknown'}:"
        f"{float(threshold):.6g}:matlab_common_mode_raw_brightness"
    )
    base.update(
        {
            "decision_required": bool(decision_required),
            "reason": "recent_average_drift_window_flagged" if decision_required else "below_threshold",
            "window_average_indices": indices,
            "latest_average_index": latest_index,
            "worst_score": float(worst_score),
            "reference_method": str(drift_analysis.get("reference_method", "") or ""),
            "trace_aggregation_method": str(drift_analysis.get("trace_aggregation_method", "") or ""),
            "drift_score_method": str(drift_analysis.get("drift_score_method", "") or ""),
            "scan_order_source": str(drift_analysis.get("scan_order_source", "") or ""),
            "scan_order_mode": str(drift_analysis.get("scan_order_mode", "") or ""),
            "data_order_for_score": str(drift_analysis.get("data_order_for_score", "") or ""),
            "scan_order_used_count": normalize_int(drift_analysis.get("scan_order_used_count")) or 0,
            "scan_order_warnings": drift_analysis.get("scan_order_warnings", [])
            if isinstance(drift_analysis.get("scan_order_warnings", []), list)
            else [],
            "entries": scored_entries,
            "decision_key": decision_key,
            "recommended_agent_decision": "continue_or_stop" if decision_required else "",
            "num_averages": normalize_int(drift_analysis.get("num_averages")),
            "num_traces": normalize_int(drift_analysis.get("num_traces")),
            "num_points": normalize_int(drift_analysis.get("num_points")),
        }
    )
    return base


def evaluate_anomaly(
    probe: dict[str, Any],
    status: dict[str, Any],
    control: dict[str, Any],
    saved_summary: dict[str, Any],
    matlab_log: dict[str, Any],
    config: dict[str, Any],
    session: dict[str, Any],
    now_monotonic: float,
) -> dict[str, Any]:
    if str(probe.get("state", "")).lower() != "running":
        return {}
    if str(status.get("state", "")).lower() != "running":
        return {}
    if bool(control.get("stop_requested", False)):
        return {}

    if isinstance(matlab_log, dict) and bool(matlab_log.get("fatal_detected", False)):
        return build_anomaly(
            "MATLAB_COMMAND_LOG_ERROR",
            f"MATLAB command-window log contains a fatal-looking error: {matlab_log.get('fatal_line', '')}",
            matlab_command_log_path=str(matlab_log.get("path", "") or ""),
            matlab_command_log_latest_line=str(matlab_log.get("latest_line", "") or ""),
            matlab_command_log_fatal_pattern=str(matlab_log.get("fatal_pattern", "") or ""),
        )

    phase = str(status.get("phase", "") or "")
    thresholds = runtime_watch_thresholds(status, config)
    current_phase_group = str(thresholds.get("phase_group", "pre_run") or "pre_run")
    monitor = status.get("monitor", {}) if isinstance(status.get("monitor"), dict) else {}
    runtime = status.get("runtime", {}) if isinstance(status.get("runtime"), dict) else {}
    saved_average_count = savedexperiment_average_count_from_raw_export(saved_summary)
    runtime_average_index = normalize_int(runtime.get("average_index")) or 0

    status_path = Path(str(probe.get("status_path", "")))
    status_age_seconds = latest_status_activity_age_seconds(status, status_path)
    if status_age_seconds is not None and status_age_seconds > float(thresholds.get("max_stale_seconds", 0.0) or 0.0):
        if current_phase_group == "finalizing":
            return {}
        if matlab_log_recent(matlab_log, config, thresholds):
            return {}
        stale_error_code = {
            "pre_run": "RUNTIME_STATUS_STALE_PRE_RUN",
            "in_run": "RUNTIME_STATUS_STALE_IN_RUN",
            "finalizing": "RUNTIME_STATUS_STALE_FINALIZING",
        }.get(current_phase_group, "RUNTIME_STATUS_STALE")
        return build_anomaly(
            stale_error_code,
            f"status.json has not updated for {status_age_seconds:.0f}s (threshold {float(thresholds.get('max_stale_seconds', 0.0)):.0f}s, phase={current_phase_group}).",
            retry_recommended=(current_phase_group == "pre_run"),
            phase=str(phase or ""),
            phase_group=current_phase_group,
            stale_age_seconds=float(status_age_seconds),
            warn_after_seconds=float(thresholds.get("warn_after_seconds", 0.0) or 0.0),
            max_stale_seconds=float(thresholds.get("max_stale_seconds", 0.0) or 0.0),
            basis_seconds=thresholds.get("basis_seconds"),
        )

    if current_phase_group == "in_run":
        expected = normalize_expected_runtime_summary(status.get("expected_runtime"))
        elapsed_seconds = normalize_float(status.get("elapsed_seconds")) or 0.0
        total_seconds = normalize_float(expected.get("total_seconds"))
        if total_seconds and total_seconds > 0:
            allowed = total_seconds * (normalize_float(config.get("expected_runtime_multiplier")) or 2.0) + (
                normalize_float(config.get("expected_runtime_grace_seconds")) or 900.0
            )
            if elapsed_seconds > allowed:
                overrun_action = str(config.get("expected_runtime_overrun_action", "advisory") or "advisory").strip().lower()
                if overrun_action in {"stop", "anomaly", "auto_stop", "auto-stop"}:
                    return build_anomaly(
                        "EXPECTED_RUNTIME_OVERRUN",
                        f"Run exceeded the expected runtime envelope ({elapsed_seconds:.0f}s > {allowed:.0f}s).",
                    )

        progress_reference = session.get("last_progress_at")
        if progress_reference is None:
            progress_reference = session.get("first_active_at")
        per_average_seconds = normalize_float(expected.get("per_average_seconds"))
        if progress_reference is not None:
            allowed_stall = max(
                normalize_float(config.get("average_stall_floor_seconds")) or 1800.0,
                (per_average_seconds or 0.0) * (normalize_float(config.get("average_stall_multiplier")) or 8.0),
            )
            stall_seconds = now_monotonic - float(progress_reference)
            if stall_seconds > allowed_stall:
                if matlab_log_recent(matlab_log, config, thresholds):
                    return {}
                average_index = normalize_int(runtime.get("average_index"))
                return build_anomaly(
                    "AVERAGE_PROGRESS_STALLED",
                    f"Average progress stalled for {stall_seconds:.0f}s near average {average_index or 0}.",
                )

    latest_entry = savedexperiment_latest_average_entry_from_raw_export(saved_summary)
    if latest_entry is not None:
        if nested_contains_nonfinite(latest_entry):
            return build_anomaly(
                "AVERAGE_DATA_CONTAINS_NAN",
                "The latest savedexperiment average contains NaN or Inf values in raw readouts.",
            )
        if not average_entry_has_raw_points(latest_entry):
            return build_anomaly(
                "AVERAGE_DATA_EMPTY",
                "The latest savedexperiment average did not contain raw readout points.",
            )

    return {}


def build_advisory(code: str, message: str, *, agent_review_recommended: bool = True, **details: Any) -> dict[str, Any]:
    payload = {
        "detected": True,
        "code": str(code or ""),
        "message": str(message or ""),
        "detected_at": now_iso(),
        "agent_review_recommended": bool(agent_review_recommended),
    }
    for key, value in details.items():
        payload[key] = copy.deepcopy(value)
    return payload


def empty_advisory() -> dict[str, Any]:
    return {
        "detected": False,
        "code": "",
        "message": "",
        "detected_at": "",
        "agent_review_recommended": False,
    }


def evaluate_advisory(
    probe: dict[str, Any],
    status: dict[str, Any],
    saved_summary: dict[str, Any],
    matlab_log: dict[str, Any],
    config: dict[str, Any],
    session: dict[str, Any],
    now_monotonic: float,
) -> dict[str, Any]:
    if str(probe.get("state", "")).lower() != "running":
        return empty_advisory()
    if str(status.get("state", "")).lower() != "running":
        return empty_advisory()

    thresholds = runtime_watch_thresholds(status, config)
    current_phase_group = str(thresholds.get("phase_group", "pre_run") or "pre_run")
    status_path = Path(str(probe.get("status_path", "")))
    status_age_seconds = latest_status_activity_age_seconds(status, status_path)
    if (
        status_age_seconds is not None
        and status_age_seconds > float(thresholds.get("max_stale_seconds", 0.0) or 0.0)
        and current_phase_group != "finalizing"
        and matlab_log_recent(matlab_log, config, thresholds)
    ):
        return build_advisory(
            "RUNTIME_STATUS_STALE_LOG_ACTIVE",
            (
                f"status.json is stale for {status_age_seconds:.0f}s, but the MATLAB "
                "command-window log is still updating; suppressing stale-status auto-stop."
            ),
            phase_group=current_phase_group,
            stale_age_seconds=float(status_age_seconds),
            matlab_command_log_path=str(matlab_log.get("path", "") or ""),
            matlab_command_log_age_seconds=normalize_float(matlab_log.get("mtime_age_seconds")),
            matlab_command_log_latest_line=str(matlab_log.get("latest_line", "") or ""),
        )

    if current_phase_group == "in_run":
        expected = normalize_expected_runtime_summary(status.get("expected_runtime"))
        elapsed_seconds = normalize_float(status.get("elapsed_seconds")) or 0.0
        total_seconds = normalize_float(expected.get("total_seconds"))
        if total_seconds and total_seconds > 0:
            allowed = total_seconds * (normalize_float(config.get("expected_runtime_multiplier")) or 2.0) + (
                normalize_float(config.get("expected_runtime_grace_seconds")) or 900.0
            )
            overrun_action = str(config.get("expected_runtime_overrun_action", "advisory") or "advisory").strip().lower()
            if elapsed_seconds > allowed and overrun_action not in {"stop", "anomaly", "auto_stop", "auto-stop"}:
                return build_advisory(
                    "EXPECTED_RUNTIME_OVERRUN",
                    (
                        f"Run exceeded the expected runtime envelope ({elapsed_seconds:.0f}s > {allowed:.0f}s); "
                        "recording advisory instead of auto-stopping."
                    ),
                    elapsed_seconds=float(elapsed_seconds),
                    allowed_seconds=float(allowed),
                    expected_total_seconds=float(total_seconds),
                    action="advisory",
                )

        progress_reference = session.get("last_progress_at")
        if progress_reference is None:
            progress_reference = session.get("first_active_at")
        per_average_seconds = normalize_float(expected.get("per_average_seconds"))
        if progress_reference is not None:
            allowed_stall = max(
                normalize_float(config.get("average_stall_floor_seconds")) or 1800.0,
                (per_average_seconds or 0.0) * (normalize_float(config.get("average_stall_multiplier")) or 8.0),
            )
            stall_seconds = now_monotonic - float(progress_reference)
            if stall_seconds > allowed_stall and matlab_log_recent(matlab_log, config, thresholds):
                runtime = status.get("runtime", {}) if isinstance(status.get("runtime"), dict) else {}
                return build_advisory(
                    "AVERAGE_PROGRESS_STALLED_LOG_ACTIVE",
                    (
                        f"Average progress is stale for {stall_seconds:.0f}s, but the MATLAB "
                        "command-window log is still updating; suppressing progress-stall auto-stop."
                    ),
                    average_index=normalize_int(runtime.get("average_index")),
                    stall_seconds=float(stall_seconds),
                    allowed_stall_seconds=float(allowed_stall),
                    matlab_command_log_path=str(matlab_log.get("path", "") or ""),
                    matlab_command_log_age_seconds=normalize_float(matlab_log.get("mtime_age_seconds")),
                    matlab_command_log_latest_line=str(matlab_log.get("latest_line", "") or ""),
                )

    _ = saved_summary
    return empty_advisory()


def request_stop_if_needed(
    probe: dict[str, Any],
    status: dict[str, Any],
    control: dict[str, Any],
    anomaly: dict[str, Any],
    config: dict[str, Any],
    session: dict[str, Any],
) -> dict[str, Any]:
    stop_request = copy.deepcopy(session.get("stop_request", {}))
    if not anomaly or not bool(anomaly.get("detected", False)):
        return stop_request

    requested_by = str(config.get("requested_by", DEFAULT_REQUESTED_BY) or DEFAULT_REQUESTED_BY)
    reason = str(anomaly.get("message", "") or anomaly.get("error_code", "") or "runtime watch requested stop")
    anomaly_phase_group = str(anomaly.get("phase_group", "") or "")

    if bool(anomaly.get("suppress_stop_request", False)):
        stop_request.update(
            {
                "requested": False,
                "requested_at": "",
                "requested_by": requested_by,
                "reason": reason,
                "request_written": False,
            }
        )
        return stop_request

    if anomaly_phase_group == "in_run" and bool(config.get("disable_auto_stop_during_run", False)):
        stop_request.update(
            {
                "requested": False,
                "requested_at": "",
                "requested_by": requested_by,
                "reason": reason,
                "request_written": False,
            }
        )
        return stop_request

    if bool(control.get("stop_requested", False)):
        stop_request.update(
            {
                "requested": True,
                "requested_at": str(control.get("requested_at", "") or ""),
                "requested_by": str(control.get("requested_by", "") or requested_by),
                "reason": str(control.get("stop_reason", "") or reason),
                "request_written": False,
            }
        )
        anomaly["requested_stop"] = True
        return stop_request

    if not bool(status.get("stop_capable", False)):
        stop_request.update(
            {
                "requested": False,
                "requested_at": "",
                "requested_by": requested_by,
                "reason": reason,
                "request_written": False,
            }
        )
        return stop_request

    control_path = Path(str(probe.get("control_path", "")))
    payload = {
        "version": int(control.get("version", 1) or 1),
        "kind": str(control.get("kind", "") or "nv_bridge_run_control"),
        "job_id": str(control.get("job_id", "") or status.get("job_id", "") or session.get("job_id", "")),
        "mode": str(control.get("mode", "") or status.get("mode", "") or "execute"),
        "stop_requested": True,
        "stop_reason": reason,
        "requested_by": requested_by,
        "requested_at": now_iso(),
        "updated_at": now_iso(),
        "stop_observed_at": str(control.get("stop_observed_at", "") or ""),
        "stop_applied": bool(control.get("stop_applied", False)),
        "stop_applied_at": str(control.get("stop_applied_at", "") or ""),
        "stop_apply_error": str(control.get("stop_apply_error", "") or ""),
    }
    write_json_atomic(control_path, payload)
    stop_request.update(
        {
            "requested": True,
            "requested_at": str(payload.get("requested_at", "") or ""),
            "requested_by": requested_by,
            "reason": reason,
            "request_written": True,
        }
    )
    anomaly["requested_stop"] = True
    anomaly["request_written"] = True
    return stop_request


def update_stop_confirmation(
    session: dict[str, Any],
    probe: dict[str, Any],
    control: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    confirmation = copy.deepcopy(session.get("stop_confirmation", {}))
    requested_at = str((session.get("stop_request", {}) or {}).get("requested_at", "") or "")
    requested_age = seconds_since_datetime(requested_at)

    confirmation["wait_seconds"] = requested_age or 0.0
    confirmation["stop_applied"] = bool(control.get("stop_applied", False))
    confirmation["stop_apply_error"] = str(control.get("stop_apply_error", "") or "")
    confirmation["final_state"] = str(probe.get("state", "") or "")
    confirmation["overdue"] = bool(
        requested_at
        and not confirmation.get("confirmed", False)
        and (requested_age or 0.0) > (normalize_float(config.get("stop_confirm_seconds")) or 180.0)
    )

    if confirmation.get("confirmed", False):
        return confirmation

    if str(probe.get("state", "")).lower() in FINAL_QUEUE_STATES:
        confirmation["confirmed"] = True
        confirmation["confirmed_at"] = now_iso()
        return confirmation

    if bool(control.get("stop_applied", False)):
        confirmation["confirmed"] = True
        confirmation["confirmed_at"] = str(control.get("stop_applied_at", "") or now_iso())
        return confirmation

    return confirmation


def runtime_watch_step(
    queue_root: Path,
    job_id: str,
    *,
    probe: dict[str, Any] | None = None,
    job: dict[str, Any] | None = None,
    config: dict[str, Any] | None = None,
    session: dict[str, Any] | None = None,
) -> dict[str, Any]:
    effective_config = default_watch_config(job, config)
    current = probe or probe_job(queue_root, job_id)
    watch_session = copy.deepcopy(session) if isinstance(session, dict) else initial_watch_session(job_id, effective_config)
    if not bool(effective_config.get("enabled", True)):
        watch_session["enabled"] = False
        return watch_session

    status = read_json_dict_if_exists(Path(str(current.get("status_path", ""))))
    control = read_json_dict_if_exists(Path(str(current.get("control_path", ""))))
    prior_anomaly = watch_session.get("anomaly", {}) if isinstance(watch_session.get("anomaly"), dict) else {}
    if bool(prior_anomaly.get("detected", False)) and str(prior_anomaly.get("error_code", "") or "") == "RUNTIME_STATUS_STALE_PRE_RUN":
        thresholds = runtime_watch_thresholds(status, effective_config)
        status_age_seconds = latest_status_activity_age_seconds(status, Path(str(current.get("status_path", ""))))
        if (
            str(thresholds.get("phase_group", "") or "") == "pre_run"
            and status_age_seconds is not None
            and status_age_seconds <= float(thresholds.get("max_stale_seconds", 0.0) or 0.0)
        ):
            watch_session["anomaly"] = {
                "detected": False,
                "error_code": "",
                "message": "",
                "detected_at": "",
                "retry_recommended": False,
                "requested_stop": False,
                "request_written": False,
            }
            watch_session["stop_request"] = {
                "requested": False,
                "requested_at": "",
                "requested_by": "",
                "reason": "",
                "request_written": False,
            }
    saved_summary = maybe_collect_savedexperiment_raw_export(status, job, effective_config, watch_session)
    watch_session["savedexperiment_raw_export"] = saved_summary
    matlab_log = analyze_matlab_command_log(current, status, effective_config)
    watch_session["matlab_command_log"] = matlab_log

    now_monotonic = time.monotonic()
    update_progress_tracking(watch_session, status, saved_summary, now_monotonic)
    drift_analysis = maybe_collect_savedexperiment_average_drift(watch_session, effective_config)
    watch_session["drift_analysis"] = drift_analysis
    watch_session["drift_decision"] = evaluate_recent_average_drift(drift_analysis, effective_config)
    watch_session["advisory"] = evaluate_advisory(
        current,
        status,
        saved_summary,
        matlab_log,
        effective_config,
        watch_session,
        now_monotonic,
    )

    anomaly = watch_session.get("anomaly", {})
    if not bool(anomaly.get("detected", False)):
        anomaly = evaluate_anomaly(
            current,
            status,
            control,
            saved_summary,
            matlab_log,
            effective_config,
            watch_session,
            now_monotonic,
        )
        if anomaly:
            watch_session["anomaly"] = anomaly

    if bool(watch_session.get("anomaly", {}).get("detected", False)):
        watch_session["stop_request"] = request_stop_if_needed(
            current,
            status,
            control,
            watch_session["anomaly"],
            effective_config,
            watch_session,
        )
        control = read_json_dict_if_exists(Path(str(current.get("control_path", ""))))

    if bool(watch_session.get("stop_request", {}).get("requested", False)):
        watch_session["stop_confirmation"] = update_stop_confirmation(watch_session, current, control, effective_config)

    observations = list(watch_session.get("recent_observations", []))
    observations.append(observation_record(current, status, control, saved_summary, matlab_log))
    limit = max(1, int(effective_config.get("observation_limit", RECENT_OBSERVATION_LIMIT) or RECENT_OBSERVATION_LIMIT))
    watch_session["recent_observations"] = observations[-limit:]
    return watch_session


def runtime_watch_summary(session: dict[str, Any]) -> dict[str, Any]:
    saved_summary = session.get("savedexperiment_raw_export", {}) if isinstance(session.get("savedexperiment_raw_export"), dict) else {}
    return {
        "enabled": bool(session.get("enabled", True)),
        "job_id": str(session.get("job_id", "") or ""),
        "savedexperiment_path": str(session.get("savedexperiment_path", "") or saved_summary.get("data_path", "") or ""),
        "savedexperiment_raw_export": saved_summary,
        "drift_analysis": copy.deepcopy(session.get("drift_analysis", {})),
        "drift_decision": copy.deepcopy(session.get("drift_decision", {})),
        "advisory": copy.deepcopy(session.get("advisory", {})),
        "matlab_command_log": copy.deepcopy(session.get("matlab_command_log", {})),
        "anomaly": copy.deepcopy(session.get("anomaly", {})),
        "stop_request": copy.deepcopy(session.get("stop_request", {})),
        "stop_confirmation": copy.deepcopy(session.get("stop_confirmation", {})),
        "recent_observations": copy.deepcopy(session.get("recent_observations", [])),
    }


def wait_for_result(
    queue_root: Path,
    job_id: str,
    timeout_seconds: float | None,
    poll_seconds: float,
    *,
    job: dict[str, Any] | None = None,
    config: dict[str, Any] | None = None,
) -> dict[str, Any]:
    started = time.monotonic()
    watch_session = initial_watch_session(job_id, default_watch_config(job, config))

    while True:
        current = probe_job(queue_root, job_id)
        state = str(current.get("state", "") or "")

        if state in {"running", "done", "failed"}:
            watch_session = runtime_watch_step(
                queue_root,
                job_id,
                probe=current,
                job=job,
                config=config,
                session=watch_session,
            )

        result_path = Path(str(current.get("result_path", "")))
        if state in FINAL_QUEUE_STATES and result_path.is_file():
            result = read_json(result_path)
            error_code = str(result.get("error_code", "") or "")
            error_message = str(result.get("error_message", "") or "")
            anomaly = watch_session.get("anomaly", {}) if isinstance(watch_session.get("anomaly"), dict) else {}
            hard_anomaly = bool(anomaly.get("detected", False)) and not bool(anomaly.get("suppress_stop_request", False))
            if not error_code and hard_anomaly:
                error_code = str(anomaly.get("error_code", "") or "")
            if not error_message and hard_anomaly:
                error_message = str(anomaly.get("message", "") or "")
            return {
                "timed_out": False,
                "final_state": state,
                "job_dir": str(current.get("job_dir", "")),
                "result_path": str(result_path),
                "result": result,
                "outcome_summary": summarize_result(result),
                "elapsed_seconds": time.monotonic() - started,
                "error_code": error_code,
                "error_message": error_message,
                "runtime_watch": runtime_watch_summary(watch_session),
            }

        elapsed = time.monotonic() - started
        if timeout_seconds is not None and timeout_seconds > 0 and elapsed >= timeout_seconds:
            if state in {"queued", "running"}:
                time.sleep(poll_seconds)
                continue
            anomaly = watch_session.get("anomaly", {}) if isinstance(watch_session.get("anomaly"), dict) else {}
            return {
                "timed_out": True,
                "final_state": "timeout",
                "job_dir": str(current.get("job_dir", "")) if current.get("job_dir") else "",
                "result_path": str(result_path) if result_path else "",
                "result": {},
                "outcome_summary": summarize_result({}),
                "elapsed_seconds": elapsed,
                "error_code": str(anomaly.get("error_code", "") or "TIMEOUT"),
                "error_message": str(anomaly.get("message", "") or "Queue helper timed out while waiting for the result."),
                "runtime_watch": runtime_watch_summary(watch_session),
            }

        time.sleep(poll_seconds)
