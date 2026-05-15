#!/usr/bin/env python3
import copy
import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path

WORKSPACE_ROOT = Path(os.environ.get("OPENCLAW_WORKSPACE_ROOT", ".")).expanduser()
DEFAULT_REQUEST_ROOT = WORKSPACE_ROOT / ".openclaw" / "matlab_bridge_requests"
DEFAULT_TIMEOUT_SECONDS = 300.0
WINDOWS_DRIVE_PATH_RE = re.compile(r"^(?P<drive>[A-Za-z]):[\\/](?P<rest>.*)$")


def slug(text: str) -> str:
    text = (text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"^_+|_+$", "", text)
    return text or "request"


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
    unc_host = "wsl.localhost"
    return f"\\\\{unc_host}\\{distro}{unc_tail}"


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


def resolve_c23_root(manifest_root: Path) -> Path:
    c23_root = Path(manifest_root).resolve()
    if c23_root.name == "sequence_manifests":
        c23_root = c23_root.parent.parent
    elif c23_root.name == "claw":
        c23_root = c23_root.parent
    if not (c23_root / "claw").is_dir():
        raise FileNotFoundError(f"Could not resolve 23-C root from manifest root: {manifest_root}")
    return c23_root


def wrapper_failure_response(error_code: str, message: str) -> dict:
    return {
        "ok": False,
        "action": "",
        "error_code": str(error_code or ""),
        "error_message": str(message or ""),
        "job_id": "",
        "job_dir": "",
        "job_path": "",
        "job": {},
        "validation": {
            "ok": False,
            "error_code": str(error_code or ""),
            "error_message": str(message or ""),
        },
        "job_advisory": {},
        "queued": {},
        "worker": {},
        "queue_root": "",
        "queue_root_source": "",
        "notes": [str(message or "")] if message else [],
        "warnings": [],
    }


def run_matlab_wrapper_request(
    request: dict,
    *,
    c23_root: Path,
    queue_root: Path,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    request_root: Path = DEFAULT_REQUEST_ROOT,
) -> tuple[dict, dict]:
    request_root.mkdir(parents=True, exist_ok=True)
    request_dir = Path(
        tempfile.mkdtemp(
            prefix=f"{slug(str(request.get('action', '') or 'request'))}_{datetime.now().strftime('%Y%m%d_%H%M%S_')}",
            dir=str(request_root),
        )
    )
    request_json_path = request_dir / "request.json"
    response_json_path = request_dir / "response.json"
    runner_path = request_dir / "run_matlab_wrapper.m"
    write_json_atomic(request_json_path, request)

    c23_root_windows = windows_path_for_matlab(c23_root)
    queue_root_windows = windows_path_for_matlab(Path(queue_root))
    request_json_windows = windows_path_for_matlab(request_json_path)
    response_json_windows = windows_path_for_matlab(response_json_path)
    runner_windows = windows_path_for_matlab(runner_path)
    init_dir_windows = windows_path_for_matlab(c23_root / "Initialization" / "NV1")
    image_dir_windows = windows_path_for_matlab(c23_root / "SavedImages")
    exp_dir_windows = windows_path_for_matlab(c23_root / "savedexperiments" / "NV1")
    sequence_dir_windows = windows_path_for_matlab(c23_root / "SavedSequences" / "SavedSequences-AWG")

    runner_code = "\n".join(
        [
            f"c23Root = '{matlab_literal(c23_root_windows)}';",
            f"queueRoot = '{matlab_literal(queue_root_windows)}';",
            f"requestPath = '{matlab_literal(request_json_windows)}';",
            f"responsePath = '{matlab_literal(response_json_windows)}';",
            f"initDir = '{matlab_literal(init_dir_windows)}';",
            f"imageDir = '{matlab_literal(image_dir_windows)}';",
            f"expDir = '{matlab_literal(exp_dir_windows)}';",
            f"sequenceDir = '{matlab_literal(sequence_dir_windows)}';",
            "setenv('NV_BRIDGE_ROOT', queueRoot);",
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
            "try",
            "    claw_wrapper_run_json(requestPath, responsePath);",
            "catch ME",
            "    response = struct();",
            "    response.ok = false;",
            "    response.action = '';",
            "    response.error_code = char(ME.identifier);",
            "    response.error_message = char(ME.message);",
            "    response.job_id = '';",
            "    response.job_dir = '';",
            "    response.job_path = '';",
            "    response.job = struct();",
            "    response.validation = struct('ok', false, 'error_code', char(ME.identifier), 'error_message', char(ME.message));",
            "    response.job_advisory = struct();",
            "    response.queued = struct();",
            "    response.worker = struct();",
            "    response.queue_root = queueRoot;",
            "    response.queue_root_source = 'env';",
            "    response.notes = {sprintf('MATLAB wrapper runner failed: %s', char(ME.message))};",
            "    response.warnings = {};",
            "    fid = fopen(responsePath, 'w');",
            "    if fid >= 0",
            "        cleanupObj = onCleanup(@() fclose(fid)); %#ok<NASGU>",
            "        fprintf(fid, '%s', jsonencode(response));",
            "    end",
            "end",
        ]
    )
    runner_path.write_text(runner_code + "\n", encoding="utf-8")

    runner_info = {
        "request_dir": str(request_dir),
        "request_json_path": str(request_json_path),
        "response_json_path": str(response_json_path),
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
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            env=os.environ.copy(),
            timeout=float(timeout_seconds),
        )
        runner_info["returncode"] = int(completed.returncode)
        runner_info["stdout"] = completed.stdout
        runner_info["stderr"] = completed.stderr
    except subprocess.TimeoutExpired as exc:
        runner_info["timed_out"] = True
        runner_info["stdout"] = exc.stdout or ""
        runner_info["stderr"] = exc.stderr or ""
        return (
            wrapper_failure_response(
                "MATLAB_WRAPPER_TIMEOUT",
                f"Timed out while waiting for MATLAB wrapper after {float(timeout_seconds):.1f} s.",
            ),
            runner_info,
        )
    except FileNotFoundError as exc:
        runner_info["stderr"] = str(exc)
        return (
            wrapper_failure_response(
                "MATLAB_WRAPPER_LAUNCH_FAILED",
                f"Failed to launch MATLAB wrapper command: {exc}",
            ),
            runner_info,
        )
    except Exception as exc:
        runner_info["stderr"] = str(exc)
        return (
            wrapper_failure_response(
                "MATLAB_WRAPPER_FAILED",
                f"Unexpected MATLAB wrapper failure: {exc}",
            ),
            runner_info,
        )

    if not response_json_path.is_file():
        message = "MATLAB wrapper did not produce a response JSON file."
        if runner_info["stderr"]:
            message = f"{message} STDERR: {runner_info['stderr'].strip()}"
        return wrapper_failure_response("MATLAB_WRAPPER_NO_OUTPUT", message), runner_info

    try:
        response = read_json(response_json_path)
    except Exception as exc:
        return wrapper_failure_response("MATLAB_WRAPPER_INVALID_JSON", f"Failed to parse wrapper response JSON: {exc}"), runner_info

    if not isinstance(response, dict):
        return wrapper_failure_response("MATLAB_WRAPPER_INVALID_PAYLOAD", "MATLAB wrapper returned a non-dictionary payload."), runner_info

    if runner_info["returncode"] != 0 and not response.get("ok", False):
        response.setdefault("error_code", "MATLAB_WRAPPER_RETURNED_ERROR")
        response.setdefault(
            "error_message",
            runner_info["stderr"].strip() or "MATLAB returned a non-zero exit code while running the wrapper.",
        )
    return response, runner_info


