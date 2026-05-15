#!/usr/bin/env python3
import argparse
import copy
import fcntl
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path

WORKSPACE_ROOT = Path("<OPENCLAW_WORKSPACE>")
DEFAULT_QUEUE_ROOT = Path("<NV_BRIDGE_ROOT>")
DEFAULT_SIMULATION_QUEUE_ROOT = Path("<MATLAB_23C_ROOT>/simulation_queue")
DEFAULT_CATALOG_PATH = WORKSPACE_ROOT / "nv_sequences.json"
DEFAULT_MANIFEST_ROOT = Path("<MATLAB_23C_ROOT>/claw/sequence_manifests")
DEFAULT_SIMULATION_MANIFEST_ROOT = WORKSPACE_ROOT / "simulation_manifests"
DEFAULT_SIMULATION_MANIFEST_ID = "hirose_nv14n_rf_rabi_v1"
DEFAULT_NV_SEED_REGISTRY_PATH = Path("<NV_BRIDGE_ROOT>/status/nv_position_registry.json")
DEFAULT_OPENCLAW_CONFIG_PATH = Path("<OPENCLAW_CONFIG>")
DEFAULT_OPENCLAW_GATEWAY_URL = "http://127.0.0.1:18789"
DEFAULT_DIRECT_RECOVERY_ROOT = WORKSPACE_ROOT / ".openclaw" / "direct_recovery"
DEFAULT_DIRECT_RECOVERY_HOOK_PATH = "/hooks/nv-direct-recovery"
DEFAULT_DIRECT_RECOVERY_PLAN_TIMEOUT_SECONDS = 600.0
DEFAULT_MEASUREMENT_PLAN_TIMEOUT_SECONDS = 45.0
DEFAULT_ACTIVE_RECOVERY_CHAIN_LOCK_PATH = DEFAULT_DIRECT_RECOVERY_ROOT / "active_chain.lock"
DEFAULT_ACTIVE_CHAIN_WAIT_SECONDS = -1.0
DEFAULT_JOB_ADVISORY_ROOT = DEFAULT_QUEUE_ROOT / "status" / "openclaw_job_advisory"
DEFAULT_JOB_ADVISORY_TIMEOUT_SECONDS = 300.0
DEFAULT_SINGLE_SUBMIT_ROOT = WORKSPACE_ROOT / ".openclaw" / "single_submit"
DEFAULT_DIRECT_SEQUENCE_AUTHORING_ROOT = WORKSPACE_ROOT / ".openclaw" / "sequence_authoring" / "direct_submit"
INTERNAL_MEASUREMENT_PLAN_ENV = "OPENCLAW_INTERNAL_MEASUREMENT_PLAN_SUBMIT"
SUBMISSION_PATH_ENV = "OPENCLAW_SUBMISSION_PATH"
CRON_MANAGED_INLINE_WATCH_SUBMISSION_PATHS = {
    "legacy_direct_external",
    "legacy_direct_internal",
    "single_item_measurement_plan",
}
TERMINAL_BATCH_STATUSES = {"completed", "failed", "stopped"}
SINGLE_ITEM_RUNNER_TERMINAL_EXIT_GRACE_SECONDS = 10.0
SINGLE_ITEM_RUNNER_TIMEOUT_GRACE_SECONDS = 60.0
WINDOWS_DRIVE_PATH_RE = re.compile(r"^(?P<drive>[A-Za-z]):[\\/](?P<rest>.*)$")

SCRIPT_ROOT = Path(__file__).resolve().parent
if str(SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPT_ROOT))

try:
    from nv_batch_run import (
        deep_merge_dicts,
        latest_failure_artifacts,
        normalize_agent_recovery_plan,
        now_iso,
        post_hook,
        resolve_hook_token,
        summarize_job_for_recovery,
        summarize_result_for_recovery,
        tail_text_file,
        wait_for_recovery_plan,
        write_json as write_pretty_json,
    )
except Exception:
    deep_merge_dicts = None
    latest_failure_artifacts = None
    normalize_agent_recovery_plan = None
    now_iso = None
    post_hook = None
    resolve_hook_token = None
    summarize_job_for_recovery = None
    summarize_result_for_recovery = None
    tail_text_file = None
    wait_for_recovery_plan = None
    write_pretty_json = None

try:
    from nv_bridge_runtime_watch import default_watch_config as build_runtime_watch_defaults
    from nv_bridge_runtime_watch import wait_for_result as runtime_watch_wait_for_result
except Exception:
    build_runtime_watch_defaults = None
    runtime_watch_wait_for_result = None

try:
    from matlab_bridge_client import (
        process_next_simulation_job_via_matlab_wrapper,
        submit_simulation_job_via_matlab_wrapper,
        submit_spec_via_matlab_wrapper,
    )
except Exception:
    process_next_simulation_job_via_matlab_wrapper = None
    submit_simulation_job_via_matlab_wrapper = None
    submit_spec_via_matlab_wrapper = None

try:
    from project_schema import normalize_sequence_authoring_spec
except Exception:
    normalize_sequence_authoring_spec = None

try:
    from design_nv_sequence import materialize_sequence_spec as materialize_staging_sequence_spec
except Exception:
    materialize_staging_sequence_spec = None

try:
    from submit_spec_utils import build_batch_item_from_submit_spec
except Exception:
    build_batch_item_from_submit_spec = None


def slug(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"^_+|_+$", "", text)
    return text or "job"


def build_job_id(prefix: str, suffix: str | None) -> str:
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    job_id = f"{slug(prefix)}_{ts}"
    if suffix:
        job_id += f"_{slug(suffix)}"
    return job_id


def normalize_path(raw_value: str, default_path: Path) -> Path:
    text = (raw_value or "").strip()
    if not text:
        return default_path.resolve()

    drive_match = WINDOWS_DRIVE_PATH_RE.match(text)
    if drive_match:
        drive = drive_match.group("drive").lower()
        rest = drive_match.group("rest").replace("\\", "/").lstrip("/")
        return (Path("/mnt") / drive / rest).resolve()

    if text.startswith("\\\\"):
        raise ValueError(
            "UNC paths are not supported from WSL. Use /mnt/<drive>/... "
            "or a Windows drive path like <NV_BRIDGE_ROOT>."
        )

    path = Path(os.path.expanduser(text))
    if path.is_absolute():
        return path.resolve()
    return (Path.cwd() / path).resolve()


def ensure_dirs(queue_root: Path) -> None:
    for name in [
        "queued",
        "running",
        "done",
        "failed",
        "logs",
        "status",
        "locks",
        "archive",
        "staging",
    ]:
        (queue_root / name).mkdir(parents=True, exist_ok=True)


def windows_path_for_matlab(path: Path) -> str:
    resolved = path.resolve()
    parts = resolved.parts
    if len(parts) >= 3 and parts[0] == "/" and parts[1] == "mnt" and len(parts[2]) == 1:
        drive = parts[2].upper()
        rest = list(parts[3:])
        if rest:
            return drive + ":\\" + "\\".join(rest)
        return drive + ":\\"

    distro = os.environ.get("WSL_DISTRO_NAME", "<WSL_DISTRO>")
    unc_tail = str(resolved).replace("/", "\\")
    if not unc_tail.startswith("\\"):
        unc_tail = "\\" + unc_tail
    return f"<WSL_UNC_PREFIX>{unc_tail}"


def matlab_literal(text: str) -> str:
    return str(text or "").replace("'", "''")


def candidate_windows_shell_paths() -> list[Path]:
    candidates: list[Path] = []

    for executable_name in ("powershell.exe", "pwsh.exe"):
        resolved = shutil.which(executable_name)
        if resolved:
            candidates.append(Path(resolved))

    windir = str(os.environ.get("WINDIR", "") or "").strip()
    if windir:
        candidates.extend(
            [
                Path(windir) / "System32" / "WindowsPowerShell" / "v1.0" / "powershell.exe",
                Path(windir) / "System32" / "pwsh.exe",
            ]
        )

    candidates.extend(
        [
            Path("/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"),
            Path("/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/powershell.exe"),
            Path("/mnt/c/Program Files/PowerShell/7/pwsh.exe"),
            Path("/mnt/c/Program Files/PowerShell/7-preview/pwsh.exe"),
        ]
    )

    deduped: list[Path] = []
    seen: set[str] = set()
    for candidate in candidates:
        key = str(candidate)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(candidate)
    return deduped


def resolve_windows_shell_path() -> Path:
    for candidate in candidate_windows_shell_paths():
        if candidate.is_file():
            return candidate
    searched = ", ".join(str(path) for path in candidate_windows_shell_paths())
    raise FileNotFoundError(
        "Could not locate a Windows PowerShell executable from WSL. "
        f"Searched: {searched}"
    )


def advisory_failure_payload(error_code: str, message: str) -> dict:
    return {
        "ok": False,
        "error_code": str(error_code or ""),
        "error_message": str(message or ""),
        "job_id": "",
        "sample_id": "",
        "sequence_name": "",
        "job": {},
        "validation": {
            "ok": False,
            "error_code": str(error_code or ""),
            "error_message": str(message or ""),
        },
        "acquisition": {},
        "estimated_runtime": {},
        "recent_nv_drift": {},
        "guidance": {},
        "warnings": [],
        "notes": [str(message or "")] if message else [],
        "blockers": [str(error_code or "JOB_ADVISORY_FAILED")],
    }


def build_runtime_estimate_context(advisory: dict) -> dict:
    if not isinstance(advisory, dict) or not advisory:
        return {}
    estimated_runtime = advisory.get("estimated_runtime", {})
    if not isinstance(estimated_runtime, dict) or not estimated_runtime:
        return {}
    estimator_mode = str(estimated_runtime.get("estimator_mode", "") or "").strip().lower()
    context = {
        "source": "matlab_pre_enqueue_advisory",
        "model_version": "",
        "estimator_mode": estimator_mode,
        "siglent_waveform_length_aware": False,
        "notes": [],
    }
    if estimator_mode == "siglent":
        context["model_version"] = "2026-04-04_siglent_tracking_and_waveform_balanced"
        context["siglent_waveform_length_aware"] = True
        context["notes"] = [
            "23-C MATLAB now estimates Siglent runtime with a fixed per-average tracking/housekeeping term, a per-scan-point programming term, and a weaker average-waveform-length term.",
            "Use advisory.estimated_runtime from MATLAB as the runtime source of truth for Siglent jobs; do not assume either the legacy fixed 12.5 s/scan-point model or the earlier overly aggressive waveform-length scaling.",
        ]
    if not context["model_version"]:
        return {}
    return context


def annotate_runtime_estimate_context(advisory: dict) -> dict:
    if not isinstance(advisory, dict) or not advisory:
        return {}
    annotated = copy.deepcopy(advisory)
    context = build_runtime_estimate_context(annotated)
    if context:
        annotated["runtime_estimate_context"] = context
    return annotated


def build_error_response(error_code: str, message: str, args: argparse.Namespace | None = None, sequence_name: str = "") -> dict:
    mode = ""
    wait_for_result = None
    requested_by = ""
    if args is not None:
        mode = str(getattr(args, "mode", "") or "")
        wait_for_result = bool(getattr(args, "wait_for_result", False))
        requested_by = str(getattr(args, "requested_by", "") or "")
    response = {
        "ok": False,
        "error_code": str(error_code or ""),
        "error_message": str(message or ""),
    }
    if mode:
        response["mode"] = mode
    if sequence_name:
        response["sequence"] = sequence_name
    if wait_for_result is not None:
        response["wait_for_result"] = wait_for_result
    if requested_by:
        response["requested_by"] = requested_by
    return response


def invoke_matlab_wrapper_submit_spec(
    submit_spec: dict,
    args: argparse.Namespace,
    manifest_root: Path,
    queue_root: Path,
    *,
    include_job_advisory: bool,
    enqueue: bool,
) -> tuple[dict, dict]:
    if not callable(submit_spec_via_matlab_wrapper):
        return (
            build_error_response(
                "MATLAB_WRAPPER_UNAVAILABLE",
                "matlab_bridge_client.submit_spec_via_matlab_wrapper is unavailable.",
                args=args,
            ),
            {"available": False},
        )

    timeout_seconds = max(float(getattr(args, "job_advisory_timeout_seconds", DEFAULT_JOB_ADVISORY_TIMEOUT_SECONDS)), 90.0)
    submit_mode = str(submit_spec.get("mode", "") or getattr(args, "mode", "") or "").strip().lower()
    effective_include_job_advisory = bool(include_job_advisory) or (bool(enqueue) and submit_mode == "execute")
    response, runner_info = submit_spec_via_matlab_wrapper(
        submit_spec,
        manifest_root=manifest_root,
        queue_root=queue_root,
        include_job_advisory=effective_include_job_advisory,
        enqueue=enqueue,
        timeout_seconds=timeout_seconds,
        job_advisory_opts={},
    )
    return response, runner_info


def invoke_matlab_wrapper_submit_simulation_job(
    job: dict,
    args: argparse.Namespace,
    manifest_root: Path,
    simulation_queue_root: Path,
    *,
    enqueue: bool,
) -> tuple[dict, dict]:
    if not callable(submit_simulation_job_via_matlab_wrapper):
        return (
            build_error_response(
                "MATLAB_SIMULATION_WRAPPER_UNAVAILABLE",
                "matlab_bridge_client.submit_simulation_job_via_matlab_wrapper is unavailable.",
                args=args,
            ),
            {"available": False},
        )

    timeout_seconds = max(float(getattr(args, "job_advisory_timeout_seconds", DEFAULT_JOB_ADVISORY_TIMEOUT_SECONDS)), 90.0)
    response, runner_info = submit_simulation_job_via_matlab_wrapper(
        job,
        manifest_root=manifest_root,
        queue_root=simulation_queue_root,
        enqueue=enqueue,
        timeout_seconds=timeout_seconds,
    )
    return response, runner_info


def invoke_matlab_wrapper_process_next_simulation_job(
    args: argparse.Namespace,
    manifest_root: Path,
    simulation_queue_root: Path,
) -> tuple[dict, dict]:
    if not callable(process_next_simulation_job_via_matlab_wrapper):
        return (
            build_error_response(
                "MATLAB_SIMULATION_WORKER_WRAPPER_UNAVAILABLE",
                "matlab_bridge_client.process_next_simulation_job_via_matlab_wrapper is unavailable.",
                args=args,
            ),
            {"available": False},
        )

    timeout_seconds = max(float(getattr(args, "timeout_seconds", 900.0)), 90.0)
    response, runner_info = process_next_simulation_job_via_matlab_wrapper(
        manifest_root=manifest_root,
        queue_root=simulation_queue_root,
        timeout_seconds=timeout_seconds,
    )
    return response, runner_info


def internal_measurement_plan_submit_allowed() -> bool:
    return str(os.environ.get(INTERNAL_MEASUREMENT_PLAN_ENV, "") or "").strip() == "1"


