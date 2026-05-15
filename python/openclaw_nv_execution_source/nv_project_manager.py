#!/usr/bin/env python3
"""Durable project-state helper for long-running NV autonomy.

The on-disk schema, paths, and human-facing text now use project terminology.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

WORKSPACE_ROOT = Path("<OPENCLAW_WORKSPACE>")
NV_RESEARCH_MEMORY_PATH = WORKSPACE_ROOT / "NV_RESEARCH_MEMORY.md"
NV_RESEARCH_KNOWLEDGE_PATH = WORKSPACE_ROOT / "NV_RESEARCH_KNOWLEDGE.md"
PROJECT_ROOT = WORKSPACE_ROOT / ".openclaw" / "projects"
CRON_STATE_ROOT = WORKSPACE_ROOT / ".openclaw" / "project_cron"
DEFAULT_CONFIG_PATH = Path("<OPENCLAW_CONFIG>")
DEFAULT_OPENCLAW_CLI_PATH = Path("<OPENCLAW_CLI>")
DEFAULT_TELEGRAM_MEDIA_OUTBOUND_DIR = Path("<OPENCLAW_MEDIA_OUTBOUND>")
DEFAULT_BRIDGE_ROOT = Path("<NV_BRIDGE_ROOT>")
DEFAULT_SAMPLE_ID = "NV23"
DEFAULT_RESEARCH_AGENT_ID = "nv-researcher"
PROJECT_STRUCTURE_VERSION = "simple_research_state_v1"
PROJECT_INTERNAL_DIRNAME = ".manager"
PROJECT_WORK_DIRNAME = "work"
PROJECT_ARTIFACTS_DIRNAME = "work/artifacts"
PROJECT_BRIDGE_JOBS_DIRNAME = "work/bridge_jobs"
RESEARCH_STATE_FILENAME = "work/state.md"
RESEARCH_AGENDA_FILENAME = "work/state.md"
EVIDENCE_INDEX_FILENAME = ".manager/evidence.jsonl"
STATE_FILENAME = ".manager/state.json"
BACKLOG_FILENAME = ".manager/backlog.json"
LEDGER_FILENAME = ".manager/ledger.jsonl"
LAB_LOG_FILENAME = "log.md"
WAKE_RECORD_SCHEMA_VERSION = 1
WAKE_RECORD_TEXT_SNAPSHOT_MAX_BYTES = int(os.environ.get("OPENCLAW_WAKE_RECORD_TEXT_SNAPSHOT_MAX_BYTES", "2000000"))
WAKE_RECORD_SKILL_PATH = WORKSPACE_ROOT / "skills" / "nv-project-manager" / "SKILL.md"
WAKE_REPLAY_EVALUATION_ROOT = WORKSPACE_ROOT / ".openclaw" / "evaluations" / "wake_replays"
DEFAULT_PULSED_ODMR_RESONANCE_EVIDENCE_VALID_MINUTES = 300
DEFAULT_DAYTIME_MAX_UNTRACKED_WINDOW_SECONDS = 600
DEFAULT_NIGHTTIME_MAX_UNTRACKED_WINDOW_SECONDS = 900
DEFAULT_DAYTIME_START_HOUR_LOCAL = 9
DEFAULT_NIGHTTIME_START_HOUR_LOCAL = 21
DEFAULT_CALIBRATION_TOTAL_SHOTS_MIN = 200_000
DEFAULT_CALIBRATION_TOTAL_SHOTS_MAX = 300_000
DEFAULT_PUBLICATION_QUALITY_MIN_TOTAL_SHOTS = 1_500_000
DEFAULT_PUBLICATION_QUALITY_TARGET_SEM_NORMALIZED_SIGNAL = 0.05
NV_RESEARCH_MEMORY_SNAPSHOT_MAX_CHARS = 16_000
VALID_PHYSICAL_RESULT_STATUSES = {
    "completed",
    "failed",
    "declined",
    "unsafe",
    "needs_clarification",
}
VALID_CODE_CHANGE_RESULT_STATUSES = {
    "completed",
    "failed",
    "declined",
    "needs_review",
    "needs_verification",
    "unsafe",
}
VALID_CODE_CHANGE_CLASSES = {
    "sequence_staging",
    "analysis_code",
    "bridge_wrapper",
    "instrument_driver",
    "legacy_gui",
    "safety_policy",
}
ACTIVE_PROJECT_LIFECYCLES = {
    "active",
    "running",
}
PAUSED_PROJECT_LIFECYCLES = {
    "paused",
}
INBOX_AUTO_ACTIVATE_PROJECT_LIFECYCLES = {
    "complete",
    "completed",
    "disabled",
    "paused",
    "stopped",
}
INACTIVE_PROJECT_LIFECYCLES = {
    "archived",
    "canceled",
    "cancelled",
    "complete",
    "completed",
    "disabled",
    "paused",
    "stopped",
}
PAUSED_PROJECT_STATUSES = PAUSED_PROJECT_LIFECYCLES
SCOPED_CODE_CHANGE_CLASSES = {
    "bridge_wrapper",
    "instrument_driver",
    "legacy_gui",
    "safety_policy",
}
VALID_BACKLOG_STATUSES = {
    "pending",
    "in_progress",
    "completed",
    "blocked",
    "failed",
    "canceled",
}
COARSE_BACKLOG_KINDS = {
    "research_task",
    "external_request",
    "blocker",
}
LEGACY_BACKLOG_KIND_MAP = {
    "analyze_evidence": "research_task",
    "build_batch": "research_task",
    "author_staging_sequence": "research_task",
    "submit_validate": "research_task",
    "submit_dry_run": "research_task",
    "submit_execute": "research_task",
    "review_code_change": "research_task",
    "write_procurement_proposal": "research_task",
    "request_physical_action": "external_request",
    "wait_for_physical_action": "external_request",
    "request_code_change": "external_request",
    "wait_for_code_change": "external_request",
    "wait_for_approval": "blocker",
    "stop_for_safety": "blocker",
}
BLOCKED_STATUSES = {
    "blocked",
    "blocked_external",
    "blocked_code",
    "blocked_physical_action",
    "blocked_code_change",
    "blocked_procurement",
    "waiting_approval",
}
VALID_ADVICE_DISPOSITIONS = {
    "processed",
    "superseded",
    "deferred",
}
VALID_ADVICE_CLASSIFICATIONS = {
    "hard_constraint",
    "preference",
    "observation",
    "approval",
    "correction",
    "hypothesis",
    "rejection",
    "note",
}
VALID_EVIDENCE_CATEGORIES = {
    "analysis",
    "artifact",
    "bridge_result",
    "calibration",
    "claim",
    "comparison",
    "figure",
    "human_guidance",
    "literature",
    "measurement",
    "note",
    "report",
    "simulation",
}
VALID_EXPERIMENT_INTENT_TERMINAL_STATUSES = {
    "completed",
    "canceled",
    "failed",
    "superseded",
}

def now_iso() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

def slug(text: str) -> str:
    value = str(text or "").strip().lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "project"

def project_lifecycle(project: dict[str, Any]) -> str:
    return str(project.get("project_lifecycle", "") or project.get("status", "") or "active").strip().lower()

def operational_state(state: dict[str, Any]) -> str:
    return str(state.get("operational_state", "") or state.get("status", "") or "active").strip().lower()

def set_project_lifecycle(project: dict[str, Any], lifecycle: str) -> None:
    value = str(lifecycle or "active").strip().lower()
    project["project_lifecycle"] = value
    project["status"] = value

def set_operational_state(state: dict[str, Any], state_value: str) -> None:
    value = str(state_value or "active").strip().lower()
    state["operational_state"] = value
    state["status"] = value

def sync_project_lifecycle_alias(project: dict[str, Any]) -> dict[str, Any]:
    lifecycle = project_lifecycle(project)
    if "project_lifecycle" not in project:
        project["project_lifecycle"] = lifecycle
    if "status" not in project:
        project["status"] = lifecycle
    return project

def sync_operational_state_alias(state: dict[str, Any]) -> dict[str, Any]:
    state_value = operational_state(state)
    if "operational_state" not in state:
        state["operational_state"] = state_value
    if "status" not in state:
        state["status"] = state_value
    return state

def normalize_backlog_kind(item: dict[str, Any]) -> str:
    """Keep backlog task routing coarse, normalizing stale labels if encountered."""
    raw_kind = str(item.get("kind", "") or "").strip()
    kind = raw_kind.lower()
    if not kind:
        return "research_task"
    if kind in COARSE_BACKLOG_KINDS:
        return kind
    normalized = LEGACY_BACKLOG_KIND_MAP.get(kind, "research_task")
    item["kind_normalized"] = True
    if kind == "wait_for_approval":
        item.setdefault("blocker_type", "approval")
    elif kind == "stop_for_safety":
        item.setdefault("blocker_type", "safety")
    elif normalized == "external_request":
        item.setdefault("request_kind", kind)
    return normalized

def read_json(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    if raw.startswith("\ufeff"):
        raw = raw[1:]
    payload = json.loads(raw)
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object.")
    return payload

def read_json_arg(value: str) -> dict[str, Any]:
    text = str(value or "").strip()
    if not text:
        return {}
    if text.startswith("@"):
        return read_json(Path(text[1:]).expanduser())
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Could not parse JSON argument: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("JSON argument must be an object.")
    return payload

def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def append_jsonl(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n")

def read_json_safely(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        payload = read_json(path)
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}

def path_is_inside(child: Path, parent: Path) -> bool:
    try:
        child.resolve(strict=False).relative_to(parent.resolve(strict=False))
        return True
    except Exception:
        return False

def terminal_evidence_payload(event: dict[str, Any]) -> bool:
    event_name = str(event.get("event", "") or "").strip()
    if event_name == "result_event_terminal_evidence_recorded":
        return True
    if "terminal_evidence" in event_name and "record" in event_name:
        return True
    if event.get("terminal_result_recorded_at") and (
        event.get("bridge_result_path")
        or event.get("bridge_status_path")
        or event.get("result_event_note_path")
    ):
        return True
    return False

def normalize_record_paths(raw: Any) -> list[str]:
    paths: list[str] = []

    def add(value: Any) -> None:
        text = str(value or "").strip()
        if text and text not in paths:
            paths.append(text)

    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                add(item.get("path", "") or item.get("file", "") or item.get("url", ""))
            else:
                add(item)
    elif isinstance(raw, dict):
        for key in ("path", "file", "url"):
            add(raw.get(key, ""))
        if isinstance(raw.get("paths"), list):
            for item in raw["paths"]:
                add(item)
    elif raw:
        add(raw)
    return paths

def extract_artifact_paths(payload: dict[str, Any]) -> list[str]:
    paths: list[str] = []

    def add(value: Any) -> None:
        for path in normalize_record_paths(value):
            if path not in paths:
                paths.append(path)

    add(payload.get("paths", []))
    for key in (
        "path",
        "file",
        "artifact_path",
        "analysis_path",
        "bridge_result_path",
        "bridge_status_path",
        "result_event_note_path",
        "saved_experiment_mat_path",
        "savedexperiment_mat_path",
        "output_path",
        "output_png",
        "output_pdf",
        "report_path",
        "tex_path",
    ):
        add(payload.get(key, ""))
    figures = payload.get("figures", [])
    if isinstance(figures, list):
        for figure in figures:
            add(figure)
    return paths

def evidence_record_id(category: str, summary: str, paths: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    digest_source = json.dumps(
        {"category": category, "summary": summary, "paths": paths, "timestamp": timestamp},
        ensure_ascii=False,
        sort_keys=True,
    )
    digest = hashlib.sha256(digest_source.encode("utf-8")).hexdigest()[:10]
    return slug(f"{category}_{timestamp}_{digest}")

def evidence_index_path(root: Path) -> Path:
    return project_path(root, EVIDENCE_INDEX_FILENAME, "evidence_index.jsonl")

def append_evidence_record(
    root: Path,
    project: dict[str, Any],
    record: dict[str, Any],
    *,
    actor: str,
    source: str,
) -> dict[str, Any]:
    ensure_project_layout(root)
    category = slug(str(record.get("category", "") or record.get("evidence_type", "") or "note"))
    if category not in VALID_EVIDENCE_CATEGORIES:
        category = "artifact" if extract_artifact_paths(record) else "note"
    paths = extract_artifact_paths(record)
    summary = str(record.get("summary", "") or record.get("title", "") or "").strip()
    raw_evidence_id = str(record.get("evidence_id", "") or record.get("id", "") or "").strip()
    evidence_id = slug(raw_evidence_id) if raw_evidence_id else ""
    if not evidence_id:
        evidence_id = evidence_record_id(category, summary, paths)
    timestamp = str(record.get("timestamp", "") or now_iso())
    tags = record.get("tags", [])
    if not isinstance(tags, list):
        tags = [str(tags)]
    related_claims = record.get("related_claims", [])
    if not isinstance(related_claims, list):
        related_claims = [str(related_claims)]
    entry: dict[str, Any] = {
        "timestamp": timestamp,
        "actor": actor,
        "source": source,
        "schema_version": 1,
        "evidence_id": evidence_id,
        "project_id": str(project.get("project_id", "") or root.name),
        "category": category,
        "summary": summary,
        "paths": paths,
        "tags": tags,
        "related_claims": related_claims,
        "provenance": record.get("provenance", {}),
    }
    for key in (
        "backlog_item_id",
        "bridge_job_id",
        "request_id",
        "intent_id",
        "comparison_target",
        "quality",
        "claim_boundary",
    ):
        if key in record:
            entry[key] = record[key]
    append_jsonl(evidence_index_path(root), entry)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": actor,
            "event": "evidence_recorded",
            "project_id": str(project.get("project_id", "") or root.name),
            "evidence_id": evidence_id,
            "category": category,
            "summary": summary,
            "paths": paths,
            "source": source,
        },
    )
    state = load_state(root)
    state["updated_at"] = now_iso()
    state["last_evidence"] = {
        "evidence_id": evidence_id,
        "category": category,
        "summary": summary,
        "paths": paths,
        "timestamp": timestamp,
    }
    write_json(get_state_path(root), state)
    return {"evidence_id": evidence_id, "category": category, "paths": paths}

def read_jsonl_tail(path: Path, limit: int = 5) -> list[dict[str, Any]]:
    if not path.is_file():
        return []
    rows: list[dict[str, Any]] = []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []
    for line in lines[-max(1, limit * 4):]:
        text = line.strip()
        if not text:
            continue
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            rows.append(payload)
    return rows[-limit:]

def count_jsonl_records(path: Path) -> int:
    if not path.is_file():
        return 0
    try:
        return sum(1 for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip())
    except OSError:
        return 0

def maybe_write_terminal_evidence_completion_marker(
    root: Path,
    project: dict[str, Any],
    event: dict[str, Any],
    *,
    actor: str,
    source: str,
) -> dict[str, Any]:
    """Release a cron inflight run when terminal-evidence-only paths made progress.

    Agent wakes are expected to write a completion marker themselves. A common
    bounded terminal-evidence path records bridge/MAT evidence and leaves the
    actual terminal review pending for the next wake; if that path exits before
    writing the marker, cron sees ledger progress and keeps the same run
    inflight until timeout. This helper writes the same small marker when the
    recorded event is terminal evidence and the current cron state points to a
    missing marker for an active agent run.
    """

    if not terminal_evidence_payload(event):
        return {"attempted": False, "sent": False, "reason": "not_terminal_evidence"}

    project_id = str(project.get("project_id", "") or root.name)
    cron_state_path = CRON_STATE_ROOT / f"{project_id}.json"
    cron_state = read_json_safely(cron_state_path)
    agent_run = cron_state.get("last_agent_run", {})
    if not isinstance(agent_run, dict) or not agent_run:
        return {"attempted": False, "sent": False, "reason": "no_last_agent_run"}

    if str(agent_run.get("status", "") or "running") not in {"running", "requested"}:
        return {
            "attempted": False,
            "sent": False,
            "reason": f"agent_run_not_inflight:{agent_run.get('status', '')}",
        }

    marker_text = str(agent_run.get("marker_path", "") or "").strip()
    if not marker_text:
        return {"attempted": False, "sent": False, "reason": "missing_marker_path"}
    marker_path = Path(marker_text)
    if marker_path.is_file():
        return {"attempted": False, "sent": False, "reason": "marker_already_exists", "marker_path": str(marker_path)}
    if not marker_path.is_absolute():
        return {"attempted": False, "sent": False, "reason": "marker_path_not_absolute", "marker_path": marker_text}
    if marker_path.suffix != ".json" or not marker_path.name.endswith(".done.json"):
        return {"attempted": False, "sent": False, "reason": "marker_path_not_done_json", "marker_path": str(marker_path)}
    if not (
        path_is_inside(marker_path, get_agent_runs_root(root))
        or path_is_inside(marker_path, root / "task_notes" / "agent_runs")
    ):
        return {"attempted": False, "sent": False, "reason": "marker_path_outside_project_agent_runs", "marker_path": str(marker_path)}

    backlog_item_id = str(event.get("backlog_item_id", "") or "")
    marker_payload = {
        "project_id": project_id,
        "completed_at": now_iso(),
        "status": "completed",
        "summary": (
            "Terminal evidence was recorded through nv_project_manager; "
            "auto-writing the required completion marker so cron can continue "
            "the pending review instead of waiting for the inflight timeout."
        ),
        "backend": "nv_project_manager_terminal_evidence_autocomplete",
        "source": source,
        "run_id": str(agent_run.get("run_id", "") or ""),
        "wake_key": str(agent_run.get("wake_key", "") or ""),
        "dispatched_at": str(agent_run.get("dispatched_at", "") or ""),
        "marker_autowritten": True,
        "touched_bridge_queue": False,
        "next_action": {
            "kind": "terminal_evidence_recorded",
            "reason": (
                "terminal evidence was recorded without an agent-written marker; "
                "cron should release the in-flight wake and schedule terminal review"
            ),
        },
        "terminal_event": {
            "event": str(event.get("event", "") or ""),
            "timestamp": str(event.get("timestamp", "") or ""),
            "summary": str(event.get("summary", "") or ""),
            "backlog_item_id": backlog_item_id,
            "bridge_job_id": str(event.get("bridge_job_id", "") or ""),
            "bridge_result_path": str(event.get("bridge_result_path", "") or ""),
            "bridge_status_path": str(event.get("bridge_status_path", "") or ""),
            "saved_experiment_mat_path": str(event.get("saved_experiment_mat_path", "") or ""),
        },
        "updated_backlog_item_ids": [backlog_item_id] if backlog_item_id else [],
    }
    write_json(marker_path, marker_payload)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": actor,
            "event": "agent_completion_marker_autowritten",
            "project_id": project_id,
            "marker_path": str(marker_path),
            "source": source,
            "run_id": str(agent_run.get("run_id", "") or ""),
            "wake_key": str(agent_run.get("wake_key", "") or ""),
            "backlog_item_id": backlog_item_id,
            "reason": "terminal_evidence_recorded_without_agent_marker",
        },
    )
    return {
        "attempted": True,
        "sent": True,
        "reason": "terminal_evidence_recorded_without_agent_marker",
        "marker_path": str(marker_path),
    }

def load_config(config_path: Path = DEFAULT_CONFIG_PATH) -> dict[str, Any]:
    if not config_path.is_file():
        return {}
    try:
        payload = read_json(config_path)
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}

def deep_merge_dicts(base: dict[str, Any], patch: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge_dicts(merged[key], value)
        else:
            merged[key] = value
    return merged

def format_lab_log_value(value: Any) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return ""
    return str(value)

def lab_log_link_target(root: Path, document_path: Path, value: str) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    try:
        path = Path(text)
        if path.is_absolute():
            target_path = path
        else:
            target_path = root / path
        text = os.path.relpath(target_path, start=document_path.parent)
    except Exception:
        pass
    return text.replace("\\", "/").replace(" ", "%20")

def normalize_lab_log_figures(raw: Any) -> list[dict[str, str]]:
    if not raw:
        return []
    if isinstance(raw, dict):
        if isinstance(raw.get("figures"), list):
            raw = raw["figures"]
        else:
            raw = [raw]
    if not isinstance(raw, list):
        raise ValueError("lab log figures must be a JSON object or array.")
    figures: list[dict[str, str]] = []
    for entry in raw:
        if isinstance(entry, str):
            path = entry
            caption = ""
        elif isinstance(entry, dict):
            path = str(entry.get("path", "") or entry.get("file", "") or "")
            caption = str(entry.get("caption", "") or entry.get("title", "") or "")
        else:
            continue
        if path.strip():
            figures.append({"path": path.strip(), "caption": caption.strip()})
    return figures

def ensure_lab_log(root: Path, project: dict[str, Any], timestamp: str) -> dict[str, Path]:
    project_id = str(project.get("project_id", "") or root.name)
    sample_id = str(project.get("sample_id", "") or DEFAULT_SAMPLE_ID)
    objective = str(project.get("objective", "") or "").strip()
    created_at = str(project.get("created_at", "") or timestamp)

    lab_log_path = get_lab_log_path(root)
    if not lab_log_path.exists():
        lab_log_path.write_text(
            "\n".join(
                [
                    f"# Research Log: {project_id}",
                    "",
                    f"- Project: {project_id}",
                    f"- Sample: {sample_id}",
                    f"- Created: {created_at}",
                    "",
                    "## Objective",
                    "",
                    objective or "(not recorded)",
                    "",
                    "## Entries",
                    "",
                ]
            ),
            encoding="utf-8",
        )

    return {"lab_log_path": lab_log_path, "daily_log_path": lab_log_path}

def append_lab_log(
    root: Path,
    project: dict[str, Any],
    *,
    title: str,
    summary: str = "",
    event: str = "",
    actor: str = "",
    details: dict[str, Any] | None = None,
    figures: list[dict[str, str]] | None = None,
) -> dict[str, str]:
    timestamp = now_iso()
    paths = ensure_lab_log(root, project, timestamp)
    def render_entry(document_path: Path) -> str:
        clean_title = str(title or "Note").strip() or "Note"
        lines = [f"### {timestamp} - {clean_title}", ""]
        if summary:
            lines.extend([str(summary).strip(), ""])
        if figures:
            lines.extend(["Figures:", ""])
            for figure in figures:
                figure_path = lab_log_link_target(root, document_path, str(figure.get("path", "") or ""))
                caption = str(figure.get("caption", "") or figure_path).strip()
                if not figure_path:
                    continue
                lines.append(f"![{caption}]({figure_path})")
                if caption:
                    lines.append(f"*{caption}*")
                lines.append("")
        metadata: dict[str, Any] = {}
        if event:
            metadata["event"] = event
        if actor:
            metadata["actor"] = actor
        if details:
            metadata.update(details)
        for key, value in metadata.items():
            rendered = format_lab_log_value(value)
            if rendered:
                lines.append(f"- {key}: {rendered}")
        lines.append("")
        return "\n".join(lines)

    written_paths: set[Path] = set()
    for path in paths.values():
        resolved_path = path.resolve()
        if resolved_path in written_paths:
            continue
        written_paths.add(resolved_path)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(render_entry(path))
    return {key: str(value) for key, value in paths.items()}

def resolve_telegram_notify_target(config_path: Path = DEFAULT_CONFIG_PATH) -> str:
    env_target = str(os.environ.get("OPENCLAW_TELEGRAM_NOTIFY_TARGET", "") or "").strip()
    if env_target:
        return env_target

    cfg = load_config(config_path)
    notify_cfg = cfg.get("notifications", {}).get("nv_projects", {}).get("telegram", {})
    if isinstance(notify_cfg, dict):
        target = str(notify_cfg.get("target", "") or "").strip()
        if target:
            return target

    channel_cfg = cfg.get("channels", {}).get("telegram", {})
    if not isinstance(channel_cfg, dict):
        return ""
    default_to = str(channel_cfg.get("defaultTo", "") or "").strip()
    if default_to:
        return default_to
    allow_from = [str(value).strip() for value in channel_cfg.get("allowFrom", []) if str(value or "").strip()]
    if len(allow_from) == 1:
        return allow_from[0]
    return ""

def resolve_telegram_notify_account(config_path: Path = DEFAULT_CONFIG_PATH) -> str:
    env_account = str(os.environ.get("OPENCLAW_TELEGRAM_NOTIFY_ACCOUNT", "") or "").strip()
    if env_account:
        return env_account
    cfg = load_config(config_path)
    notify_cfg = cfg.get("notifications", {}).get("nv_projects", {}).get("telegram", {})
    if isinstance(notify_cfg, dict):
        account = str(notify_cfg.get("accountId", "") or "").strip()
        if account:
            return account
    return "default"

def resolve_telegram_bot_token(config_path: Path = DEFAULT_CONFIG_PATH) -> str:
    env_token = str(os.environ.get("OPENCLAW_TELEGRAM_BOT_TOKEN", "") or "").strip()
    if env_token:
        return env_token
    cfg = load_config(config_path)
    channel_cfg = cfg.get("channels", {}).get("telegram", {})
    if not isinstance(channel_cfg, dict):
        return ""
    for key in ("botToken", "token"):
        token = str(channel_cfg.get(key, "") or "").strip()
        if token:
            return token
    accounts = channel_cfg.get("accounts", {})
    if isinstance(accounts, dict):
        account_id = resolve_telegram_notify_account(config_path)
        account_cfg = accounts.get(account_id, {})
        if isinstance(account_cfg, dict):
            for key in ("botToken", "token"):
                token = str(account_cfg.get(key, "") or "").strip()
                if token:
                    return token
    return ""

def normalize_telegram_chat_id(target: str) -> str:
    text = str(target or "").strip()
    if text.startswith("telegram:"):
        return text[len("telegram:") :]
    return text

def telegram_bot_api_call(
    token: str,
    method: str,
    *,
    fields: dict[str, Any],
    files: dict[str, Path] | None = None,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    if not token:
        return {"ok": False, "error": "missing_telegram_bot_token"}
    url = f"https://api.telegram.org/bot{token}/{method}"
    clean_fields = {key: str(value) for key, value in fields.items() if value is not None and str(value) != ""}
    headers: dict[str, str] = {}
    if files:
        boundary = f"----openclaw-telegram-{uuid.uuid4().hex}"
        body = bytearray()
        for key, value in clean_fields.items():
            body.extend(f"--{boundary}\r\n".encode("utf-8"))
            body.extend(f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode("utf-8"))
            body.extend(value.encode("utf-8"))
            body.extend(b"\r\n")
        for field_name, path in files.items():
            filename = path.name
            content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
            body.extend(f"--{boundary}\r\n".encode("utf-8"))
            body.extend(
                (
                    f'Content-Disposition: form-data; name="{field_name}"; filename="{filename}"\r\n'
                    f"Content-Type: {content_type}\r\n\r\n"
                ).encode("utf-8")
            )
            body.extend(path.read_bytes())
            body.extend(b"\r\n")
        body.extend(f"--{boundary}--\r\n".encode("utf-8"))
        data = bytes(body)
        headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
    else:
        data = urllib.parse.urlencode(clean_fields).encode("utf-8")
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    request = urllib.request.Request(url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            text = response.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        return {"ok": False, "error": f"http_{exc.code}", "response_text": body[-2000:]}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
    try:
        payload = json.loads(text)
    except Exception:
        payload = {"raw": text}
    return {"ok": bool(payload.get("ok", False)) if isinstance(payload, dict) else False, "response": payload}

def send_telegram_text_via_bot_api(text: str, *, dry_run: bool = False, timeout_seconds: int = 60) -> dict[str, Any]:
    config_path = DEFAULT_CONFIG_PATH
    target = resolve_telegram_notify_target(config_path)
    if not target:
        return {"attempted": False, "sent": False, "reason": "no_telegram_target", "transport": "bot_api"}
    token = resolve_telegram_bot_token(config_path)
    if not token:
        return {"attempted": False, "sent": False, "reason": "missing_telegram_bot_token", "transport": "bot_api"}
    chat_id = normalize_telegram_chat_id(target)
    if dry_run:
        return {"attempted": True, "sent": False, "dry_run": True, "transport": "bot_api", "method": "sendMessage", "target": chat_id}
    result = telegram_bot_api_call(
        token,
        "sendMessage",
        fields={"chat_id": chat_id, "text": str(text or "")[:4096]},
        timeout_seconds=timeout_seconds,
    )
    return {
        "attempted": True,
        "sent": bool(result.get("ok", False)),
        "transport": "bot_api",
        "method": "sendMessage",
        "target": chat_id,
        "reason": "" if bool(result.get("ok", False)) else str(result.get("error", "telegram_api_failed")),
        "telegram_response": result.get("response", {}),
    }

def stage_telegram_media(media_path: str | Path, *, outbound_dir: Path | None = None) -> dict[str, Any]:
    src = Path(media_path).expanduser()
    if not src.is_absolute():
        src = src.resolve()
    if not src.is_file():
        return {"ok": False, "reason": "media_not_found", "source_path": str(src)}

    root = Path(
        outbound_dir
        or os.environ.get("OPENCLAW_TELEGRAM_MEDIA_OUTBOUND_DIR", str(DEFAULT_TELEGRAM_MEDIA_OUTBOUND_DIR))
    ).expanduser()
    date_dir = root / datetime.now().strftime("%Y-%m-%d")
    date_dir.mkdir(parents=True, exist_ok=True)

    digest = hashlib.sha256(src.read_bytes()).hexdigest()[:16]
    safe_stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", src.stem).strip("._") or "media"
    suffix = src.suffix if src.suffix else ".bin"
    dest = date_dir / f"{safe_stem}_{digest}{suffix}"
    if src.resolve() != dest.resolve():
        shutil.copy2(src, dest)
    return {"ok": True, "source_path": str(src), "staged_path": str(dest)}

def send_telegram_media(
    media_path: str | Path,
    *,
    message: str = "",
    dry_run: bool = False,
    force_document: bool = False,
    text_first: bool = True,
    transport: str | None = None,
    timeout_seconds: int = 60,
) -> dict[str, Any]:
    config_path = DEFAULT_CONFIG_PATH
    target = resolve_telegram_notify_target(config_path)
    if not target:
        return {"attempted": False, "sent": False, "reason": "no_telegram_target"}
    staged = stage_telegram_media(media_path)
    if not bool(staged.get("ok", False)):
        return {"attempted": False, "sent": False, **staged}

    selected_transport = str(
        transport
        or os.environ.get("OPENCLAW_TELEGRAM_MEDIA_TRANSPORT", "bot_api")
        or "bot_api"
    ).strip().lower()
    if selected_transport in {"bot", "telegram_bot", "telegram_bot_api", "direct"}:
        selected_transport = "bot_api"
    if selected_transport in {"openclaw", "cli", "message_send"}:
        selected_transport = "openclaw_cli"

    text_result: dict[str, Any] = {}
    clean_message = str(message or "").strip()
    staged_path = Path(str(staged["staged_path"]))
    if selected_transport == "bot_api":
        token = resolve_telegram_bot_token(config_path)
        if token:
            chat_id = normalize_telegram_chat_id(target)
            if clean_message and text_first:
                text_result = send_telegram_text_via_bot_api(
                    clean_message,
                    dry_run=dry_run,
                    timeout_seconds=timeout_seconds,
                )
            suffix = staged_path.suffix.lower()
            image_suffixes = {".jpg", ".jpeg", ".png", ".webp"}
            use_document = bool(force_document) or suffix not in image_suffixes
            method = "sendDocument" if use_document else "sendPhoto"
            file_field = "document" if use_document else "photo"
            caption = clean_message[:1024] if clean_message and not text_first else ""
            if dry_run:
                return {
                    "attempted": True,
                    "sent": False,
                    "dry_run": True,
                    "transport": "bot_api",
                    "method": method,
                    "target": chat_id,
                    "source_path": str(staged["source_path"]),
                    "staged_path": str(staged_path),
                    "text_first": bool(text_first),
                    "text_result": text_result,
                }
            api_result = telegram_bot_api_call(
                token,
                method,
                fields={"chat_id": chat_id, "caption": caption},
                files={file_field: staged_path},
                timeout_seconds=timeout_seconds,
            )
            sent = bool(api_result.get("ok", False))
            return {
                "attempted": True,
                "sent": sent,
                "dry_run": False,
                "transport": "bot_api",
                "method": method,
                "target": chat_id,
                "returncode": 0 if sent else 1,
                "reason": "" if sent else str(api_result.get("error", "telegram_api_failed")),
                "source_path": str(staged["source_path"]),
                "staged_path": str(staged_path),
                "text_first": bool(text_first),
                "text_result": text_result,
                "telegram_response": api_result.get("response", {}),
            }
        if transport == "bot_api":
            return {
                "attempted": False,
                "sent": False,
                "transport": "bot_api",
                "reason": "missing_telegram_bot_token",
                "source_path": str(staged["source_path"]),
                "staged_path": str(staged_path),
            }
        selected_transport = "openclaw_cli"

    cli_path = Path(os.environ.get("OPENCLAW_CLI_PATH", str(DEFAULT_OPENCLAW_CLI_PATH))).expanduser()
    if not cli_path.is_file():
        return {"attempted": False, "sent": False, "reason": "missing_openclaw_cli", "cli_path": str(cli_path)}

    if clean_message and text_first:
        text_result = send_telegram_notification(clean_message, dry_run=dry_run)

    command = [
        str(cli_path),
        "message",
        "send",
        "--channel",
        "telegram",
        "--target",
        target,
        "--account",
        resolve_telegram_notify_account(config_path),
        "--media",
        str(staged_path),
        "--json",
    ]
    if clean_message and not text_first:
        command.extend(["--message", clean_message])
    if force_document:
        command.append("--force-document")
    if dry_run:
        command.append("--dry-run")
    completed = subprocess.run(command, capture_output=True, text=True, timeout=timeout_seconds)
    return {
        "attempted": True,
        "sent": completed.returncode == 0 and not dry_run,
        "dry_run": bool(dry_run),
        "transport": "openclaw_cli",
        "returncode": completed.returncode,
        "source_path": str(staged["source_path"]),
        "staged_path": str(staged_path),
        "text_first": bool(text_first),
        "text_result": text_result,
        "stdout": completed.stdout[-2000:],
        "stderr": completed.stderr[-2000:],
    }

def send_telegram_notification(text: str, *, dry_run: bool = False) -> dict[str, Any]:
    config_path = DEFAULT_CONFIG_PATH
    target = resolve_telegram_notify_target(config_path)
    if not target:
        return {"attempted": False, "sent": False, "reason": "no_telegram_target"}
    cli_path = Path(os.environ.get("OPENCLAW_CLI_PATH", str(DEFAULT_OPENCLAW_CLI_PATH))).expanduser()
    if not cli_path.is_file():
        return {"attempted": False, "sent": False, "reason": "missing_openclaw_cli", "cli_path": str(cli_path)}

    command = [
        str(cli_path),
        "message",
        "send",
        "--channel",
        "telegram",
        "--target",
        target,
        "--account",
        resolve_telegram_notify_account(config_path),
        "--message",
        text,
        "--json",
    ]
    if dry_run:
        command.append("--dry-run")
    completed = subprocess.run(command, capture_output=True, text=True, timeout=30)
    return {
        "attempted": True,
        "sent": completed.returncode == 0 and not dry_run,
        "dry_run": bool(dry_run),
        "returncode": completed.returncode,
    }

def notify_project_request(
    root: Path,
    project: dict[str, Any],
    *,
    request_type: str,
    request_id: str,
    summary: str,
    request_path: Path,
    blocking: bool,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    project_id = str(project.get("project_id", "") or root.name)
    lines = [
        f"NV project request: {request_type}",
        f"Project: {project_id}",
        f"Request: {request_id}",
        f"Blocking: {'yes' if blocking else 'no'}",
    ]
    if summary:
        lines.append(f"Summary: {summary}")
    if extra:
        for key, value in extra.items():
            rendered = format_lab_log_value(value)
            if rendered:
                lines.append(f"{key}: {rendered}")
    lines.append(f"Path: {request_path}")
    try:
        result = send_telegram_notification("\n".join(lines))
    except Exception as exc:
        result = {
            "attempted": True,
            "sent": False,
            "reason": f"{type(exc).__name__}: {exc}",
        }
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": "openclaw-project-manager",
            "event": "telegram_notification",
            "project_id": project_id,
            "request_type": request_type,
            "request_id": request_id,
            "attempted": bool(result.get("attempted", False)),
            "sent": bool(result.get("sent", False)),
            "reason": str(result.get("reason", "") or ""),
            "returncode": result.get("returncode", ""),
        },
    )
    return result

def project_dir(project_id: str) -> Path:
    return PROJECT_ROOT / slug(project_id)

def project_path(root: Path, new_rel: str, legacy_rel: str = "") -> Path:
    """Return the new structure path, while preserving old projects in place."""

    new_path = root / new_rel
    if legacy_rel:
        legacy_path = root / legacy_rel
        if legacy_path.exists() and not new_path.exists():
            return legacy_path
    return new_path

def project_path_any(root: Path, new_rel: str, legacy_rels: list[str]) -> Path:
    new_path = root / new_rel
    if new_path.exists():
        return new_path
    for rel in legacy_rels:
        legacy_path = root / rel
        if legacy_path.exists():
            return legacy_path
    return new_path

def get_state_path(root: Path) -> Path:
    return project_path(root, STATE_FILENAME, "state.json")

def get_backlog_path(root: Path) -> Path:
    return project_path(root, BACKLOG_FILENAME, "backlog.json")

def get_ledger_path(root: Path) -> Path:
    return project_path(root, LEDGER_FILENAME, "ledger.jsonl")

def get_lab_log_path(root: Path) -> Path:
    return project_path(root, LAB_LOG_FILENAME, "lab_log.md")

def get_daily_log_root(root: Path) -> Path:
    return project_path_any(root, ".manager/daily", ["work/daily", "daily_log"])

def get_figure_root(root: Path) -> Path:
    return project_path_any(root, "work/artifacts/figures", ["artifacts/figures", "figures"])

def get_summary_root(root: Path) -> Path:
    return project_path_any(root, "work/artifacts/reports", ["reports", "summaries"])

def get_task_notes_root(root: Path) -> Path:
    return project_path_any(root, "work/notes", ["work/tasks", "task_notes"])

def get_agent_runs_root(root: Path) -> Path:
    return project_path_any(root, ".manager/agent_runs", ["work/agent_runs", "task_notes/agent_runs"])

def get_wake_records_root(root: Path) -> Path:
    return project_path_any(root, ".manager/wake_records", ["work/wake_records", "task_notes/wake_records"])

def get_wake_replay_evaluation_root() -> Path:
    return WAKE_REPLAY_EVALUATION_ROOT

def sha256_text(text: str) -> str:
    return hashlib.sha256(str(text or "").encode("utf-8")).hexdigest()

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def write_text_snapshot(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

def wake_record_id_from_marker(marker_path: Path, fallback: str = "wake") -> str:
    name = marker_path.name if marker_path else ""
    for suffix in (".done.json", ".timeout.json", ".json"):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
            break
    return slug(name or fallback)

def is_probably_text_snapshot_path(path: Path) -> bool:
    suffix = path.suffix.lower()
    if suffix in {
        ".csv",
        ".ini",
        ".json",
        ".jsonl",
        ".log",
        ".m",
        ".md",
        ".py",
        ".sh",
        ".toml",
        ".txt",
        ".xml",
        ".yaml",
        ".yml",
    }:
        return True
    mime, _ = mimetypes.guess_type(str(path))
    return bool(mime and (mime.startswith("text/") or mime in {"application/json", "application/xml"}))

def snapshot_file_for_wake_record(record_dir: Path, original_path: Path, snapshot_relpath: str) -> dict[str, Any]:
    path = Path(str(original_path)).expanduser()
    info: dict[str, Any] = {
        "original_path": str(path),
        "snapshot_relpath": snapshot_relpath,
        "exists": path.is_file(),
        "copied": False,
    }
    if not path.is_file():
        return info
    try:
        stat = path.stat()
        info["size_bytes"] = stat.st_size
        info["updated_epoch"] = stat.st_mtime
        info["sha256"] = sha256_file(path)
        if stat.st_size > WAKE_RECORD_TEXT_SNAPSHOT_MAX_BYTES:
            info["copy_skipped_reason"] = "file_too_large_for_text_snapshot"
            return info
        if not is_probably_text_snapshot_path(path):
            info["copy_skipped_reason"] = "non_text_or_unknown_type"
            return info
        text = path.read_text(encoding="utf-8", errors="replace")
        snapshot_path = record_dir / snapshot_relpath
        write_text_snapshot(snapshot_path, text)
        info["copied"] = True
        info["snapshot_path"] = str(snapshot_path)
        info["snapshot_size_bytes"] = len(text.encode("utf-8", errors="replace"))
    except Exception as exc:
        info["copy_error"] = f"{type(exc).__name__}: {exc}"
    return info

def collect_wake_record_evidence_paths(report: dict[str, Any]) -> list[str]:
    found: list[str] = []

    def add(value: Any) -> None:
        if isinstance(value, str) and value.strip():
            found.append(value.strip())

    def walk(value: Any) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                if key in {"path", "paths", "artifact_path", "artifact_paths", "result_path", "figure", "figures"}:
                    if isinstance(child, list):
                        for item in child:
                            add(item)
                    else:
                        add(child)
                elif key in {"recent_evidence", "evidence", "research_context"}:
                    walk(child)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(report.get("research_context", {}))
    next_action = report.get("next_action", {}) if isinstance(report.get("next_action"), dict) else {}
    walk(next_action.get("research_context", {}))
    seen: set[str] = set()
    unique: list[str] = []
    for path in found:
        if path in seen:
            continue
        seen.add(path)
        unique.append(path)
    return unique[:80]

def record_wake_context(
    root: Path,
    *,
    record_id: str,
    payload: dict[str, Any],
    report: dict[str, Any],
    wake_key: str,
    marker_path: Path,
    actor: str,
    source: str,
    hook_path: str = "",
    gateway_url: str = "",
    dispatch_mode: str = "",
) -> dict[str, Any]:
    record_id = slug(record_id or wake_record_id_from_marker(marker_path, fallback=wake_key))
    record_dir = get_wake_records_root(root) / record_id
    record_dir.mkdir(parents=True, exist_ok=True)

    prompt_text = str(payload.get("message", "") or "")
    prompt_path = record_dir / "wake_prompt.md"
    payload_path = record_dir / "wake_payload.json"
    report_path = record_dir / "wake_report.json"
    write_text_snapshot(prompt_path, prompt_text)
    write_json(payload_path, payload)
    write_json(report_path, report)

    shared_memory = report.get("shared_research_memory", {}) if isinstance(report.get("shared_research_memory"), dict) else {}
    snapshot_targets: list[tuple[str, Path]] = [
        ("md/NV_RESEARCH_MEMORY.md", Path(str(shared_memory.get("path", "") or NV_RESEARCH_MEMORY_PATH))),
        ("md/NV_RESEARCH_KNOWLEDGE.md", Path(str(shared_memory.get("detailed_knowledge_path", "") or NV_RESEARCH_KNOWLEDGE_PATH))),
        ("md/nv-project-manager_SKILL.md", WAKE_RECORD_SKILL_PATH),
        ("project/project.json", root / "project.json"),
        ("project/brief.md", root / "brief.md"),
        ("project/human_advice.md", root / "human_advice.md"),
        ("project/work_state.md", root / RESEARCH_STATE_FILENAME),
        ("project/log.md", get_lab_log_path(root)),
        ("project/manager_state.json", get_state_path(root)),
        ("project/manager_backlog.json", get_backlog_path(root)),
        ("project/manager_evidence.jsonl", evidence_index_path(root)),
        ("project/manager_ledger.jsonl", get_ledger_path(root)),
    ]
    for index, path_text in enumerate(collect_wake_record_evidence_paths(report), start=1):
        path = Path(path_text).expanduser()
        safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", path.name or f"evidence_{index}")
        snapshot_targets.append((f"evidence/{index:03d}_{safe_name}", path))

    snapshots: list[dict[str, Any]] = []
    seen_original_paths: set[str] = set()
    for relpath, path in snapshot_targets:
        original_key = str(Path(str(path)).expanduser())
        if original_key in seen_original_paths:
            continue
        seen_original_paths.add(original_key)
        snapshots.append(snapshot_file_for_wake_record(record_dir, path, relpath))

    manifest = {
        "schema_version": WAKE_RECORD_SCHEMA_VERSION,
        "created_at": now_iso(),
        "cutoff_time": now_iso(),
        "cutoff_epoch": time.time(),
        "cutoff_rule": "future-blind replay may use only prompt, payload, report, and file snapshots captured in this wake record, or explicit current-memory overlay snapshots selected by the evaluator",
        "actor": actor,
        "source": source,
        "project_id": str(report.get("project_id", "") or root.name),
        "project_dir": str(root),
        "record_id": record_id,
        "wake_key": wake_key,
        "marker_path": str(marker_path),
        "hook_path": hook_path,
        "gateway_url": gateway_url,
        "dispatch_mode": dispatch_mode,
        "agent": {
            "id": str(payload.get("agentId", "") or ""),
            "session_key": str(payload.get("sessionKey", "") or ""),
            "model": str(payload.get("model", "") or ""),
            "thinking": str(payload.get("thinking", "") or ""),
            "name": str(payload.get("name", "") or ""),
        },
        "prompt_path": str(prompt_path),
        "prompt_sha256": sha256_text(prompt_text),
        "payload_path": str(payload_path),
        "payload_sha256": sha256_text(json.dumps(payload, ensure_ascii=False, sort_keys=True)),
        "report_path": str(report_path),
        "next_action": report.get("next_action", {}),
        "snapshots": snapshots,
    }
    manifest_path = record_dir / "context_manifest.json"
    write_json(manifest_path, manifest)
    return {
        "record_id": record_id,
        "record_dir": str(record_dir),
        "manifest_path": str(manifest_path),
        "prompt_path": str(prompt_path),
        "payload_path": str(payload_path),
        "report_path": str(report_path),
        "prompt_sha256": manifest["prompt_sha256"],
        "payload_sha256": manifest["payload_sha256"],
    }

def write_wake_record_dispatch_result(record_dir: str | Path, payload: dict[str, Any]) -> dict[str, Any]:
    path = Path(str(record_dir)).expanduser()
    dispatch = {
        "schema_version": 1,
        "recorded_at": now_iso(),
        "dispatch": payload,
    }
    write_json(path / "dispatch_result.json", dispatch)
    return dispatch

def shared_nv_research_memory_context(*, include_snapshot: bool = False) -> dict[str, Any]:
    context: dict[str, Any] = {
        "path": str(NV_RESEARCH_MEMORY_PATH),
        "startup_memory_path": str(NV_RESEARCH_MEMORY_PATH),
        "detailed_knowledge_path": str(NV_RESEARCH_KNOWLEDGE_PATH),
        "read_required": True,
        "read_required_for": ["nv-researcher", "nv_project_work", "nv-project-manager"],
        "read_policy": "read_startup_memory_every_wake; read_detailed_knowledge_sections_on_demand_by_memory_index",
        "scope": "compact_startup_contract_and_detailed_nv_knowledge_router",
        "source": "NV_RESEARCH_MEMORY.md",
        "detailed_source": "NV_RESEARCH_KNOWLEDGE.md",
    }
    if NV_RESEARCH_MEMORY_PATH.is_file():
        stat = NV_RESEARCH_MEMORY_PATH.stat()
        context["exists"] = True
        context["updated_epoch"] = stat.st_mtime
        context["size_bytes"] = stat.st_size
        if include_snapshot:
            text = NV_RESEARCH_MEMORY_PATH.read_text(encoding="utf-8", errors="replace")
            context["snapshot_char_limit"] = NV_RESEARCH_MEMORY_SNAPSHOT_MAX_CHARS
            context["snapshot_truncated"] = len(text) > NV_RESEARCH_MEMORY_SNAPSHOT_MAX_CHARS
            context["snapshot"] = text[:NV_RESEARCH_MEMORY_SNAPSHOT_MAX_CHARS]
    else:
        context["exists"] = False
    if NV_RESEARCH_KNOWLEDGE_PATH.is_file():
        knowledge_stat = NV_RESEARCH_KNOWLEDGE_PATH.stat()
        context["detailed_knowledge_exists"] = True
        context["detailed_knowledge_updated_epoch"] = knowledge_stat.st_mtime
        context["detailed_knowledge_size_bytes"] = knowledge_stat.st_size
    else:
        context["detailed_knowledge_exists"] = False
    return context

def ensure_shared_nv_research_memory_context(project: dict[str, Any], *, include_snapshot: bool = False) -> dict[str, Any]:
    defaults = shared_nv_research_memory_context(include_snapshot=include_snapshot)
    existing = project.get("shared_research_memory", {})
    if not isinstance(existing, dict):
        existing = {}
    merged = {**defaults, **existing}
    if include_snapshot and defaults.get("snapshot"):
        merged["snapshot"] = defaults["snapshot"]
        merged["snapshot_char_limit"] = defaults["snapshot_char_limit"]
        merged["snapshot_truncated"] = defaults["snapshot_truncated"]
    project["shared_research_memory"] = merged
    architecture = project.get("research_architecture", {})
    if not isinstance(architecture, dict):
        architecture = {}
    architecture.setdefault("shared_research_memory_path", str(NV_RESEARCH_MEMORY_PATH))
    architecture.setdefault("shared_research_knowledge_path", str(NV_RESEARCH_KNOWLEDGE_PATH))
    architecture.setdefault("shared_research_memory_required", True)
    architecture.setdefault("shared_research_knowledge_read_policy", "on_demand_by_memory_index")
    project["research_architecture"] = architecture
    return merged

def ensure_project_layout(root: Path) -> None:
    for rel in (
        PROJECT_INTERNAL_DIRNAME,
        PROJECT_WORK_DIRNAME,
        "work/notes",
        PROJECT_BRIDGE_JOBS_DIRNAME,
        "work/artifacts",
        "advice/inbox",
        "advice/processed",
        "advice/superseded",
    ):
        (root / rel).mkdir(parents=True, exist_ok=True)

def default_research_state_text(project: dict[str, Any]) -> str:
    project_id = str(project.get("project_id", "") or "")
    objective = str(project.get("objective", "") or "").strip()
    return "\n".join(
        [
            f"# Project State: {project_id}",
            "",
            "This is the main readable project state. Keep it short, current, and useful.",
            "Keep bridge-execution contracts in `work/bridge_jobs/` or the live bridge queue.",
            "Put detailed derivations, checks, and failed ideas in `work/notes/` so future wakes",
            "can look them up without carrying everything in context.",
            "",
            "## Objective",
            "",
            objective or "(not recorded)",
            "",
            "## Vibe Physics Operating Pattern",
            "",
            "- Work in small, separately summarized tasks.",
            "- Record what was actually checked; do not write that something is verified unless it was checked.",
            "- When a result matters, include the calculation, bridge artifact, code path, or evidence id that supports it.",
            "- If an assertion is only taste, intuition, or a candidate interpretation, label it that way.",
            "- Repeat verification after fixes; finding one issue is not proof that the rest is clean.",
            "",
            "## Standing Operational Assumptions",
            "",
            f"- Read the shared NV startup memory at `{NV_RESEARCH_MEMORY_PATH}` before choosing NV project steps.",
            f"- Use its Memory Index to read relevant sections from `{NV_RESEARCH_KNOWLEDGE_PATH}` only when the current state, evidence, or human advice makes them useful.",
            f"- When an NV wake produces a durable reusable detailed lesson, update `{NV_RESEARCH_KNOWLEDGE_PATH}` in the relevant section with a concise dated note and provenance pointer.",
            (
                "- New NV projects use the `start-project` -> cron/force wake `nv-researcher` flow. "
                "`start-project` preserves the human request and durable state; `nv-researcher` owns "
                "the research agenda, backlog expansion, evidence synthesis, and experiment-design judgment."
            ),
            (
                "- Treat backlog items as execution/audit pointers, not as a complete scientific plan. "
                "Keep any seed backlog item minimal unless the operator explicitly asked for detailed gates."
            ),
            (
                "- For usual-NV recovery, prefer recent tracking, explicit human seeds, or prompt-visible "
                "label-dataset evidence before standalone Imaging/TrackCenter. Do not use the legacy live "
                "landmark-map route for future execution or recovery."
            ),
            (
                "- If NV tracking remains continuous and counts/alignment evidence stay healthy, "
                "absolute position motion by itself is not a reason to stop or block an experiment. "
                "Treat the motion as provenance and drift evidence to record, while continuing "
                "bounded work when the scientific intent and safety gates still hold."
            ),
            (
                "- Do pause or re-check when tracking is lost, counts collapse, a discontinuous "
                "jump or branch switch lacks continuous tracking provenance, hardware safety is "
                "uncertain, or a project-specific human constraint explicitly requires a fixed "
                "landmark/position."
            ),
            "",
            "## Current Status",
            "",
            "- (agent-maintained)",
            "",
            "## Candidate Findings",
            "",
            "- (agent-maintained)",
            "",
            "## Final Claims",
            "",
            "- (agent-maintained; cite evidence ids from `.manager/evidence.jsonl` or referenced bridge artifacts)",
            "",
            "## Decisions",
            "",
            "- (agent-maintained)",
            "",
            "## Next Step",
            "",
            "- (agent-maintained)",
            "",
            "## Evidence Pointers",
            "",
            "- (agent-maintained)",
            "",
            "## Note Convention",
            "",
            "For each meaningful unit of work, write one short Markdown note under",
            "`work/notes/` with: question, inputs read, action taken, result, checks",
            "actually performed, remaining uncertainty, and next pointer.",
            "",
            "Bridge-job JSON should contain execution contracts only: sequence/manifest, scan,",
            "numeric variables, hard limits, queue/execute opt-in, target labels, and Markdown",
            "note pointers. Scientific interpretation belongs in this file and `work/notes/`.",
            "",
        ]
    )

def default_research_agenda_text(project: dict[str, Any]) -> str:
    return default_research_state_text(project)

def ensure_project_knowledge_files(root: Path, project: dict[str, Any]) -> dict[str, str]:
    ensure_project_layout(root)
    brief = root / "brief.md"
    if not brief.exists():
        objective = str(project.get("objective", "") or "").strip()
        project_id = str(project.get("project_id", "") or root.name)
        brief.write_text(
            "\n".join(
                [
                    f"# Project Brief: {project_id}",
                    "",
                    "## Human Request / Objective",
                    "",
                    objective or "(not recorded)",
                    "",
                    "## Research Posture",
                    "",
                    "The agent owns research judgment inside hard bridge, hardware, and code-safety boundaries.",
                    "Use `work/state.md` as the compact living project state and `work/notes/` for small retrievable task summaries.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    work_readme = root / "work" / "README.md"
    if not work_readme.exists():
        work_readme.write_text(
            "\n".join(
                [
                    "# Work Tree",
                    "",
                    "Keep research work in small files that can be read independently.",
                    "",
                    "- `state.md`: main readable project state, candidate findings, final claims, decisions, and next pointers",
                    "- `bridge_jobs/`: bridge-execution contract JSON only",
                    "- `notes/`: one note per calculation, analysis, experiment decision, check, or review",
                    "",
                    "Generated figures, tables, and reports may live under `artifacts/`.",
                    "Do not use polished prose as a substitute for evidence. Record what was actually checked.",
                    "Scientific interpretation belongs in Markdown (`state.md` and `notes/`), not boolean-heavy bridge job metadata.",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    research_agenda = root / RESEARCH_AGENDA_FILENAME
    if not research_agenda.exists():
        research_agenda.parent.mkdir(parents=True, exist_ok=True)
        research_agenda.write_text(default_research_agenda_text(project), encoding="utf-8")
    research_state = root / RESEARCH_STATE_FILENAME
    if research_state != research_agenda and not research_state.exists():
        research_state.parent.mkdir(parents=True, exist_ok=True)
        research_state.write_text(default_research_state_text(project), encoding="utf-8")
    evidence_index = evidence_index_path(root)
    if not evidence_index.exists():
        evidence_index.parent.mkdir(parents=True, exist_ok=True)
        evidence_index.write_text("", encoding="utf-8")
    return {
        "brief_path": str(brief),
        "research_state_path": str(research_state),
        "research_agenda_path": str(research_agenda),
        "shared_research_memory_path": str(NV_RESEARCH_MEMORY_PATH),
        "shared_research_knowledge_path": str(NV_RESEARCH_KNOWLEDGE_PATH),
        "evidence_index_path": str(evidence_index),
        "experiment_intents_root": str(root / "experiment_intents"),
    }

def list_experiment_intent_files(root: Path, status: str) -> list[Path]:
    intent_root = root / "experiment_intents" / status
    if not intent_root.is_dir():
        return []
    return sorted(path for path in intent_root.glob("*.json") if path.is_file())

def research_context_overview(root: Path, project: dict[str, Any]) -> dict[str, Any]:
    paths = ensure_project_knowledge_files(root, project)
    evidence_path = Path(paths["evidence_index_path"])
    return {
        **paths,
        "evidence_count": count_jsonl_records(evidence_path),
        "recent_evidence": read_jsonl_tail(evidence_path, limit=5),
        "experiment_intents": {
            "queued": len(list_experiment_intent_files(root, "queued")),
            "verified": len(list_experiment_intent_files(root, "verified")),
            "rejected": len(list_experiment_intent_files(root, "rejected")),
            "done": len(list_experiment_intent_files(root, "done")),
        },
        "backlog_role": "execution_queue_and_audit_not_complete_research_plan",
        "scheduler_role": "event_state_pointer_agent_selects_scientific_next_step",
    }

def load_project(root: Path) -> dict[str, Any]:
    return sync_project_lifecycle_alias(read_json(root / "project.json"))

def load_state(root: Path) -> dict[str, Any]:
    state_path = get_state_path(root)
    if state_path.is_file():
        return sync_operational_state_alias(read_json(state_path))
    return sync_operational_state_alias({
        "schema_version": 1,
        "project_id": root.name,
        "status": "active",
        "operational_state": "active",
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "tick_count": 0,
        "blocking_request_id": "",
        "last_next_action": {"kind": "idle", "reason": "state created"},
    })

def latest_advice_inbox_file(root: Path) -> dict[str, Any]:
    inbox = root / "advice" / "inbox"
    if not inbox.is_dir():
        return {}
    latest_path: Path | None = None
    latest_mtime = 0.0
    for path in inbox.iterdir():
        if not path.is_file() or path.name.startswith("."):
            continue
        try:
            mtime = float(path.stat().st_mtime)
        except OSError:
            continue
        if latest_path is None or mtime > latest_mtime:
            latest_path = path
            latest_mtime = mtime
    if latest_path is None:
        return {}
    return {
        "path": str(latest_path),
        "relative_path": str(latest_path.relative_to(root)),
        "name": latest_path.name,
        "mtime_epoch": latest_mtime,
        "mtime": datetime.fromtimestamp(latest_mtime).strftime("%Y-%m-%dT%H:%M:%S"),
    }

def list_advice_inbox_files(root: Path) -> list[dict[str, Any]]:
    inbox = root / "advice" / "inbox"
    if not inbox.is_dir():
        return []
    items: list[dict[str, Any]] = []
    for path in inbox.iterdir():
        if not path.is_file() or path.name.startswith("."):
            continue
        try:
            stat = path.stat()
        except OSError:
            continue
        items.append(
            {
                "path": str(path),
                "relative_path": str(path.relative_to(root)),
                "name": path.name,
                "size_bytes": int(stat.st_size),
                "mtime_epoch": float(stat.st_mtime),
                "mtime": datetime.fromtimestamp(float(stat.st_mtime)).strftime("%Y-%m-%dT%H:%M:%S"),
            }
        )
    return sorted(items, key=lambda item: (float(item.get("mtime_epoch", 0.0) or 0.0), str(item.get("name", ""))))

def resolve_advice_inbox_path(root: Path, value: str) -> Path:
    text = str(value or "").strip()
    if not text:
        raise ValueError("--file is required.")
    candidate = Path(text).expanduser()
    if not candidate.is_absolute():
        if text.replace("\\", "/").startswith("advice/inbox/"):
            candidate = root / candidate
        else:
            candidate = root / "advice" / "inbox" / candidate
    candidate = candidate.resolve(strict=False)
    inbox = (root / "advice" / "inbox").resolve(strict=False)
    if not path_is_inside(candidate, inbox):
        raise ValueError(f"advice file must be inside {inbox}: {candidate}")
    if not candidate.is_file():
        raise FileNotFoundError(str(candidate))
    return candidate

def unique_advice_destination(path: Path) -> Path:
    if not path.exists():
        return path
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    stem = path.stem
    suffix = path.suffix
    candidate = path.with_name(f"{stem}_{timestamp}{suffix}")
    counter = 2
    while candidate.exists():
        candidate = path.with_name(f"{stem}_{timestamp}_{counter}{suffix}")
        counter += 1
    return candidate

def ensure_human_advice_document(path: Path) -> None:
    if path.exists():
        return
    path.write_text("# Human Advice\n\n", encoding="utf-8")

def append_effective_human_advice(
    root: Path,
    *,
    timestamp: str,
    classification: str,
    effective_guidance: str,
    source_relative_path: str,
) -> None:
    guidance = str(effective_guidance or "").strip()
    if not guidance:
        return
    human_advice_path = root / "human_advice.md"
    ensure_human_advice_document(human_advice_path)
    existing = human_advice_path.read_text(encoding="utf-8")
    if existing and not existing.endswith("\n"):
        existing += "\n"
    date_label = timestamp.replace("T", " ")
    source = str(source_relative_path or "").strip()
    source_text = f" Source: `{source}`." if source else ""
    line = f"- {date_label}: [{classification}] {guidance}{source_text}\n"
    human_advice_path.write_text(existing + line, encoding="utf-8")

def list_advice_inbox(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    ensure_project_layout(root)
    files = list_advice_inbox_files(root)
    total_count = len(files)
    limit = int(getattr(args, "limit", 0) or 0)
    if limit > 0:
        files = files[:limit]
    return {
        "ok": True,
        "action": "list_advice_inbox",
        "project_id": str(project.get("project_id", "") or root.name),
        "count": len(files),
        "total_count": total_count,
        "files": files,
    }

def dispose_advice(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    ensure_project_layout(root)
    project = load_project(root)
    state = load_state(root)
    disposition = str(args.disposition or "").strip().lower()
    classification = str(args.classification or "note").strip().lower()
    if disposition not in VALID_ADVICE_DISPOSITIONS:
        raise ValueError(f"--disposition must be one of: {', '.join(sorted(VALID_ADVICE_DISPOSITIONS))}")
    if classification not in VALID_ADVICE_CLASSIFICATIONS:
        raise ValueError(f"--classification must be one of: {', '.join(sorted(VALID_ADVICE_CLASSIFICATIONS))}")

    summary = str(args.summary or "").strip()
    reason = str(args.reason or "").strip()
    effective_guidance = str(args.effective_guidance or "").strip()
    if not summary:
        raise ValueError("--summary is required so the advice disposition is auditable.")
    if disposition == "deferred" and not reason:
        raise ValueError("--reason is required when --disposition deferred.")
    if disposition != "processed" and effective_guidance:
        raise ValueError("--effective-guidance is only valid with --disposition processed.")

    source_path = resolve_advice_inbox_path(root, args.file)
    raw_bytes = source_path.read_bytes()
    details = read_json_arg(args.details_json) if args.details_json else {}
    timestamp = now_iso()
    project_id = str(project.get("project_id", "") or root.name)
    source_relative = str(source_path.relative_to(root))
    target_path = source_path
    target_relative = source_relative
    moved = False

    if disposition in {"processed", "superseded"}:
        target_dir = root / "advice" / disposition
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = unique_advice_destination(target_dir / source_path.name)
        shutil.move(str(source_path), str(target_path))
        target_relative = str(target_path.relative_to(root))
        moved = True
        if disposition == "processed" and effective_guidance:
            append_effective_human_advice(
                root,
                timestamp=timestamp,
                classification=classification,
                effective_guidance=effective_guidance,
                source_relative_path=target_relative,
            )

    event = {
        "timestamp": timestamp,
        "actor": args.actor,
        "event": "advice_disposed",
        "project_id": project_id,
        "source_path": source_relative,
        "target_path": target_relative,
        "disposition": disposition,
        "classification": classification,
        "summary": summary,
        "reason": reason,
        "effective_guidance": effective_guidance,
        "message_sha256": hashlib.sha256(raw_bytes).hexdigest(),
        "message_bytes": len(raw_bytes),
        "moved": moved,
    }
    if details:
        event["details"] = details
    append_jsonl(get_ledger_path(root), event)

    lab_log_paths: dict[str, str] = {}
    if not bool(getattr(args, "no_lab_log", False)):
        lab_log_paths = append_lab_log(
            root,
            project,
            title=f"Advice {disposition}: {source_path.name}",
            summary=summary,
            event="advice_disposed",
            actor=args.actor,
            details={
                "source_path": source_relative,
                "target_path": target_relative,
                "disposition": disposition,
                "classification": classification,
                "reason": reason,
                "effective_guidance": effective_guidance,
                "message_sha256": event["message_sha256"],
            },
        )

    state["updated_at"] = timestamp
    state["last_advice_disposition"] = {
        "timestamp": timestamp,
        "source_path": source_relative,
        "target_path": target_relative,
        "disposition": disposition,
        "classification": classification,
        "summary": summary,
        "reason": reason,
        "effective_guidance_applied": bool(effective_guidance and disposition == "processed"),
    }
    write_json(get_state_path(root), state)

    return {
        "ok": True,
        "action": "dispose_advice",
        "project_id": project_id,
        "source_path": source_relative,
        "target_path": target_relative,
        "disposition": disposition,
        "classification": classification,
        "moved": moved,
        "effective_guidance_applied": bool(effective_guidance and disposition == "processed"),
        "lab_log_path": lab_log_paths.get("lab_log_path", ""),
        "daily_log_path": lab_log_paths.get("daily_log_path", ""),
    }

def project_pause_reference_epoch(root: Path, project: dict[str, Any], state: dict[str, Any]) -> float:
    candidates: list[float] = []
    for event in recent_jsonl_records(get_ledger_path(root), max_lines=1000):
        updated_keys = event.get("updated_keys", [])
        if (
            isinstance(updated_keys, list)
            and bool({"status", "project_lifecycle"} & {str(value or "") for value in updated_keys})
            and str(event.get("event", "") or "") == "project_updated"
        ):
            timestamp = parse_local_iso_datetime(event.get("timestamp", ""))
            if timestamp is not None:
                candidates.append(timestamp.timestamp())
    if candidates:
        return max(candidates)
    for value in (
        project.get("paused_at", ""),
        project.get("updated_at", ""),
        state.get("paused_at", ""),
        state.get("updated_at", ""),
    ):
        timestamp = parse_local_iso_datetime(value)
        if timestamp is not None:
            candidates.append(timestamp.timestamp())
    return max(candidates) if candidates else 0.0

def auto_resume_paused_project_on_new_inbox(
    root: Path,
    project: dict[str, Any],
    state: dict[str, Any],
    *,
    actor: str,
) -> dict[str, Any]:
    lifecycle = project_lifecycle(project)
    if isinstance(project.get("inbox_auto_activate"), dict):
        policy = project.get("inbox_auto_activate", {})
    elif isinstance(project.get("inbox_auto_resume"), dict):
        policy = project.get("inbox_auto_resume", {})
    else:
        policy = {}
    if policy.get("enabled") is False:
        return {"attempted": True, "resumed": False, "activated": False, "reason": "disabled_by_project_policy"}
    if lifecycle in ACTIVE_PROJECT_LIFECYCLES:
        return {
            "attempted": False,
            "resumed": False,
            "activated": False,
            "reason": "project_already_active",
            "project_lifecycle": lifecycle,
        }
    blocked_lifecycles = {
        str(value or "").strip().lower()
        for value in policy.get("does_not_auto_activate", [])
        if str(value or "").strip()
    }
    if lifecycle in blocked_lifecycles:
        return {
            "attempted": False,
            "resumed": False,
            "activated": False,
            "reason": "project_lifecycle_explicitly_excluded_from_inbox_auto_activate",
            "project_lifecycle": lifecycle,
        }
    allowed_lifecycles = {
        str(value or "").strip().lower()
        for value in policy.get("auto_activate_lifecycles", [])
        if str(value or "").strip()
    } or INBOX_AUTO_ACTIVATE_PROJECT_LIFECYCLES
    if lifecycle not in allowed_lifecycles:
        return {
            "attempted": False,
            "resumed": False,
            "activated": False,
            "reason": "project_lifecycle_not_auto_activatable",
            "project_lifecycle": lifecycle,
        }

    latest_inbox = latest_advice_inbox_file(root)
    if not latest_inbox:
        return {"attempted": True, "resumed": False, "activated": False, "reason": "no_inbox_messages"}
    pause_epoch = project_pause_reference_epoch(root, project, state)
    latest_epoch = float(latest_inbox.get("mtime_epoch", 0.0) or 0.0)
    if latest_epoch <= pause_epoch:
        return {
            "attempted": True,
            "resumed": False,
            "activated": False,
            "reason": "no_inbox_message_newer_than_pause",
            "latest_inbox": latest_inbox,
            "pause_reference_epoch": pause_epoch,
        }

    timestamp = now_iso()
    updated_project = dict(project)
    set_project_lifecycle(updated_project, "active")
    updated_project["updated_at"] = timestamp
    updated_project["auto_resumed_from_inbox"] = {
        "timestamp": timestamp,
        "latest_inbox": latest_inbox,
        "pause_reference_epoch": pause_epoch,
    }
    write_json(root / "project.json", updated_project)

    updated_state = dict(state)
    set_operational_state(updated_state, "active")
    updated_state["updated_at"] = timestamp
    updated_state["last_inbox_auto_resume"] = {
        "timestamp": timestamp,
        "latest_inbox": latest_inbox,
        "pause_reference_epoch": pause_epoch,
    }
    write_json(get_state_path(root), updated_state)

    event = {
        "timestamp": timestamp,
        "actor": actor,
        "event": "project_auto_activated_from_inbox",
        "project_id": str(project.get("project_id", "") or root.name),
        "summary": "Auto-activated project because advice/inbox contains a message newer than the inactive lifecycle transition.",
        "previous_project_lifecycle": lifecycle,
        "latest_inbox": latest_inbox,
        "pause_reference_epoch": pause_epoch,
    }
    append_jsonl(get_ledger_path(root), event)
    append_lab_log(
        root,
        updated_project,
        title="Auto-activated project from new inbox advice",
        summary=event["summary"],
        event="project_auto_activated_from_inbox",
        actor=actor,
        details={
            "previous_project_lifecycle": lifecycle,
            "latest_inbox": latest_inbox,
            "pause_reference_epoch": pause_epoch,
        },
    )
    return {
        "attempted": True,
        "resumed": True,
        "activated": True,
        "reason": "new_inbox_message_after_inactive_lifecycle",
        "previous_project_lifecycle": lifecycle,
        "latest_inbox": latest_inbox,
        "pause_reference_epoch": pause_epoch,
    }

def default_project(project_id: str, objective: str, sample_id: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "project_id": slug(project_id),
        "objective": objective,
        "sample_id": sample_id or DEFAULT_SAMPLE_ID,
        "project_lifecycle": "active",
        "status": "active",
        "created_at": now_iso(),
        "research_architecture": {
            "project_structure_version": PROJECT_STRUCTURE_VERSION,
            "visible_structure": [
                "brief.md",
                "work/state.md",
                "work/notes/",
                "work/bridge_jobs/",
                ".manager/",
            ],
            "internal_state_root": PROJECT_INTERNAL_DIRNAME,
            "project_execution_agent_id": DEFAULT_RESEARCH_AGENT_ID,
            "project_execution_agent_model": "openai-codex/gpt-5.5",
            "project_execution_agent_thinking": "xhigh",
            "agent_role": "researcher",
            "python_role": "durable_state_queue_safety_audit_and_hard_boundaries",
            "project_json_scope": "policy_constraints_lifecycle_and_human_request",
            "research_state_path": RESEARCH_STATE_FILENAME,
            "research_agenda_path": RESEARCH_AGENDA_FILENAME,
            "shared_research_memory_path": str(NV_RESEARCH_MEMORY_PATH),
            "shared_research_knowledge_path": str(NV_RESEARCH_KNOWLEDGE_PATH),
            "shared_research_memory_required": True,
            "shared_research_knowledge_read_policy": "on_demand_by_memory_index",
            "evidence_registry_path": EVIDENCE_INDEX_FILENAME,
            "backlog_path": BACKLOG_FILENAME,
            "ledger_path": LEDGER_FILENAME,
            "state_path": STATE_FILENAME,
            "experiment_intent_flow": "agent_authored_intent_to_python_safety_verifier_to_bridge_tools",
            "backlog_role": "execution_queue_and_audit_not_complete_research_plan",
            "scheduler_role": "event_state_pointer_agent_selects_scientific_next_step",
            "vibe_physics_principles": [
                "small_retrievable_notes",
                "agent_updates_state_md_as_it_learns",
                "explicit_honesty_about_what_was_checked",
                "repeat_verification_until_no_new_issue_found",
                "cross_check_important_claims_with_independent_methods_or_models_when_available",
                "human_or_policy_sets_hard_boundaries_agent_owns_research_direction",
            ],
        },
        "shared_research_memory": shared_nv_research_memory_context(include_snapshot=True),
        "project_bootstrap_policy": {
            "preferred_flow": [
                "start-project",
                "cron_or_force_wake_nv_researcher",
                "nv_researcher_updates_research_agenda_or_backlog",
            ],
            "start_project_role": "preserve_human_request_and_create_durable_state",
            "direct_chat_main_role": "do_not_pretranslate_human_request_into_scientific_backlog",
            "project_manager_role": "state_queue_safety_audit_and_hard_boundaries",
            "initial_backlog_default": "empty_or_minimal_seed_only",
            "seed_backlog_contract": (
                "If a seed item is unavoidable, tell nv-researcher to read the human request, "
                "shared memory, project state, evidence, and hard bridge/hardware/code safety "
                "constraints, then start the same-wake runnable work loop from the next safe "
                "grounded task. Do not add scientific gates, "
                "shot-credit restrictions, accepted-corridor labels, or repeat-measurement "
                "blockers unless the operator explicitly asked for them."
            ),
        },
        "durable_record_policy": {
            "machine_consumed_records_language": "plain_english_ascii_preferred",
            "applies_to": [
                "human_advice",
                "work/notes",
                "backlog",
                "completion_markers",
                "stop_cancel_instructions",
                "project_notes",
            ],
            "reason": "avoid_mojibake_across_windows_wsl_slack_logs_and_keep_urgent_keywords_searchable",
            "user_facing_chat_language": "japanese_allowed",
        },
        "windows_codex_migration_policy": {
            "wsl_project_state_is_canonical": True,
            "windows_openclaw_projects_are": "scratch_migration_signal_not_active_runner",
            "import_before_autonomous_resume": [
                "<NV_BRIDGE_ROOT>/done",
                "<NV_BRIDGE_ROOT>/failed",
                "<NV_BRIDGE_ROOT>/status",
                "<MATLAB_23C_ROOT>/.openclaw/projects",
            ],
            "record_imported_facts_in": [
                EVIDENCE_INDEX_FILENAME,
                LAB_LOG_FILENAME,
                "human_advice.md",
                BACKLOG_FILENAME,
                "work/notes",
            ],
            "must_mark_superseded_or_canceled_evidence": True,
        },
        "evidence_policy": {
            "pulsed_odmr_resonance_evidence": {
                "valid_window_minutes": DEFAULT_PULSED_ODMR_RESONANCE_EVIDENCE_VALID_MINUTES,
                "separate_from_tracking_evidence": True,
                "analysis_required_before_downstream_use": True,
                "analysis_instruction": (
                    "For pulsed ODMR refresh/calibration jobs, do not request automatic "
                    "bridge-job fitting. Use terminal savedexperiment raw export and plots "
                    "as the first evidence handoff. If a downstream center is needed, the "
                    "project agent must base it on raw/readout-aware review plus a transparent "
                    "task-specific analysis or model comparison with recorded assumptions, "
                    "artifacts, provenance, and residual behavior."
                ),
                "non_authoritative_center_methods": [
                    "direct_minimum",
                    "local_quadratic",
                    "centroid",
                    "ad_hoc_tmp_podmr_scripts",
                ],
                "summary": (
                    "For this NV experimental system, execute-backed pulsed ODMR resonance evidence "
                    "is normally valid for about 5 hours / 300 minutes unless direct drift, calibration, or tracking "
                    "evidence contradicts it. Do not apply the shorter fresh-tracking window to pulsed "
                    "ODMR resonance evidence, and do not use direct-minimum-only or opaque default-fit "
                    "center choices as the downstream resonance without raw/readout-aware review."
                ),
            }
        },
        "tracking_cadence_policy": {
            "timezone": "local system time",
            "daytime_start_hour_local": DEFAULT_DAYTIME_START_HOUR_LOCAL,
            "nighttime_start_hour_local": DEFAULT_NIGHTTIME_START_HOUR_LOCAL,
            "daytime_max_untracked_window_seconds": DEFAULT_DAYTIME_MAX_UNTRACKED_WINDOW_SECONDS,
            "nighttime_max_untracked_window_seconds": DEFAULT_NIGHTTIME_MAX_UNTRACKED_WINDOW_SECONDS,
            "applies_to": "pre_enqueue_advisory drift_planning_window_seconds / per_average_seconds",
            "does_not_change": "Imaging GUI or legacy Experiment tracking_period defaults",
            "summary": (
                "For drift safety, plan tracking windows at about 10 minutes during daytime "
                "and 15 minutes at night. This is an agent/advisory planning policy, not an "
                "Imaging GUI default change."
            ),
        },
        "tracking_continuity_policy": {
            "continuous_tracking_overrides_absolute_position_match": True,
            "position_motion_alone_is_not_a_blocker": True,
            "record_motion_as_provenance": True,
            "continue_allowed_when": [
                "tracking_history_supports_continuous_tracking",
                "counts_and_alignment_are_healthy",
                "bridge_runtime_safety_gates_pass",
                "scientific_intent_remains_valid",
            ],
            "pause_or_recheck_when": [
                "tracking_loss",
                "counts_collapse",
                "unexplained_discontinuous_jump",
                "branch_switch_without_continuous_tracking_provenance",
                "hardware_safety_uncertainty",
                "project_specific_fixed_position_constraint",
            ],
            "summary": (
                "If the NV is continuously tracked and count/alignment evidence remains healthy, "
                "the experiment may continue even when the absolute position moves. Record the "
                "motion as provenance; do not block solely on mismatch to an older landmark cluster. "
                "Only pause or re-check for lost tracking, counts collapse, unexplained discontinuity, "
                "safety uncertainty, or an explicit fixed-position human constraint."
            ),
        },
        "imaging_tracking_recovery_policy": {
            "usual_nv_reference_dataset": {
                "path": "<NV_BRIDGE_ROOT>/status/openclaw_imaging/labeled_dataset_2026_03_12_onward",
                "files": [
                    "gold_labels.csv",
                    "image_index.csv",
                    "dataset_summary.json",
                    "README.md",
                    "gold_overlays",
                ],
                "helpers": {
                    "build_dataset": "<MATLAB_23C_ROOT>/claw/claw_build_imaging_tracking_label_dataset.m",
                    "evaluate_pattern_match": "<MATLAB_23C_ROOT>/claw/claw_evaluate_imaging_tracking_pattern_match.m",
                },
                "role": "prompt_visible_seed_selection_evidence_not_hard_gate",
                "helper_role": "refresh_or_evaluate_dataset_only; default integration reads existing CSV/JSON/overlay artifacts",
            },
            "legacy_landmark_route": {
                "enabled": False,
                "legacy_helpers": [
                    "claw_find_nv_by_landmarks",
                    "claw_nv_landmark_map",
                    "metadata.require_landmark_match=true",
                ],
            },
            "windows_bridge_implementation": {
                "recipe_registry": "<MATLAB_23C_ROOT>/claw/recipe_registry.m",
                "dispatch": "<MATLAB_23C_ROOT>/claw/run_23c_job.m",
                "validator": "<MATLAB_23C_ROOT>/claw/validate_job.m",
                "runner_diary": "<MATLAB_23C_ROOT>/claw/process_next_job.m",
                "queue_gate": "<MATLAB_23C_ROOT>/claw/claw_queue_execute_gate.m",
                "imaging_runner": "<MATLAB_23C_ROOT>/claw/claw_run_imaging_scan_local.m",
                "track_center_runner": "<MATLAB_23C_ROOT>/claw/claw_run_track_center_local.m",
                "seed_promotion": "<MATLAB_23C_ROOT>/claw/claw_promote_recent_nv_seed.m",
                "legacy_landmark_helpers": [
                    "<MATLAB_23C_ROOT>/claw/claw_find_nv_by_landmarks.m",
                    "<MATLAB_23C_ROOT>/claw/claw_nv_landmark_map.m",
                ],
            },
            "execute_gate": {
                "lab_opt_in": "NV_BRIDGE_QUEUE_EXECUTE_OPT_IN=1",
                "job_opt_in": "metadata.queue_execute_opt_in=true",
                "approval_token_required": False,
            },
            "atomic_enqueue_policy": {
                "required": True,
                "staging_directory_shape": "staging/<job_id>__staging",
                "queued_directory_shape": "queued/<job_id>",
                "rule": "write job.json completely under staging, then move the completed directory into queued",
                "failure_prevented": "NVBridge:MissingJSONFile from process_next_job seeing a half-created queued directory",
            },
            "preferred_seed_sources": [
                "recent_tracking_history",
                "explicit_human_seed",
                "usual_nv_label_dataset_evidence",
                "standalone_imaging_plus_agent_pattern_match_reasoning",
            ],
            "standalone_recipes": {
                "imaging_scan_v1": {
                    "role": "agent_selected_imaging_scan",
                    "preferred_enqueue_helper": "<OPENCLAW_WORKSPACE>/enqueue_nv_imaging_direct.py scan",
                    "requires_queue_execute_opt_in": True,
                    "requires_allow_stage_motion": True,
                },
                "track_center_v1": {
                    "role": "agent_selected_track_center_from_seed",
                    "preferred_enqueue_helper": "<OPENCLAW_WORKSPACE>/enqueue_nv_imaging_direct.py track",
                    "update_registry_default": False,
                    "supports_tracking_z_seed_offsets_um": True,
                },
            },
            "routing_rule": (
                "Use enqueue_nv_imaging_direct.py for standalone imaging_scan_v1 and track_center_v1 jobs. "
                "Do not route these non-sequence recipes through manifest-backed nv-batch/nv-queue submit-spec "
                "helpers unless those helpers have explicit top-level imaging/tracking support."
            ),
            "promotion_rule": (
                "TrackCenter results with update_registry=false are candidate evidence until "
                "nv-researcher explicitly decides to promote or continue."
            ),
        },
        "shot_budget_policy": {
            "calibration_total_shots_range": [
                DEFAULT_CALIBRATION_TOTAL_SHOTS_MIN,
                DEFAULT_CALIBRATION_TOTAL_SHOTS_MAX,
            ],
            "publication_quality_min_total_shots": DEFAULT_PUBLICATION_QUALITY_MIN_TOTAL_SHOTS,
            "publication_quality_target_sem_normalized_signal": DEFAULT_PUBLICATION_QUALITY_TARGET_SEM_NORMALIZED_SIGNAL,
            "normalized_signal_range": [0, 1],
            "total_shots_definition": "averages * repetitions",
            "sem_scaling_validation": (
                "Photon shot-noise sqrt(total shots) estimates are not sufficient by themselves. "
                "When savedexperiment data with at least two stored averages exists, run/use "
                "analyze_savedexperiment_sem_scaling.m to check cumulative average-to-average "
                "SEM against the expected 1/sqrt(K) trend before making publication-quality "
                "or marginal-shot-value claims."
            ),
            "preserve_total_shots_before_reducing_quality": True,
            "if_drift_limited": (
                "Prefer reducing repetitions per average and increasing averages, or splitting "
                "into shorter jobs, before reducing total shots."
            ),
            "claim_boundary": (
                "Calibration/scout/resonance/pulse checks are usually fine at 2e5-3e5 shots, "
                "but publication-level science data targeting about 5% SEM on normalized 0..1 "
                "signal needs at least 1.5e6 total shots. Do not call lower-shot data "
                "publication quality without explicit justification, and treat shot-noise-only "
                "SEM estimates as lower-bound sanity checks until savedexperiment average-to-average "
                "SEM scaling has been inspected when available."
            ),
        },
        "success_metrics": [],
        "autonomy": {
            "agent_capability_assumption": {
                "project_execution_agent": "codex_api_gpt_5_5_xhigh",
                "project_execution_agent_id": DEFAULT_RESEARCH_AGENT_ID,
                "research_judgment_owner": "agent",
                "python_role": "state_queue_safety_audit_and_hard_boundaries",
                "avoid_over_specifying_scientific_steps": True,
            },
            "max_autonomy_within_safety": True,
            "allow_agent_backlog_expansion": True,
            "continue_when_backlog_empty": True,
            "allow_autonomous_next_action_selection": True,
            "allow_project_state_updates": True,
            "allow_analysis": True,
            "allow_staging_sequence_authoring": True,
            "allow_analysis_code_changes": True,
            "allow_bridge_wrapper_code_changes": True,
            "allow_instrument_driver_code_changes": False,
            "allow_legacy_gui_code_changes": False,
            "allow_validate": True,
            "allow_dry_run": True,
            "allow_execute_existing_validated": True,
            "allow_physical_action_requests": True,
            "allow_procurement_proposals": True,
            "require_approval_for_execute": False,
            "require_approval_for_high_risk_changes": True,
            "require_code_change_review_before_execute": False,
            "require_physical_result_before_resume": True,
            "phase_execution": {
                "enabled": True,
                "preferred_unit": "same_wake_runnable_work_loop",
                "allow_pre_execute_chain_in_one_wake": True,
                "allow_execute_in_same_wake_when_ready": True,
                "execute_requires_separate_wake": False,
                "execute_can_follow_pre_execute_chain": True,
                "route_policy": {
                    "staging_new_or_changed": ["validate", "dry_run", "execute"],
                    "validated_manifest_recent_same_route_success_bounded": ["execute"],
                    "validated_manifest_optional_extra_confidence": ["validate", "execute"],
                },
                "pre_execute_chain": [
                    "build_or_adjust",
                    "validate_if_route_unknown_or_extra_confidence_needed",
                    "read_validate_terminal_evidence_if_invoked",
                    "dry_run_only_for_staging_new_changed_or_route_unknown",
                    "read_dry_run_terminal_evidence_if_invoked",
                    "prepare_execute_candidate",
                    "bridge_execute_submission",
                ],
                "coarse_task_contract": {
                    "next_action_kinds": ["advance_project", "blocked_external", "blocked_code", "blocked", "idle"],
                    "backlog_kinds": ["research_task", "external_request", "blocker"],
                    "fine_grained_work_classes_disabled": True,
                    "stale_fine_grained_labels_are_normalized": True,
                },
                "experiment_intent_contract": {
                    "enabled": True,
                    "agent_writes_scientific_intent": True,
                    "python_verifies_safety_and_queue_state": True,
                    "verified_intent_is_not_a_bridge_job": True,
                    "bridge_job_materialization_remains_with_existing_nv_batch_and_queue_tools": True,
                },
                "event_driven_research_agenda": {
                    "enabled": True,
                    "research_agenda_path": RESEARCH_AGENDA_FILENAME,
                    "bridge_jobs_dir": PROJECT_BRIDGE_JOBS_DIRNAME,
                    "events": [
                        "terminal_bridge_result",
                        "bridge_idle",
                        "new_human_advice",
                        "new_evidence",
                        "runtime_anomaly_or_drift_alert",
                        "scheduled_review",
                    ],
                    "backlog_priority_is_advisory": True,
                },
                "validated_manifest_bounded_execute_fast_path": True,
                "execute_reachability_priority": True,
                "same_wake_runnable_work_loop": True,
                "same_wake_runnable_work_loop_applies_to_all_task_types": True,
                "single_phase_stop_contract_disabled": True,
                "continue_after_queuing_next_runnable_item": True,
                "openclaw_freshness_and_provenance_checks_are_advisory": True,
                "dry_run_default_for_validated_manifest_fast_path": False,
                "short_validate_or_dry_run_should_not_wait_for_next_cron": True,
                "completion_marker_releases_inflight": True,
                "allow_parallel_project_work_during_bridge_running": True,
                "parallel_project_work_contract": {
                    "first_class_project_component": True,
                    "not_secondary_to_experiment": True,
                    "prefer_one_meaningful_non_monitoring_contribution": True,
                    "mid_run_monitoring_alone_is_not_default_endpoint": True,
                    "record_reason_when_skipping_non_monitoring_work": True,
                    "eligible_backlog_item_kind": "research_task",
                    "compatibility_item_field": "run_while_bridge_running",
                    "proactively_consider_when_waiting": [
                        "science_objective_analysis_of_completed_or_autosaved_data",
                        "science_objective_model_calculations_or_simulations",
                        "science_objective_literature_or_paper_pdf_review",
                        "figure_table_or_note_updates",
                        "evidence_gap_closure",
                        "backlog_cleanup_after_science_objective_options",
                    ],
                    "parallel_work_opportunity_review_enabled": True,
                    "parallel_work_opportunity_review_min_tick_interval_seconds": 1800,
                    "forbidden_during_running": [
                        "submit_bridge_job",
                        "mutate_bridge_queue",
                        "stop_running_job",
                        "mark_running_job_terminal_without_terminal_evidence"
                    ],
                    "bridge_queue_items_must_set": "requires_bridge_idle or touches_bridge_queue"
                },
                "stop_before_execute_unless_explicit_phase": False,
                "stop_when_bridge_running": False,
                "stop_bridge_touching_work_when_bridge_running": True,
                "bridge_running_does_not_stop_bridge_free_research": True,
                "wake_stop_conditions": [
                    "bridge_queued_or_running_blocks_next_bridge_touching_item_and_no_useful_bridge_free_project_work_remains",
                    "legacy_bridge_rejection_of_invoked_validate_dry_run_or_execute",
                    "missing_or_unmaterializable_payload",
                    "real_external_blocker",
                    "project_objective_for_this_wake_genuinely_exhausted",
                    "high_risk_change_outside_policy",
                ],
                "stop_on_validate_or_dry_run_failure": True,
                "stop_on_openclaw_safety_or_provenance_blocker": False,
                "stop_on_legacy_bridge_rejection": True,
                "stop_before_execute_only_for": [
                    "bridge_queued_or_running",
                    "missing_or_unmaterializable_payload",
                    "missing_manifest",
                    "legacy_bridge_rejection_of_invoked_validate_dry_run_or_execute",
                    "project_policy_explicitly_disallows_execute",
                ],
            },
        },
        "approval_policy": {
            "no_human_approval_required_for": {
                "validated_manifest_bounded_execute": True,
                "validate": True,
                "dry_run": True,
                "analysis": True,
                "low_risk_code_change": {
                    "enabled": True,
                    "classes": ["analysis_code", "bridge_wrapper"],
                    "bridge_wrapper_files": [
                        "project_schema.py",
                        "direct_plan_support.py",
                        "nv_batch_run.py",
                        "nv_bridge_runtime_watch.py",
                        "nv_project_scheduler_runner.py",
                        "nv_project_scheduler_runner.sh",
                        "nv_project_manager.py",
                        "submit_spec_utils.py"
                    ],
                    "requires_limited_allowed_write_scopes": True,
                    "requires_passed_verification": True,
                    "forbidden_change_classes": ["instrument_driver", "legacy_gui", "safety_policy"],
                    "forbidden_scopes": [
                        "<MATLAB_23C_ROOT>/**",
                        "instruments/**",
                        "start-controlsoftware/**",
                        "imaging/GUI/**",
                        "experiment/Functions/**",
                        "execute gate removal",
                        "manifest safety limits"
                    ],
                    "suppress_human_notification": True
                },
                "agent_trackable_nv_state_evidence": {
                    "enabled": True,
                    "requires_recent_tracking_evidence": True,
                    "max_evidence_age_minutes": 30,
                    "minimum_final_counts_kcps": 25,
                    "requires_queue_clear": True,
                    "requires_no_recent_alignment_failure": True,
                    "route_unmet_evidence_to_backlog": True
                }
            },
            "still_requires_human_approval_for": [
                "instrument_driver changes",
                "legacy GUI changes",
                "safety_policy changes",
                "hardware safety limit widening",
                "execute-gate changes",
                "manifest safety limit changes",
                "unknown non-trackable hardware/manual optical state"
            ]
        },
        "budgets": {
            "max_single_job_duration_seconds": 7200,
            "default_max_untracked_window_seconds": DEFAULT_DAYTIME_MAX_UNTRACKED_WINDOW_SECONDS,
        },
        "stop_conditions": [
            "the request would require editing or widening legacy bridge/MATLAB hardware safety limits",
            "bridge queued/running is not clear for bridge-touching queue submission or queue mutation",
            "the execute payload cannot be materialized from an available manifest and sequence",
            "legacy bridge validate, dry_run, or execute gate rejects the job",
            "high-risk code-change result is missing required review or verification evidence; low-risk auto-approved code changes require allowed-scope and passed-verification evidence",
        ],
    }

def default_backlog(project: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "project_id": str(project.get("project_id", "") or ""),
        "items": [],
    }

def init_project(args: argparse.Namespace) -> dict[str, Any]:
    if args.spec_json:
        project = read_json_arg(args.spec_json)
    elif args.spec_file:
        project = read_json(Path(args.spec_file).expanduser())
    else:
        project = default_project(args.project_id, args.objective, args.sample_id)

    project_id = slug(str(project.get("project_id", "") or args.project_id or args.objective))
    if not project_id:
        raise ValueError("Project id is required.")
    project["project_id"] = project_id
    if args.objective and not str(project.get("objective", "") or "").strip():
        project["objective"] = args.objective
    if args.sample_id and not str(project.get("sample_id", "") or "").strip():
        project["sample_id"] = args.sample_id
    shared_memory = ensure_shared_nv_research_memory_context(project, include_snapshot=True)
    sync_project_lifecycle_alias(project)
    project.setdefault("status", "active")
    project.setdefault("created_at", now_iso())

    root = project_dir(project_id)
    ensure_project_layout(root)
    knowledge_paths = ensure_project_knowledge_files(root, project)
    project_path = root / "project.json"
    if project_path.exists() and not args.force:
        raise ValueError(f"Project already exists: {project_path}. Use --force to replace the legacy project.json.")
    write_json(project_path, project)

    state = load_state(root)
    state.update(
        {
            "project_id": project_id,
            "updated_at": now_iso(),
            "last_next_action": {"kind": "advance_project", "reason": "project initialized"},
            "shared_research_memory": {
                "path": str(shared_memory.get("path", "")),
                "detailed_knowledge_path": str(shared_memory.get("detailed_knowledge_path", "")),
                "read_required": bool(shared_memory.get("read_required", True)),
                "read_policy": str(shared_memory.get("read_policy", "")),
                "snapshot_truncated": bool(shared_memory.get("snapshot_truncated", False)),
            },
        }
    )
    set_operational_state(state, "active")
    write_json(get_state_path(root), state)

    backlog_path = get_backlog_path(root)
    if not backlog_path.exists() or args.force:
        write_json(backlog_path, default_backlog(project))

    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "project_initialized",
            "project_id": project_id,
            "summary": str(project.get("objective", "") or ""),
            "shared_research_memory_path": str(shared_memory.get("path", "")),
            "shared_research_knowledge_path": str(shared_memory.get("detailed_knowledge_path", "")),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Project initialized",
        summary=str(project.get("objective", "") or ""),
        event="project_initialized",
        actor=args.actor,
        details={
            "project_id": project_id,
            "sample_id": str(project.get("sample_id", "") or DEFAULT_SAMPLE_ID),
            "shared_research_memory_path": str(shared_memory.get("path", "")),
            "shared_research_knowledge_path": str(shared_memory.get("detailed_knowledge_path", "")),
        },
    )
    return {
        "ok": True,
        "action": "init",
        "project_id": project_id,
        "project_dir": str(root),
        "project_path": str(project_path),
        "project_id": project_id,
        "project_dir": str(root),
        "project_path": str(project_path),
        "state_path": str(get_state_path(root)),
        "backlog_path": str(backlog_path),
        "research_state_path": knowledge_paths["research_state_path"],
        "research_agenda_path": knowledge_paths["research_agenda_path"],
        "shared_research_memory_path": knowledge_paths["shared_research_memory_path"],
        "shared_research_knowledge_path": knowledge_paths["shared_research_knowledge_path"],
        "evidence_index_path": knowledge_paths["evidence_index_path"],
        "experiment_intents_root": knowledge_paths["experiment_intents_root"],
        "lab_log_path": lab_log_paths["lab_log_path"],
        "daily_log_path": lab_log_paths["daily_log_path"],
    }

def append_human_request(root: Path, project: dict[str, Any], human_request: str) -> dict[str, str]:
    text = str(human_request or "").strip()
    if not text:
        raise ValueError("human request is required.")
    timestamp = now_iso()
    advice_path = root / "human_advice.md"
    if not advice_path.exists():
        advice_path.write_text("# Human Advice\n\n", encoding="utf-8")
    existing = advice_path.read_text(encoding="utf-8")
    if existing and not existing.endswith("\n"):
        existing += "\n"
    entry = "\n".join(
        [
            f"### {timestamp} - Initial Human Request",
            "",
            text,
            "",
        ]
    )
    advice_path.write_text(existing + entry, encoding="utf-8")
    return {
        "human_advice_path": str(advice_path),
        "recorded_at": timestamp,
        "preview": text[:500],
    }

def start_project(args: argparse.Namespace) -> dict[str, Any]:
    init_payload = init_project(args)
    project_id = str(init_payload.get("project_id", "") or args.project_id or "")
    root = project_dir(project_id)
    project = load_project(root)
    advice_record = append_human_request(root, project, args.human_request)

    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": advice_record["recorded_at"],
            "actor": args.actor,
            "event": "initial_human_request_recorded",
            "project_id": project_id,
            "summary": "Initial human request recorded for the research agent.",
            "human_advice_path": advice_record["human_advice_path"],
            "human_request_preview": advice_record["preview"],
            "source": "start-project",
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Initial human request recorded",
        summary=(
            "The initial human request was recorded in human_advice.md. "
            "The project agent should treat it as effective guidance and choose concrete research steps from evidence and policy."
        ),
        event="initial_human_request_recorded",
        actor=args.actor,
        details={
            "human_advice_path": advice_record["human_advice_path"],
            "human_request_preview": advice_record["preview"],
        },
    )
    state = load_state(root)
    state["updated_at"] = now_iso()
    state["last_human_request"] = {
        "recorded_at": advice_record["recorded_at"],
        "human_advice_path": advice_record["human_advice_path"],
        "preview": advice_record["preview"],
        "source": "start-project",
    }
    state["last_lab_log_entry"] = {
        "title": "Initial human request recorded",
        "event": "initial_human_request_recorded",
        "summary": "Initial human request recorded in human_advice.md.",
        "lab_log_path": lab_log_paths["lab_log_path"],
        "daily_log_path": lab_log_paths["daily_log_path"],
    }
    write_json(get_state_path(root), state)

    init_payload.update(
        {
            "action": "start_project",
            "human_advice_path": advice_record["human_advice_path"],
            "human_request_recorded_at": advice_record["recorded_at"],
            "lab_log_path": lab_log_paths["lab_log_path"],
            "daily_log_path": lab_log_paths["daily_log_path"],
        }
    )
    return init_payload

def update_project(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    if args.patch_json:
        patch = read_json_arg(args.patch_json)
    elif args.patch_file:
        patch = read_json(Path(args.patch_file).expanduser())
    else:
        patch = {}
    if not patch:
        raise ValueError("project patch is required.")
    if "project_lifecycle" in patch and "status" not in patch:
        patch["status"] = str(patch.get("project_lifecycle", "") or "")
    elif "status" in patch and "project_lifecycle" not in patch:
        patch["project_lifecycle"] = str(patch.get("status", "") or "")
    if "project_id" in patch and slug(str(patch.get("project_id", "") or "")) != str(project.get("project_id", "") or root.name):
        raise ValueError("project_id/project_id cannot be changed by update-project.")
    patch.pop("project_id", None)
    updated = deep_merge_dicts(project, patch)
    sync_project_lifecycle_alias(updated)
    updated["updated_at"] = now_iso()
    write_json(root / "project.json", updated)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "project_updated",
            "project_id": str(project.get("project_id", "") or root.name),
            "summary": args.summary or "Updated project policy/spec.",
            "updated_keys": sorted(patch.keys()),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        updated,
        title="Project updated",
        summary=args.summary or "Updated project policy/spec.",
        event="project_updated",
        actor=args.actor,
        details={"updated_keys": sorted(patch.keys())},
    )
    state = load_state(root)
    state["updated_at"] = now_iso()
    state["last_project_update"] = {
        "summary": args.summary or "Updated project policy/spec.",
        "updated_keys": sorted(patch.keys()),
    }
    write_json(get_state_path(root), state)
    return {
        "ok": True,
        "action": "update_project",
        "project_id": str(updated.get("project_id", "") or root.name),
        "project_path": str(root / "project.json"),
        "project_id": str(updated.get("project_id", "") or root.name),
        "project_path": str(root / "project.json"),
        "updated_keys": sorted(patch.keys()),
        "lab_log_path": lab_log_paths["lab_log_path"],
    }

def pending_backlog_overview(root: Path) -> dict[str, Any]:
    backlog_path = get_backlog_path(root)
    if not backlog_path.is_file():
        return {"count": 0, "preview": []}
    backlog = read_json(backlog_path)
    items = backlog.get("items", [])
    if not isinstance(items, list):
        return {"count": 0, "preview": []}
    pending: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        if str(item.get("status", "pending") or "pending") != "pending":
            continue
        pending.append(
            {
                "id": str(item.get("id", "") or ""),
                "kind": normalize_backlog_kind(item),
                "blocker_type": str(item.get("blocker_type", "") or ""),
                "request_kind": str(item.get("request_kind", "") or ""),
                "run_while_bridge_running": bool(item.get("run_while_bridge_running", item.get("can_run_while_bridge_running", False))),
                "requires_bridge_idle": bool(item.get("requires_bridge_idle", False)),
                "touches_bridge_queue": bool(item.get("touches_bridge_queue", False)),
                "priority": str(item.get("priority", "") or ""),
                "summary": str(item.get("summary", "") or ""),
                "agent_prompt": str(item.get("agent_prompt", "") or ""),
            }
        )
    return {"count": len(pending), "preview": pending[:20]}

def load_backlog(root: Path, project: dict[str, Any]) -> dict[str, Any]:
    backlog_path = get_backlog_path(root)
    if backlog_path.is_file():
        backlog = read_json(backlog_path)
    else:
        backlog = default_backlog(project)
    items = backlog.get("items", [])
    if not isinstance(items, list):
        backlog["items"] = []
    backlog.setdefault("schema_version", 1)
    backlog.setdefault("project_id", str(project.get("project_id", "") or root.name))
    return backlog

def is_pending_approval_backlog_item(item: dict[str, Any]) -> bool:
    if str(item.get("status", "pending") or "pending") != "pending":
        return False
    kind = str(item.get("kind", "") or "").strip().lower()
    blocker_type = str(item.get("blocker_type", "") or "").strip().lower()
    return (
        kind == "wait_for_approval"
        or (kind == "blocker" and blocker_type in {"approval", "wait_for_approval", "backlog_approval"})
    )

SCIENTIFIC_UNCERTAINTY_BLOCKER_TYPES = {
    "ambiguous_candidate",
    "ambiguous_result",
    "candidate_only",
    "interpretation_uncertainty",
    "invalid_resonance",
    "low_counts",
    "low_trackcenter_counts",
    "low_trackcenter_counts_after_fresh_usual_identity",
    "no_candidate",
    "no_current_candidate",
    "no_robust_claim",
    "no_useful_candidate",
    "no_valid_resonance",
    "science_strategy",
    "scientific_strategy",
    "strategy",
    "strategy_guidance",
    "valid_resonance_false",
}


SCIENTIFIC_UNCERTAINTY_BLOCKER_PHRASES = (
    "ambiguous candidate",
    "ambiguous result",
    "candidate only",
    "current-position/count gate",
    "interpretation uncertainty",
    "invalid resonance",
    "low counts",
    "low trackcenter counts",
    "no current candidate",
    "no robust",
    "no useful candidate",
    "no valid resonance",
    "science strategy",
    "scientific strategy",
    "strategy blocker",
    "valid_resonance=false",
)


def is_scientific_uncertainty_backlog_blocker_item(item: dict[str, Any]) -> bool:
    """Return whether a pending blocker is actually agent-side science strategy work."""
    if str(item.get("kind", "") or "").strip().lower() != "blocker":
        return False
    blocker_type = str(item.get("blocker_type", "") or "").strip().lower()
    if blocker_type in SCIENTIFIC_UNCERTAINTY_BLOCKER_TYPES:
        return True
    haystack = " ".join(
        str(item.get(key, "") or "")
        for key in ("id", "summary", "agent_prompt", "request_kind")
    ).lower()
    return any(phrase in haystack for phrase in SCIENTIFIC_UNCERTAINTY_BLOCKER_PHRASES)


def latest_approval_telegram_record(root: Path, item_id: str) -> dict[str, Any]:
    ledger_path = get_ledger_path(root)
    if not ledger_path.is_file():
        return {}
    latest: dict[str, Any] = {}
    try:
        lines = ledger_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return {}
    for line in lines:
        text = line.strip()
        if not text:
            continue
        try:
            record = json.loads(text)
        except json.JSONDecodeError:
            continue
        if not isinstance(record, dict):
            continue
        if str(record.get("event", "") or "") != "telegram_notification":
            continue
        if str(record.get("request_type", "") or "") not in {"approval", "backlog_approval", "wait_for_approval"}:
            continue
        if str(record.get("request_id", "") or "") != item_id and str(record.get("backlog_item_id", "") or "") != item_id:
            continue
        latest = record
    return latest

def approval_notification_already_recorded(root: Path, item: dict[str, Any]) -> dict[str, Any]:
    item_id = str(item.get("id", "") or "")
    if not item_id:
        return {"already_recorded": False, "reason": "missing_item_id"}
    if bool(item.get("approval_notification_sent", False)):
        return {"already_recorded": True, "reason": "item_approval_notification_sent"}
    if bool(item.get("approval_notification_attempted", False)):
        return {"already_recorded": True, "reason": "item_approval_notification_attempted"}
    ledger_record = latest_approval_telegram_record(root, item_id)
    if ledger_record:
        return {
            "already_recorded": True,
            "reason": "ledger_telegram_notification_exists",
            "ledger_record": ledger_record,
        }
    return {"already_recorded": False, "reason": ""}

def notify_approval_backlog_item_if_needed(
    root: Path,
    project: dict[str, Any],
    backlog: dict[str, Any],
    item: dict[str, Any],
    *,
    actor: str,
) -> dict[str, Any]:
    if not is_pending_approval_backlog_item(item):
        return {"attempted": False, "sent": False, "reason": "not_pending_approval_blocker"}

    item_id = str(item.get("id", "") or "")
    duplicate = approval_notification_already_recorded(root, item)
    if bool(duplicate.get("already_recorded", False)):
        ledger_record = duplicate.get("ledger_record", {}) if isinstance(duplicate.get("ledger_record"), dict) else {}
        item["approval_notification_attempted"] = True
        item["approval_notification_checked_at"] = now_iso()
        item["approval_notification_suppressed_reason"] = str(duplicate.get("reason", "") or "")
        if bool(ledger_record.get("sent", False)):
            item["approval_notification_sent"] = True
            item.setdefault("approval_notification_sent_at", str(ledger_record.get("timestamp", "") or now_iso()))
        write_json(get_backlog_path(root), backlog)
        return {
            "attempted": False,
            "sent": bool(item.get("approval_notification_sent", False)),
            "suppressed": True,
            "reason": str(duplicate.get("reason", "") or ""),
        }

    extra = {
        "backlog_item_id": item_id,
        "kind": str(item.get("kind", "") or ""),
        "priority": str(item.get("priority", "") or ""),
    }
    for key in (
        "resume_conditions",
        "blocked_reason",
        "related_backlog_item_id",
        "fresh_supporting_evidence_expires_at",
        "recommended_mw_freq_hz_if_approved_while_still_fresh",
    ):
        if key in item:
            extra[key] = item.get(key)

    result = notify_project_request(
        root,
        project,
        request_type="approval",
        request_id=item_id,
        summary=str(item.get("summary", "") or ""),
        request_path=get_backlog_path(root),
        blocking=True,
        extra=extra,
    )
    timestamp = now_iso()
    item["approval_notification_attempted"] = bool(result.get("attempted", False))
    item["approval_notification_attempted_at"] = timestamp
    item["approval_notification_result"] = {
        "attempted": bool(result.get("attempted", False)),
        "sent": bool(result.get("sent", False)),
        "reason": str(result.get("reason", "") or ""),
        "returncode": result.get("returncode", ""),
    }
    if bool(result.get("sent", False)):
        item["approval_notification_sent"] = True
        item["approval_notification_sent_at"] = timestamp
    write_json(get_backlog_path(root), backlog)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": timestamp,
            "actor": actor,
            "event": "approval_backlog_notification_checked",
            "project_id": str(project.get("project_id", "") or root.name),
            "backlog_item_id": item_id,
            "attempted": bool(result.get("attempted", False)),
            "sent": bool(result.get("sent", False)),
            "reason": str(result.get("reason", "") or ""),
        },
    )
    return result

def notify_pending_approval_backlog_items(root: Path, project: dict[str, Any], *, actor: str) -> list[dict[str, Any]]:
    backlog = load_backlog(root, project)
    results: list[dict[str, Any]] = []
    for item in backlog.get("items", []):
        if not isinstance(item, dict):
            continue
        if not is_pending_approval_backlog_item(item):
            continue
        result = notify_approval_backlog_item_if_needed(root, project, backlog, item, actor=actor)
        results.append({"backlog_item_id": str(item.get("id", "") or ""), **result})
    return results

def queue_backlog_item(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    backlog = load_backlog(root, project)
    item = read_json_arg(args.item_json)
    item_id = slug(str(item.get("id", "") or args.item_id or item.get("summary", "") or f"item_{now_iso()}"))
    if not item_id:
        raise ValueError("backlog item id is required.")
    existing_ids = {
        str(existing.get("id", "") or "")
        for existing in backlog.get("items", [])
        if isinstance(existing, dict)
    }
    if item_id in existing_ids and not args.force:
        raise ValueError(f"backlog item already exists: {item_id}. Use --force to replace it.")

    item.update(
        {
            "id": item_id,
            "status": str(item.get("status", "") or "pending"),
        }
    )
    item["kind"] = normalize_backlog_kind(item)
    if is_scientific_uncertainty_backlog_blocker_item(item):
        blocker_type = str(item.pop("blocker_type", "") or "").strip()
        item["former_kind"] = "blocker"
        if blocker_type:
            item["strategy_issue_type"] = blocker_type
        item["kind"] = "research_task"
        item["kind_normalized"] = True
        item["normalization_note"] = (
            "Scientific uncertainty and route failures are agent-side bridge-free work, "
            "not external blockers."
        )
        item.setdefault(
            "agent_prompt",
            "Resolve this issue bridge-free through synthesis, notes/evidence/backlog updates, "
            "and the next safe research_task when possible. Ask the operator only for physical/manual "
            "apparatus checks, explicit STOP/approval ordering, code/safety work, or hard "
            "bridge/hardware failures that cannot be handled by agent-side recovery.",
        )
    if str(item.get("status", "") or "") not in VALID_BACKLOG_STATUSES:
        raise ValueError(f"backlog status must be one of {sorted(VALID_BACKLOG_STATUSES)}.")
    item.setdefault("priority", "normal")
    item.setdefault("summary", "")
    item.setdefault("created_at", now_iso())

    items = []
    replaced = False
    for existing in backlog.get("items", []):
        if isinstance(existing, dict) and str(existing.get("id", "") or "") == item_id:
            items.append(item)
            replaced = True
        else:
            items.append(existing)
    if not replaced:
        items.append(item)
    backlog["items"] = items
    write_json(get_backlog_path(root), backlog)

    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "backlog_item_queued" if not replaced else "backlog_item_replaced",
            "project_id": str(project.get("project_id", "") or root.name),
            "backlog_item_id": item_id,
            "kind": str(item.get("kind", "") or ""),
            "summary": str(item.get("summary", "") or ""),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Backlog item queued" if not replaced else "Backlog item replaced",
        summary=str(item.get("summary", "") or ""),
        event="backlog_item_queued" if not replaced else "backlog_item_replaced",
        actor=args.actor,
        details={
            "backlog_item_id": item_id,
            "kind": str(item.get("kind", "") or ""),
            "priority": str(item.get("priority", "") or ""),
            "status": str(item.get("status", "") or ""),
        },
    )
    approval_notification = notify_approval_backlog_item_if_needed(
        root,
        project,
        backlog,
        item,
        actor=args.actor,
    )
    return {
        "ok": True,
        "action": "queue_backlog_item",
        "project_id": str(project.get("project_id", "") or root.name),
        "backlog_item_id": item_id,
        "replaced": replaced,
        "backlog_path": str(get_backlog_path(root)),
        "lab_log_path": lab_log_paths["lab_log_path"],
        "approval_notification": approval_notification,
    }

def update_backlog_item(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    backlog = load_backlog(root, project)
    item_id = slug(str(args.item_id or ""))
    if not item_id:
        raise ValueError("backlog item id is required.")
    status = str(args.status or "").strip()
    if status and status not in VALID_BACKLOG_STATUSES:
        raise ValueError(f"backlog status must be one of {sorted(VALID_BACKLOG_STATUSES)}.")
    details = read_json_arg(args.update_json) if args.update_json else {}

    updated_item: dict[str, Any] | None = None
    for item in backlog.get("items", []):
        if not isinstance(item, dict):
            continue
        if str(item.get("id", "") or "") != item_id:
            continue
        if status:
            item["status"] = status
        if args.summary:
            item["last_summary"] = args.summary
        for key, value in details.items():
            if key not in {"id", "project_id"}:
                item[key] = value
        item["updated_at"] = now_iso()
        updated_item = item
        break
    if updated_item is None:
        raise ValueError(f"backlog item not found: {item_id}")

    write_json(get_backlog_path(root), backlog)
    state = load_state(root)
    state["updated_at"] = now_iso()
    state["last_backlog_update"] = {
        "item_id": item_id,
        "status": str(updated_item.get("status", "") or ""),
        "summary": args.summary,
    }
    write_json(get_state_path(root), state)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "backlog_item_updated",
            "project_id": str(project.get("project_id", "") or root.name),
            "backlog_item_id": item_id,
            "status": str(updated_item.get("status", "") or ""),
            "summary": args.summary,
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Backlog item updated",
        summary=args.summary or str(updated_item.get("summary", "") or ""),
        event="backlog_item_updated",
        actor=args.actor,
        details={
            "backlog_item_id": item_id,
            "status": str(updated_item.get("status", "") or ""),
        },
    )
    approval_notification = notify_approval_backlog_item_if_needed(
        root,
        project,
        backlog,
        updated_item,
        actor=args.actor,
    )
    marker_event = {
        "event": "backlog_item_terminal_evidence_recorded",
        "timestamp": now_iso(),
        "backlog_item_id": item_id,
        "summary": args.summary,
    }
    for key, value in details.items():
        marker_event[key] = value
    completion_marker = maybe_write_terminal_evidence_completion_marker(
        root,
        project,
        marker_event,
        actor=args.actor,
        source="update_backlog_item",
    )
    return {
        "ok": True,
        "action": "update_backlog_item",
        "project_id": str(project.get("project_id", "") or root.name),
        "backlog_item_id": item_id,
        "status": str(updated_item.get("status", "") or ""),
        "backlog_path": str(get_backlog_path(root)),
        "lab_log_path": lab_log_paths["lab_log_path"],
        "approval_notification": approval_notification,
        "completion_marker": completion_marker,
    }

def list_pending_physical_requests(root: Path) -> list[dict[str, Any]]:
    queued = root / "physical_action_requests" / "queued"
    requests: list[dict[str, Any]] = []
    for path in sorted(queued.glob("*.json")):
        try:
            payload = read_json(path)
        except Exception:
            continue
        payload["_path"] = str(path)
        requests.append(payload)
    return requests

def list_pending_code_change_requests(root: Path) -> list[dict[str, Any]]:
    queued = root / "code_change_requests" / "queued"
    requests: list[dict[str, Any]] = []
    for path in sorted(queued.glob("*.json")):
        try:
            payload = read_json(path)
        except Exception:
            continue
        payload["_path"] = str(path)
        requests.append(payload)
    return requests

def default_code_change_risk(change_class: str) -> str:
    if change_class in {"sequence_staging", "analysis_code"}:
        return "autonomous_staging"
    if change_class == "bridge_wrapper":
        return "scoped_bridge_wrapper"
    if change_class == "instrument_driver":
        return "supervised_hardware"
    if change_class == "legacy_gui":
        return "legacy_gui_review"
    return "safety_stop"

def validate_code_change_request(request: dict[str, Any]) -> None:
    change_class = str(request.get("change_class", "") or "sequence_staging").strip()
    if change_class not in VALID_CODE_CHANGE_CLASSES:
        raise ValueError(f"change_class must be one of {sorted(VALID_CODE_CHANGE_CLASSES)}.")

    allowed_write_scopes = request.get("allowed_write_scopes", [])
    if not (isinstance(allowed_write_scopes, list) and any(str(item or "").strip() for item in allowed_write_scopes)):
        raise ValueError(f"change_class={change_class} requires non-empty allowed_write_scopes.")

    if change_class in {"instrument_driver", "legacy_gui", "safety_policy"}:
        request["review_required"] = True
        request["blocking"] = True

def approval_policy(project: dict[str, Any]) -> dict[str, Any]:
    policy = project.get("approval_policy", {})
    return policy if isinstance(policy, dict) else {}

def no_human_approval_policy(project: dict[str, Any]) -> dict[str, Any]:
    policy = approval_policy(project).get("no_human_approval_required_for", {})
    return policy if isinstance(policy, dict) else {}

def auto_code_change_policy(project: dict[str, Any]) -> dict[str, Any]:
    policy = no_human_approval_policy(project).get("low_risk_code_change", {})
    return policy if isinstance(policy, dict) else {}

def normalized_scope_text(value: Any) -> str:
    text = str(value or "").strip().replace("\\", "/")
    text = re.sub(r"/+", "/", text)
    return text.strip("/")

def path_matches_scope(path_text: str, scope_text: str) -> bool:
    path_norm = normalized_scope_text(path_text)
    scope_norm = normalized_scope_text(scope_text)
    if not path_norm or not scope_norm:
        return False
    if scope_norm.endswith("/**"):
        prefix = scope_norm[:-3].rstrip("/")
        return path_norm == prefix or path_norm.startswith(prefix + "/")
    if scope_norm.endswith("/*"):
        prefix = scope_norm[:-2].rstrip("/")
        if not (path_norm == prefix or path_norm.startswith(prefix + "/")):
            return False
        remainder = path_norm[len(prefix):].strip("/")
        return bool(remainder) and "/" not in remainder
    return path_norm == scope_norm or path_norm.endswith("/" + scope_norm)

def changed_files_within_allowed_scopes(changed_files: list[Any], allowed_write_scopes: list[Any]) -> bool:
    files = [str(item or "").strip() for item in changed_files if str(item or "").strip()]
    scopes = [str(item or "").strip() for item in allowed_write_scopes if str(item or "").strip()]
    if not files or not scopes:
        return False
    return all(any(path_matches_scope(path, scope) for scope in scopes) for path in files)

def allowed_write_scopes_are_limited(allowed_write_scopes: list[Any]) -> bool:
    broad_roots = {
        "",
        "home",
        "home/<USER>",
        "home/<USER>/.openclaw",
        "home/<USER>/OPENCLAW_WORKSPACE",
        "mnt",
        "mnt/z",
        "mnt/z/qeg",
        "mnt/z/qeg/documents",
        "mnt/z/qeg/documents/matlab",
        "mnt/z/qeg/documents/matlab/23-c",
    }
    scopes = [normalized_scope_text(item).lower() for item in allowed_write_scopes if str(item or "").strip()]
    if not scopes:
        return False
    for scope in scopes:
        if scope in broad_roots:
            return False
        if scope.endswith("/**"):
            prefix = scope[:-3].rstrip("/")
            if prefix in broad_roots or prefix.count("/") < 4:
                return False
        if scope.endswith("/*"):
            prefix = scope[:-2].rstrip("/")
            if prefix in broad_roots or prefix.count("/") < 4:
                return False
    return True

def has_forbidden_code_change_path(value: Any) -> bool:
    text = normalized_scope_text(value).lower()
    forbidden_fragments = (
        "<MATLAB_23C_ROOT>",
        "mnt/z/qeg/documents/matlab/23-c",
        "<MATLAB_23C_ROOT>",
        "instrument",
        "start-controlsoftware",
        "imaging/gui",
        "experiment/functions",
        "execute gate",
        "manifest safety",
        "safety_policy",
    )
    return any(fragment in text for fragment in forbidden_fragments)

def verification_passed_for_auto_resume(result: dict[str, Any]) -> bool:
    verification = result.get("verification", [])
    if not isinstance(verification, list) or not verification:
        return False
    passed_kinds = set()
    for entry in verification:
        if not isinstance(entry, dict):
            return False
        status = str(entry.get("status", "") or "").strip().lower()
        if status in {"failed", "unsafe", "declined", "needs_review", "needs_verification"}:
            return False
        if status == "passed":
            passed_kinds.add(str(entry.get("kind", "") or "").strip().lower())
    if not passed_kinds:
        return False
    required_tokens = ("syntax", "test", "smoke", "verification", "captured_status")
    return any(any(token in kind for token in required_tokens) for kind in passed_kinds)

def code_change_auto_approval_decision(
    project: dict[str, Any],
    request: dict[str, Any],
    result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    policy = auto_code_change_policy(project)
    if not bool(policy.get("enabled", False)):
        return {"eligible": False, "reason": "low-risk code-change auto-approval policy is disabled"}

    change_class = str(request.get("change_class", "") or "").strip()
    allowed_classes = [str(item or "").strip() for item in policy.get("classes", [])]
    if change_class not in allowed_classes:
        return {"eligible": False, "reason": f"change_class={change_class} is not auto-approvable"}

    allowed_scopes = request.get("allowed_write_scopes", [])
    if not isinstance(allowed_scopes, list) or not any(str(item or "").strip() for item in allowed_scopes):
        return {"eligible": False, "reason": "allowed_write_scopes is empty"}
    if any(has_forbidden_code_change_path(scope) for scope in allowed_scopes):
        return {"eligible": False, "reason": "allowed_write_scopes include a forbidden hardware or MATLAB tree scope"}
    if bool(policy.get("requires_limited_allowed_write_scopes", True)) and not allowed_write_scopes_are_limited(allowed_scopes):
        return {"eligible": False, "reason": "allowed_write_scopes are too broad for auto approval"}

    if change_class == "bridge_wrapper":
        wrapper_files = [str(item or "").strip() for item in policy.get("bridge_wrapper_files", [])]
        if not wrapper_files:
            return {"eligible": False, "reason": "no bridge wrapper files are auto-approvable"}
        changed_files = result.get("changed_files", []) if isinstance(result, dict) else []
        if not changed_files:
            if not changed_files_within_allowed_scopes(allowed_scopes, wrapper_files):
                return {"eligible": False, "reason": "bridge wrapper allowed scopes are outside the auto-approvable wrapper list"}
            return {"eligible": True, "reason": "bridge wrapper request is limited to an auto-approvable surface"}
        if not changed_files_within_allowed_scopes(changed_files, wrapper_files):
            return {"eligible": False, "reason": "bridge wrapper changed files are outside the auto-approvable wrapper list"}

    if isinstance(result, dict):
        if str(result.get("status", "") or "") != "completed":
            return {"eligible": False, "reason": "result is not completed"}
        changed_files = result.get("changed_files", [])
        if not isinstance(changed_files, list) or not changed_files:
            return {"eligible": False, "reason": "changed_files is empty"}
        if any(has_forbidden_code_change_path(path) for path in changed_files):
            return {"eligible": False, "reason": "changed_files include a forbidden hardware or MATLAB tree path"}
        if not changed_files_within_allowed_scopes(changed_files, allowed_scopes):
            return {"eligible": False, "reason": "changed_files are outside allowed_write_scopes"}
        if not verification_passed_for_auto_resume(result):
            return {"eligible": False, "reason": "required verification did not pass"}

    return {"eligible": True, "reason": "low-risk code-change policy allows auto resume without human approval"}

def read_code_change_request_record(root: Path, request_id: str) -> dict[str, Any]:
    candidates = [
        root / "code_change_requests" / "queued" / f"{request_id}.json",
        root / "code_change_requests" / "done" / f"{request_id}.request.json",
        root / "code_change_requests" / "failed" / f"{request_id}.request.json",
    ]
    for path in candidates:
        if path.is_file():
            try:
                return read_json(path)
            except Exception:
                return {}
    return {}

def apply_auto_code_change_resume_if_allowed(
    project: dict[str, Any],
    request: dict[str, Any],
    result: dict[str, Any],
) -> dict[str, Any]:
    if bool(result.get("resume_ok", False)):
        return {"applied": False, "reason": "resume_ok already true"}
    decision = code_change_auto_approval_decision(project, request, result)
    if not bool(decision.get("eligible", False)):
        return {"applied": False, "reason": str(decision.get("reason", "") or "")}

    review = result.get("review", {})
    if not isinstance(review, dict):
        review = {}
    review.update(
        {
            "required": False,
            "status": "auto_approved",
            "approved_by": "project_auto_approval_policy",
            "approved_at": now_iso(),
            "evidence": str(decision.get("reason", "") or ""),
        }
    )
    result["review"] = review
    result["resume_ok"] = True
    result["auto_approval"] = {
        "applied": True,
        "policy": "no_human_approval_required_for.low_risk_code_change",
        "reason": str(decision.get("reason", "") or ""),
    }
    return {"applied": True, "reason": str(decision.get("reason", "") or "")}

def agent_trackable_nv_state_evidence_policy(project: dict[str, Any]) -> dict[str, Any]:
    approval = no_human_approval_policy(project)
    policy = approval.get("agent_trackable_nv_state_evidence", {})
    if isinstance(policy, dict) and policy:
        return policy
    legacy_policy = approval.get("agent_trackable_nv_state_confirmation", {})
    if isinstance(legacy_policy, dict) and legacy_policy:
        return legacy_policy
    legacy_policy = approval.get("physical_state_good_confirmation", {})
    return legacy_policy if isinstance(legacy_policy, dict) else {}

def agent_trackable_nv_state_confirmation_policy(project: dict[str, Any]) -> dict[str, Any]:
    return agent_trackable_nv_state_evidence_policy(project)

def physical_state_confirmation_policy(project: dict[str, Any]) -> dict[str, Any]:
    return agent_trackable_nv_state_evidence_policy(project)

def parse_local_iso_datetime(value: Any) -> datetime | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone().replace(tzinfo=None)
    return parsed

def recent_jsonl_records(path: Path, max_lines: int = 300) -> list[dict[str, Any]]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            lines = handle.readlines()[-max_lines:]
    except OSError:
        return []
    records: list[dict[str, Any]] = []
    for line in lines:
        text = line.strip()
        if not text:
            continue
        try:
            payload = json.loads(text)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            records.append(payload)
    return records

def sample_matches_tracking_event(event: dict[str, Any], sample_id: str) -> bool:
    if not sample_id:
        return True
    needle = sample_id.strip().lower()
    fields = [
        event.get("sample_id", ""),
        event.get("nv_name", ""),
        event.get("requested_name", ""),
    ]
    context = event.get("context", {})
    if isinstance(context, dict):
        fields.extend([context.get("sample_id", ""), context.get("nv_name", ""), context.get("requested_name", "")])
    clean_fields = [str(item or "").strip().lower() for item in fields if str(item or "").strip()]
    return not clean_fields or needle in clean_fields

def bridge_queue_counts(bridge_root: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    for name in ("queued", "running"):
        folder = bridge_root / name
        try:
            counts[name] = sum(1 for path in folder.glob("*.json") if path.is_file())
        except OSError:
            counts[name] = -1
    return counts

def tracking_evidence_sufficient_for_agent_trackable_nv_state(root: Path, project: dict[str, Any]) -> dict[str, Any]:
    policy = agent_trackable_nv_state_evidence_policy(project)
    if not bool(policy.get("enabled", False)):
        return {"ok": False, "reason": "agent-trackable NV-state evidence policy is disabled"}
    if not bool(policy.get("requires_recent_tracking_evidence", True)):
        return {"ok": False, "reason": "policy does not permit tracking-only evidence"}

    bridge_root = Path(str(policy.get("bridge_root", "") or "<NV_BRIDGE_ROOT>"))
    tracking_path = Path(str(policy.get("tracking_history_path", "") or bridge_root / "status" / "tracking_history.jsonl"))
    records = recent_jsonl_records(tracking_path)
    if not records:
        return {"ok": False, "reason": f"no readable tracking history at {tracking_path}"}

    sample_id = str(project.get("sample_id", "") or DEFAULT_SAMPLE_ID)
    now = datetime.now()
    max_age_minutes = float(policy.get("max_evidence_age_minutes", 30) or 30)
    minimum_final_counts_kcps = float(policy.get("minimum_final_counts_kcps", 25) or 25)
    candidates: list[tuple[datetime, dict[str, Any]]] = []
    for record in records:
        if str(record.get("event_kind", "") or "") != "tracking_event":
            continue
        finished_at = parse_local_iso_datetime(record.get("finished_at", ""))
        if finished_at is None or not sample_matches_tracking_event(record, sample_id):
            continue
        status = str(record.get("status", "") or "").strip().lower()
        if status == "completed" and isinstance(record.get("final_counts_kcps", None), (int, float)):
            candidates.append((finished_at, record))

    if not candidates:
        return {"ok": False, "reason": f"no completed tracking event found for {sample_id}"}
    latest_finished_at, latest = max(candidates, key=lambda item: item[0])
    latest_age_minutes = max(0.0, (now - latest_finished_at).total_seconds() / 60.0)
    latest_counts = float(latest.get("final_counts_kcps", 0.0) or 0.0)
    if latest_age_minutes > max_age_minutes:
        return {
            "ok": False,
            "reason": f"latest tracking evidence is stale: {latest_age_minutes:.1f} min > {max_age_minutes:.1f} min",
            "latest_finished_at": str(latest.get("finished_at", "") or ""),
            "latest_final_counts_kcps": latest_counts,
        }
    if latest_counts < minimum_final_counts_kcps:
        return {
            "ok": False,
            "reason": f"latest final counts are too low: {latest_counts:.3f} kcps < {minimum_final_counts_kcps:.3f} kcps",
            "latest_finished_at": str(latest.get("finished_at", "") or ""),
            "latest_final_counts_kcps": latest_counts,
        }

    recent_failures_after_latest: list[dict[str, Any]] = []
    for record in records:
        if str(record.get("event_kind", "") or "") != "tracking_event":
            continue
        finished_at = parse_local_iso_datetime(record.get("finished_at", ""))
        if finished_at is None or finished_at <= latest_finished_at or not sample_matches_tracking_event(record, sample_id):
            continue
        age_minutes = max(0.0, (now - finished_at).total_seconds() / 60.0)
        status = str(record.get("status", "") or "").strip().lower()
        exception_identifier = str(record.get("exception_identifier", "") or "").strip()
        exception_message = str(record.get("exception_message", "") or "").strip()
        if age_minutes <= max_age_minutes and (status not in {"", "completed"} or exception_identifier or exception_message):
            recent_failures_after_latest.append(
                {
                    "finished_at": str(record.get("finished_at", "") or ""),
                    "status": status,
                    "exception_identifier": exception_identifier,
                    "exception_message": exception_message,
                }
            )

    queue_counts = bridge_queue_counts(bridge_root)
    if bool(policy.get("requires_queue_clear", True)) and (queue_counts.get("queued", -1) != 0 or queue_counts.get("running", -1) != 0):
        return {
            "ok": False,
            "reason": "bridge queue is not clear or could not be inspected",
            "bridge_queue_counts": queue_counts,
        }
    if bool(policy.get("requires_no_recent_alignment_failure", True)) and recent_failures_after_latest:
        return {
            "ok": False,
            "reason": "agent-trackable tracking/alignment failure evidence exists after the latest good tracking event",
            "recent_failures": recent_failures_after_latest[-3:],
        }

    return {
        "ok": True,
        "reason": "recent agent-trackable tracking evidence and bridge queue status are sufficient",
        "tracking_history_path": str(tracking_path),
        "latest_finished_at": str(latest.get("finished_at", "") or ""),
        "latest_route": str(latest.get("route", "") or ""),
        "latest_source_label": str(latest.get("source_label", "") or ""),
        "latest_final_counts_kcps": latest_counts,
        "latest_age_minutes": round(latest_age_minutes, 2),
        "minimum_final_counts_kcps": minimum_final_counts_kcps,
        "bridge_queue_counts": queue_counts,
    }

def tracking_evidence_sufficient_for_physical_state(root: Path, project: dict[str, Any]) -> dict[str, Any]:
    return tracking_evidence_sufficient_for_agent_trackable_nv_state(root, project)

def request_text_blob(request: dict[str, Any]) -> str:
    parts: list[str] = []
    for key in ("action_type", "reason", "resume_condition", "target", "risk_class"):
        parts.append(str(request.get(key, "") or ""))
    for key in ("instructions", "expected_evidence", "stop_conditions"):
        value = request.get(key, [])
        if isinstance(value, list):
            parts.extend(str(item or "") for item in value)
        else:
            parts.append(str(value or ""))
    return " ".join(parts).lower()

def is_agent_trackable_nv_state_evidence_request(request: dict[str, Any]) -> bool:
    action_type = str(request.get("action_type", "") or "").strip().lower()
    explicit_actions = {
        "confirm_agent_trackable_nv_state",
        "agent_trackable_nv_state_evidence",
        "collect_agent_trackable_nv_state_evidence",
        "request_fresh_nv23_tracking_evidence",
        "check_current_nv23_tracking_counts",
        "check_current_nv23_agent_trackable_state",
    }
    legacy_actions = {
        "agent_trackable_nv_state_confirmation",
        "confirm_physical_state_good",
        "physical_state_good_confirmation",
        "request_fresh_nv23_physical_evidence",
        "check_current_nv23_physical_state",
    }
    text = request_text_blob(request)
    disqualifiers = (
        "duplicate",
        "shared-tree",
        "shared tree",
        "mount",
        "visibility",
        "manual recovery",
        "repeat failure",
        "repeated failure",
        "hardware state",
        "microwave",
        "laser power state",
        "instrument state",
        "driver",
        "gui",
        "reposition",
        "adjust",
    )
    if any(token in text for token in disqualifiers):
        return False
    if action_type in explicit_actions or action_type in legacy_actions:
        return True
    state_tokens = ("nv state", "alignment", "tracking", "counts", "kcps")
    intent_tokens = ("evidence", "confirm", "check", "fresh", "current")
    return any(token in text for token in state_tokens) and any(token in text for token in intent_tokens)

def is_physical_state_good_confirmation_request(request: dict[str, Any]) -> bool:
    return is_agent_trackable_nv_state_evidence_request(request)

def auto_agent_trackable_nv_state_evidence_decision(
    root: Path,
    project: dict[str, Any],
    request: dict[str, Any],
) -> dict[str, Any]:
    if not is_agent_trackable_nv_state_evidence_request(request):
        return {"eligible": False, "reason": "request is not a narrow agent-trackable NV-state evidence request"}
    evidence = tracking_evidence_sufficient_for_agent_trackable_nv_state(root, project)
    if not bool(evidence.get("ok", False)):
        return {"eligible": False, "reason": str(evidence.get("reason", "") or ""), "evidence": evidence}
    return {
        "eligible": True,
        "reason": "recent agent-trackable tracking/counts evidence is sufficient",
        "evidence": evidence,
    }

def auto_physical_state_confirmation_decision(
    root: Path,
    project: dict[str, Any],
    request: dict[str, Any],
) -> dict[str, Any]:
    return auto_agent_trackable_nv_state_evidence_decision(root, project, request)

def compute_next_action(root: Path, project: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    autonomy = project.get("autonomy", {}) if isinstance(project.get("autonomy"), dict) else {}
    research_context = research_context_overview(root, project)
    blocking_request_id = str(state.get("blocking_request_id", "") or "").strip()
    pending_physical = list_pending_physical_requests(root)
    if blocking_request_id:
        for request in pending_physical:
            if str(request.get("request_id", "") or "") == blocking_request_id:
                return {
                    "kind": "blocked_external",
                    "blocker_type": "physical_action",
                    "request_id": blocking_request_id,
                    "reason": "project is blocked on a physical-action request",
                    "research_context": research_context,
                }
        done_result = root / "physical_action_requests" / "done" / f"{blocking_request_id}.result.json"
        if done_result.is_file():
            result = read_json(done_result)
            if bool(result.get("resume_ok", False)):
                return {
                    "kind": "advance_project",
                    "reason": "physical-action result is complete; continue with the next safe project work",
                    "request_id": blocking_request_id,
                    "result_path": str(done_result),
                    "research_context": research_context,
                }
        return {
            "kind": "blocked",
            "blocker_type": "physical_action_result_missing",
            "request_id": blocking_request_id,
            "reason": "blocking physical-action request has no resumable result",
            "research_context": research_context,
        }

    if pending_physical:
        request = pending_physical[0]
        return {
            "kind": "blocked_external",
            "blocker_type": "physical_action",
            "request_id": str(request.get("request_id", "") or ""),
            "reason": "physical-action request is queued",
            "request_path": str(request.get("_path", "") or ""),
            "research_context": research_context,
        }

    blocking_code_change_request_id = str(state.get("blocking_code_change_request_id", "") or "").strip()
    pending_code_changes = list_pending_code_change_requests(root)
    if blocking_code_change_request_id:
        for request in pending_code_changes:
            if str(request.get("request_id", "") or "") == blocking_code_change_request_id:
                return {
                    "kind": "blocked_code",
                    "blocker_type": "code_change",
                    "request_id": blocking_code_change_request_id,
                    "reason": "project is blocked on a code-change request",
                    "research_context": research_context,
                }
        done_result = root / "code_change_requests" / "done" / f"{blocking_code_change_request_id}.result.json"
        if done_result.is_file():
            result = read_json(done_result)
            if bool(result.get("resume_ok", False)):
                return {
                    "kind": "advance_project",
                    "reason": "code-change result is complete; continue with the next safe project work",
                    "request_id": blocking_code_change_request_id,
                    "result_path": str(done_result),
                    "research_context": research_context,
                }
        return {
            "kind": "blocked",
            "blocker_type": "code_change_result_missing",
            "request_id": blocking_code_change_request_id,
            "reason": "blocking code-change request has no resumable result",
            "research_context": research_context,
        }

    if pending_code_changes:
        request = pending_code_changes[0]
        return {
            "kind": "blocked_code",
            "blocker_type": "code_change",
            "request_id": str(request.get("request_id", "") or ""),
            "reason": "code-change request is queued",
            "request_path": str(request.get("_path", "") or ""),
            "change_class": str(request.get("change_class", "") or ""),
            "risk_class": str(request.get("risk_class", "") or ""),
            "research_context": research_context,
        }

    pending_backlog = pending_backlog_overview(root)
    if int(pending_backlog.get("count", 0) or 0) > 0:
        scientific_uncertainty_blockers: list[dict[str, Any]] = []
        for item in pending_backlog.get("preview", []):
            if not isinstance(item, dict):
                continue
            if str(item.get("kind", "") or "") != "blocker":
                continue
            if is_scientific_uncertainty_backlog_blocker_item(item):
                scientific_uncertainty_blockers.append(item)
                continue
            return {
                "kind": "blocked_external",
                "blocker_type": str(item.get("blocker_type", "") or "backlog_blocker"),
                "backlog_item_id": str(item.get("id", "") or ""),
                "reason": "pending backlog blocker exists",
                "pending_backlog_count": int(pending_backlog.get("count", 0) or 0),
                "pending_backlog_preview": pending_backlog.get("preview", []),
                "research_context": research_context,
            }
        if scientific_uncertainty_blockers:
            return {
                "kind": "advance_project",
                "reason": (
                    "pending scientific-strategy backlog blocker exists; treat it as agent-side "
                    "bridge-free strategy work, not an external block"
                ),
                "pending_backlog_count": int(pending_backlog.get("count", 0) or 0),
                "pending_backlog_preview": pending_backlog.get("preview", []),
                "scientific_uncertainty_blocker_count": len(scientific_uncertainty_blockers),
                "research_context": research_context,
                "agent_prompt": (
                    "A pending backlog item is labeled kind=blocker, but it is science/strategy uncertainty. "
                    "Do not stop for the operator on that basis. Resolve or supersede it with bridge-free synthesis, "
                    "then create or execute the next safe research_task when possible. Reserve kind=blocker / "
                    "blocked_external for physical/manual apparatus checks, explicit STOP or approval requirements, "
                    "code/safety work, or hard bridge/hardware failures that cannot be handled by agent-side recovery."
                ),
            }
        return {
            "kind": "advance_project",
            "reason": "pending execution queue entries exist; agent should choose the next safe project work from work/state.md, objective, human advice, evidence, backlog, and safety policy",
            "pending_backlog_count": int(pending_backlog.get("count", 0) or 0),
            "pending_backlog_preview": pending_backlog.get("preview", []),
            "research_context": research_context,
            "agent_prompt": (
                "Treat this next_action and backlog preview as state pointers, not a research plan. Read "
                "NV_RESEARCH_MEMORY.md startup memory first, then brief.md, human_advice.md, work/state.md, "
                "and the compact state/backlog preview. Use the Memory Index to read relevant sections from "
                "NV_RESEARCH_KNOWLEDGE.md only as needed. Read .manager/evidence.jsonl, project policy, "
                "detailed backlog entries, and directly referenced work/notes files only as needed for the current decision. "
                "Python owns state, queue safety, audit logs, and hard hardware/code safety boundaries; the agent owns research judgment, "
                "chunk planning, evidence synthesis, and experiment-design reasoning. Keep bridge queue safety hard: do not submit or mutate "
                "bridge jobs while queued/running is occupied, except for explicit running-job stop control after evidence-backed safety review. "
                "For inbox advice, use list-advice-inbox and dispose-advice; do not leave opened messages in advice/inbox. "
                "If the wake yields a reusable detailed NV lesson, update NV_RESEARCH_KNOWLEDGE.md in the relevant section with a concise dated note and provenance pointer. "
                "Record decisions in work/state.md, work/notes, log.md, backlog, and ledger, then write the completion marker when this wake ends."
            ),
        }

    if project_lifecycle(project) not in ACTIVE_PROJECT_LIFECYCLES:
        return {
            "kind": "idle",
            "reason": f"project lifecycle is {project_lifecycle(project)}",
            "research_context": research_context,
        }
    if bool(autonomy.get("continue_when_backlog_empty", True)):
        return {
            "kind": "advance_project",
            "reason": "execution queue is empty; wake the agent to synthesize or update the research agenda and advance all currently runnable safe project work from objective, evidence, human advice, and safety policy",
            "research_context": research_context,
            "agent_prompt": (
                "Treat this as an event-driven research wake. Read NV_RESEARCH_MEMORY.md startup memory first, then "
                "brief.md, human_advice.md, work/state.md, and compact project state. Use the Memory Index to read "
                "relevant sections from NV_RESEARCH_KNOWLEDGE.md only as needed. Read .manager/evidence.jsonl, "
                "project policy, detailed backlog entries, and directly relevant evidence only as needed, then use the "
                "same-wake runnable work loop to complete, update, or queue all currently runnable safe project work until "
                "a real stop condition is reached. Python should stay "
                "limited to state, queue safety, audit logs, and hard boundaries; the agent should own the scientific plan. "
                "Process advice inbox messages with list-advice-inbox/dispose-advice when present, record evidence, update backlog, "
                "write work/state.md, log.md, and work/notes files as useful, update NV_RESEARCH_KNOWLEDGE.md for reusable detailed lessons, "
                "and write the completion marker."
            ),
        }
    return {
        "kind": "idle",
        "reason": "no pending backlog or blocking request",
        "research_context": research_context,
    }

def status_or_tick(args: argparse.Namespace, *, tick: bool) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    research_context = research_context_overview(root, project)
    state = load_state(root)
    inbox_auto_activate = auto_resume_paused_project_on_new_inbox(root, project, state, actor=args.actor)
    if bool(inbox_auto_activate.get("activated", inbox_auto_activate.get("resumed", False))):
        project = load_project(root)
        state = load_state(root)
    next_action = compute_next_action(root, project, state)
    approval_notifications: list[dict[str, Any]] = []
    if tick:
        state["tick_count"] = int(state.get("tick_count", 0) or 0) + 1
        state["updated_at"] = now_iso()
        state["last_next_action"] = next_action
        action_kind = str(next_action.get("kind", "") or "")
        if action_kind == "blocked_external":
            set_operational_state(state, "blocked_external")
            if next_action.get("request_id"):
                state["blocking_request_id"] = next_action["request_id"]
        elif action_kind == "blocked_code":
            set_operational_state(state, "blocked_code")
            if next_action.get("request_id"):
                state["blocking_code_change_request_id"] = next_action["request_id"]
        elif action_kind == "blocked":
            set_operational_state(state, "blocked")
        elif operational_state(state) in BLOCKED_STATUSES and action_kind not in {"blocked", "blocked_external", "blocked_code"}:
            set_operational_state(state, "active")
            state["blocking_request_id"] = ""
            state["blocking_code_change_request_id"] = ""
        else:
            sync_operational_state_alias(state)
        write_json(get_state_path(root), state)
        append_jsonl(
            get_ledger_path(root),
            {
                "timestamp": now_iso(),
                "actor": args.actor,
                "event": "project_tick",
                "project_id": str(project.get("project_id", "") or root.name),
                "next_action": next_action,
            },
        )
        approval_notifications = notify_pending_approval_backlog_items(root, project, actor=args.actor)
    return {
        "ok": True,
        "action": "tick" if tick else "status",
        "project_id": str(project.get("project_id", "") or root.name),
        "project_dir": str(root),
        "project_id": str(project.get("project_id", "") or root.name),
        "project_dir": str(root),
        "status": operational_state(state),
        "project_lifecycle": project_lifecycle(project),
        "operational_state": operational_state(state),
        "legacy_project_status": str(project.get("status", "") or ""),
        "legacy_state_status": str(state.get("status", "") or ""),
        "tick_count": state.get("tick_count", 0),
        "blocking_request_id": state.get("blocking_request_id", ""),
        "blocking_code_change_request_id": state.get("blocking_code_change_request_id", ""),
        "next_action": next_action,
        "research_context": research_context,
        "shared_research_memory": project.get("shared_research_memory", shared_nv_research_memory_context(include_snapshot=False)),
        "approval_notifications": approval_notifications,
        "inbox_auto_activate": inbox_auto_activate,
        "inbox_auto_resume": inbox_auto_activate,
    }

def queue_physical_request(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    state = load_state(root)
    request = read_json_arg(args.request_json)
    request_id = slug(str(request.get("request_id", "") or args.request_id or f"physical_{now_iso()}"))
    request.update(
        {
            "kind": "physical_action_request",
            "schema_version": int(request.get("schema_version", 1) or 1),
            "request_id": request_id,
            "project_id": str(project.get("project_id", "") or root.name),
        }
    )
    request.setdefault("created_at", now_iso())
    request.setdefault("blocking", True)
    request.setdefault("target", "human_or_robot")
    request.setdefault("risk_class", "inspect")
    request.setdefault("expected_evidence", [])
    request.setdefault("stop_conditions", [])
    request.setdefault("resume_condition", "")
    auto_nv_state_decision = auto_agent_trackable_nv_state_evidence_decision(root, project, request)
    if bool(auto_nv_state_decision.get("eligible", False)):
        request["blocking"] = False
        request["human_approval_required"] = False
        request["auto_resolved"] = True
        request["auto_approval_policy"] = "no_human_approval_required_for.agent_trackable_nv_state_evidence"
        request["auto_resolution"] = auto_nv_state_decision
        done_root = root / "physical_action_requests" / "done"
        request_path = done_root / f"{request_id}.request.json"
        result_path = done_root / f"{request_id}.result.json"
        result = {
            "kind": "physical_action_result",
            "schema_version": 1,
            "request_id": request_id,
            "project_id": str(project.get("project_id", "") or root.name),
            "status": "completed",
            "completed_at": now_iso(),
            "completed_by": "project_auto_approval_policy",
            "summary": "Recent agent-trackable NV tracking/counts evidence was sufficient; no human check was required.",
            "resume_ok": True,
            "changed_physical_state": False,
            "auto_approval": {
                "applied": True,
                "policy": "no_human_approval_required_for.agent_trackable_nv_state_evidence",
                "reason": str(auto_nv_state_decision.get("reason", "") or ""),
            },
            "findings": auto_nv_state_decision.get("evidence", {}),
        }
        write_json(request_path, request)
        write_json(result_path, result)
        append_jsonl(
            get_ledger_path(root),
            {
                "timestamp": now_iso(),
                "actor": args.actor,
                "event": "agent_trackable_nv_state_evidence_auto_resolved",
                "project_id": str(project.get("project_id", "") or root.name),
                "request_id": request_id,
                "request_path": str(request_path),
                "result_path": str(result_path),
                "summary": str(request.get("reason", "") or request.get("action_type", "") or ""),
                "auto_resolution": auto_nv_state_decision,
            },
        )
        lab_log_paths = append_lab_log(
            root,
            project,
            title="Agent-trackable NV-state evidence auto-resolved",
            summary=str(result.get("summary", "") or ""),
            event="agent_trackable_nv_state_evidence_auto_resolved",
            actor=args.actor,
            details={
                "request_id": request_id,
                "target": str(request.get("target", "") or ""),
                "risk_class": str(request.get("risk_class", "") or ""),
                "blocking": False,
                "resume_ok": True,
                "auto_resolution": auto_nv_state_decision,
                "request_path": str(request_path),
                "result_path": str(result_path),
            },
        )
        return {
            "ok": True,
            "action": "queue_physical_request",
            "project_id": str(project.get("project_id", "") or root.name),
            "request_id": request_id,
            "request_path": str(request_path),
            "result_path": str(result_path),
            "blocking": False,
            "auto_resolved": True,
            "resume_ok": True,
            "lab_log_path": lab_log_paths["lab_log_path"],
            "telegram_notification": {
                "attempted": False,
                "sent": False,
                "reason": "auto_approval_policy_no_human_notification",
                "returncode": "",
            },
        }
    if is_agent_trackable_nv_state_evidence_request(request):
        request["auto_resolution"] = auto_nv_state_decision
        policy = agent_trackable_nv_state_evidence_policy(project)
        if bool(policy.get("route_unmet_evidence_to_backlog", True)):
            backlog = load_backlog(root, project)
            backlog_item_id = slug(f"{request_id}_collect_nv_state_evidence")
            item = {
                "id": backlog_item_id,
                "status": "pending",
                "kind": "collect_agent_trackable_nv_state_evidence",
                "priority": str(request.get("priority", "") or "high"),
                "summary": (
                    "Collect fresh agent-trackable NV tracking/counts evidence; do not ask for a human check."
                ),
                "created_at": now_iso(),
                "source_request_id": request_id,
                "agent_prompt": (
                    "Collect or cite bounded NV tracking/counts evidence for the requested execute-readiness check. "
                    "Use agent-operable tracking/status routes where available, record final_counts_kcps and bridge "
                    "queue/running state, then resume evidence analysis. Ask the operator only for non-trackable hardware, "
                    "manual alignment, safety, or instrument-state uncertainty."
                ),
                "evidence_needed": {
                    "latest_tracking_age_minutes_max": policy.get("max_evidence_age_minutes", 30),
                    "minimum_final_counts_kcps": policy.get("minimum_final_counts_kcps", 25),
                    "requires_queue_clear": bool(policy.get("requires_queue_clear", True)),
                    "requires_no_recent_alignment_failure": bool(policy.get("requires_no_recent_alignment_failure", True)),
                },
            }
            existing_items = backlog.get("items", [])
            if not isinstance(existing_items, list):
                existing_items = []
            replaced = False
            updated_items: list[Any] = []
            for existing in existing_items:
                if isinstance(existing, dict) and str(existing.get("id", "") or "") == backlog_item_id:
                    updated_items.append(item)
                    replaced = True
                else:
                    updated_items.append(existing)
            if not replaced:
                updated_items.append(item)
            backlog["items"] = updated_items
            write_json(get_backlog_path(root), backlog)

            done_root = root / "physical_action_requests" / "done"
            request["blocking"] = False
            request["human_approval_required"] = False
            request["auto_redirected_to_agent_backlog"] = True
            request["backlog_item_id"] = backlog_item_id
            request_path = done_root / f"{request_id}.request.json"
            result_path = done_root / f"{request_id}.result.json"
            result = {
                "kind": "physical_action_result",
                "schema_version": 1,
                "request_id": request_id,
                "project_id": str(project.get("project_id", "") or root.name),
                "status": "completed",
                "completed_at": now_iso(),
                "completed_by": "project_auto_routing_policy",
                "summary": (
                    "Agent-trackable NV tracking/counts evidence was needed, so the request was redirected "
                    "to backlog for agent evidence collection."
                ),
                "resume_ok": False,
                "changed_physical_state": False,
                "backlog_item_id": backlog_item_id,
                "auto_routing": {
                    "applied": True,
                    "policy": "no_human_approval_required_for.agent_trackable_nv_state_evidence.route_unmet_evidence_to_backlog",
                    "reason": str(auto_nv_state_decision.get("reason", "") or ""),
                },
                "findings": auto_nv_state_decision.get("evidence", {}),
            }
            write_json(request_path, request)
            write_json(result_path, result)
            append_jsonl(
                get_ledger_path(root),
                {
                    "timestamp": now_iso(),
                    "actor": args.actor,
                    "event": "agent_trackable_nv_state_request_redirected",
                    "project_id": str(project.get("project_id", "") or root.name),
                    "request_id": request_id,
                    "backlog_item_id": backlog_item_id,
                    "request_path": str(request_path),
                    "result_path": str(result_path),
                    "summary": str(result.get("summary", "") or ""),
                    "auto_resolution": auto_nv_state_decision,
                },
            )
            lab_log_paths = append_lab_log(
                root,
                project,
                title="Agent-trackable NV-state request redirected",
                summary=str(result.get("summary", "") or ""),
                event="agent_trackable_nv_state_request_redirected",
                actor=args.actor,
                details={
                    "request_id": request_id,
                    "backlog_item_id": backlog_item_id,
                    "resume_ok": False,
                    "auto_resolution": auto_nv_state_decision,
                    "request_path": str(request_path),
                    "result_path": str(result_path),
                },
            )
            return {
                "ok": True,
                "action": "queue_physical_request",
                "project_id": str(project.get("project_id", "") or root.name),
                "request_id": request_id,
                "request_path": str(request_path),
                "result_path": str(result_path),
                "blocking": False,
                "auto_redirected_to_agent_backlog": True,
                "backlog_item_id": backlog_item_id,
                "lab_log_path": lab_log_paths["lab_log_path"],
                "telegram_notification": {
                    "attempted": False,
                    "sent": False,
                    "reason": "agent_trackable_nv_state_request_routed_to_backlog",
                    "returncode": "",
                },
            }
    if is_agent_trackable_nv_state_evidence_request(request):
        request["auto_resolution"] = auto_nv_state_decision
    out_path = root / "physical_action_requests" / "queued" / f"{request_id}.json"
    write_json(out_path, request)
    if bool(request.get("blocking", True)):
        set_operational_state(state, "blocked_physical_action")
        state["blocking_request_id"] = request_id
        state["updated_at"] = now_iso()
        write_json(get_state_path(root), state)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "physical_action_requested",
            "project_id": str(project.get("project_id", "") or root.name),
            "request_id": request_id,
            "request_path": str(out_path),
            "summary": str(request.get("reason", "") or request.get("action_type", "") or ""),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Physical action requested",
        summary=str(request.get("reason", "") or request.get("action_type", "") or ""),
        event="physical_action_requested",
        actor=args.actor,
        details={
            "request_id": request_id,
            "target": str(request.get("target", "") or ""),
            "risk_class": str(request.get("risk_class", "") or ""),
            "blocking": bool(request.get("blocking", True)),
            "resume_condition": str(request.get("resume_condition", "") or ""),
            "request_path": str(out_path),
        },
    )
    telegram_notification = notify_project_request(
        root,
        project,
        request_type="physical_action",
        request_id=request_id,
        summary=str(request.get("reason", "") or request.get("action_type", "") or ""),
        request_path=out_path,
        blocking=bool(request.get("blocking", True)),
        extra={
            "target": str(request.get("target", "") or ""),
            "risk_class": str(request.get("risk_class", "") or ""),
            "resume_condition": str(request.get("resume_condition", "") or ""),
        },
    )
    return {
        "ok": True,
        "action": "queue_physical_request",
        "project_id": str(project.get("project_id", "") or root.name),
        "request_id": request_id,
        "request_path": str(out_path),
        "blocking": bool(request.get("blocking", True)),
        "lab_log_path": lab_log_paths["lab_log_path"],
        "telegram_notification": {
            "attempted": bool(telegram_notification.get("attempted", False)),
            "sent": bool(telegram_notification.get("sent", False)),
            "reason": str(telegram_notification.get("reason", "") or ""),
            "returncode": telegram_notification.get("returncode", ""),
        },
    }

def complete_physical_request(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    state = load_state(root)
    result = read_json_arg(args.result_json)
    request_id = slug(str(result.get("request_id", "") or args.request_id))
    if not request_id:
        raise ValueError("request_id is required.")
    status = str(result.get("status", "") or "").strip()
    if status not in VALID_PHYSICAL_RESULT_STATUSES:
        raise ValueError(f"physical action result status must be one of {sorted(VALID_PHYSICAL_RESULT_STATUSES)}.")
    result.update(
        {
            "kind": "physical_action_result",
            "schema_version": int(result.get("schema_version", 1) or 1),
            "request_id": request_id,
            "project_id": str(project.get("project_id", "") or root.name),
        }
    )
    result.setdefault("completed_at", now_iso())
    done_root = root / "physical_action_requests" / ("done" if status == "completed" else "failed")
    result_path = done_root / f"{request_id}.result.json"
    write_json(result_path, result)
    queued_path = root / "physical_action_requests" / "queued" / f"{request_id}.json"
    if queued_path.is_file():
        archive_path = done_root / f"{request_id}.request.json"
        shutil.move(str(queued_path), str(archive_path))
    if str(state.get("blocking_request_id", "") or "") == request_id:
        if bool(result.get("resume_ok", False)):
            set_operational_state(state, "active")
            state["blocking_request_id"] = ""
        else:
            set_operational_state(state, "blocked_physical_action")
        state["updated_at"] = now_iso()
        write_json(get_state_path(root), state)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "physical_action_result",
            "project_id": str(project.get("project_id", "") or root.name),
            "request_id": request_id,
            "status": status,
            "resume_ok": bool(result.get("resume_ok", False)),
            "result_path": str(result_path),
            "summary": str(result.get("summary", "") or ""),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Physical action result recorded",
        summary=str(result.get("summary", "") or ""),
        event="physical_action_result",
        actor=args.actor,
        details={
            "request_id": request_id,
            "status": status,
            "resume_ok": bool(result.get("resume_ok", False)),
            "changed_physical_state": result.get("changed_physical_state", ""),
            "result_path": str(result_path),
        },
    )
    return {
        "ok": True,
        "action": "complete_physical_request",
        "project_id": str(project.get("project_id", "") or root.name),
        "request_id": request_id,
        "status": status,
        "resume_ok": bool(result.get("resume_ok", False)),
        "result_path": str(result_path),
        "lab_log_path": lab_log_paths["lab_log_path"],
    }

def queue_code_change_request(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    state = load_state(root)
    request = read_json_arg(args.request_json)
    request_id = slug(str(request.get("request_id", "") or args.request_id or f"code_change_{now_iso()}"))
    change_class = str(request.get("change_class", "") or "sequence_staging").strip()
    request.update(
        {
            "kind": "code_change_request",
            "schema_version": int(request.get("schema_version", 1) or 1),
            "request_id": request_id,
            "project_id": str(project.get("project_id", "") or root.name),
            "change_class": change_class,
        }
    )
    request.setdefault("created_at", now_iso())
    request.setdefault("blocking", True)
    request.setdefault("risk_class", default_code_change_risk(change_class))
    request.setdefault("allowed_write_scopes", [])
    request.setdefault("forbidden_write_scopes", [])
    request.setdefault("required_evidence_before_edit", [])
    request.setdefault("required_verification", [])
    request.setdefault("rollback_plan", "")
    request.setdefault("review_required", change_class in SCOPED_CODE_CHANGE_CLASSES)
    request.setdefault("resume_condition", "")
    validate_code_change_request(request)
    auto_request_decision = code_change_auto_approval_decision(project, request)
    if bool(auto_request_decision.get("eligible", False)):
        request["review_required"] = False
        request["human_approval_required"] = False
        request["auto_resume_after_verification"] = True
        request["auto_approval_policy"] = "no_human_approval_required_for.low_risk_code_change"
        request.setdefault("suppress_human_notification", True)
    else:
        request.setdefault("human_approval_required", bool(request.get("review_required", False)))

    out_path = root / "code_change_requests" / "queued" / f"{request_id}.json"
    write_json(out_path, request)
    if bool(request.get("blocking", True)):
        set_operational_state(state, "blocked_code_change")
        state["blocking_code_change_request_id"] = request_id
        state["updated_at"] = now_iso()
        write_json(get_state_path(root), state)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "code_change_requested",
            "project_id": str(project.get("project_id", "") or root.name),
            "request_id": request_id,
            "request_path": str(out_path),
            "change_class": change_class,
            "risk_class": str(request.get("risk_class", "") or ""),
            "summary": str(request.get("reason", "") or request.get("intended_behavior", "") or ""),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Code change requested",
        summary=str(request.get("reason", "") or request.get("intended_behavior", "") or ""),
        event="code_change_requested",
        actor=args.actor,
        details={
            "request_id": request_id,
            "change_class": change_class,
            "risk_class": str(request.get("risk_class", "") or ""),
            "blocking": bool(request.get("blocking", True)),
            "review_required": bool(request.get("review_required", False)),
            "human_approval_required": bool(request.get("human_approval_required", False)),
            "auto_resume_after_verification": bool(request.get("auto_resume_after_verification", False)),
            "allowed_write_scopes": request.get("allowed_write_scopes", []),
            "request_path": str(out_path),
        },
    )
    if bool(request.get("suppress_human_notification", False)):
        telegram_notification = {
            "attempted": False,
            "sent": False,
            "reason": "auto_approval_policy_no_human_notification",
            "returncode": "",
        }
    else:
        telegram_notification = notify_project_request(
            root,
            project,
            request_type="code_change",
            request_id=request_id,
            summary=str(request.get("reason", "") or request.get("intended_behavior", "") or ""),
            request_path=out_path,
            blocking=bool(request.get("blocking", True)),
            extra={
                "change_class": change_class,
                "risk_class": str(request.get("risk_class", "") or ""),
                "review_required": bool(request.get("review_required", False)),
                "human_approval_required": bool(request.get("human_approval_required", False)),
                "allowed_write_scopes": request.get("allowed_write_scopes", []),
            },
        )
    return {
        "ok": True,
        "action": "queue_code_change_request",
        "project_id": str(project.get("project_id", "") or root.name),
        "request_id": request_id,
        "request_path": str(out_path),
        "change_class": change_class,
        "risk_class": str(request.get("risk_class", "") or ""),
        "blocking": bool(request.get("blocking", True)),
        "review_required": bool(request.get("review_required", False)),
        "human_approval_required": bool(request.get("human_approval_required", False)),
        "auto_resume_after_verification": bool(request.get("auto_resume_after_verification", False)),
        "lab_log_path": lab_log_paths["lab_log_path"],
        "telegram_notification": {
            "attempted": bool(telegram_notification.get("attempted", False)),
            "sent": bool(telegram_notification.get("sent", False)),
            "reason": str(telegram_notification.get("reason", "") or ""),
            "returncode": telegram_notification.get("returncode", ""),
        },
    }

def complete_code_change_request(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    state = load_state(root)
    result = read_json_arg(args.result_json)
    request_id = slug(str(result.get("request_id", "") or args.request_id))
    if not request_id:
        raise ValueError("request_id is required.")
    status = str(result.get("status", "") or "").strip()
    if status not in VALID_CODE_CHANGE_RESULT_STATUSES:
        raise ValueError(f"code-change result status must be one of {sorted(VALID_CODE_CHANGE_RESULT_STATUSES)}.")
    result.update(
        {
            "kind": "code_change_result",
            "schema_version": int(result.get("schema_version", 1) or 1),
            "request_id": request_id,
            "project_id": str(project.get("project_id", "") or root.name),
        }
    )
    result.setdefault("completed_at", now_iso())
    result.setdefault("changed_files", [])
    result.setdefault("verification", [])
    result.setdefault("review", {})
    result.setdefault("resume_ok", False)
    request_record = read_code_change_request_record(root, request_id)
    auto_resume = apply_auto_code_change_resume_if_allowed(project, request_record, result)
    done_root = root / "code_change_requests" / ("done" if status == "completed" else "failed")
    result_path = done_root / f"{request_id}.result.json"
    write_json(result_path, result)
    queued_path = root / "code_change_requests" / "queued" / f"{request_id}.json"
    if queued_path.is_file():
        archive_path = done_root / f"{request_id}.request.json"
        shutil.move(str(queued_path), str(archive_path))
    if str(state.get("blocking_code_change_request_id", "") or "") == request_id:
        if bool(result.get("resume_ok", False)):
            set_operational_state(state, "active")
            state["blocking_code_change_request_id"] = ""
        else:
            set_operational_state(state, "blocked_code_change")
        state["updated_at"] = now_iso()
        write_json(get_state_path(root), state)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "code_change_result",
            "project_id": str(project.get("project_id", "") or root.name),
            "request_id": request_id,
            "status": status,
            "resume_ok": bool(result.get("resume_ok", False)),
            "result_path": str(result_path),
            "summary": str(result.get("summary", "") or ""),
            "changed_files": result.get("changed_files", []),
            "auto_resume": auto_resume,
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Code change result recorded",
        summary=str(result.get("summary", "") or ""),
        event="code_change_result",
        actor=args.actor,
        details={
            "request_id": request_id,
            "status": status,
            "resume_ok": bool(result.get("resume_ok", False)),
            "changed_files": result.get("changed_files", []),
            "auto_resume": auto_resume,
            "result_path": str(result_path),
        },
    )
    return {
        "ok": True,
        "action": "complete_code_change_request",
        "project_id": str(project.get("project_id", "") or root.name),
        "request_id": request_id,
        "status": status,
        "resume_ok": bool(result.get("resume_ok", False)),
        "result_path": str(result_path),
        "lab_log_path": lab_log_paths["lab_log_path"],
    }

def record_evidence(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    record = read_json_arg(args.evidence_json) if args.evidence_json else {}
    if args.evidence_id:
        record["evidence_id"] = args.evidence_id
    if args.category:
        record["category"] = args.category
    if args.summary:
        record["summary"] = args.summary
    if args.path:
        paths = normalize_record_paths(record.get("paths", []))
        for path in args.path:
            if str(path or "").strip() not in paths:
                paths.append(str(path or "").strip())
        record["paths"] = [path for path in paths if path]
    if not str(record.get("summary", "") or "").strip() and not extract_artifact_paths(record):
        raise ValueError("evidence needs either --summary/evidence_json.summary or at least one --path.")
    evidence = append_evidence_record(
        root,
        project,
        record,
        actor=args.actor,
        source="record-evidence",
    )
    return {
        "ok": True,
        "action": "record_evidence",
        "project_id": str(project.get("project_id", "") or root.name),
        "evidence_index_path": str(evidence_index_path(root)),
        **evidence,
    }

def event_to_evidence_record(event: dict[str, Any]) -> dict[str, Any]:
    paths = extract_artifact_paths(event)
    if not terminal_evidence_payload(event) and not paths:
        return {}
    category = "bridge_result" if terminal_evidence_payload(event) else "artifact"
    if event.get("figures"):
        category = "figure"
    return {
        "category": category,
        "summary": str(event.get("summary", "") or event.get("event", "") or ""),
        "paths": paths,
        "backlog_item_id": event.get("backlog_item_id", ""),
        "bridge_job_id": event.get("bridge_job_id", ""),
        "provenance": {
            "ledger_event": str(event.get("event", "") or ""),
            "timestamp": str(event.get("timestamp", "") or ""),
        },
    }

def experiment_intent_path(root: Path, status: str, intent_id: str) -> Path:
    return root / "experiment_intents" / status / f"{slug(intent_id)}.json"

def find_experiment_intent(root: Path, intent_id: str) -> tuple[Path, dict[str, Any]]:
    normalized = slug(intent_id)
    if not normalized:
        raise ValueError("intent_id is required.")
    for status in ("queued", "verified", "rejected", "done"):
        path = experiment_intent_path(root, status, normalized)
        if path.is_file():
            return path, read_json(path)
    raise FileNotFoundError(f"experiment intent not found: {normalized}")

def normalize_experiment_intent(intent: dict[str, Any], project: dict[str, Any], intent_id: str) -> dict[str, Any]:
    normalized_id = slug(str(intent.get("intent_id", "") or intent.get("id", "") or intent_id or intent.get("summary", "") or f"intent_{now_iso()}"))
    if not normalized_id:
        raise ValueError("intent_id is required.")
    payload = dict(intent)
    payload.update(
        {
            "schema_version": int(payload.get("schema_version", 1) or 1),
            "kind": "experiment_intent",
            "intent_id": normalized_id,
            "project_id": str(project.get("project_id", "") or ""),
            "status": "queued",
        }
    )
    payload.setdefault("created_at", now_iso())
    payload.setdefault("agent_authored", True)
    payload.setdefault("python_role", "safety_verifier_not_research_planner")
    payload.setdefault("summary", "")
    payload.setdefault("scientific_rationale", "")
    payload.setdefault("comparison_targets", [])
    payload.setdefault("expected_evidence", [])
    payload.setdefault("success_criteria", [])
    payload.setdefault("stop_conditions", [])
    payload.setdefault("touches_bridge_queue", False)
    payload.setdefault("requires_bridge_idle", bool(payload.get("touches_bridge_queue", False)))
    payload.setdefault("safety_contract", {
        "must_use_existing_bridge_validation": True,
        "must_not_widen_hardware_or_manifest_safety_limits": True,
        "python_verifies_queue_state_and_hard_boundaries": True,
    })
    return payload

def bridge_queue_activity(bridge_root: Path) -> dict[str, Any]:
    activity: dict[str, Any] = {
        "bridge_root": str(bridge_root),
        "exists": bridge_root.is_dir(),
        "queued": False,
        "running": False,
        "queued_items": [],
        "running_items": [],
    }
    for name in ("queued", "running"):
        folder = bridge_root / name
        items: list[str] = []
        if folder.is_dir():
            for path in sorted(folder.iterdir()):
                if path.name.startswith("."):
                    continue
                items.append(path.name)
        activity[f"{name}_items"] = items
        activity[name] = bool(items)
    activity["busy"] = bool(activity["queued"] or activity["running"])
    return activity

def intent_requests_bridge_queue(intent: dict[str, Any]) -> bool:
    if bool(intent.get("touches_bridge_queue", False)) or bool(intent.get("requires_bridge_idle", False)):
        return True
    action_text = " ".join(
        str(intent.get(key, "") or "")
        for key in ("bridge_action", "intended_bridge_action", "execution_route", "summary")
    ).lower()
    return any(token in action_text for token in ("execute", "submit", "queue", "bridge job", "bridge_job"))

def safety_check_experiment_intent(
    intent: dict[str, Any],
    project: dict[str, Any],
    *,
    bridge_root: Path,
) -> dict[str, Any]:
    hard_errors: list[str] = []
    blockers: list[str] = []
    warnings: list[str] = []
    forbidden_bool_keys = (
        "bypass_bridge",
        "bypass_matlab_bridge",
        "disable_execute_gate",
        "disable_safety_checks",
        "widen_hardware_safety_limits",
        "widen_manifest_safety_limits",
        "edit_hardware_safety_limits",
        "ignore_manifest_limits",
    )
    for key in forbidden_bool_keys:
        if bool(intent.get(key, False)):
            hard_errors.append(f"intent sets forbidden safety bypass key: {key}")

    serialized = json.dumps(intent, ensure_ascii=False, sort_keys=True).lower()
    forbidden_phrases = (
        "bypass bridge",
        "bypass matlab bridge",
        "disable execute gate",
        "disable safety",
        "widen hardware safety",
        "widen manifest safety",
        "ignore manifest limits",
    )
    for phrase in forbidden_phrases:
        if phrase in serialized:
            hard_errors.append(f"intent text contains forbidden safety-bypass phrase: {phrase}")

    bridge_activity = bridge_queue_activity(bridge_root)
    bridge_touching = intent_requests_bridge_queue(intent)
    if bridge_touching and bool(bridge_activity.get("busy", False)):
        blockers.append("bridge queued/running is occupied; bridge-touching intent cannot be verified for submission now")
    if bridge_touching and not bool(intent.get("requires_bridge_idle", False)):
        warnings.append("bridge-touching intent should set requires_bridge_idle=true")
    if not str(intent.get("scientific_rationale", "") or "").strip():
        warnings.append("scientific_rationale is empty; agent should add rationale before relying on this intent")
    if not intent.get("comparison_targets"):
        warnings.append("comparison_targets is empty; agent should record prior/literature/result comparison targets when relevant")
    if not intent.get("expected_evidence"):
        warnings.append("expected_evidence is empty; agent should state what evidence would make the experiment useful")

    if hard_errors:
        verdict = "rejected"
    elif blockers:
        verdict = "blocked"
    else:
        verdict = "verified"
    return {
        "verdict": verdict,
        "hard_errors": hard_errors,
        "blockers": blockers,
        "warnings": warnings,
        "bridge_touching": bridge_touching,
        "bridge_activity": bridge_activity,
        "python_role": "safety_queue_and_hard_boundary_verifier",
        "agent_role": "scientific_intent_author",
        "project_id": str(project.get("project_id", "") or ""),
    }

def queue_experiment_intent(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    ensure_project_knowledge_files(root, project)
    raw_intent = read_json_arg(args.intent_json)
    intent = normalize_experiment_intent(raw_intent, project, args.intent_id)
    intent_id = str(intent["intent_id"])
    out_path = experiment_intent_path(root, "queued", intent_id)
    if out_path.exists() and not args.force:
        raise ValueError(f"experiment intent already exists: {intent_id}. Use --force to replace it.")
    write_json(out_path, intent)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "experiment_intent_queued",
            "project_id": str(project.get("project_id", "") or root.name),
            "intent_id": intent_id,
            "summary": str(intent.get("summary", "") or ""),
            "intent_path": str(out_path),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Experiment intent queued",
        summary=str(intent.get("summary", "") or ""),
        event="experiment_intent_queued",
        actor=args.actor,
        details={"intent_id": intent_id, "intent_path": str(out_path)},
    )
    return {
        "ok": True,
        "action": "queue_experiment_intent",
        "project_id": str(project.get("project_id", "") or root.name),
        "intent_id": intent_id,
        "intent_path": str(out_path),
        "lab_log_path": lab_log_paths["lab_log_path"],
    }

def verify_experiment_intent(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    ensure_project_knowledge_files(root, project)
    source_path, intent = find_experiment_intent(root, args.intent_id)
    if source_path.parent.name not in {"queued", "verified"}:
        raise ValueError(f"intent must be queued or verified to run safety verification: {source_path}")
    verification_input = read_json_arg(args.verification_json) if args.verification_json else {}
    if verification_input:
        intent["agent_verification_context"] = verification_input
    bridge_root = Path(str(args.bridge_root or DEFAULT_BRIDGE_ROOT)).expanduser()
    safety = safety_check_experiment_intent(intent, project, bridge_root=bridge_root)
    intent["safety_verification"] = {
        "checked_at": now_iso(),
        **safety,
    }
    intent["updated_at"] = now_iso()
    verdict = str(safety.get("verdict", "") or "blocked")
    moved_to = ""
    if verdict == "verified":
        intent["status"] = "verified"
        target = experiment_intent_path(root, "verified", str(intent.get("intent_id", "") or args.intent_id))
        write_json(target, intent)
        if source_path != target and source_path.is_file():
            source_path.unlink()
        moved_to = str(target)
    elif verdict == "rejected":
        intent["status"] = "rejected"
        target = experiment_intent_path(root, "rejected", str(intent.get("intent_id", "") or args.intent_id))
        write_json(target, intent)
        if source_path != target and source_path.is_file():
            source_path.unlink()
        moved_to = str(target)
    else:
        intent["status"] = "queued"
        write_json(source_path, intent)
        moved_to = str(source_path)
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "experiment_intent_safety_verified",
            "project_id": str(project.get("project_id", "") or root.name),
            "intent_id": str(intent.get("intent_id", "") or args.intent_id),
            "verdict": verdict,
            "intent_path": moved_to,
            "hard_errors": safety.get("hard_errors", []),
            "blockers": safety.get("blockers", []),
            "warnings": safety.get("warnings", []),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Experiment intent safety verification",
        summary=f"Intent {intent.get('intent_id', args.intent_id)} safety verifier verdict: {verdict}.",
        event="experiment_intent_safety_verified",
        actor=args.actor,
        details={
            "intent_id": str(intent.get("intent_id", "") or args.intent_id),
            "verdict": verdict,
            "intent_path": moved_to,
            "hard_errors": safety.get("hard_errors", []),
            "blockers": safety.get("blockers", []),
            "warnings": safety.get("warnings", []),
        },
    )
    return {
        "ok": True,
        "action": "verify_experiment_intent",
        "project_id": str(project.get("project_id", "") or root.name),
        "intent_id": str(intent.get("intent_id", "") or args.intent_id),
        "verdict": verdict,
        "intent_path": moved_to,
        "safety_verification": safety,
        "lab_log_path": lab_log_paths["lab_log_path"],
    }

def complete_experiment_intent(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    source_path, intent = find_experiment_intent(root, args.intent_id)
    result = read_json_arg(args.result_json)
    status = str(result.get("status", "") or "").strip().lower()
    if status not in VALID_EXPERIMENT_INTENT_TERMINAL_STATUSES:
        raise ValueError(f"experiment intent result status must be one of {sorted(VALID_EXPERIMENT_INTENT_TERMINAL_STATUSES)}.")
    intent["status"] = status
    intent["completed_at"] = now_iso()
    intent["result"] = result
    target = experiment_intent_path(root, "done", str(intent.get("intent_id", "") or args.intent_id))
    write_json(target, intent)
    if source_path != target and source_path.is_file():
        source_path.unlink()
    append_jsonl(
        get_ledger_path(root),
        {
            "timestamp": now_iso(),
            "actor": args.actor,
            "event": "experiment_intent_completed",
            "project_id": str(project.get("project_id", "") or root.name),
            "intent_id": str(intent.get("intent_id", "") or args.intent_id),
            "status": status,
            "summary": str(result.get("summary", "") or ""),
            "intent_path": str(target),
        },
    )
    lab_log_paths = append_lab_log(
        root,
        project,
        title="Experiment intent completed",
        summary=str(result.get("summary", "") or ""),
        event="experiment_intent_completed",
        actor=args.actor,
        details={"intent_id": str(intent.get("intent_id", "") or args.intent_id), "status": status, "intent_path": str(target)},
    )
    return {
        "ok": True,
        "action": "complete_experiment_intent",
        "project_id": str(project.get("project_id", "") or root.name),
        "intent_id": str(intent.get("intent_id", "") or args.intent_id),
        "status": status,
        "intent_path": str(target),
        "lab_log_path": lab_log_paths["lab_log_path"],
    }

def record_event(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    payload = read_json_arg(args.event_json) if args.event_json else {}
    figures = normalize_lab_log_figures(payload.get("figures", []))
    event = {
        "timestamp": now_iso(),
        "actor": args.actor,
        "event": args.event or str(payload.get("event", "") or "note"),
        "project_id": str(project.get("project_id", "") or root.name),
        "summary": args.summary or str(payload.get("summary", "") or ""),
    }
    for key, value in payload.items():
        if key not in event:
            event[key] = value
    append_jsonl(get_ledger_path(root), event)
    lab_log_paths: dict[str, str] = {}
    if not bool(getattr(args, "no_lab_log", False)):
        lab_log_details = {
            key: value
            for key, value in event.items()
            if key not in {"timestamp", "actor", "event", "project_id", "summary", "figures"}
        }
        lab_log_paths = append_lab_log(
            root,
            project,
            title=f"Event recorded: {event['event']}",
            summary=str(event.get("summary", "") or ""),
            event=str(event.get("event", "") or ""),
            actor=args.actor,
            details=lab_log_details,
            figures=figures,
        )
    state = load_state(root)
    state["updated_at"] = now_iso()
    state["last_event"] = event
    if lab_log_paths:
        state["last_lab_log_entry"] = {
            "title": f"Event recorded: {event['event']}",
            "event": str(event.get("event", "") or ""),
            "summary": str(event.get("summary", "") or ""),
            "lab_log_path": lab_log_paths.get("lab_log_path", ""),
            "daily_log_path": lab_log_paths.get("daily_log_path", ""),
        }
    write_json(get_state_path(root), state)
    evidence_recorded: dict[str, Any] = {}
    evidence_candidate = event_to_evidence_record(event)
    if evidence_candidate:
        evidence_recorded = append_evidence_record(
            root,
            project,
            evidence_candidate,
            actor=args.actor,
            source="record-event",
        )
    completion_marker = maybe_write_terminal_evidence_completion_marker(
        root,
        project,
        event,
        actor=args.actor,
        source="record_event",
    )
    return {
        "ok": True,
        "action": "record_event",
        "project_id": str(project.get("project_id", "") or root.name),
        "event": event,
        "lab_log_path": lab_log_paths.get("lab_log_path", ""),
        "daily_log_path": lab_log_paths.get("daily_log_path", ""),
        "evidence_recorded": evidence_recorded,
        "completion_marker": completion_marker,
    }

def record_lab_log(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    details = read_json_arg(args.details_json) if args.details_json else {}
    figures = normalize_lab_log_figures(details.pop("figures", []))
    if args.figure_json:
        figures.extend(normalize_lab_log_figures(read_json_arg(args.figure_json)))
    for figure_path in args.figure or []:
        figures.append({"path": str(figure_path), "caption": ""})
    title = str(args.title or "Project note").strip() or "Project note"
    summary = str(args.summary or details.pop("summary", "") or "").strip()
    event_name = str(args.event or "lab_log_note").strip() or "lab_log_note"
    lab_log_paths = append_lab_log(
        root,
        project,
        title=title,
        summary=summary,
        event=event_name,
        actor=args.actor,
        details=details,
        figures=figures,
    )
    event = {
        "timestamp": now_iso(),
        "actor": args.actor,
        "event": event_name,
        "project_id": str(project.get("project_id", "") or root.name),
        "title": title,
        "summary": summary,
        "details": details,
        "figures": figures,
        "lab_log_path": lab_log_paths["lab_log_path"],
        "daily_log_path": lab_log_paths["daily_log_path"],
    }
    append_jsonl(get_ledger_path(root), event)
    evidence_recorded: list[dict[str, Any]] = []
    if figures:
        evidence_recorded.append(
            append_evidence_record(
                root,
                project,
                {
                    "category": "figure",
                    "summary": f"{title}: {summary}" if summary else title,
                    "paths": [figure.get("path", "") for figure in figures if str(figure.get("path", "") or "").strip()],
                    "provenance": {
                        "ledger_event": event_name,
                        "lab_log_path": lab_log_paths["lab_log_path"],
                        "daily_log_path": lab_log_paths["daily_log_path"],
                    },
                },
                actor=args.actor,
                source="record-lab-log",
            )
        )
    state = load_state(root)
    state["updated_at"] = now_iso()
    state["last_lab_log_entry"] = {
        "title": title,
        "event": event_name,
        "summary": summary,
        "figure_count": len(figures),
        "lab_log_path": lab_log_paths["lab_log_path"],
        "daily_log_path": lab_log_paths["daily_log_path"],
    }
    write_json(get_state_path(root), state)
    return {
        "ok": True,
        "action": "record_lab_log",
        "project_id": str(project.get("project_id", "") or root.name),
        "title": title,
        "figure_count": len(figures),
        "lab_log_path": lab_log_paths["lab_log_path"],
        "daily_log_path": lab_log_paths["daily_log_path"],
        "event": event,
        "evidence_recorded": evidence_recorded,
    }

def audit_add(findings: list[dict[str, Any]], severity: str, check: str, summary: str, *, recommendation: str = "", details: Any = None) -> None:
    finding: dict[str, Any] = {
        "severity": severity,
        "check": check,
        "summary": summary,
    }
    if recommendation:
        finding["recommendation"] = recommendation
    if details is not None:
        finding["details"] = details
    findings.append(finding)

def audit_scheduler_research_agent(findings: list[dict[str, Any]]) -> None:
    scheduler_path = WORKSPACE_ROOT / "nv_project_scheduler_runner.sh"
    if not scheduler_path.is_file():
        audit_add(findings, "warn", "scheduler_research_agent", "scheduler runner was not found.", recommendation=str(scheduler_path))
        return
    text = scheduler_path.read_text(encoding="utf-8", errors="replace")
    if "NV_PROJECT_AGENT_ID" not in text:
        audit_add(
            findings,
            "warn",
            "scheduler_research_agent",
            "scheduler runner does not expose NV_PROJECT_AGENT_ID.",
            recommendation="Use a dedicated researcher agent id instead of hard-coding main.",
        )
    if "--agent-id main" in text:
        audit_add(
            findings,
            "error",
            "scheduler_research_agent",
            "scheduler runner still hard-codes --agent-id main.",
            recommendation="Route project wakes to nv-researcher.",
        )

def audit_openclaw_config(findings: list[dict[str, Any]], config_path: Path) -> None:
    cfg = read_json_safely(config_path)
    agents = cfg.get("agents", {}) if isinstance(cfg.get("agents"), dict) else {}
    agent_list = agents.get("list", []) if isinstance(agents.get("list"), list) else []
    agent_ids = {str(agent.get("id", "") or "") for agent in agent_list if isinstance(agent, dict)}
    if DEFAULT_RESEARCH_AGENT_ID not in agent_ids:
        audit_add(
            findings,
            "warn",
            "openclaw_research_agent",
            f"OpenClaw config does not list {DEFAULT_RESEARCH_AGENT_ID}.",
            recommendation="Add a dedicated nv-researcher agent profile for project execution.",
        )
    defaults = agents.get("defaults", {}) if isinstance(agents.get("defaults"), dict) else {}
    default_model = ""
    if isinstance(defaults.get("model"), dict):
        default_model = str(defaults.get("model", {}).get("primary", "") or "")
    if default_model != "openai-codex/gpt-5.5":
        audit_add(findings, "warn", "openclaw_model", "Default OpenClaw model is not openai-codex/gpt-5.5.", details={"model": default_model})
    research_agent = next(
        (agent for agent in agent_list if isinstance(agent, dict) and str(agent.get("id", "") or "") == DEFAULT_RESEARCH_AGENT_ID),
        {},
    )
    research_thinking = str(research_agent.get("thinkingDefault", "") or defaults.get("thinkingDefault", "") or "")
    if research_thinking != "xhigh":
        audit_add(
            findings,
            "warn",
            "openclaw_thinking",
            f"Default OpenClaw thinking level for {DEFAULT_RESEARCH_AGENT_ID} is not xhigh.",
            details={"thinkingDefault": research_thinking},
        )
    hooks = cfg.get("hooks", {}) if isinstance(cfg.get("hooks"), dict) else {}
    prefixes = hooks.get("allowedSessionKeyPrefixes", []) if isinstance(hooks.get("allowedSessionKeyPrefixes"), list) else []
    if hooks.get("allowRequestSessionKey") is not True:
        audit_add(
            findings,
            "warn",
            "hook_session_isolation",
            "hooks.allowRequestSessionKey is not enabled, so cron cannot request a project-specific researcher session key.",
            recommendation="Enable it only with restrictive allowedSessionKeyPrefixes.",
        )
    if not any(str(prefix).startswith(f"agent:{DEFAULT_RESEARCH_AGENT_ID}:hook:") for prefix in prefixes):
        audit_add(
            findings,
            "warn",
            "hook_session_prefix",
            "allowedSessionKeyPrefixes does not include the nv-researcher hook namespace.",
            recommendation=f"Add agent:{DEFAULT_RESEARCH_AGENT_ID}:hook: to keep project wakes isolated.",
        )
    mappings = hooks.get("mappings", []) if isinstance(hooks.get("mappings"), list) else []
    nv_mapping_issues: list[dict[str, str]] = []
    for mapping in mappings:
        if not isinstance(mapping, dict):
            continue
        match = mapping.get("match", {}) if isinstance(mapping.get("match"), dict) else {}
        path = str(match.get("path", "") or "")
        if not path.startswith("nv-"):
            continue
        agent_id = str(mapping.get("agentId", "") or "")
        session_key = str(mapping.get("sessionKey", "") or "")
        if agent_id != DEFAULT_RESEARCH_AGENT_ID or not session_key.startswith(f"agent:{DEFAULT_RESEARCH_AGENT_ID}:hook:"):
            nv_mapping_issues.append({"path": path, "agentId": agent_id, "sessionKey": session_key})
    if nv_mapping_issues:
        audit_add(
            findings,
            "warn",
            "nv_hook_research_agent",
            "One or more NV hook mappings are not routed to nv-researcher with an agent-scoped hook session.",
            recommendation="Set agentId=nv-researcher and sessionKey=agent:nv-researcher:hook:... for NV project hooks.",
            details=nv_mapping_issues,
        )

def audit_backlog_autonomy(root: Path, findings: list[dict[str, Any]]) -> None:
    backlog_path = get_backlog_path(root)
    if not backlog_path.is_file():
        return
    backlog = read_json_safely(backlog_path)
    items = backlog.get("items", []) if isinstance(backlog.get("items"), list) else []
    overspec_pattern = re.compile(r"\b(averages|repetitions|tau|mw_freq|shots)\s*[=:]\s*[^,;\n]+", re.IGNORECASE)
    for item in items:
        if not isinstance(item, dict) or str(item.get("status", "pending") or "pending") != "pending":
            continue
        item_id = str(item.get("id", "") or "")
        text = "\n".join(str(item.get(key, "") or "") for key in ("summary", "agent_prompt", "details", "last_summary"))
        matches = overspec_pattern.findall(text)
        if matches and not bool(item.get("human_specified", False)):
            audit_add(
                findings,
                "info",
                "backlog_scientific_specificity",
                f"Pending backlog item {item_id} appears to encode measurement parameters.",
                recommendation="Keep exact scientific choices in research_state/experiment_intent unless they are explicit human constraints or evidence-derived.",
                details={"item_id": item_id, "matched_terms": sorted(set(matches))},
            )
        bridge_touching = bool(item.get("touches_bridge_queue", False) or item.get("requires_bridge_idle", False))
        kind = normalize_backlog_kind(item)
        if kind == "research_task" and any(token in text.lower() for token in ("execute", "submit bridge", "queue bridge")) and not bridge_touching:
            audit_add(
                findings,
                "warn",
                "backlog_bridge_flags",
                f"Pending backlog item {item_id} may touch the bridge but lacks bridge idle flags.",
                recommendation="Set requires_bridge_idle=true or touches_bridge_queue=true for bridge-touching queue work.",
                details={"item_id": item_id},
            )

def closeout_report_exists(root: Path) -> bool:
    summaries = root / "summaries"
    if not summaries.is_dir():
        return False
    tex_files = {path.stem for path in summaries.glob("*.tex")}
    pdf_files = {path.stem for path in summaries.glob("*.pdf")}
    return bool(tex_files & pdf_files)

def autonomy_audit(args: argparse.Namespace) -> dict[str, Any]:
    root = project_dir(args.project_id)
    project = load_project(root)
    research_context = research_context_overview(root, project)
    findings: list[dict[str, Any]] = []

    architecture = project.get("research_architecture", {}) if isinstance(project.get("research_architecture"), dict) else {}
    if architecture.get("project_execution_agent_id") != DEFAULT_RESEARCH_AGENT_ID:
        audit_add(
            findings,
            "warn",
            "project_research_agent",
            "project research_architecture does not point to nv-researcher.",
            recommendation="Patch research_architecture.project_execution_agent_id to nv-researcher unless this project intentionally overrides it.",
            details={"project_execution_agent_id": architecture.get("project_execution_agent_id", "")},
        )
    if architecture.get("project_json_scope") != "policy_constraints_lifecycle_and_human_request":
        audit_add(
            findings,
            "info",
            "project_json_scope",
            "project.json does not explicitly declare the policy/constraint-only scope.",
            recommendation="Keep scientific plans in research_state, research_agenda, evidence_index, and experiment_intents.",
        )
    for key, path_text in (
        ("research_state_path", research_context.get("research_state_path", "")),
        ("research_agenda_path", research_context.get("research_agenda_path", "")),
        ("evidence_index_path", research_context.get("evidence_index_path", "")),
    ):
        if not Path(str(path_text)).exists():
            audit_add(findings, "error", key, f"{key} is missing.", recommendation="Run status/tick or init to recreate project knowledge files.")

    intent_counts = research_context.get("experiment_intents", {}) if isinstance(research_context.get("experiment_intents"), dict) else {}
    if not isinstance(intent_counts, dict) or not {"queued", "verified", "rejected", "done"}.issubset(set(intent_counts.keys())):
        audit_add(findings, "error", "experiment_intents", "experiment_intents directories are incomplete.")

    inbox_count = len(list_advice_inbox_files(root))
    if inbox_count:
        audit_add(
            findings,
            "warn",
            "advice_inbox",
            f"{inbox_count} advice inbox message(s) are unprocessed.",
            recommendation="Use list-advice-inbox and dispose-advice after interpreting each message.",
        )

    audit_backlog_autonomy(root, findings)
    audit_scheduler_research_agent(findings)
    audit_openclaw_config(findings, Path(str(args.config_path or DEFAULT_CONFIG_PATH)).expanduser())

    lifecycle = project_lifecycle(project)
    if lifecycle in INACTIVE_PROJECT_LIFECYCLES and not closeout_report_exists(root):
        audit_add(
            findings,
            "warn",
            "closeout_report",
            f"Project lifecycle is {lifecycle}, but no paired LaTeX/PDF closeout report was found in summaries/.",
            recommendation="Create a detailed LaTeX report with figures before treating the project as finished.",
        )

    severity_rank = {"error": 3, "warn": 2, "info": 1}
    max_severity = max((severity_rank.get(str(item.get("severity", "")), 0) for item in findings), default=0)
    return {
        "ok": True,
        "action": "autonomy_audit",
        "project_id": str(project.get("project_id", "") or root.name),
        "project_dir": str(root),
        "status": "error" if max_severity >= 3 else "warn" if max_severity == 2 else "ok",
        "finding_count": len(findings),
        "findings": findings,
        "research_context": research_context,
    }

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage durable OpenClaw NV project state.")
    parser.add_argument("--actor", default="openclaw-project-manager")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="Create a project directory and initial state.")
    init.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", default="")
    init.add_argument("--objective", default="")
    init.add_argument("--sample-id", default=DEFAULT_SAMPLE_ID)
    init.add_argument("--spec-json", default="")
    init.add_argument("--spec-file", default="")
    init.add_argument("--force", action="store_true")

    start = sub.add_parser("start-project", help="Create a project and record the initial human request.")
    start.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    start.add_argument("--objective", required=True)
    start.add_argument("--human-request", required=True)
    start.add_argument("--sample-id", default=DEFAULT_SAMPLE_ID)
    start.add_argument("--spec-json", default="")
    start.add_argument("--spec-file", default="")
    start.add_argument("--force", action="store_true")

    update = sub.add_parser("update-project", help="Patch project policy/spec fields.")
    update.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    update.add_argument("--patch-json", default="")
    update.add_argument("--patch-file", default="")
    update.add_argument("--summary", default="")

    status = sub.add_parser("status", help="Read project state and compute the next action.")
    status.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)

    tick = sub.add_parser("tick", help="Persist a project tick and next action.")
    tick.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)

    backlog = sub.add_parser("queue-backlog-item", help="Add or replace a project backlog item.")
    backlog.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    backlog.add_argument("--item-json", required=True)
    backlog.add_argument("--item-id", default="")
    backlog.add_argument("--force", action="store_true")

    backlog_update = sub.add_parser("update-backlog-item", help="Update a project backlog item status or metadata.")
    backlog_update.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    backlog_update.add_argument("--item-id", required=True)
    backlog_update.add_argument("--status", default="")
    backlog_update.add_argument("--summary", default="")
    backlog_update.add_argument("--update-json", default="")

    physical = sub.add_parser("queue-physical-request", help="Queue a physical-action request.")
    physical.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    physical.add_argument("--request-json", required=True)
    physical.add_argument("--request-id", default="")

    complete = sub.add_parser("complete-physical-request", help="Record a physical-action result.")
    complete.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    complete.add_argument("--result-json", required=True)
    complete.add_argument("--request-id", default="")

    code_change = sub.add_parser("queue-code-change-request", help="Queue a bounded experiment-code change request.")
    code_change.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    code_change.add_argument("--request-json", required=True)
    code_change.add_argument("--request-id", default="")

    code_complete = sub.add_parser("complete-code-change-request", help="Record a code-change result.")
    code_complete.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    code_complete.add_argument("--result-json", required=True)
    code_complete.add_argument("--request-id", default="")

    evidence = sub.add_parser("record-evidence", help="Append a project evidence-index record.")
    evidence.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    evidence.add_argument("--evidence-json", default="")
    evidence.add_argument("--evidence-id", default="")
    evidence.add_argument("--category", default="")
    evidence.add_argument("--summary", default="")
    evidence.add_argument("--path", action="append", default=[])

    intent = sub.add_parser("queue-experiment-intent", help="Queue an agent-authored scientific experiment intent.")
    intent.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    intent.add_argument("--intent-json", required=True)
    intent.add_argument("--intent-id", default="")
    intent.add_argument("--force", action="store_true")

    intent_verify = sub.add_parser("verify-experiment-intent", help="Run deterministic safety/queue checks for an experiment intent.")
    intent_verify.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    intent_verify.add_argument("--intent-id", required=True)
    intent_verify.add_argument("--verification-json", default="")
    intent_verify.add_argument("--bridge-root", default=str(DEFAULT_BRIDGE_ROOT))

    intent_complete = sub.add_parser("complete-experiment-intent", help="Move an experiment intent to done with a terminal result.")
    intent_complete.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    intent_complete.add_argument("--intent-id", required=True)
    intent_complete.add_argument("--result-json", required=True)

    record = sub.add_parser("record-event", help="Append an arbitrary project ledger event.")
    record.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    record.add_argument("--event", default="")
    record.add_argument("--summary", default="")
    record.add_argument("--event-json", default="")
    record.add_argument("--no-lab-log", action="store_true")

    lab_log = sub.add_parser("record-lab-log", help="Append a human-facing lab log entry with optional figures.")
    lab_log.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    lab_log.add_argument("--title", default="")
    lab_log.add_argument("--summary", default="")
    lab_log.add_argument("--event", default="lab_log_note")
    lab_log.add_argument("--details-json", default="")
    lab_log.add_argument("--figure-json", default="")
    lab_log.add_argument("--figure", action="append", default=[])

    advice_list = sub.add_parser("list-advice-inbox", help="List unprocessed advice inbox messages.")
    advice_list.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    advice_list.add_argument("--limit", type=int, default=0)

    advice_dispose = sub.add_parser("dispose-advice", help="Record and move one advice inbox message.")
    advice_dispose.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    advice_dispose.add_argument("--file", required=True)
    advice_dispose.add_argument("--disposition", choices=sorted(VALID_ADVICE_DISPOSITIONS), required=True)
    advice_dispose.add_argument("--classification", choices=sorted(VALID_ADVICE_CLASSIFICATIONS), default="note")
    advice_dispose.add_argument("--summary", required=True)
    advice_dispose.add_argument("--effective-guidance", default="")
    advice_dispose.add_argument("--reason", default="")
    advice_dispose.add_argument("--details-json", default="")
    advice_dispose.add_argument("--no-lab-log", action="store_true")

    audit = sub.add_parser("autonomy-audit", help="Audit whether project architecture is preserving researcher-agent autonomy.")
    audit.add_argument("--project-id", dest="project_id", metavar="PROJECT_ID", required=True)
    audit.add_argument("--config-path", default=str(DEFAULT_CONFIG_PATH))
    return parser

def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "init":
            payload = init_project(args)
        elif args.command == "start-project":
            payload = start_project(args)
        elif args.command == "update-project":
            payload = update_project(args)
        elif args.command == "status":
            payload = status_or_tick(args, tick=False)
        elif args.command == "tick":
            payload = status_or_tick(args, tick=True)
        elif args.command == "queue-backlog-item":
            payload = queue_backlog_item(args)
        elif args.command == "update-backlog-item":
            payload = update_backlog_item(args)
        elif args.command == "queue-physical-request":
            payload = queue_physical_request(args)
        elif args.command == "complete-physical-request":
            payload = complete_physical_request(args)
        elif args.command == "queue-code-change-request":
            payload = queue_code_change_request(args)
        elif args.command == "complete-code-change-request":
            payload = complete_code_change_request(args)
        elif args.command == "record-evidence":
            payload = record_evidence(args)
        elif args.command == "queue-experiment-intent":
            payload = queue_experiment_intent(args)
        elif args.command == "verify-experiment-intent":
            payload = verify_experiment_intent(args)
        elif args.command == "complete-experiment-intent":
            payload = complete_experiment_intent(args)
        elif args.command == "record-event":
            payload = record_event(args)
        elif args.command == "record-lab-log":
            payload = record_lab_log(args)
        elif args.command == "list-advice-inbox":
            payload = list_advice_inbox(args)
        elif args.command == "dispose-advice":
            payload = dispose_advice(args)
        elif args.command == "autonomy-audit":
            payload = autonomy_audit(args)
        else:
            raise ValueError(f"unsupported command: {args.command}")
    except Exception as exc:
        payload = {
            "ok": False,
            "error": type(exc).__name__,
            "message": str(exc),
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit("Direct execution of this execution-source file is disabled in the public release.")