def execute_enqueue_requests_advisory(payload: dict, enqueue: bool) -> bool:
    if not enqueue or not isinstance(payload, dict):
        return False
    mode = str(payload.get("mode", "") or "").strip().lower()
    return mode == "execute"


def submit_job_via_matlab_wrapper(
    job: dict,
    *,
    manifest_root: Path,
    queue_root: Path,
    include_job_advisory: bool = False,
    enqueue: bool = True,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    job_advisory_opts: dict | None = None,
) -> tuple[dict, dict]:
    job_payload = copy.deepcopy(job if isinstance(job, dict) else {})
    effective_include_job_advisory = bool(include_job_advisory) or execute_enqueue_requests_advisory(job_payload, enqueue)
    request = {
        "action": "submit_job",
        "job": job_payload,
        "options": {
            "include_job_advisory": effective_include_job_advisory,
            "enqueue": bool(enqueue),
        },
    }
    if isinstance(job_advisory_opts, dict) and job_advisory_opts:
        request["options"]["job_advisory_opts"] = copy.deepcopy(job_advisory_opts)
    return run_matlab_wrapper_request(
        request,
        c23_root=resolve_c23_root(Path(manifest_root)),
        queue_root=Path(queue_root),
        timeout_seconds=timeout_seconds,
    )


def submit_spec_via_matlab_wrapper(
    spec: dict,
    *,
    manifest_root: Path,
    queue_root: Path,
    include_job_advisory: bool = False,
    enqueue: bool = True,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    job_advisory_opts: dict | None = None,
) -> tuple[dict, dict]:
    spec_payload = copy.deepcopy(spec if isinstance(spec, dict) else {})
    effective_include_job_advisory = bool(include_job_advisory) or execute_enqueue_requests_advisory(spec_payload, enqueue)
    request = {
        "action": "submit_spec",
        "spec": spec_payload,
        "options": {
            "include_job_advisory": effective_include_job_advisory,
            "enqueue": bool(enqueue),
        },
    }
    if isinstance(job_advisory_opts, dict) and job_advisory_opts:
        request["options"]["job_advisory_opts"] = copy.deepcopy(job_advisory_opts)
    return run_matlab_wrapper_request(
        request,
        c23_root=resolve_c23_root(Path(manifest_root)),
        queue_root=Path(queue_root),
        timeout_seconds=timeout_seconds,
    )


def submit_simulation_job_via_matlab_wrapper(
    job: dict,
    *,
    manifest_root: Path,
    queue_root: Path,
    enqueue: bool = True,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
) -> tuple[dict, dict]:
    request = {
        "action": "submit_simulation_job",
        "job": copy.deepcopy(job if isinstance(job, dict) else {}),
        "options": {
            "enqueue": bool(enqueue),
            "queue_root": windows_path_for_matlab(Path(queue_root)),
        },
    }
    return run_matlab_wrapper_request(
        request,
        c23_root=resolve_c23_root(Path(manifest_root)),
        queue_root=Path(queue_root),
        timeout_seconds=timeout_seconds,
    )


def process_next_simulation_job_via_matlab_wrapper(
    *,
    manifest_root: Path,
    queue_root: Path,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
) -> tuple[dict, dict]:
    request = {
        "action": "process_next_simulation_job",
        "options": {
            "queue_root": windows_path_for_matlab(Path(queue_root)),
            "process_opts": {},
        },
    }
    return run_matlab_wrapper_request(
        request,
        c23_root=resolve_c23_root(Path(manifest_root)),
        queue_root=Path(queue_root),
        timeout_seconds=timeout_seconds,
    )