def resolve_submission_path(args: argparse.Namespace) -> str:
    env_path = str(os.environ.get(SUBMISSION_PATH_ENV, "") or "").strip()
    if env_path:
        return env_path
    if bool(getattr(args, "skip_measurement_plan", False)):
        return "legacy_direct_internal"
    return "legacy_direct_external"


def build_job_advisory(job: dict, args: argparse.Namespace, manifest_root: Path) -> tuple[dict, dict]:
    advisory_root = normalize_path(getattr(args, "job_advisory_root", ""), DEFAULT_JOB_ADVISORY_ROOT)
    advisory_root.mkdir(parents=True, exist_ok=True)

    job_id = str(job.get("job_id", "") or "job").strip() or "job"
    request_dir = advisory_root / f"{slug(job_id)}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
    request_dir.mkdir(parents=True, exist_ok=False)

    job_json_path = request_dir / "job.json"
    output_json_path = request_dir / "advisory.json"
    runner_path = request_dir / "run_preview_advisory.m"
    write_json_atomic(job_json_path, job)

    c23_root = manifest_root
    if c23_root.name == "sequence_manifests":
        c23_root = c23_root.parent.parent
    elif c23_root.name == "claw":
        c23_root = c23_root.parent
    if not (c23_root / "claw").is_dir():
        c23_root = DEFAULT_MANIFEST_ROOT.parent.parent

    c23_root_windows = windows_path_for_matlab(c23_root)
    job_json_windows = windows_path_for_matlab(job_json_path)
    output_json_windows = windows_path_for_matlab(output_json_path)
    runner_windows = windows_path_for_matlab(runner_path)

    init_dir_windows = windows_path_for_matlab(c23_root / "Initialization" / "NV1")
    image_dir_windows = windows_path_for_matlab(c23_root / "SavedImages")
    exp_dir_windows = windows_path_for_matlab(c23_root / "savedexperiments" / "NV1")
    sequence_dir_windows = windows_path_for_matlab(c23_root / "SavedSequences" / "SavedSequences-AWG")

    runner_code = "\n".join(
        [
            f"c23Root = '{matlab_literal(c23_root_windows)}';",
            f"jobJsonPath = '{matlab_literal(job_json_windows)}';",
            f"outputPath = '{matlab_literal(output_json_windows)}';",
            f"initDir = '{matlab_literal(init_dir_windows)}';",
            f"imageDir = '{matlab_literal(image_dir_windows)}';",
            f"expDir = '{matlab_literal(exp_dir_windows)}';",
            f"sequenceDir = '{matlab_literal(sequence_dir_windows)}';",
            "if ~(ispref('nv') && ispref('nv', 'SavedInitializationDirectory'))",
            "    setpref('nv', 'SavedInitializationDirectory', initDir);",
            "end",
            "if ~(ispref('nv') && ispref('nv', 'SavedImageDirectory'))",
            "    setpref('nv', 'SavedImageDirectory', imageDir);",
            "end",
            "if ~(ispref('nv') && ispref('nv', 'SavedExpDirectory'))",
            "    setpref('nv', 'SavedExpDirectory', expDir);",
            "end",
            "if ~(ispref('nv') && ispref('nv', 'SavedSequenceDirectory'))",
            "    setpref('nv', 'SavedSequenceDirectory', sequenceDir);",
            "end",
            "addpath(c23Root);",
            "addpath(fullfile(c23Root, 'claw'));",
            "advisory = struct();",
            "try",
            "    advisory = claw_preview_job_advisory(jobJsonPath, struct());",
            "catch ME",
            "    advisory = struct();",
            "    advisory.ok = false;",
            "    advisory.error_code = char(ME.identifier);",
            "    advisory.error_message = char(ME.message);",
            "    advisory.job_id = '';",
            "    advisory.sample_id = '';",
            "    advisory.sequence_name = '';",
            "    advisory.job = struct();",
            "    advisory.validation = struct('ok', false, 'error_code', char(ME.identifier), 'error_message', char(ME.message));",
            "    advisory.acquisition = struct();",
            "    advisory.estimated_runtime = struct();",
            "    advisory.recent_nv_drift = struct();",
            "    advisory.guidance = struct();",
            "    advisory.warnings = {};",
            "    advisory.notes = {sprintf('MATLAB advisory runner failed: %s', char(ME.message))};",
            "    advisory.blockers = {char(ME.identifier)};",
            "end",
            "fid = fopen(outputPath, 'w');",
            "if fid < 0",
            "    error('NVBridge:PreviewAdvisoryWriteFailed', 'Failed to open advisory output path: %s', outputPath);",
            "end",
            "cleanupObj = onCleanup(@() fclose(fid)); %#ok<NASGU>",
            "fprintf(fid, '%s', jsonencode(advisory));",
        ]
    )
    runner_path.write_text(runner_code + "\n", encoding="utf-8")

    env = os.environ.copy()
    timeout_seconds = float(getattr(args, "job_advisory_timeout_seconds", DEFAULT_JOB_ADVISORY_TIMEOUT_SECONDS))
    runner_info = {
        "request_dir": str(request_dir),
        "job_json_path": str(job_json_path),
        "output_json_path": str(output_json_path),
        "runner_path": str(runner_path),
        "shell_path": "",
        "returncode": 0,
        "stdout": "",
        "stderr": "",
        "timed_out": False,
        "command": [],
    }

    try:
        shell_path = resolve_windows_shell_path()
        command = [
            str(shell_path),
            "-NoProfile",
            "-Command",
            f"matlab -batch \"run('{matlab_literal(runner_windows)}')\"",
        ]
        runner_info["shell_path"] = str(shell_path)
        runner_info["command"] = command
        completed = subprocess.run(command, capture_output=True, text=True, env=env, timeout=timeout_seconds)
        runner_info["returncode"] = int(completed.returncode)
        runner_info["stdout"] = completed.stdout
        runner_info["stderr"] = completed.stderr
    except subprocess.TimeoutExpired as exc:
        runner_info["timed_out"] = True
        runner_info["stdout"] = exc.stdout or ""
        runner_info["stderr"] = exc.stderr or ""
        return advisory_failure_payload("JOB_ADVISORY_TIMEOUT", f"Timed out while waiting for MATLAB advisory after {timeout_seconds:.1f} s."), runner_info
    except FileNotFoundError as exc:
        runner_info["stderr"] = str(exc)
        return advisory_failure_payload("JOB_ADVISORY_LAUNCH_FAILED", f"Failed to launch MATLAB advisory command: {exc}"), runner_info
    except Exception as exc:
        runner_info["stderr"] = str(exc)
        return advisory_failure_payload("JOB_ADVISORY_FAILED", f"Unexpected job-advisory failure: {exc}"), runner_info

    if not output_json_path.is_file():
        message = "MATLAB advisory did not produce an output JSON file."
        if runner_info["stderr"]:
            message = f"{message} STDERR: {runner_info['stderr'].strip()}"
        return advisory_failure_payload("JOB_ADVISORY_NO_OUTPUT", message), runner_info

    try:
        advisory = read_json(output_json_path)
    except Exception as exc:
        return advisory_failure_payload("JOB_ADVISORY_INVALID_JSON", f"Failed to parse advisory output JSON: {exc}"), runner_info

    if not isinstance(advisory, dict):
        return advisory_failure_payload("JOB_ADVISORY_INVALID_PAYLOAD", "MATLAB advisory returned a non-dictionary payload."), runner_info

    if runner_info["returncode"] != 0 and not advisory.get("ok", False):
        advisory.setdefault("error_code", "JOB_ADVISORY_MATLAB_RETURNED_ERROR")
        advisory.setdefault("error_message", runner_info["stderr"].strip() or "MATLAB returned a non-zero exit code while building the advisory.")
    return advisory, runner_info


def acquire_active_recovery_chain_lock(lock_path: Path, payload: dict, wait_seconds: float, poll_seconds: float) -> object:
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = open(lock_path, "a+", encoding="utf-8")
    started = time.monotonic()
    while True:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            break
        except BlockingIOError:
            if wait_seconds >= 0 and (time.monotonic() - started) >= wait_seconds:
                handle.seek(0)
                current = handle.read().strip()
                handle.close()
                owner_message = f" Active chain: {current}" if current else ""
                raise RuntimeError(
                    "Another direct execute recovery chain is still active and did not clear "
                    "before the active-chain wait timeout."
                    + owner_message
                )
            time.sleep(max(poll_seconds, 0.2))
            handle.seek(0)

    handle.seek(0)
    handle.truncate()
    json.dump(payload, handle, ensure_ascii=False)
    handle.write("\n")
    handle.flush()
    os.fsync(handle.fileno())
    return handle


