#!/usr/bin/env python3
"""Submit standalone OpenClaw Imaging/TrackCenter jobs to the NV bridge queue."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_BRIDGE_ROOT = Path("<NV_BRIDGE_ROOT>")


def bridge_root() -> Path:
    raw = os.environ.get("NV_BRIDGE_ROOT", "").strip()
    if raw:
        return Path(raw)
    return DEFAULT_BRIDGE_ROOT


def slug(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_") or "job"


def make_job_id(prefix: str) -> str:
    return f"{slug(prefix)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


def base_job(args: argparse.Namespace, recipe: str, job_id_prefix: str) -> dict[str, Any]:
    metadata: dict[str, Any] = {
        "requested_by": args.requested_by,
        "queue_execute_opt_in": args.mode == "execute",
        "require_landmark_match": False,
    }
    if args.intent:
        metadata["intent"] = args.intent

    return {
        "job_id": args.job_id or make_job_id(job_id_prefix),
        "mode": args.mode,
        "recipe": recipe,
        "sample_id": args.sample_id,
        "limits": {
            "max_mw_power_dbm": 0,
            "allow_stage_motion": True,
            "allow_laser_profile": False,
        },
        "metadata": metadata,
    }


def submit_job(job: dict[str, Any], root: Path) -> Path:
    queued = root / "queued"
    staging = root / "staging"
    queued.mkdir(parents=True, exist_ok=True)
    staging.mkdir(parents=True, exist_ok=True)
    job_dir = queued / str(job["job_id"])
    staging_dir = staging / f"{job['job_id']}__staging"
    if job_dir.exists():
        raise SystemExit(f"Queued job directory already exists: {job_dir}")
    if staging_dir.exists():
        raise SystemExit(f"Staging job directory already exists: {staging_dir}")

    try:
        staging_dir.mkdir(parents=True, exist_ok=False)
        tmp_path = staging_dir / "job.json.tmp"
        path = staging_dir / "job.json"
        tmp_path.write_text(json.dumps(job, indent=2, sort_keys=False) + "\n", encoding="utf-8")
        os.replace(tmp_path, path)
        os.replace(staging_dir, job_dir)
    except Exception:
        if staging_dir.exists():
            shutil.rmtree(staging_dir, ignore_errors=True)
        raise
    return job_dir / "job.json"


def add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--mode", choices=["validate", "dry_run", "execute"], default="execute")
    parser.add_argument("--sample-id", default="NV23")
    parser.add_argument("--job-id", default="")
    parser.add_argument("--requested-by", default="openclaw")
    parser.add_argument("--intent", default="")
    parser.add_argument("--bridge-root", default="")
    parser.add_argument("--print-json", action="store_true")


def scan_job(args: argparse.Namespace) -> dict[str, Any]:
    job = base_job(args, "imaging_scan_v1", f"{args.sample_id}_imaging_scan")
    job["imaging"] = {
        "center": [float(v) for v in args.center],
        "half_span_um": [float(v) for v in args.half_span_um],
        "xy_points": int(args.xy_points),
        "z_offsets_um": [float(v) for v in args.z_offsets_um],
        "dwell_seconds": float(args.dwell_seconds),
        "artifact_label": args.artifact_label,
    }
    return job


def track_job(args: argparse.Namespace) -> dict[str, Any]:
    job = base_job(args, "track_center_v1", f"{args.sample_id}_track_center")
    job["tracking"] = {
        "seed_position": [float(v) for v in args.seed_position],
        "minimum_final_kcps": float(args.minimum_final_kcps),
        "tracking_z_seed_offsets_um": [float(v) for v in args.tracking_z_seed_offsets_um],
        "update_registry": bool(args.update_registry),
    }
    if args.nv_name:
        job["tracking"]["nv_name"] = args.nv_name
        job["metadata"]["nv_name"] = args.nv_name
    return job


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Queue standalone Imaging scan.")
    add_common(scan)
    scan.add_argument("--center", nargs=3, type=float, required=True, metavar=("X", "Y", "Z"))
    scan.add_argument("--half-span-um", nargs=2, type=float, default=[5.0, 5.0], metavar=("X", "Y"))
    scan.add_argument("--xy-points", type=int, default=61)
    scan.add_argument("--z-offsets-um", nargs="+", type=float, default=[-1.0, 0.0, 1.0])
    scan.add_argument("--dwell-seconds", type=float, default=0.005)
    scan.add_argument("--artifact-label", default="agent_imaging_scan")
    scan.set_defaults(builder=scan_job)

    track = sub.add_parser("track", help="Queue standalone TrackCenter.")
    add_common(track)
    track.add_argument("--seed-position", nargs=3, type=float, required=True, metavar=("X", "Y", "Z"))
    track.add_argument("--minimum-final-kcps", type=float, default=8.0)
    track.add_argument("--tracking-z-seed-offsets-um", nargs="+", type=float, default=[0.0, -0.5, 0.5])
    track.add_argument("--update-registry", action="store_true")
    track.add_argument("--nv-name", default="")
    track.set_defaults(builder=track_job)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    job = args.builder(args)
    if args.print_json:
        print(json.dumps(job, indent=2))
        return 0

    root = Path(args.bridge_root) if args.bridge_root else bridge_root()
    path = submit_job(job, root)
    print(json.dumps({"ok": True, "job_id": job["job_id"], "job_path": str(path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit("Direct execution of this execution-source file is disabled in the public release.")