def write_json_atomic(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, ensure_ascii=False)
            handle.write("\n")
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def read_json(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    if raw.startswith("\ufeff"):
        raw = raw[1:]
    return json.loads(raw)


def load_catalog(path: Path) -> dict:
    catalog = read_json(path)
    if not isinstance(catalog, dict) or not isinstance(catalog.get("sequences"), dict):
        raise ValueError(f"Invalid sequence catalog: {path}")
    return catalog


def load_nv_seed_registry(registry_path: Path) -> dict:
    if not registry_path.is_file():
        return {"path": registry_path, "entries": []}

    registry = read_json(registry_path)
    raw_entries = registry.get("entries", [])
    entries: list[dict] = []
    if isinstance(raw_entries, dict):
        entries = [raw_entries]
    elif isinstance(raw_entries, list):
        entries = [entry for entry in raw_entries if isinstance(entry, dict)]

    return {"path": registry_path, "entries": entries}


def lookup_seed_registry_entry(registry_info: dict, sample_id: str) -> dict:
    sample_key = (sample_id or "").strip().lower()
    if not sample_key:
        return {}

    entries = registry_info.get("entries", [])
    for entry in reversed(entries):
        if not isinstance(entry, dict):
            continue
        if str(entry.get("sample_id", "")).strip().lower() == sample_key:
            return entry
    return {}


def load_manifest(manifest_root: Path, manifest_id: str) -> dict:
    manifest_id = (manifest_id or "").strip()
    if not manifest_id:
        raise ValueError("sequence_manifest_id is required to load a manifest")

    file_name = manifest_id if manifest_id.endswith(".json") else f"{manifest_id}.json"
    candidates = [
        ("validated", manifest_root / "validated" / file_name),
        ("staging", manifest_root / "staging" / file_name),
    ]

    for scope, path in candidates:
        if path.is_file():
            manifest = read_json(path)
            if not isinstance(manifest, dict):
                raise ValueError(f"Invalid manifest JSON: {path}")
            return {
                "scope": scope,
                "path": path,
                "manifest": manifest,
            }

    raise ValueError(f"Sequence manifest not found: {manifest_id}")


def load_simulation_manifest(simulation_manifest_root: Path, manifest_id: str) -> dict:
    manifest_id = (manifest_id or "").strip()
    if not manifest_id:
        raise ValueError("simulation_manifest_id is required to load a simulation manifest")

    file_name = manifest_id if manifest_id.endswith(".json") else f"{manifest_id}.json"
    candidates = [
        ("validated", simulation_manifest_root / "validated" / file_name),
        ("staging", simulation_manifest_root / "staging" / file_name),
        ("root", simulation_manifest_root / file_name),
    ]

    for scope, path in candidates:
        if path.is_file():
            manifest = read_json(path)
            if not isinstance(manifest, dict):
                raise ValueError(f"Invalid simulation manifest JSON: {path}")
            return {
                "scope": scope,
                "path": path,
                "manifest": manifest,
            }

    raise ValueError(f"Simulation manifest not found: {manifest_id}")


def simulation_manifest_description(manifest_id: str, manifest: dict, scope: str) -> str:
    description = str(manifest.get("description", "") or "").strip()
    if description:
        return description
    status = str(manifest.get("status", scope)).strip().lower() or str(scope or "").strip().lower()
    prefix = "Validated" if status == "validated" else (status.capitalize() if status else "Simulation")
    return f"{prefix} simulation manifest for {manifest_id}."


def resolve_simulation_entry(catalog: dict, args: argparse.Namespace, provided_submit_spec: dict, simulation_manifest_root: Path) -> tuple[str, dict, dict]:
    manifest_id = str(
        provided_submit_spec.get("simulation_manifest_id", "")
        or getattr(args, "simulation_manifest_id", "")
        or ""
    ).strip()
    sequence_name = str(provided_submit_spec.get("sequence", "") or getattr(args, "sequence", "") or "").strip()
    entry: dict = {}

    if not manifest_id and sequence_name:
        try:
            resolved_name, resolved_entry = resolve_sequence(catalog, sequence_name)
        except ValueError:
            resolved_name, resolved_entry = "", {}
        if isinstance(resolved_entry, dict) and str(resolved_entry.get("simulation_manifest_id", "") or "").strip():
            sequence_name = resolved_name
            entry = resolved_entry
            manifest_id = str(entry.get("simulation_manifest_id", "") or "").strip()

    if not manifest_id:
        manifest_id = DEFAULT_SIMULATION_MANIFEST_ID
        if not sequence_name:
            sequence_name = slug(manifest_id)

    manifest_info = load_simulation_manifest(simulation_manifest_root, manifest_id)
    manifest = manifest_info["manifest"]
    if not sequence_name:
        sequence_name = slug(str(manifest.get("catalog_key", "") or manifest_id))
    if not entry:
        entry = {
            "enabled": str(manifest.get("status", manifest_info["scope"])).strip().lower() != "retired",
            "label": manifest.get("label", manifest_id),
            "description": simulation_manifest_description(manifest_id, manifest, manifest_info["scope"]),
            "analysis_kind": "simulation",
            "job_id_prefix": manifest.get("job_id_prefix", f"sim_{slug(manifest_id)}"),
            "simulation_manifest_id": manifest_id,
            "metadata_defaults": copy.deepcopy(manifest.get("metadata_defaults", {})) if isinstance(manifest.get("metadata_defaults"), dict) else {},
            "catalog_source": f"simulation_manifest_{manifest_info['scope']}",
        }
    return sequence_name, entry, manifest_info


def build_simulation_job_from_submit_spec(
    args: argparse.Namespace,
    provided_submit_spec: dict,
    sequence_name: str,
    entry: dict,
    manifest_info: dict,
) -> dict:
    manifest = manifest_info.get("manifest", {}) if isinstance(manifest_info, dict) else {}
    manifest_id = str(
        provided_submit_spec.get("simulation_manifest_id", "")
        or entry.get("simulation_manifest_id", "")
        or manifest.get("id", "")
        or ""
    ).strip()

    simulation = copy.deepcopy(manifest.get("simulation", {})) if isinstance(manifest.get("simulation"), dict) else {}
    spec_simulation = copy.deepcopy(provided_submit_spec.get("simulation", {})) if isinstance(provided_submit_spec.get("simulation"), dict) else {}
    simulation_patch = copy.deepcopy(provided_submit_spec.get("simulation_patch", {})) if isinstance(provided_submit_spec.get("simulation_patch"), dict) else {}
    if spec_simulation:
        simulation = _deep_merge(simulation, spec_simulation)
    if simulation_patch:
        simulation = _deep_merge(simulation, simulation_patch)
    if not simulation:
        raise ValueError("Simulation submit spec must provide a simulation block or a simulation_manifest_id.")
    simulation.setdefault("model", "hirose_nv14n_two_qubit_v1")

    metadata = copy.deepcopy(manifest.get("metadata_defaults", {})) if isinstance(manifest.get("metadata_defaults"), dict) else {}
    if isinstance(entry.get("metadata_defaults"), dict):
        metadata = _deep_merge(metadata, entry["metadata_defaults"])
    if isinstance(provided_submit_spec.get("metadata"), dict):
        metadata = _deep_merge(metadata, provided_submit_spec["metadata"])

    requested_by = str(provided_submit_spec.get("requested_by", "") or args.requested_by or "openclaw").strip() or "openclaw"
    metadata["requested_by"] = requested_by
    metadata["submission_path"] = resolve_submission_path(args)
    metadata["simulation_manifest_id"] = manifest_id
    metadata["simulation_manifest_path"] = str(manifest_info.get("path", "") or "")
    metadata["simulation_manifest_scope"] = str(manifest_info.get("scope", "") or "")
    metadata["simulation_queue"] = True
    if args.intent or provided_submit_spec.get("intent"):
        metadata["intent"] = str(provided_submit_spec.get("intent", "") or args.intent)

    job_id = str(provided_submit_spec.get("job_id", "") or "").strip()
    if not job_id:
        prefix = str(
            provided_submit_spec.get("job_id_prefix", "")
            or args.job_id_prefix
            or entry.get("job_id_prefix", "")
            or manifest.get("job_id_prefix", "")
            or f"sim_{sequence_name}"
        )
        suffix = str(provided_submit_spec.get("job_id_suffix", "") or args.job_id_suffix or sequence_name)
        job_id = build_job_id(prefix, suffix or None)

    job = {
        "job_id": job_id,
        "mode": "simulate",
        "simulation_manifest_id": manifest_id,
        "simulation": simulation,
        "metadata": metadata,
    }
    sample_id = str(provided_submit_spec.get("sample_id", "") or entry.get("sample_id", "") or "").strip()
    if sample_id:
        job["sample_id"] = sample_id
    return job


def manifest_route_description(manifest_id: str, manifest: dict, scope: str) -> str:
    description = str(manifest.get("description", "") or "").strip()
    if description:
        return description

    status = str(manifest.get("status", scope)).strip().lower() or str(scope or "").strip().lower()
    if status == "validated":
        prefix = "Validated"
    elif status == "staging":
        prefix = "Staging"
    elif status == "retired":
        prefix = "Retired"
    else:
        prefix = status.capitalize() if status else "Manifest"
    return f"{prefix} manifest-backed generic bridge route for {manifest_id}."


def manifest_scan_defaults(manifest: dict) -> dict:
    scan_defaults = manifest.get("scan_defaults") or {}
    if not isinstance(scan_defaults, dict):
        return {}
    return copy.deepcopy(scan_defaults)


def manifest_float_defaults(manifest: dict) -> dict:
    defaults: dict[str, object] = {}
    for name, spec in (manifest.get("float_vars") or {}).items():
        if isinstance(spec, dict) and "default" in spec:
            defaults[name] = spec["default"]
    return defaults


def manifest_limits(manifest: dict) -> dict:
    limits = manifest.get("limits") or {}
    if not isinstance(limits, dict):
        return {}
    return copy.deepcopy(limits)


def manifest_acquisition_defaults(manifest: dict) -> dict:
    acquisition = manifest.get("acquisition_defaults") or {}
    if not isinstance(acquisition, dict):
        return {}
    return copy.deepcopy(acquisition)


def merge_dicts(base: dict, override: dict) -> dict:
    merged = copy.deepcopy(base)
    merged.update(copy.deepcopy(override))
    return merged


def prepare_direct_sequence_authoring_spec(raw_payload: dict, default_sample_id: str) -> dict:
    if not callable(normalize_sequence_authoring_spec):
        raise ValueError("sequence_authoring support is unavailable because project_schema.py could not be imported.")

    authoring = normalize_sequence_authoring_spec(raw_payload, "")
    if not authoring:
        raise ValueError(
            "sequence_authoring JSON must include non-empty new_id, label, description, and base_manifest_id fields."
        )

    base_manifest_overrides = {
        "allowed_modes": ["validate", "dry_run", "execute"],
        "requires": {},
    }
    manifest_overrides = authoring.get("manifest_overrides", {}) if isinstance(authoring.get("manifest_overrides"), dict) else {}
    if callable(deep_merge_dicts):
        authoring["manifest_overrides"] = deep_merge_dicts(base_manifest_overrides, manifest_overrides)
    else:
        authoring["manifest_overrides"] = merge_dicts(base_manifest_overrides, manifest_overrides)
    return authoring


def materialize_direct_sequence_authoring(
    *,
    raw_payload: dict,
    manifest_root: Path,
    default_sample_id: str,
    authoring_hint: str = "",
) -> dict:
    if not callable(materialize_staging_sequence_spec):
        raise ValueError("sequence_authoring support is unavailable because design_nv_sequence.py could not be imported.")

    authoring = prepare_direct_sequence_authoring_spec(raw_payload, default_sample_id)
    repo_root = manifest_root.parent.parent
    authoring_root = (DEFAULT_DIRECT_SEQUENCE_AUTHORING_ROOT / slug(authoring_hint or authoring.get("new_id", "") or "sequence")).resolve()
    authoring_root.mkdir(parents=True, exist_ok=True)
    spec_path = authoring_root / f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.spec.json"
    write_json_atomic(spec_path, authoring)

    response = materialize_staging_sequence_spec(
        authoring,
        repo_root=repo_root,
        manifest_root=manifest_root,
        staging_sequence_dir=repo_root / "SavedSequences" / "SavedSequences-AWG" / "_openclaw_staging",
        staging_manifest_dir=manifest_root / "staging",
        dry_run=False,
    )
    manifest_id = str(((response.get("staging_manifest") or {}) if isinstance(response.get("staging_manifest"), dict) else {}).get("id", "") or authoring.get("new_id", "")).strip()
    if not manifest_id:
        raise ValueError("sequence_authoring materialization did not produce a staging manifest id.")

    return {
        "sequence_manifest_id": manifest_id,
        "sequence_authoring": copy.deepcopy(authoring),
        "generated_sequence": {
            "materialized_at": _safe_now_iso(),
            "spec_path": str(spec_path),
            "manifest_path": str(response.get("manifest_output_path", "") or ""),
            "sequence_path": str(response.get("sequence_output_path", "") or ""),
            "base_manifest_id": str(authoring.get("base_manifest_id", "") or ""),
            "new_id": str(authoring.get("new_id", "") or ""),
            "xml_source": str(response.get("xml_source", "") or ""),
        },
    }


def attach_sequence_authoring_response_fields(response: dict, sequence_authoring_context: dict | None) -> dict:
    updated = response if isinstance(response, dict) else {}
    context = sequence_authoring_context if isinstance(sequence_authoring_context, dict) else {}
    authoring_spec = context.get("sequence_authoring", {}) if isinstance(context.get("sequence_authoring"), dict) else {}
    generated_sequence = context.get("generated_sequence", {}) if isinstance(context.get("generated_sequence"), dict) else {}
    if authoring_spec:
        updated["sequence_authoring"] = copy.deepcopy(authoring_spec)
    if generated_sequence:
        updated["generated_sequence"] = copy.deepcopy(generated_sequence)
    return updated


def apply_alignment_metadata_overrides(metadata: dict, args: argparse.Namespace) -> dict:
    updated = copy.deepcopy(metadata)

    def assign_if_present(key: str, value: object) -> None:
        if value is not None:
            updated[key] = copy.deepcopy(value)

    assign_if_present("minimum_final_kcps", args.minimum_final_kcps)
    assign_if_present("search_scan_xy_points", args.search_scan_xy_points)
    assign_if_present("search_scan_half_span_um", list(args.search_scan_half_span_um) if args.search_scan_half_span_um is not None else None)
    assign_if_present("search_scan_z_offsets_um", list(args.search_scan_z_offsets_um) if args.search_scan_z_offsets_um is not None else None)
    assign_if_present("search_scan_dwell_seconds", args.search_scan_dwell_seconds)
    assign_if_present("search_scan_stale_hours", args.search_scan_stale_hours)
    assign_if_present("search_scan_landmark_match_radius_um", args.search_scan_landmark_match_radius_um)
    assign_if_present("search_scan_minimum_landmark_matches", args.search_scan_minimum_landmark_matches)
    assign_if_present("local_fine_search_xy_points", args.local_fine_search_xy_points)
    assign_if_present("local_fine_search_half_span_um", list(args.local_fine_search_half_span_um) if args.local_fine_search_half_span_um is not None else None)
    assign_if_present("local_fine_search_z_offsets_um", list(args.local_fine_search_z_offsets_um) if args.local_fine_search_z_offsets_um is not None else None)
    assign_if_present("local_fine_search_dwell_seconds", args.local_fine_search_dwell_seconds)
    assign_if_present("tracking_z_seed_offsets_um", list(args.tracking_z_seed_offsets_um) if args.tracking_z_seed_offsets_um is not None else None)
    assign_if_present("scheduled_tracking_period_seconds", args.scheduled_tracking_period_seconds)

    if args.search_scan_on_tracking_failure is not None:
        updated["search_scan_on_tracking_failure"] = bool(args.search_scan_on_tracking_failure)
    if args.local_fine_search_before_tracking is not None:
        updated["local_fine_search_before_tracking"] = bool(args.local_fine_search_before_tracking)
    if args.local_fine_search_promote_xy is not None:
        updated["local_fine_search_promote_xy"] = bool(args.local_fine_search_promote_xy)
    if args.enable_scheduled_tracking_after_run is not None:
        updated["enable_scheduled_tracking_after_run"] = bool(args.enable_scheduled_tracking_after_run)

    legacy_landmark_requested = (
        bool(updated.get("require_landmark_match"))
        or updated.get("allow_seed_fallback") is False
        or bool(updated.get("allow_search_scan"))
        or bool(updated.get("search_scan_on_tracking_failure"))
    )
    if getattr(args, "require_landmark_match", False):
        legacy_landmark_requested = True
    if legacy_landmark_requested:
        updated["legacy_landmark_map_requested"] = True
    updated["require_landmark_match"] = False
    if updated.get("allow_seed_fallback") is False:
        updated["allow_seed_fallback"] = True
    updated["allow_search_scan"] = False
    updated["search_scan_on_tracking_failure"] = False

    return updated


def apply_acquisition_overrides(metadata: dict, args: argparse.Namespace) -> dict:
    acquisition = copy.deepcopy(metadata.get("acquisition", {}))
    if not isinstance(acquisition, dict):
        acquisition = {}

    if args.averages is not None:
        acquisition["averages"] = int(args.averages)
    if args.repetitions is not None:
        acquisition["repetitions"] = int(args.repetitions)
    if args.average_continuously is not None:
        acquisition["average_continuously"] = bool(args.average_continuously)

    if acquisition:
        metadata["acquisition"] = acquisition
    else:
        metadata.pop("acquisition", None)
    return metadata


def expand_catalog_with_manifests(catalog: dict, manifest_root: Path) -> dict:
    expanded = copy.deepcopy(catalog)
    sequences = expanded.setdefault("sequences", {})
    explicit_manifest_ids = {
        str(entry.get("sequence_manifest_id", "")).strip()
        for entry in sequences.values()
        if isinstance(entry, dict)
    }
    validated_root = manifest_root / "validated"
    if not validated_root.is_dir():
        return expanded

    for manifest_path in sorted(validated_root.glob("*.json")):
        manifest = read_json(manifest_path)
        if not isinstance(manifest, dict):
            continue

        manifest_id = str(manifest.get("id", "")).strip() or manifest_path.stem
        if not manifest_id or manifest_id in explicit_manifest_ids:
            continue
        if str(manifest.get("status", "")).strip().lower() == "retired":
            continue

        sequence_name = slug(str(manifest.get("catalog_key", "")).strip() or manifest_id)
        if not sequence_name:
            sequence_name = slug(manifest_id)

        metadata_defaults = {
            "intent": f"openclaw auto manifest direct enqueue helper for {manifest_id}",
            "queue_execute_opt_in": True,
            "auto_align_nv": True,
            "require_landmark_match": False,
            "local_fine_search_before_tracking": False,
        }
        acquisition_defaults = manifest_acquisition_defaults(manifest)
        if acquisition_defaults:
            metadata_defaults["acquisition"] = acquisition_defaults

        entry = {
            "enabled": str(manifest.get("status", "validated")).strip().lower() == "validated",
            "label": manifest.get("label", manifest_id),
            "aliases": manifest.get("aliases", []),
            "description": manifest_route_description(manifest_id, manifest, "validated"),
            "analysis_kind": "generic_xml",
            "job_id_prefix": f"nv23_{sequence_name}",
            "recipe": "xml_generic_v1",
            "sequence_manifest_id": manifest_id,
            "scan": manifest_scan_defaults(manifest),
            "metadata_defaults": metadata_defaults,
            "catalog_source": "manifest_auto",
        }

        target_name = sequence_name
        suffix = 2
        while target_name in sequences:
            target_name = f"{sequence_name}_{suffix}"
            suffix += 1
        sequences[target_name] = entry

    return expanded


def list_sequences(catalog: dict, manifest_root: Path) -> dict:
    entries = []
    for name, entry in catalog.get("sequences", {}).items():
        manifest_id = entry.get("sequence_manifest_id", "")
        manifest_info = None
        manifest_error = ""
        if manifest_id:
            try:
                manifest_info = load_manifest(manifest_root, manifest_id)
            except ValueError as exc:
                manifest_error = str(exc)

        resolved_sequence_file = entry.get("sequence_file", "")
        resolved_sample_id = entry.get("sample_id", "")
        resolved_recipe = entry.get("recipe", "")
        manifest_status = ""
        if manifest_info:
            manifest = manifest_info["manifest"]
            resolved_sequence_file = manifest.get("sequence_file", resolved_sequence_file)
            manifest_status = manifest.get("status", manifest_info["scope"])

        entries.append(
            {
                "name": name,
                "enabled": bool(entry.get("enabled", False)),
                "label": entry.get("label", ""),
                "recipe": resolved_recipe,
                "sequence_manifest_id": manifest_id,
                "simulation_manifest_id": entry.get("simulation_manifest_id", ""),
                "sequence_file": resolved_sequence_file,
                "sample_id": resolved_sample_id,
                "manifest_status": manifest_status,
                "aliases": entry.get("aliases", []),
                "description": entry.get("description", ""),
                "disabled_reason": entry.get("disabled_reason", ""),
                "manifest_error": manifest_error,
                "catalog_source": entry.get("catalog_source", "catalog"),
            }
        )
    return {
        "default_sequence": catalog.get("default_sequence", ""),
        "sequences": entries,
    }


def synthesize_entry_from_manifest(manifest_id: str, manifest_info: dict) -> tuple[str, dict]:
    manifest = manifest_info["manifest"]
    manifest_key = slug(str(manifest.get("catalog_key", "")).strip() or manifest_id)
    sequence_name = manifest_key or slug(manifest_id)
    status = str(manifest.get("status", manifest_info["scope"])).strip().lower()
    metadata_defaults = {
        "intent": f"openclaw manifest direct enqueue helper for {manifest_id}",
        "auto_align_nv": True,
        "require_landmark_match": False,
        "local_fine_search_before_tracking": False,
    }
    acquisition_defaults = manifest_acquisition_defaults(manifest)
    if acquisition_defaults:
        metadata_defaults["acquisition"] = acquisition_defaults

    entry = {
        "enabled": status != "retired",
        "label": manifest.get("label", manifest_id),
        "aliases": manifest.get("aliases", []),
        "description": manifest_route_description(manifest_id, manifest, manifest_info["scope"]),
        "analysis_kind": "generic_xml",
        "job_id_prefix": f"nv23_{sequence_name}",
        "recipe": "xml_generic_v1",
        "sequence_manifest_id": manifest_id,
        "scan": manifest_scan_defaults(manifest),
        "metadata_defaults": metadata_defaults,
        "catalog_source": f"manifest_{manifest_info['scope']}",
        "sample_id": "",
    }
    if status == "retired":
        entry["disabled_reason"] = "This sequence manifest is retired."
    return sequence_name, entry


def resolve_sequence(catalog: dict, requested_name: str) -> tuple[str, dict]:
    sequences = catalog.get("sequences", {})
    normalized = slug(requested_name)
    matches: list[tuple[str, dict]] = []

    for name, entry in sequences.items():
        aliases = [slug(name)] + [slug(alias) for alias in entry.get("aliases", [])]
        if normalized in aliases:
            matches.append((name, entry))

    if matches:
        for name, entry in matches:
            if entry.get("enabled", False):
                return name, entry
        return matches[0]

    available = ", ".join(sorted(sequences.keys()))
    raise ValueError(f"Unknown sequence '{requested_name}'. Available sequences: {available}")


def parse_key_value_pairs(pairs: list[str] | None) -> dict:
    result = {}
    for raw in pairs or []:
        if "=" not in raw:
            raise ValueError(f"Expected key=value, got: {raw}")
        key, value = raw.split("=", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            raise ValueError(f"Missing key in assignment: {raw}")
        try:
            result[key] = json.loads(value)
        except json.JSONDecodeError:
            try:
                result[key] = float(value)
            except ValueError:
                result[key] = value
    return result


def parse_submit_spec_json(raw_value: str) -> dict:
    return parse_json_object_argument(raw_value, label="submit spec")


def parse_sequence_authoring_json(raw_value: str) -> dict:
    return parse_json_object_argument(raw_value, label="sequence authoring")


def parse_json_object_argument(raw_value: str, *, label: str) -> dict:
    payload_text = str(raw_value or "").strip()
    if not payload_text:
        return {}

    candidate_path_text = ""
    if payload_text.startswith("@"):
        candidate_path_text = payload_text[1:].strip()
    elif not payload_text.startswith("{"):
        candidate_path_text = payload_text

    if candidate_path_text:
        try:
            candidate_path = normalize_path(candidate_path_text, Path.cwd())
        except Exception:
            candidate_path = None
        if candidate_path is not None and candidate_path.is_file():
            payload_text = candidate_path.read_text(encoding="utf-8")

    if payload_text.startswith("\ufeff"):
        payload_text = payload_text[1:]

    try:
        payload = json.loads(payload_text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Could not parse {label} JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"{label} JSON must contain a top-level object.")
    return payload


def apply_scan_overrides(scan: dict, args: argparse.Namespace) -> dict:
    updated = copy.deepcopy(scan)
    if args.scan_vary_prop is not None:
        updated["vary_prop"] = list(args.scan_vary_prop)
    if args.scan_begin is not None:
        updated["begin"] = list(args.scan_begin)
    if args.scan_end is not None:
        updated["end"] = list(args.scan_end)
    if args.scan_points is not None:
        updated["points"] = list(args.scan_points)
    return updated


def build_submit_spec(
    args: argparse.Namespace,
    job_id: str,
    sequence_name: str,
    entry: dict,
    *,
    sequence_manifest_id_override: str = "",
) -> dict:
    if not entry.get("enabled", False):
        reason = entry.get("disabled_reason", "This sequence is disabled in the catalog.")
        raise ValueError(f"Sequence '{sequence_name}' is disabled: {reason}")

    recipe = str(entry.get("recipe", "") or "xml_generic_v1").strip()
    sequence_manifest_id = str(sequence_manifest_id_override or args.sequence_manifest_id or entry.get("sequence_manifest_id", "") or "").strip()
    sample_id = str(args.sample_id or entry.get("sample_id", "") or "NV23").strip() or "NV23"
    if not sequence_manifest_id:
        raise ValueError(
            f"Sequence '{sequence_name}' must define sequence_manifest_id in the catalog or on the command line."
        )
    if not recipe:
        raise ValueError(f"Sequence '{sequence_name}' is missing recipe in the catalog.")

    scan = apply_scan_overrides(copy.deepcopy(entry.get("scan", {})), args)
    float_vars = merge_dicts(copy.deepcopy(entry.get("float_vars", {})), parse_key_value_pairs(args.set_float_var))
    limits = copy.deepcopy(entry.get("limits", {})) if isinstance(entry.get("limits"), dict) else {}
    metadata = copy.deepcopy(entry.get("metadata_defaults", {}))
    if not isinstance(metadata, dict):
        metadata = {}

    requested_by = str(args.requested_by or "openclaw").strip() or "openclaw"
    submission_path = resolve_submission_path(args)
    if args.intent:
        metadata["intent"] = args.intent
    metadata = apply_acquisition_overrides(metadata, args)
    metadata = apply_alignment_metadata_overrides(metadata, args)
    if "local_fine_search_before_tracking" not in metadata:
        metadata["local_fine_search_before_tracking"] = False

    submit_spec = {
        "job_id": job_id,
        "mode": args.mode,
        "recipe": recipe,
        "sample_id": sample_id,
        "sequence_manifest_id": sequence_manifest_id,
        "requested_by": requested_by,
        "submission_path": submission_path,
        "measurement_plan_verified": submission_path == "single_item_measurement_plan",
    }

    if scan:
        submit_spec["scan"] = scan
    if float_vars:
        submit_spec["float_vars"] = float_vars
    if limits:
        submit_spec["limits"] = limits
    if metadata:
        submit_spec["metadata"] = metadata

    acquisition = metadata.get("acquisition", {}) if isinstance(metadata.get("acquisition"), dict) else {}
    if acquisition:
        submit_spec["acquisition"] = copy.deepcopy(acquisition)

    intent_text = str(args.intent or metadata.get("intent", "") or "").strip()
    if intent_text:
        submit_spec["intent"] = intent_text

    resolved_reference_data = str(args.reference_data or entry.get("reference_data", "") or "").strip()
    if resolved_reference_data:
        submit_spec["reference_data"] = resolved_reference_data
    if args.nv_position:
        submit_spec["nv_position"] = [float(value) for value in args.nv_position]
    if args.allow_seed_fallback:
        submit_spec["allow_seed_fallback"] = True

    return submit_spec


def apply_submit_spec_cli_fallbacks(
    submit_spec: dict,
    args: argparse.Namespace,
    sequence_name: str,
    entry: dict,
    job_id: str,
    *,
    sequence_manifest_id_override: str = "",
) -> dict:
    updated = copy.deepcopy(submit_spec if isinstance(submit_spec, dict) else {})
    if not updated:
        return {}
    updated.pop("approval_token", None)
    updated.pop("approval_required", None)
    updated.pop("approval", None)

    if not str(updated.get("mode", "") or "").strip():
        updated["mode"] = str(args.mode)
    if not str(updated.get("recipe", "") or "").strip():
        updated["recipe"] = str(entry.get("recipe", "") or "xml_generic_v1")
    if not str(updated.get("sample_id", "") or "").strip():
        updated["sample_id"] = str(args.sample_id or entry.get("sample_id", "") or "NV23").strip() or "NV23"

    override_manifest_id = str(sequence_manifest_id_override or "").strip()
    if override_manifest_id:
        updated["sequence_manifest_id"] = override_manifest_id
        updated.pop("sequence", None)
    elif not str(updated.get("sequence_manifest_id", "") or "").strip():
        manifest_id = str(args.sequence_manifest_id or entry.get("sequence_manifest_id", "") or "").strip()
        if manifest_id:
            updated["sequence_manifest_id"] = manifest_id
    if not str(updated.get("sequence", "") or "").strip() and not str(updated.get("sequence_manifest_id", "") or "").strip():
        updated["sequence"] = str(sequence_name)

    if not str(updated.get("requested_by", "") or "").strip():
        updated["requested_by"] = str(args.requested_by or "openclaw").strip() or "openclaw"
    if not str(updated.get("submission_path", "") or "").strip():
        updated["submission_path"] = resolve_submission_path(args)
    if "measurement_plan_verified" not in updated:
        updated["measurement_plan_verified"] = (resolve_submission_path(args) == "single_item_measurement_plan")
    if not str(updated.get("intent", "") or "").strip() and args.intent:
        updated["intent"] = str(args.intent)
    if not str(updated.get("reference_data", "") or "").strip() and args.reference_data:
        updated["reference_data"] = str(args.reference_data)
    if "nv_position" not in updated and args.nv_position:
        updated["nv_position"] = [float(value) for value in args.nv_position]
    if "allow_seed_fallback" not in updated and args.allow_seed_fallback:
        updated["allow_seed_fallback"] = True

    metadata = copy.deepcopy(updated.get("metadata", {})) if isinstance(updated.get("metadata"), dict) else {}
    if "local_fine_search_before_tracking" not in metadata:
        metadata["local_fine_search_before_tracking"] = False
    updated["metadata"] = metadata

    if not str(updated.get("job_id", "") or "").strip() and not str(updated.get("job_id_prefix", "") or "").strip():
        updated["job_id"] = str(job_id)
    return updated


def build_job(
    args: argparse.Namespace,
    job_id: str,
    sequence_name: str,
    entry: dict,
    manifest_root: Path,
    seed_registry_path: Path,
    *,
    sequence_manifest_id_override: str = "",
) -> dict:
    _ = manifest_root
    _ = seed_registry_path
    return build_submit_spec(args, job_id, sequence_name, entry, sequence_manifest_id_override=sequence_manifest_id_override)


def build_single_submit_item(
    args: argparse.Namespace,
    sequence_name: str,
    entry: dict,
    *,
    submit_spec: dict | None = None,
    sequence_authoring_context: dict | None = None,
) -> dict:
    job_id_prefix = str(args.job_id_prefix or entry.get("job_id_prefix", "") or f"nv23_{sequence_name}")
    preview_job_id = build_job_id(job_id_prefix, args.job_id_suffix or None)
    resolved_submit_spec = copy.deepcopy(submit_spec if isinstance(submit_spec, dict) else {})
    if not resolved_submit_spec:
        resolved_submit_spec = build_submit_spec(args, preview_job_id, sequence_name, entry)
    elif not str(resolved_submit_spec.get("job_id", "") or "").strip():
        resolved_submit_spec["job_id"] = preview_job_id

    authoring_context = sequence_authoring_context if isinstance(sequence_authoring_context, dict) else {}
    authoring_spec = authoring_context.get("sequence_authoring", {}) if isinstance(authoring_context.get("sequence_authoring"), dict) else {}
    extra_fields: dict[str, object] = {}
    if authoring_spec:
        extra_fields["sequence_authoring"] = copy.deepcopy(authoring_spec)
    generated_sequence = authoring_context.get("generated_sequence", {}) if isinstance(authoring_context.get("generated_sequence"), dict) else {}
    if generated_sequence:
        extra_fields["generated_sequence"] = copy.deepcopy(generated_sequence)

    item_id = slug(
        args.job_id_suffix
        or resolved_submit_spec.get("sequence_manifest_id", "")
        or authoring_spec.get("new_id", "")
        or sequence_name
    )

    if callable(build_batch_item_from_submit_spec):
        return build_batch_item_from_submit_spec(
            resolved_submit_spec,
            item_id=item_id,
            job_id_prefix=job_id_prefix,
            job_id_suffix=str(args.job_id_suffix or item_id),
            include_job_id=False,
            extra_fields=extra_fields or None,
        )

    fallback_item = copy.deepcopy(resolved_submit_spec)
    fallback_item.pop("job_id", None)
    fallback_item["id"] = item_id
    fallback_item["job_id_prefix"] = job_id_prefix
    fallback_item["job_id_suffix"] = str(args.job_id_suffix or item_id)
    if extra_fields:
        fallback_item.update(copy.deepcopy(extra_fields))
    return fallback_item


def build_single_submit_batch_spec(
    args: argparse.Namespace,
    batch_id: str,
    sequence_name: str,
    entry: dict,
    *,
    submit_spec: dict | None = None,
    sequence_authoring_context: dict | None = None,
) -> dict:
    item = build_single_submit_item(
        args,
        sequence_name,
        entry,
        submit_spec=submit_spec,
        sequence_authoring_context=sequence_authoring_context,
    )
    requested_sample_id = str(item.get("sample_id", "") or "").strip()
    authoring_spec = (sequence_authoring_context or {}).get("sequence_authoring", {}) if isinstance(sequence_authoring_context, dict) else {}
    description = (
        str(item.get("sequence_manifest_id", "") or "")
        or str(authoring_spec.get("new_id", "") or "")
        or args.sequence_manifest_id
        or entry.get("sequence_manifest_id", "")
        or sequence_name
    )
    batch_spec = {
        "batch_id": batch_id,
        "requested_by": str(args.requested_by or "openclaw"),
        "mode": str(args.mode),
        "requested_sample_id": requested_sample_id,
        "selected_templates": [],
        "natural_language_request": f"Single-job submit for {description}",
        "items": [item],
        "policy": {
            "measurement_plan_enabled": False,
            "measurement_plan_required": False,
        },
    }
    return batch_spec


def try_parse_json_text(text: str) -> dict:
    payload_text = str(text or "").strip()
    if not payload_text:
        return {}
    try:
        parsed = json.loads(payload_text)
    except json.JSONDecodeError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def read_text_if_exists(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""
    except Exception as exc:
        return f"[failed to read {path}: {exc}]"


def read_batch_state_if_exists(path: Path) -> dict:
    try:
        payload = read_json(path)
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def batch_state_is_terminal(batch_state: dict) -> bool:
    return str(batch_state.get("status", "") or "").strip().lower() in TERMINAL_BATCH_STATUSES


def terminate_process(process: subprocess.Popen, *, grace_seconds: float = 5.0) -> bool:
    if process.poll() is not None:
        return False
    process.terminate()
    try:
        process.wait(timeout=max(float(grace_seconds), 0.1))
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=max(float(grace_seconds), 0.1))
    return True


def batch_terminal_returncode(batch_state: dict, fallback: int | None = None) -> int:
    status = str(batch_state.get("status", "") or "").strip().lower()
    if status == "completed":
        return 0
    if status == "stopped":
        return 3
    if status == "failed":
        return 1
    return int(fallback) if fallback is not None else 124


def run_single_item_runner_command(
    command: list[str],
    *,
    env: dict,
    batch_root: Path,
    batch_id: str,
    state_path: Path,
    timeout_seconds: float,
    measurement_plan_timeout_seconds: float,
) -> tuple[int, dict, str, str, dict]:
    log_root = batch_root / "runner_logs"
    log_root.mkdir(parents=True, exist_ok=True)
    stdout_path = log_root / f"{batch_id}.stdout.json"
    stderr_path = log_root / f"{batch_id}.stderr.txt"

    started = time.monotonic()
    timeout_deadline = (
        started
        + max(float(timeout_seconds or 0.0), 0.0)
        + max(float(measurement_plan_timeout_seconds or 0.0), 0.0)
        + SINGLE_ITEM_RUNNER_TIMEOUT_GRACE_SECONDS
    )
    terminal_seen_at: float | None = None
    batch_state: dict = {}
    timed_out = False
    terminated_after_terminal_state = False

    with stdout_path.open("w", encoding="utf-8", newline="\n") as stdout_handle, stderr_path.open(
        "w", encoding="utf-8", newline="\n"
    ) as stderr_handle:
        process = subprocess.Popen(command, stdout=stdout_handle, stderr=stderr_handle, text=True, env=env)
        while True:
            returncode = process.poll()
            if returncode is not None:
                break

            current_state = read_batch_state_if_exists(state_path)
            if current_state:
                batch_state = current_state
            if batch_state_is_terminal(batch_state):
                if terminal_seen_at is None:
                    terminal_seen_at = time.monotonic()
                elif time.monotonic() - terminal_seen_at >= SINGLE_ITEM_RUNNER_TERMINAL_EXIT_GRACE_SECONDS:
                    terminated_after_terminal_state = terminate_process(process)
                    returncode = process.returncode
                    break

            if time.monotonic() >= timeout_deadline:
                timed_out = True
                terminate_process(process)
                returncode = process.returncode
                break

            time.sleep(1.0)

    stdout = read_text_if_exists(stdout_path)
    stderr = read_text_if_exists(stderr_path)
    stdout_state = try_parse_json_text(stdout)
    if stdout_state:
        batch_state = stdout_state
    elif not batch_state:
        batch_state = read_batch_state_if_exists(state_path)

    effective_returncode = batch_terminal_returncode(batch_state, returncode) if batch_state_is_terminal(batch_state) else (
        int(returncode) if returncode is not None else 124
    )
    runner_info = {
        "command": command,
        "stdout_path": str(stdout_path),
        "stderr_path": str(stderr_path),
        "returncode": int(returncode) if returncode is not None else None,
        "effective_returncode": int(effective_returncode),
        "timed_out": bool(timed_out),
        "terminated_after_terminal_state": bool(terminated_after_terminal_state),
        "elapsed_seconds": time.monotonic() - started,
    }
    return effective_returncode, batch_state, stdout, stderr, runner_info


def latest_item_history_entry(item_state: dict, event_name: str) -> dict:
    history = item_state.get("history", []) if isinstance(item_state, dict) else []
    if not isinstance(history, list):
        return {}
    for entry in reversed(history):
        if isinstance(entry, dict) and str(entry.get("event", "") or "") == event_name:
            return entry
    return {}


def synthesize_single_submit_response(
    batch_state: dict,
    batch_spec_path: Path,
    state_path: Path,
    control_path: Path,
    sequence_name: str,
    args: argparse.Namespace,
) -> dict:
    items = batch_state.get("items", []) if isinstance(batch_state.get("items"), list) else []
    item_state = items[0] if items and isinstance(items[0], dict) else {}
    batch_spec = read_json(batch_spec_path) if batch_spec_path.is_file() else {}
    batch_items = batch_spec.get("items", []) if isinstance(batch_spec.get("items"), list) else []
    batch_item = batch_items[0] if batch_items and isinstance(batch_items[0], dict) else {}
    queue_entry = latest_item_history_entry(item_state, "queue_submit")
    queue_response = try_parse_json_text(queue_entry.get("stdout", ""))
    planning_entry = latest_item_history_entry(item_state, "measurement_plan")
    planning_plan = planning_entry.get("plan", {}) if isinstance(planning_entry.get("plan"), dict) else {}
    pre_enqueue_advisory = annotate_runtime_estimate_context(
        planning_entry.get("pre_enqueue_advisory", {}) if isinstance(planning_entry.get("pre_enqueue_advisory"), dict) else {}
    )

    if queue_response:
        response = copy.deepcopy(queue_response)
    else:
        response = {
            "ok": False,
            "mode": str(args.mode),
            "sequence": sequence_name,
            "job_id": "",
            "job": {},
            "error_code": str(item_state.get("last_error_code", "") or ""),
            "error_message": str(item_state.get("last_error_message", "") or batch_state.get("status", "") or ""),
            "final_state": str(batch_state.get("status", "") or ""),
            "timed_out": False,
        }

    response["single_item_measurement_plan"] = True
    response["submission_path"] = "single_item_measurement_plan"
    response["batch_id"] = str(batch_state.get("batch_id", "") or batch_spec_path.stem)
    response["batch_spec_path"] = str(batch_spec_path)
    response["batch_state_path"] = str(state_path)
    response["batch_control_path"] = str(control_path)
    response["batch_status"] = str(batch_state.get("status", "") or "")
    response["mode"] = str(response.get("mode", "") or args.mode)
    response["sequence"] = str(response.get("sequence", "") or sequence_name)

    if planning_entry:
        response["measurement_plan"] = {
            "message": str(planning_entry.get("message", "") or ""),
            "request_path": str(planning_entry.get("request_path", "") or ""),
            "plan_path": str(planning_entry.get("plan_path", "") or ""),
            "hook_ok": bool(planning_entry.get("hook_ok", False)),
            "plan": copy.deepcopy(planning_plan),
        }
    if pre_enqueue_advisory:
        response["pre_enqueue_advisory"] = copy.deepcopy(pre_enqueue_advisory)
        if args.include_job_advisory:
            response["job_advisory"] = copy.deepcopy(pre_enqueue_advisory)
        runtime_estimate_context = pre_enqueue_advisory.get("runtime_estimate_context", {})
        if isinstance(runtime_estimate_context, dict) and runtime_estimate_context:
            response["runtime_estimate_context"] = copy.deepcopy(runtime_estimate_context)
    response["measurement_plan_verified"] = bool(
        planning_entry
        and response.get("measurement_plan", {}).get("request_path", "")
        and response.get("measurement_plan", {}).get("plan_path", "")
        and pre_enqueue_advisory
    )

    if not queue_response:
        response["outcome_summary"] = {}
        response["result_path"] = ""
        response["queue_root"] = str(normalize_path(args.queue_root, DEFAULT_QUEUE_ROOT))

    attach_sequence_authoring_response_fields(
        response,
        {
            "sequence_authoring": copy.deepcopy(batch_item.get("sequence_authoring", {})) if isinstance(batch_item.get("sequence_authoring"), dict) else {},
            "generated_sequence": copy.deepcopy(batch_item.get("generated_sequence", {})) if isinstance(batch_item.get("generated_sequence"), dict) else {},
        },
    )
    return response


def run_single_item_via_batch_runner(
    args: argparse.Namespace,
    sequence_name: str,
    entry: dict,
    *,
    submit_spec: dict | None = None,
    sequence_authoring_context: dict | None = None,
) -> tuple[int, dict, str, str]:
    batch_root = DEFAULT_SINGLE_SUBMIT_ROOT.resolve()
    batch_root.mkdir(parents=True, exist_ok=True)

    batch_id = build_job_id(args.job_id_prefix or entry.get("job_id_prefix") or f"single_{sequence_name}", args.job_id_suffix or None)
    batch_spec_path = batch_root / "batch_specs" / f"{batch_id}.json"
    state_path = batch_root / "batches" / f"{batch_id}.state.json"
    control_path = batch_root / "batches" / f"{batch_id}.control.json"
    batch_spec = build_single_submit_batch_spec(
        args,
        batch_id,
        sequence_name,
        entry,
        submit_spec=submit_spec,
        sequence_authoring_context=sequence_authoring_context,
    )
    write_json_atomic(batch_spec_path, batch_spec)

    runner_path = WORKSPACE_ROOT / "nv_batch_run.py"
    command = [
        sys.executable,
        str(runner_path),
        "--batch-spec",
        str(batch_spec_path),
        "--state-path",
        str(state_path),
        "--control-path",
        str(control_path),
        "--timeout-seconds",
        str(args.timeout_seconds),
        "--poll-seconds",
        str(args.poll_seconds),
        "--measurement-plan-timeout-seconds",
        str(args.measurement_plan_timeout_seconds),
    ]
    if args.gateway_url:
        command.extend(["--gateway-url", str(args.gateway_url)])
    if args.config_path:
        command.extend(["--config-path", str(args.config_path)])

    env = os.environ.copy()
    env["NV_BRIDGE_ROOT"] = str(normalize_path(args.queue_root, DEFAULT_QUEUE_ROOT))
    env["NV_SEQUENCE_CATALOG"] = str(normalize_path(args.catalog, DEFAULT_CATALOG_PATH))
    env["NV_SEQUENCE_MANIFEST_ROOT"] = str(normalize_path(args.manifest_root, DEFAULT_MANIFEST_ROOT))
    env["NV_SEED_REGISTRY_PATH"] = str(normalize_path(args.seed_registry_path, DEFAULT_NV_SEED_REGISTRY_PATH))
    returncode, batch_state, stdout, stderr, runner_info = run_single_item_runner_command(
        command,
        env=env,
        batch_root=batch_root,
        batch_id=batch_id,
        state_path=state_path,
        timeout_seconds=float(args.timeout_seconds),
        measurement_plan_timeout_seconds=float(args.measurement_plan_timeout_seconds),
    )

    if isinstance(batch_state, dict) and batch_state:
        response = synthesize_single_submit_response(
            batch_state=batch_state,
            batch_spec_path=batch_spec_path,
            state_path=state_path,
            control_path=control_path,
            sequence_name=sequence_name,
            args=args,
        )
    else:
        response = {
            "ok": False,
            "mode": str(args.mode),
            "sequence": sequence_name,
            "single_item_measurement_plan": True,
            "batch_id": batch_id,
            "batch_spec_path": str(batch_spec_path),
            "batch_state_path": str(state_path),
            "batch_control_path": str(control_path),
            "error_code": "SINGLE_SUBMIT_BATCH_FAILED",
            "error_message": stderr.strip() or stdout.strip() or "Single-item batch submission failed before a batch state was produced.",
        }
    response["single_item_runner"] = runner_info
    if runner_info.get("timed_out") and not batch_state_is_terminal(batch_state):
        response["ok"] = False
        response["timed_out"] = True
        response["error_code"] = str(response.get("error_code", "") or "SINGLE_SUBMIT_RUNNER_TIMEOUT")
        response["error_message"] = str(
            response.get("error_message", "")
            or "Single-item batch runner exceeded the local wrapper deadline; check batch_state_path and bridge queue state."
        )

    return returncode, response, stdout, stderr


def probe_job(queue_root: Path, job_id: str) -> dict:
    for state in ["done", "failed", "running", "queued"]:
        job_dir = queue_root / state / job_id
        if job_dir.is_dir():
            return {
                "state": state,
                "job_dir": job_dir,
                "result_path": job_dir / "result.json",
            }
    return {
        "state": "missing",
        "job_dir": Path(),
        "result_path": Path(),
    }


def summarize_result(result: dict) -> dict:
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


def wait_for_result(
    queue_root: Path,
    job_id: str,
    timeout_seconds: float | None,
    poll_seconds: float,
    *,
    job: dict | None = None,
    runtime_watch_config: dict | None = None,
) -> dict:
    if callable(runtime_watch_wait_for_result):
        return runtime_watch_wait_for_result(
            queue_root,
            job_id,
            timeout_seconds,
            poll_seconds,
            job=job if isinstance(job, dict) else None,
            config=runtime_watch_config if isinstance(runtime_watch_config, dict) else None,
        )
    started = time.monotonic()
    while True:
        current = probe_job(queue_root, job_id)
        state = current["state"]
        result_path = current["result_path"]

        if state in {"done", "failed"} and result_path.is_file():
            result = read_json(result_path)
            return {
                "timed_out": False,
                "final_state": state,
                "job_dir": str(current["job_dir"]),
                "result_path": str(result_path),
                "result": result,
                "outcome_summary": summarize_result(result),
                "elapsed_seconds": time.monotonic() - started,
            }

        elapsed = time.monotonic() - started
        if timeout_seconds is not None and timeout_seconds > 0 and elapsed >= timeout_seconds:
            # Stay attached to the specific job while it is still visible in the queue.
            # This keeps direct agent-recovery flows alive even if other jobs are submitted
            # and our target job spends a long time queued or running.
            if state in {"queued", "running"}:
                time.sleep(poll_seconds)
                continue
            return {
                "timed_out": True,
                "final_state": "timeout",
                "job_dir": str(current["job_dir"]) if current["job_dir"] else "",
                "result_path": str(result_path) if result_path else "",
                "result": {},
                "outcome_summary": summarize_result({}),
                "elapsed_seconds": elapsed,
            }

        time.sleep(poll_seconds)


def enqueue_job_payload(queue_root: Path, job: dict) -> dict:
    job_id = str(job.get("job_id", "") or "").strip()
    if not job_id:
        raise ValueError("job payload is missing job_id")

    queued_dir = queue_root / "queued" / job_id
    staging_dir = queue_root / "staging" / f"{job_id}__staging"

    if queued_dir.exists():
        raise FileExistsError(f"Queued job directory already exists: {queued_dir}")
    if staging_dir.exists():
        raise FileExistsError(f"Staging directory already exists: {staging_dir}")

    try:
        staging_dir.mkdir(parents=True, exist_ok=False)
        write_json_atomic(staging_dir / "job.json", job)
        os.replace(staging_dir, queued_dir)
    except Exception:
        if staging_dir.exists():
            for path in sorted(staging_dir.glob("**/*"), reverse=True):
                if path.is_file():
                    path.unlink(missing_ok=True)
            for path in sorted(staging_dir.glob("**/*"), reverse=True):
                if path.is_dir():
                    path.rmdir()
            if staging_dir.exists():
                staging_dir.rmdir()
        raise

    return {
        "job_id": job_id,
        "job_dir": str(queued_dir),
        "job_path": str(queued_dir / "job.json"),
    }


def _safe_now_iso() -> str:
    if callable(now_iso):
        return now_iso()
    return datetime.utcnow().isoformat() + "Z"


def _deep_merge(base: dict, override: dict) -> dict:
    if callable(deep_merge_dicts):
        return deep_merge_dicts(base, override)
    merged = copy.deepcopy(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged.get(key, {}), value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def build_runtime_watch_config(args: argparse.Namespace, job: dict) -> dict | None:
    if not getattr(args, "runtime_watch", True):
        return {"enabled": False}

    metadata = copy.deepcopy(job.get("metadata", {})) if isinstance(job.get("metadata"), dict) else {}
    runtime_watch = copy.deepcopy(metadata.get("runtime_watch", {})) if isinstance(metadata.get("runtime_watch"), dict) else {}
    inline_override = getattr(args, "inline_runtime_watch", None)
    if inline_override is None and runtime_watch.get("inline_enabled", None) is not None:
        inline_override = bool(runtime_watch.get("inline_enabled"))

    # Cron now owns active runtime monitoring for queued bridge jobs unless explicitly re-enabled.
    submission_path = str(metadata.get("submission_path", "") or "").strip()
    inline_enabled = bool(inline_override) if inline_override is not None else submission_path not in CRON_MANAGED_INLINE_WATCH_SUBMISSION_PATHS
    if not inline_enabled:
        return {"enabled": False}

    overrides = {
        "enabled": True,
        "requested_by": str(getattr(args, "runtime_watch_requested_by", "") or "openclaw-runtime-watch"),
    }
    if callable(build_runtime_watch_defaults):
        return build_runtime_watch_defaults(job if isinstance(job, dict) else None, overrides)

    runtime_watch.update(overrides)
    runtime_watch.setdefault("enabled", True)
    return runtime_watch


def runtime_watch_recovery_requested(wait_response: dict) -> bool:
    runtime_watch = wait_response.get("runtime_watch", {}) if isinstance(wait_response, dict) else {}
    if not isinstance(runtime_watch, dict):
        return False
    anomaly = runtime_watch.get("anomaly", {})
    if not isinstance(anomaly, dict) or not bool(anomaly.get("detected", False)):
        return False
    if not bool(anomaly.get("retry_recommended", False)):
        return False
    final_state = str(wait_response.get("final_state", "") or "").strip().lower()
    return final_state in {"failed", "timeout"}


def should_request_agent_recovery(job: dict, wait_response: dict) -> bool:
    if not isinstance(job, dict) or not isinstance(wait_response, dict):
        return False
    if str(job.get("mode", "") or "").strip().lower() != "execute":
        return False
    final_state = str(wait_response.get("final_state", "") or "").strip().lower()
    if final_state not in {"failed", "timeout"}:
        return False
    if runtime_watch_recovery_requested(wait_response):
        return True

    result = wait_response.get("result", {})
    if not isinstance(result, dict):
        return False

    summary = result.get("summary", {})
    align = summary.get("align_nv", {}) if isinstance(summary, dict) else {}
    if not isinstance(align, dict):
        return False

    return bool(align.get("gui_tracking_attempted")) and bool(align.get("agent_seed_selection_required"))


def build_direct_recovery_request_payload(job: dict, wait_response: dict, request_path: Path, plan_path: Path, retry_round: int) -> dict:
    result_payload = wait_response.get("result", {}) if isinstance(wait_response.get("result"), dict) else {}
    runtime_watch = wait_response.get("runtime_watch", {}) if isinstance(wait_response.get("runtime_watch"), dict) else {}
    runtime_watch_anomaly = runtime_watch.get("anomaly", {}) if isinstance(runtime_watch.get("anomaly"), dict) else {}
    artifacts = latest_failure_artifacts(wait_response) if callable(latest_failure_artifacts) else {}
    bridge_log_tail = ""
    if isinstance(artifacts, dict) and artifacts.get("bridge_log_path") and callable(tail_text_file):
        bridge_log_tail = tail_text_file(Path(artifacts["bridge_log_path"]))

    metadata = copy.deepcopy(job.get("metadata", {})) if isinstance(job.get("metadata"), dict) else {}
    current_item_context = {
        "id": str(job.get("job_id", "") or ""),
        "mode": str(job.get("mode", "") or ""),
        "sample_id": str(job.get("sample_id", "") or ""),
        "sequence": str(job.get("sequence_manifest_id", "") or job.get("sequence_file", "") or ""),
        "sequence_manifest_id": str(job.get("sequence_manifest_id", "") or ""),
        "sequence_file": str(job.get("sequence_file", "") or ""),
        "scan": copy.deepcopy(job.get("scan", {})) if isinstance(job.get("scan"), dict) else {},
        "float_vars": copy.deepcopy(job.get("float_vars", {})) if isinstance(job.get("float_vars"), dict) else {},
        "analysis": {},
        "acquisition": copy.deepcopy(metadata.get("acquisition", {})) if isinstance(metadata.get("acquisition"), dict) else {},
        "metadata": metadata,
    }

    return {
        "request_kind": "direct_execute_recovery",
        "batch_id": f"direct:{str(job.get('job_id', '') or '')}",
        "state_path": "",
        "item_id": str(job.get("job_id", "") or ""),
        "attempt": int(retry_round),
        "requested_at": _safe_now_iso(),
        "request_path": str(request_path),
        "plan_path": str(plan_path),
        "current_item_spec": copy.deepcopy(job),
        "current_item_context": current_item_context,
        "item_state": {
            "status": "failed",
            "attempts": int(retry_round),
            "last_error_code": str(result_payload.get("error_code", "") or runtime_watch_anomaly.get("error_code", "") or ""),
            "last_error_message": str(result_payload.get("error_message", "") or runtime_watch_anomaly.get("message", "") or ""),
            "retry_overrides": {},
            "recent_history": [],
        },
        "case_library_matches": [],
        "direct_job_context": {
            "job_id": str(job.get("job_id", "") or ""),
            "mode": str(job.get("mode", "") or ""),
            "sequence_manifest_id": str(job.get("sequence_manifest_id", "") or ""),
            "sequence_file": str(job.get("sequence_file", "") or ""),
            "requested_by": str(metadata.get("requested_by", "") or ""),
        },
        "failure": {
            "action": "retry",
            "reason": "runtime_watch_requested_retry" if bool(runtime_watch_anomaly.get("detected", False)) else "direct_execute_failed",
            "rule_source": "runtime_watch" if bool(runtime_watch_anomaly.get("detected", False)) else "direct_execute_agent_recovery",
            "error_code": str(result_payload.get("error_code", "") or runtime_watch_anomaly.get("error_code", "") or ""),
            "error_message": str(result_payload.get("error_message", "") or runtime_watch_anomaly.get("message", "") or ""),
            "response_summary": {
                "job_id": str(wait_response.get("job_id", "") or job.get("job_id", "") or ""),
                "final_state": str(wait_response.get("final_state", "") or ""),
                "timed_out": bool(wait_response.get("timed_out", False)),
                "result_path": str(wait_response.get("result_path", "") or ""),
                "outcome_summary": copy.deepcopy(wait_response.get("outcome_summary", {})),
            },
            "runtime_watch": copy.deepcopy(runtime_watch),
            "artifacts": artifacts if isinstance(artifacts, dict) else {},
            "job_summary": summarize_job_for_recovery(job) if callable(summarize_job_for_recovery) else copy.deepcopy(job),
            "result_summary": summarize_result_for_recovery(result_payload) if callable(summarize_result_for_recovery) else copy.deepcopy(result_payload),
            "bridge_log_tail": bridge_log_tail,
        },
    }


def build_retry_submit_spec(job: dict, plan: dict, retry_round: int) -> dict:
    metadata = copy.deepcopy(job.get("metadata", {})) if isinstance(job.get("metadata"), dict) else {}
    acquisition = copy.deepcopy(metadata.get("acquisition", {})) if isinstance(metadata.get("acquisition"), dict) else {}
    updated = {
        "job_id": build_job_id(str(job.get("job_id", "") or "nv23_retry"), f"agent_recovery_{retry_round:02d}"),
        "mode": str(job.get("mode", "") or "execute"),
        "recipe": str(job.get("recipe", "") or "xml_generic_v1"),
        "sample_id": str(job.get("sample_id", "") or "NV23"),
        "sequence_manifest_id": str(job.get("sequence_manifest_id", "") or ""),
        "requested_by": str(metadata.get("requested_by", "") or "openclaw"),
        "submission_path": str(metadata.get("submission_path", "") or ""),
        "measurement_plan_verified": bool(metadata.get("measurement_plan_verified", False)),
        "scan": copy.deepcopy(job.get("scan", {})) if isinstance(job.get("scan"), dict) else {},
        "float_vars": copy.deepcopy(job.get("float_vars", {})) if isinstance(job.get("float_vars"), dict) else {},
        "limits": copy.deepcopy(job.get("limits", {})) if isinstance(job.get("limits"), dict) else {},
        "metadata": metadata,
        "acquisition": acquisition,
    }

    overrides = copy.deepcopy(plan.get("item_overrides", {})) if isinstance(plan.get("item_overrides"), dict) else {}

    if isinstance(overrides.get("scan"), dict):
        updated["scan"] = _deep_merge(updated.get("scan", {}) if isinstance(updated.get("scan"), dict) else {}, overrides["scan"])
    if isinstance(overrides.get("float_vars"), dict):
        updated["float_vars"] = _deep_merge(updated.get("float_vars", {}) if isinstance(updated.get("float_vars"), dict) else {}, overrides["float_vars"])
    if isinstance(overrides.get("limits"), dict):
        updated["limits"] = _deep_merge(updated.get("limits", {}) if isinstance(updated.get("limits"), dict) else {}, overrides["limits"])

    metadata = copy.deepcopy(updated.get("metadata", {})) if isinstance(updated.get("metadata"), dict) else {}
    if isinstance(overrides.get("metadata"), dict):
        metadata = _deep_merge(metadata, overrides["metadata"])

    if isinstance(overrides.get("acquisition"), dict):
        acquisition = _deep_merge(acquisition, overrides["acquisition"])

    if "allow_seed_fallback" in overrides:
        allow_seed_fallback = bool(overrides.get("allow_seed_fallback"))
        if not allow_seed_fallback:
            metadata["legacy_landmark_map_requested"] = True
        metadata["allow_seed_fallback"] = True
        updated["allow_seed_fallback"] = True

    if "reference_data" in overrides and overrides.get("reference_data"):
        updated["reference_data"] = str(overrides.get("reference_data") or "")
    elif metadata.get("reference_data"):
        updated["reference_data"] = str(metadata.get("reference_data") or "")

    if metadata.get("intent"):
        updated["intent"] = str(metadata.get("intent") or "")

    metadata["direct_agent_recovery"] = {
        "enabled": True,
        "retry_round": int(retry_round),
        "source_job_id": str(job.get("job_id", "") or ""),
        "operator_message": str(plan.get("operator_message", "") or ""),
        "reason": str(plan.get("reason", "") or ""),
        "planned_at": _safe_now_iso(),
    }
    if acquisition:
        metadata["acquisition"] = acquisition
        updated["acquisition"] = acquisition
    elif "acquisition" in metadata:
        metadata.pop("acquisition", None)
        updated.pop("acquisition", None)
    updated["metadata"] = metadata
    return updated


def maybe_run_agent_recovery(
    args: argparse.Namespace,
    queue_root: Path,
    manifest_root: Path,
    job: dict,
    wait_response: dict,
    retry_round: int,
) -> dict:
    outcome = {
        "attempted": False,
        "eligible": should_request_agent_recovery(job, wait_response),
        "reason": "",
        "request_path": "",
        "plan_path": "",
        "plan": {},
        "retry_job_id": "",
        "retry_submit_response": {},
        "retry_submit_runner": {},
        "retry_response": {},
    }
    if not args.agent_recovery:
        outcome["reason"] = "agent_recovery_disabled"
        return outcome
    if not outcome["eligible"]:
        outcome["reason"] = "not_eligible"
        return outcome
    if not callable(resolve_hook_token) or not callable(post_hook) or not callable(wait_for_recovery_plan) or not callable(normalize_agent_recovery_plan) or not callable(write_pretty_json):
        outcome["reason"] = "agent_recovery_helpers_unavailable"
        return outcome

    config_path = normalize_path(args.config_path, DEFAULT_OPENCLAW_CONFIG_PATH)
    hook_token = resolve_hook_token(config_path)
    if not hook_token:
        outcome["reason"] = "missing_hook_token"
        return outcome

    recovery_root = normalize_path(args.direct_recovery_root, DEFAULT_DIRECT_RECOVERY_ROOT)
    request_dir = recovery_root / str(job.get("job_id", "job"))
    request_dir.mkdir(parents=True, exist_ok=True)
    request_path = request_dir / f"attempt_{int(retry_round):02d}.request.json"
    plan_path = request_dir / f"attempt_{int(retry_round):02d}.plan.json"
    request_payload = build_direct_recovery_request_payload(job, wait_response, request_path, plan_path, retry_round)
    write_pretty_json(request_path, request_payload)

    hook_payload = {
        "jobId": str(job.get("job_id", "") or ""),
        "attempt": int(retry_round),
        "errorCode": str(request_payload.get("failure", {}).get("error_code", "") or ""),
        "errorMessage": str(request_payload.get("failure", {}).get("error_message", "") or ""),
        "requestPath": str(request_path),
        "planPath": str(plan_path),
    }
    hook_ok = post_hook(args.gateway_url, hook_token, args.recovery_hook_path, hook_payload)

    outcome["attempted"] = True
    outcome["request_path"] = str(request_path)
    outcome["plan_path"] = str(plan_path)
    if not hook_ok:
        outcome["reason"] = "recovery_hook_failed"
        return outcome

    planned = wait_for_recovery_plan(plan_path, float(args.recovery_plan_timeout_seconds))
    default_mode = str(job.get("mode", "") or "execute").strip() or "execute"
    default_sample_id = str(job.get("sample_id", "") or "NV23").strip() or "NV23"
    plan = normalize_agent_recovery_plan(planned or {}, default_mode, default_sample_id)
    outcome["plan"] = plan
    if not plan:
        outcome["reason"] = "missing_or_invalid_plan"
        return outcome
    if plan.get("action") != "retry":
        outcome["reason"] = f"plan_action_{plan.get('action', 'unknown')}"
        return outcome

    retry_submit_spec = build_retry_submit_spec(job, plan, retry_round)
    submit_response, submit_runner = invoke_matlab_wrapper_submit_spec(
        retry_submit_spec,
        args,
        manifest_root,
        queue_root,
        include_job_advisory=False,
        enqueue=True,
    )
    outcome["retry_submit_response"] = submit_response
    outcome["retry_submit_runner"] = submit_runner
    if not isinstance(submit_response, dict) or not submit_response.get("ok", False):
        outcome["reason"] = "retry_submit_failed"
        return outcome

    normalized_retry_job = copy.deepcopy(submit_response.get("job", {}))
    retry_job_id = str(submit_response.get("job_id", "") or normalized_retry_job.get("job_id", "") or "")
    if not retry_job_id:
        outcome["reason"] = "retry_submit_missing_job_id"
        return outcome

    retry_response = wait_for_result(
        queue_root,
        retry_job_id,
        args.timeout_seconds,
        args.poll_seconds,
        job=normalized_retry_job,
        runtime_watch_config=build_runtime_watch_config(args, normalized_retry_job),
    )

    outcome["reason"] = "retry_enqueued"
    outcome["retry_job_id"] = retry_job_id
    outcome["retry_job"] = normalized_retry_job
    outcome["retry_response"] = retry_response
    return outcome


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Safely enqueue a direct NV sequence job from the preferred manifest-backed catalog.")
    parser.add_argument("--queue-root", default=os.environ.get("NV_BRIDGE_ROOT", "") or str(DEFAULT_QUEUE_ROOT))
    parser.add_argument("--simulation-queue-root", default=os.environ.get("NV_SIM_QUEUE_ROOT", "") or str(DEFAULT_SIMULATION_QUEUE_ROOT))
    parser.add_argument("--catalog", default=os.environ.get("NV_SEQUENCE_CATALOG", "") or str(DEFAULT_CATALOG_PATH))
    parser.add_argument(
        "--manifest-root",
        default=os.environ.get("NV_SEQUENCE_MANIFEST_ROOT", "") or str(DEFAULT_MANIFEST_ROOT),
    )
    parser.add_argument(
        "--simulation-manifest-root",
        default=os.environ.get("NV_SIMULATION_MANIFEST_ROOT", "") or str(DEFAULT_SIMULATION_MANIFEST_ROOT),
    )
    parser.add_argument(
        "--seed-registry-path",
        default=os.environ.get("NV_SEED_REGISTRY_PATH", "") or str(DEFAULT_NV_SEED_REGISTRY_PATH),
    )
    parser.add_argument("--list-sequences", action="store_true")
    parser.add_argument("--mode", choices=["validate", "dry_run", "execute", "simulate"], default="execute")
    parser.add_argument("--sequence", default="")
    parser.add_argument("--sequence-manifest-id", default="")
    parser.add_argument("--simulation-manifest-id", default="")
    parser.add_argument("--submit-spec-json", default="")
    parser.add_argument(
        "--sequence-authoring-json",
        default="",
        help="Inline JSON object or @path/to/file.json describing a sequence_authoring request for a new staging XML/manifest.",
    )
    parser.add_argument("--sample-id", default="")
    parser.add_argument("--job-id-prefix", default="")
    parser.add_argument("--job-id-suffix", default="")
    parser.add_argument("--requested-by", default="openclaw")
    parser.add_argument("--intent", default="")
    parser.add_argument("--reference-data", default="")
    parser.add_argument("--scan-vary-prop", nargs="+")
    parser.add_argument("--scan-begin", nargs="+", type=float)
    parser.add_argument("--scan-end", nargs="+", type=float)
    parser.add_argument("--scan-points", nargs="+", type=int)
    parser.add_argument("--set-float-var", action="append", default=[], metavar="KEY=VALUE")
    parser.add_argument("--auto-align-nv", dest="auto_align_nv", action="store_true", default=True)
    parser.add_argument("--no-auto-align-nv", dest="auto_align_nv", action="store_false")
    parser.add_argument("--require-landmark-match", dest="require_landmark_match", action="store_true", default=False)
    parser.add_argument("--no-require-landmark-match", dest="require_landmark_match", action="store_false")
    parser.add_argument("--allow-seed-fallback", action="store_true", default=False)
    parser.add_argument("--nv-position", nargs=3, type=float, metavar=("X", "Y", "Z"))
    parser.add_argument("--averages", type=int)
    parser.add_argument("--repetitions", type=int)
    parser.add_argument("--average-continuously", dest="average_continuously", action="store_true")
    parser.add_argument("--no-average-continuously", dest="average_continuously", action="store_false")
    parser.set_defaults(average_continuously=None)
    parser.add_argument("--minimum-final-kcps", dest="minimum_final_kcps", type=float)
    parser.add_argument("--search-scan-xy-points", dest="search_scan_xy_points", type=int)
    parser.add_argument("--search-scan-half-span-um", dest="search_scan_half_span_um", nargs=2, type=float)
    parser.add_argument("--search-scan-z-offsets-um", dest="search_scan_z_offsets_um", nargs="+", type=float)
    parser.add_argument("--search-scan-dwell-seconds", dest="search_scan_dwell_seconds", type=float)
    parser.add_argument("--search-scan-stale-hours", dest="search_scan_stale_hours", type=float)
    parser.add_argument("--search-scan-landmark-match-radius-um", dest="search_scan_landmark_match_radius_um", type=float)
    parser.add_argument("--search-scan-minimum-landmark-matches", dest="search_scan_minimum_landmark_matches", type=int)
    parser.add_argument("--search-scan-on-tracking-failure", dest="search_scan_on_tracking_failure", action="store_true")
    parser.add_argument("--no-search-scan-on-tracking-failure", dest="search_scan_on_tracking_failure", action="store_false")
    parser.set_defaults(search_scan_on_tracking_failure=None)
    parser.add_argument("--local-fine-search-before-tracking", dest="local_fine_search_before_tracking", action="store_true")
    parser.add_argument("--no-local-fine-search-before-tracking", dest="local_fine_search_before_tracking", action="store_false")
    parser.set_defaults(local_fine_search_before_tracking=None)
    parser.add_argument("--local-fine-search-xy-points", dest="local_fine_search_xy_points", type=int)
    parser.add_argument("--local-fine-search-half-span-um", dest="local_fine_search_half_span_um", nargs=2, type=float)
    parser.add_argument("--local-fine-search-z-offsets-um", dest="local_fine_search_z_offsets_um", nargs="+", type=float)
    parser.add_argument("--local-fine-search-dwell-seconds", dest="local_fine_search_dwell_seconds", type=float)
    parser.add_argument("--local-fine-search-promote-xy", dest="local_fine_search_promote_xy", action="store_true")
    parser.add_argument("--no-local-fine-search-promote-xy", dest="local_fine_search_promote_xy", action="store_false")
    parser.set_defaults(local_fine_search_promote_xy=None)
    parser.add_argument("--tracking-z-seed-offsets-um", dest="tracking_z_seed_offsets_um", nargs="+", type=float)
    parser.add_argument("--enable-scheduled-tracking-after-run", dest="enable_scheduled_tracking_after_run", action="store_true")
    parser.add_argument("--no-enable-scheduled-tracking-after-run", dest="enable_scheduled_tracking_after_run", action="store_false")
    parser.set_defaults(enable_scheduled_tracking_after_run=None)
    parser.add_argument("--scheduled-tracking-period-seconds", dest="scheduled_tracking_period_seconds", type=float)
    parser.add_argument("--wait-for-result", dest="wait_for_result", action="store_true", default=True)
    parser.add_argument("--no-wait-for-result", dest="wait_for_result", action="store_false")
    parser.add_argument("--skip-measurement-plan", dest="skip_measurement_plan", action="store_true", default=False)
    parser.add_argument("--timeout-seconds", type=float, default=900.0)
    parser.add_argument("--poll-seconds", type=float, default=2.0)
    parser.add_argument("--runtime-watch", dest="runtime_watch", action="store_true", default=True)
    parser.add_argument("--no-runtime-watch", dest="runtime_watch", action="store_false")
    parser.add_argument("--inline-runtime-watch", dest="inline_runtime_watch", action="store_true", default=None)
    parser.add_argument("--no-inline-runtime-watch", dest="inline_runtime_watch", action="store_false")
    parser.add_argument("--runtime-watch-requested-by", default="openclaw-runtime-watch")
    parser.add_argument("--include-job-advisory", dest="include_job_advisory", action="store_true", default=False)
    parser.add_argument("--preview-job-advisory-only", dest="preview_job_advisory_only", action="store_true", default=False)
    parser.add_argument("--simulation-inline-process", dest="simulation_inline_process", action="store_true", default=True)
    parser.add_argument("--no-simulation-inline-process", dest="simulation_inline_process", action="store_false")
    parser.add_argument("--job-advisory-root", default=str(DEFAULT_JOB_ADVISORY_ROOT))
    parser.add_argument("--job-advisory-timeout-seconds", type=float, default=DEFAULT_JOB_ADVISORY_TIMEOUT_SECONDS)
    parser.add_argument("--agent-recovery", dest="agent_recovery", action="store_true", default=True)
    parser.add_argument("--no-agent-recovery", dest="agent_recovery", action="store_false")
    parser.add_argument("--max-agent-retries", type=int, default=1)
    parser.add_argument("--gateway-url", default=os.environ.get("OPENCLAW_GATEWAY_URL", DEFAULT_OPENCLAW_GATEWAY_URL))
    parser.add_argument("--config-path", default=str(DEFAULT_OPENCLAW_CONFIG_PATH))
    parser.add_argument("--direct-recovery-root", default=str(DEFAULT_DIRECT_RECOVERY_ROOT))
    parser.add_argument("--recovery-hook-path", default=DEFAULT_DIRECT_RECOVERY_HOOK_PATH)
    parser.add_argument("--recovery-plan-timeout-seconds", type=float, default=DEFAULT_DIRECT_RECOVERY_PLAN_TIMEOUT_SECONDS)
    parser.add_argument("--measurement-plan-timeout-seconds", type=float, default=DEFAULT_MEASUREMENT_PLAN_TIMEOUT_SECONDS)
    parser.add_argument("--active-chain-wait-seconds", type=float, default=DEFAULT_ACTIVE_CHAIN_WAIT_SECONDS)
    return parser


def parse_args_with_unquoted_intent_recovery(parser: argparse.ArgumentParser, argv: list[str] | None = None) -> argparse.Namespace:
    argv = list(sys.argv[1:] if argv is None else argv)
    args, unknown = parser.parse_known_args(argv)
    if not unknown:
        return args

    intent_tail: list[str] = []
    if args.intent:
        for index, token in enumerate(argv):
            if token == "--intent":
                tail_start = index + 2
            elif token.startswith("--intent="):
                tail_start = index + 1
            else:
                continue

            tail: list[str] = []
            for value in argv[tail_start:]:
                if value.startswith("--"):
                    break
                tail.append(value)
            if tail and tail == unknown:
                intent_tail = tail
                break

    if intent_tail:
        args.intent = " ".join([str(args.intent).strip(), *intent_tail]).strip()
        print(
            "warning: recovered unquoted --intent trailing words; quote free-text values or prefer --submit-spec-json",
            file=sys.stderr,
        )
        return args

    parser.error("unrecognized arguments: " + " ".join(unknown))
    raise AssertionError("argparse parser.error should exit")


def main() -> int:
    parser = build_parser()
    args = parse_args_with_unquoted_intent_recovery(parser)
    active_chain_lock = None

    try:
        if args.timeout_seconds <= 0:
            parser.error("timeout-seconds must be > 0")
        if args.poll_seconds <= 0:
            parser.error("poll-seconds must be > 0")
        if args.max_agent_retries < 0:
            parser.error("max-agent-retries must be >= 0")
        if args.recovery_plan_timeout_seconds <= 0:
            parser.error("recovery-plan-timeout-seconds must be > 0")
        if args.measurement_plan_timeout_seconds <= 0:
            parser.error("measurement-plan-timeout-seconds must be > 0")
        if args.job_advisory_timeout_seconds <= 0:
            parser.error("job-advisory-timeout-seconds must be > 0")

        try:
            queue_root = normalize_path(args.queue_root, DEFAULT_QUEUE_ROOT)
            simulation_queue_root = normalize_path(args.simulation_queue_root, DEFAULT_SIMULATION_QUEUE_ROOT)
            catalog_path = normalize_path(args.catalog, DEFAULT_CATALOG_PATH)
            manifest_root = normalize_path(args.manifest_root, DEFAULT_MANIFEST_ROOT)
            simulation_manifest_root = normalize_path(args.simulation_manifest_root, DEFAULT_SIMULATION_MANIFEST_ROOT)
            seed_registry_path = normalize_path(args.seed_registry_path, DEFAULT_NV_SEED_REGISTRY_PATH)
            catalog = expand_catalog_with_manifests(load_catalog(catalog_path), manifest_root)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2

        try:
            provided_submit_spec = parse_submit_spec_json(args.submit_spec_json) if args.submit_spec_json else {}
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        try:
            provided_sequence_authoring = parse_sequence_authoring_json(args.sequence_authoring_json) if args.sequence_authoring_json else {}
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2
        submit_mode = str(provided_submit_spec.get("mode", "") or "").strip().lower()
        if submit_mode in {"validate", "dry_run", "execute", "simulate"}:
            args.mode = submit_mode

        if args.list_sequences:
            print(json.dumps(list_sequences(catalog, manifest_root), ensure_ascii=False))
            return 0

        if args.mode == "simulate":
            try:
                sequence_name, entry, simulation_manifest_info = resolve_simulation_entry(
                    catalog,
                    args,
                    provided_submit_spec,
                    simulation_manifest_root,
                )
                simulation_job = build_simulation_job_from_submit_spec(
                    args,
                    provided_submit_spec,
                    sequence_name,
                    entry,
                    simulation_manifest_info,
                )
            except ValueError as exc:
                response = build_error_response("SIMULATION_SUBMIT_SPEC_FAILED", str(exc), args=args)
                response["queue_root"] = str(simulation_queue_root)
                response["simulation_manifest_root"] = str(simulation_manifest_root)
                print(json.dumps(response, ensure_ascii=False))
                return 2

            ensure_dirs(simulation_queue_root)
            wrapper_response, wrapper_runner = invoke_matlab_wrapper_submit_simulation_job(
                simulation_job,
                args,
                manifest_root,
                simulation_queue_root,
                enqueue=not args.preview_job_advisory_only,
            )

            response_job_id = str(wrapper_response.get("job_id", "") or simulation_job.get("job_id", ""))
            response_queued_dir = simulation_queue_root / "queued" / response_job_id if response_job_id else Path()
            response = {
                "ok": bool(wrapper_response.get("ok", False)),
                "mode": "simulate",
                "sequence": sequence_name,
                "simulation_manifest_id": str(simulation_job.get("simulation_manifest_id", "")),
                "simulation_manifest_path": str(simulation_manifest_info.get("path", "") or ""),
                "job_id": response_job_id,
                "job_dir": str(response_queued_dir) if response_job_id and not args.preview_job_advisory_only else "",
                "job_path": str(response_queued_dir / "job.json") if response_job_id and not args.preview_job_advisory_only else "",
                "queue_root": str(simulation_queue_root),
                "simulation_queue_root": str(simulation_queue_root),
                "wait_for_result": bool(args.wait_for_result),
                "preview_only": bool(args.preview_job_advisory_only),
                "submit_spec": copy.deepcopy(provided_submit_spec),
                "job": copy.deepcopy(wrapper_response.get("job", simulation_job)),
                "submission_path": resolve_submission_path(args),
                "matlab_wrapper": wrapper_runner,
            }
            if wrapper_response.get("error_code"):
                response["error_code"] = str(wrapper_response.get("error_code", "") or "")
            if wrapper_response.get("error_message"):
                response["error_message"] = str(wrapper_response.get("error_message", "") or "")

            if not response["ok"] or args.preview_job_advisory_only:
                print(json.dumps(response, ensure_ascii=False))
                return 0 if response["ok"] else 6

            if args.wait_for_result and bool(args.simulation_inline_process):
                worker_response, worker_runner = invoke_matlab_wrapper_process_next_simulation_job(
                    args,
                    manifest_root,
                    simulation_queue_root,
                )
                response["simulation_worker"] = worker_response
                response["simulation_worker_runner"] = worker_runner
                if not isinstance(worker_response, dict) or not worker_response.get("ok", False):
                    response["ok"] = False
                    if isinstance(worker_response, dict):
                        worker_error_code = str(worker_response.get("error_code", "") or "SIMULATION_WORKER_FAILED")
                        worker_error_message = str(worker_response.get("error_message", "") or "Simulation worker failed.")
                    else:
                        worker_error_code = "SIMULATION_WORKER_FAILED"
                        worker_error_message = "Simulation worker failed."
                    response.setdefault("error_code", worker_error_code)
                    response.setdefault("error_message", worker_error_message)
                    print(json.dumps(response, ensure_ascii=False))
                    return 6

            if args.wait_for_result:
                wait_response = wait_for_result(
                    simulation_queue_root,
                    str(response["job_id"]),
                    args.timeout_seconds,
                    args.poll_seconds,
                    job=response.get("job", simulation_job),
                    runtime_watch_config={"enabled": False},
                )
                response.update(wait_response)

            print(json.dumps(response, ensure_ascii=False))
            return 0

        sequence_authoring_context: dict = {}
        if provided_sequence_authoring:
            try:
                sequence_authoring_context = materialize_direct_sequence_authoring(
                    raw_payload=provided_sequence_authoring,
                    manifest_root=manifest_root,
                    default_sample_id=str(provided_submit_spec.get("sample_id", "") or args.sample_id or "NV23"),
                    authoring_hint=str(
                        provided_sequence_authoring.get("new_id", "")
                        or provided_submit_spec.get("sequence_manifest_id", "")
                        or provided_submit_spec.get("sequence", "")
                        or args.sequence_manifest_id
                        or args.sequence
                        or args.job_id_suffix
                        or "sequence_authoring"
                    ),
                )
            except ValueError as exc:
                response = build_error_response(
                    "SEQUENCE_AUTHORING_FAILED",
                    str(exc),
                    args=args,
                    sequence_name=str(
                        provided_sequence_authoring.get("new_id", "")
                        or provided_submit_spec.get("sequence", "")
                        or args.sequence
                    ),
                )
                attach_sequence_authoring_response_fields(
                    response,
                    {"sequence_authoring": copy.deepcopy(provided_sequence_authoring)},
                )
                print(json.dumps(response, ensure_ascii=False))
                return 2

        try:
            authored_manifest_id = str(sequence_authoring_context.get("sequence_manifest_id", "") or "").strip()
            submit_manifest_id = authored_manifest_id or str(provided_submit_spec.get("sequence_manifest_id", "") or "").strip()
            submit_sequence = str(provided_submit_spec.get("sequence", "") or "").strip()
            if submit_manifest_id:
                manifest_info = load_manifest(manifest_root, submit_manifest_id)
                sequence_name, entry = synthesize_entry_from_manifest(submit_manifest_id, manifest_info)
            elif args.sequence_manifest_id:
                manifest_info = load_manifest(manifest_root, args.sequence_manifest_id)
                sequence_name, entry = synthesize_entry_from_manifest(args.sequence_manifest_id, manifest_info)
            else:
                sequence_request = submit_sequence or args.sequence or catalog.get("default_sequence", "")
                if not sequence_request:
                    print("No sequence selected and the catalog has no default_sequence.", file=sys.stderr)
                    return 2
                sequence_name, entry = resolve_sequence(catalog, sequence_request)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2

        ensure_dirs(queue_root)

        if args.skip_measurement_plan and not internal_measurement_plan_submit_allowed():
            response = build_error_response(
                "MEASUREMENT_PLAN_BYPASS_FORBIDDEN",
                "Direct execute bypass is reserved for the internal batch runner. Re-run without --skip-measurement-plan.",
                args=args,
                sequence_name=sequence_name,
            )
            print(json.dumps(response, ensure_ascii=False))
            return 6

        if args.mode == "execute" and not args.skip_measurement_plan and not args.preview_job_advisory_only and not args.wait_for_result:
            response = build_error_response(
                "MEASUREMENT_PLAN_REQUIRED",
                "External execute submissions must use --wait-for-result so the managed single-item batch path can run validation and advisories before queueing.",
                args=args,
                sequence_name=sequence_name,
            )
            print(json.dumps(response, ensure_ascii=False))
            return 6

        use_single_item_measurement_plan = (
            args.mode == "execute"
            and args.wait_for_result
            and not args.skip_measurement_plan
            and not args.preview_job_advisory_only
        )

        job_id_prefix = args.job_id_prefix or entry.get("job_id_prefix") or f"nv23_{sequence_name}"
        job_id = build_job_id(job_id_prefix, args.job_id_suffix or None)
        try:
            if provided_submit_spec:
                submit_spec = apply_submit_spec_cli_fallbacks(
                    provided_submit_spec,
                    args,
                    sequence_name,
                    entry,
                    job_id,
                    sequence_manifest_id_override=str(sequence_authoring_context.get("sequence_manifest_id", "") or ""),
                )
            else:
                submit_spec = build_job(
                    args,
                    job_id,
                    sequence_name,
                    entry,
                    manifest_root,
                    seed_registry_path,
                    sequence_manifest_id_override=str(sequence_authoring_context.get("sequence_manifest_id", "") or ""),
                )
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 2

        if use_single_item_measurement_plan:
            returncode, response, _batch_stdout, batch_stderr = run_single_item_via_batch_runner(
                args,
                sequence_name,
                entry,
                submit_spec=submit_spec,
                sequence_authoring_context=sequence_authoring_context,
            )
            if batch_stderr:
                sys.stderr.write(batch_stderr)
            print(json.dumps(response, ensure_ascii=False))
            return returncode

        wrapper_response, wrapper_runner = invoke_matlab_wrapper_submit_spec(
            submit_spec,
            args,
            manifest_root,
            queue_root,
            include_job_advisory=(args.include_job_advisory or args.preview_job_advisory_only),
            enqueue=not args.preview_job_advisory_only,
        )

        if args.preview_job_advisory_only:
            preview_response = {
                "ok": bool(wrapper_response.get("ok", False)),
                "preview_only": True,
                "mode": args.mode,
                "sequence": sequence_name,
                "job_id": str(wrapper_response.get("job_id", "") or job_id),
                "queue_root": str(queue_root),
                "submit_spec": copy.deepcopy(submit_spec),
                "job": copy.deepcopy(wrapper_response.get("job", {})),
                "validation": copy.deepcopy(wrapper_response.get("validation", {})),
                "job_advisory": copy.deepcopy(wrapper_response.get("job_advisory", {})),
                "matlab_wrapper": wrapper_runner,
            }
            if wrapper_response.get("error_code"):
                preview_response["error_code"] = str(wrapper_response.get("error_code", "") or "")
            if wrapper_response.get("error_message"):
                preview_response["error_message"] = str(wrapper_response.get("error_message", "") or "")
            attach_sequence_authoring_response_fields(preview_response, sequence_authoring_context)
            print(json.dumps(preview_response, ensure_ascii=False))
            wrapper_error_code = str(wrapper_response.get("error_code", "") or "")
            if wrapper_error_code.startswith("MATLAB_WRAPPER_"):
                return 4
            return 0

        if not isinstance(wrapper_response, dict) or not wrapper_response.get("ok", False):
            error_response = copy.deepcopy(wrapper_response if isinstance(wrapper_response, dict) else {})
            if not error_response:
                error_response = build_error_response(
                    "MATLAB_WRAPPER_SUBMIT_FAILED",
                    "MATLAB wrapper submit failed without a structured response.",
                    args=args,
                    sequence_name=sequence_name,
                )
            error_response["mode"] = str(error_response.get("mode", "") or args.mode)
            error_response["sequence"] = str(error_response.get("sequence", "") or sequence_name)
            error_response["job_id"] = str(error_response.get("job_id", "") or job_id)
            error_response["queue_root"] = str(queue_root)
            error_response["submit_spec"] = copy.deepcopy(submit_spec)
            error_response["job"] = copy.deepcopy(error_response.get("job", {}))
            error_response["submission_path"] = resolve_submission_path(args)
            error_metadata = error_response.get("job", {}).get("metadata", {}) if isinstance(error_response.get("job", {}), dict) else {}
            error_response["measurement_plan_verified"] = bool(
                (error_metadata.get("measurement_plan_verified", False) if isinstance(error_metadata, dict) else False)
                or submit_spec.get("measurement_plan_verified", False)
            )
            error_response["matlab_wrapper"] = wrapper_runner
            attach_sequence_authoring_response_fields(error_response, sequence_authoring_context)
            print(json.dumps(error_response, ensure_ascii=False))
            wrapper_error_code = str(error_response.get("error_code", "") or "")
            if wrapper_error_code.startswith("MATLAB_WRAPPER_"):
                return 4
            return 6

        job = copy.deepcopy(wrapper_response.get("job", {}))
        job_id = str(wrapper_response.get("job_id", "") or job_id)
        job_advisory = annotate_runtime_estimate_context(copy.deepcopy(wrapper_response.get("job_advisory", {})))
        job_advisory_runner = wrapper_runner

        if args.mode == "execute" and args.wait_for_result and args.agent_recovery:
            lock_payload = {
                "job_id": job_id,
                "sequence": sequence_name,
                "sample_id": str(job.get("sample_id", "") or ""),
                "requested_by": str(job.get("metadata", {}).get("requested_by", "") or ""),
                "pid": os.getpid(),
                "started_at": _safe_now_iso(),
            }
            try:
                active_chain_lock = acquire_active_recovery_chain_lock(
                    normalize_path(str(DEFAULT_ACTIVE_RECOVERY_CHAIN_LOCK_PATH), DEFAULT_ACTIVE_RECOVERY_CHAIN_LOCK_PATH),
                    lock_payload,
                    float(args.active_chain_wait_seconds),
                    float(args.poll_seconds),
                )
            except RuntimeError as exc:
                print(str(exc), file=sys.stderr)
                return 5

        enqueue_info = copy.deepcopy(wrapper_response.get("queued", {}))

        response = {
            "ok": True,
            "mode": args.mode,
            "sequence": sequence_name,
            "job_id": job_id,
            "job_dir": str(enqueue_info.get("job_dir", "") or wrapper_response.get("job_dir", "") or ""),
            "job_path": str(enqueue_info.get("job_path", "") or wrapper_response.get("job_path", "") or ""),
            "queue_root": str(queue_root),
            "wait_for_result": args.wait_for_result,
            "submit_spec": submit_spec,
            "job": job,
            "submission_path": resolve_submission_path(args),
            "measurement_plan_verified": bool(
                ((job.get("metadata", {}) if isinstance(job.get("metadata"), dict) else {}).get("measurement_plan_verified", False))
                or submit_spec.get("measurement_plan_verified", False)
            ),
            "validation": copy.deepcopy(wrapper_response.get("validation", {})),
            "matlab_wrapper": wrapper_runner,
        }
        attach_sequence_authoring_response_fields(response, sequence_authoring_context)
        if args.include_job_advisory:
            response["job_advisory"] = job_advisory
            response["job_advisory_runner"] = job_advisory_runner
        runtime_estimate_context = job_advisory.get("runtime_estimate_context", {}) if isinstance(job_advisory, dict) else {}
        if isinstance(runtime_estimate_context, dict) and runtime_estimate_context:
            response["runtime_estimate_context"] = copy.deepcopy(runtime_estimate_context)

        if args.wait_for_result:
            initial_wait = wait_for_result(
                queue_root,
                job_id,
                args.timeout_seconds,
                args.poll_seconds,
                job=job,
                runtime_watch_config=build_runtime_watch_config(args, job),
            )
            final_wait = copy.deepcopy(initial_wait)
            final_job = copy.deepcopy(job)
            recovery_rounds: list[dict] = []

            if args.agent_recovery and args.mode == "execute":
                current_job = copy.deepcopy(job)
                current_wait = copy.deepcopy(initial_wait)
                for retry_round in range(1, int(args.max_agent_retries) + 1):
                    recovery = maybe_run_agent_recovery(args, queue_root, manifest_root, current_job, current_wait, retry_round)
                    if not recovery.get("attempted") and recovery.get("reason") == "not_eligible":
                        break
                    if recovery.get("attempted") or recovery.get("reason"):
                        recovery_rounds.append(
                            {
                                "attempted": bool(recovery.get("attempted", False)),
                                "eligible": bool(recovery.get("eligible", False)),
                                "reason": str(recovery.get("reason", "") or ""),
                                "request_path": str(recovery.get("request_path", "") or ""),
                                "plan_path": str(recovery.get("plan_path", "") or ""),
                                "plan": copy.deepcopy(recovery.get("plan", {})),
                                "retry_job_id": str(recovery.get("retry_job_id", "") or ""),
                                "retry_final_state": str(recovery.get("retry_response", {}).get("final_state", "") or ""),
                                "retry_result_path": str(recovery.get("retry_response", {}).get("result_path", "") or ""),
                                "retry_outcome_summary": copy.deepcopy(recovery.get("retry_response", {}).get("outcome_summary", {})),
                                "retry_runtime_watch": copy.deepcopy(recovery.get("retry_response", {}).get("runtime_watch", {})),
                            }
                        )
                    retry_response = recovery.get("retry_response", {})
                    if not isinstance(retry_response, dict) or not retry_response:
                        break
                    final_wait = copy.deepcopy(retry_response)
                    final_job = copy.deepcopy(recovery.get("retry_job", current_job))
                    current_job = copy.deepcopy(final_job)
                    current_wait = copy.deepcopy(final_wait)
                    if not should_request_agent_recovery(current_job, current_wait):
                        break

            if recovery_rounds:
                response["initial_attempt"] = copy.deepcopy(initial_wait)
                response["agent_recovery"] = {
                    "attempted": True,
                    "rounds": recovery_rounds,
                }
                response["job_id"] = str(final_job.get("job_id", "") or response["job_id"])
                response["job"] = final_job
            response.update(final_wait)

        print(json.dumps(response, ensure_ascii=False))
        return 0
    finally:
        if active_chain_lock is not None:
            try:
                active_chain_lock.close()
            except Exception:
                pass


if __name__ == "__main__":
    raise SystemExit("Direct execution of this execution-source file is disabled in the public release.")
