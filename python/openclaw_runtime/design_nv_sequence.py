#!/usr/bin/env python3
"""Create staging XML + staging manifest proposals for new NV sequences."""

from __future__ import annotations

import argparse
import copy
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DEFAULT_REPO_ROOT = Path(os.environ.get("MATLAB_23C_ROOT", "<MATLAB_23C_ROOT>")).expanduser()
DEFAULT_MANIFEST_ROOT = DEFAULT_REPO_ROOT / "claw" / "sequence_manifests"
DEFAULT_STAGING_SEQUENCE_DIR = DEFAULT_REPO_ROOT / "SavedSequences" / "SavedSequences-AWG" / "_openclaw_staging"
DEFAULT_STAGING_MANIFEST_DIR = DEFAULT_REPO_ROOT / "claw" / "sequence_manifests" / "staging"
VALID_ALLOWED_MODES = {"validate", "dry_run", "execute"}

FLOAT_LINE_RE = re.compile(
    r"^(?P<prefix>\s*(?P<name>[A-Za-z]\w*)\s*=\s*float\s*\()\s*(?P<default>[^,]+)(?P<suffix>\s*,\s*[^,]+,\s*[^\)]+\)\s*;?.*)$",
    re.IGNORECASE,
)
BOOLEAN_LINE_RE = re.compile(
    r"^(?P<prefix>\s*(?P<name>[A-Za-z]\w*)\s*=\s*boolean\s*\()\s*(?P<default>[^\)]+)(?P<suffix>\s*\)\s*;?.*)$",
    re.IGNORECASE,
)


def slug(text: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "_", (text or "").strip().lower()).strip("_")
    return value or "sequence"


def normalize_path(raw_value: str, default_path: Path) -> Path:
    text = (raw_value or "").strip()
    if not text:
        return default_path.resolve()
    return Path(os.path.expanduser(text)).resolve()


def read_json(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    if raw.startswith("\ufeff"):
        raw = raw[1:]
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return data


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def deep_merge_dicts(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge_dicts(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def load_manifest(manifest_root: Path, manifest_id: str) -> tuple[dict[str, Any], Path, str]:
    file_name = manifest_id if manifest_id.endswith(".json") else f"{manifest_id}.json"
    candidates = [
        ("validated", manifest_root / "validated" / file_name),
        ("staging", manifest_root / "staging" / file_name),
    ]
    for scope, path in candidates:
        if path.is_file():
            return read_json(path), path, scope
    raise ValueError(f"Sequence manifest not found: {manifest_id}")


def list_validated_manifests(manifest_root: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    validated_root = manifest_root / "validated"
    if not validated_root.is_dir():
        return entries
    for path in sorted(validated_root.glob("*.json")):
        try:
            manifest = read_json(path)
        except Exception as exc:
            entries.append({"id": path.stem, "error": str(exc), "path": str(path)})
            continue
        entries.append(
            {
                "id": manifest.get("id", path.stem),
                "label": manifest.get("label", ""),
                "sequence_file": manifest.get("sequence_file", ""),
                "catalog_key": manifest.get("catalog_key", ""),
                "legacy_recipe": manifest.get("legacy_recipe", ""),
                "path": str(path),
            }
        )
    return entries


def load_spec(path: Path) -> dict[str, Any]:
    spec = read_json(path)
    spec.setdefault("notes", [])
    spec.setdefault("aliases", [])
    spec.setdefault("default_overrides", {})
    return spec


def resolve_repo_path(repo_root: Path, relative_path: str) -> Path:
    candidate = (repo_root / relative_path).resolve()
    return candidate


def relative_to_repo(repo_root: Path, path: Path) -> str:
    return path.resolve().relative_to(repo_root.resolve()).as_posix()


def format_float(value: float) -> str:
    return format(float(value), ".15g")


def build_xml_default_map(manifest: dict[str, Any]) -> dict[str, Any]:
    desired: dict[str, Any] = {}
    typed_vars = manifest.get("typed_vars") or {}
    float_vars = manifest.get("float_vars") or {}

    for name, meta in typed_vars.items():
        if isinstance(meta, dict) and "default" in meta:
            desired[name] = meta["default"]

    for name, meta in float_vars.items():
        if name not in desired and isinstance(meta, dict) and "default" in meta:
            desired[name] = meta["default"]

    return desired


def replace_variable_defaults(xml_text: str, desired_defaults: dict[str, Any]) -> tuple[str, list[str], list[str]]:
    lines = xml_text.splitlines(keepends=True)
    seen: list[str] = []
    typed_touched: list[str] = []

    updated_lines: list[str] = []
    for line in lines:
        replaced = False
        float_match = FLOAT_LINE_RE.match(line.rstrip("\n"))
        if float_match:
            name = float_match.group("name")
            if name in desired_defaults:
                value = desired_defaults[name]
                prefix = float_match.group("prefix")
                suffix = float_match.group("suffix")
                newline = "\n" if line.endswith("\n") else ""
                updated_lines.append(f"{prefix}{format_float(float(value))}{suffix}{newline}")
                seen.append(name)
                typed_touched.append(name)
                replaced = True
        if not replaced:
            bool_match = BOOLEAN_LINE_RE.match(line.rstrip("\n"))
            if bool_match:
                name = bool_match.group("name")
                if name in desired_defaults:
                    value = desired_defaults[name]
                    prefix = bool_match.group("prefix")
                    suffix = bool_match.group("suffix")
                    rendered = "1" if bool(value) else "0"
                    newline = "\n" if line.endswith("\n") else ""
                    updated_lines.append(f"{prefix}{rendered}{suffix}{newline}")
                    seen.append(name)
                    typed_touched.append(name)
                    replaced = True
        if not replaced:
            updated_lines.append(line)

    return "".join(updated_lines), seen, typed_touched


def update_manifest_defaults(manifest: dict[str, Any], overrides: dict[str, Any]) -> tuple[dict[str, Any], list[str], list[str]]:
    updated = copy.deepcopy(manifest)
    float_vars = updated.setdefault("float_vars", {})
    typed_vars = updated.setdefault("typed_vars", copy.deepcopy(float_vars))
    float_touched: list[str] = []
    typed_touched: list[str] = []

    for name, value in overrides.items():
        if name in float_vars and isinstance(float_vars[name], dict):
            float_vars[name]["default"] = float(value)
            float_touched.append(name)
        if name in typed_vars and isinstance(typed_vars[name], dict):
            field_type = str(typed_vars[name].get("type", "float")).lower()
            if field_type == "boolean":
                typed_vars[name]["default"] = bool(value)
            else:
                typed_vars[name]["default"] = float(value)
            typed_touched.append(name)

    return updated, float_touched, typed_touched


def validate_spec(spec: dict[str, Any], base_manifest: dict[str, Any]) -> None:
    required = ["new_id", "label", "description", "base_manifest_id"]
    missing = [field for field in required if not str(spec.get(field, "")).strip()]
    if missing:
        raise ValueError(f"Spec is missing required fields: {', '.join(missing)}")

    overrides = spec.get("default_overrides", {})
    if not isinstance(overrides, dict):
        raise ValueError("default_overrides must be an object.")

    allowed_names = set((base_manifest.get("typed_vars") or {}).keys()) | set((base_manifest.get("float_vars") or {}).keys())
    unknown = sorted(name for name in overrides if name not in allowed_names)
    if unknown:
        raise ValueError(f"default_overrides contains unknown variables for the base manifest: {', '.join(unknown)}")

    scan_defaults = spec.get("scan_defaults")
    if scan_defaults is not None:
        if not isinstance(scan_defaults, dict):
            raise ValueError("scan_defaults must be an object.")
        for key in ("vary_prop", "begin", "end", "points"):
            if key not in scan_defaults:
                raise ValueError(f"scan_defaults.{key} is required when scan_defaults is provided.")

    xml_text = spec.get("xml_text")
    if xml_text is not None and not isinstance(xml_text, str):
        raise ValueError("xml_text must be a string when provided.")

    manifest_overrides = spec.get("manifest_overrides")
    if manifest_overrides is not None and not isinstance(manifest_overrides, dict):
        raise ValueError("manifest_overrides must be an object when provided.")
    if isinstance(manifest_overrides, dict):
        allowed_modes = manifest_overrides.get("allowed_modes")
        if allowed_modes is not None:
            if not isinstance(allowed_modes, list):
                raise ValueError("manifest_overrides.allowed_modes must be a list when provided.")
            invalid_modes = [str(mode or "") for mode in allowed_modes if str(mode or "") not in VALID_ALLOWED_MODES]
            if invalid_modes:
                raise ValueError(
                    "manifest_overrides.allowed_modes contains invalid modes: " + ", ".join(invalid_modes)
                )


def build_staging_manifest(
    spec: dict[str, Any],
    base_manifest: dict[str, Any],
    sequence_relative_path: str,
    updated_manifest_defaults: dict[str, Any],
    touched_float_names: list[str],
    touched_typed_names: list[str],
) -> dict[str, Any]:
    manifest = copy.deepcopy(updated_manifest_defaults)
    manifest_id = spec["new_id"].strip()

    manifest["id"] = manifest_id
    manifest["status"] = "staging"
    manifest["label"] = spec["label"].strip()
    manifest["description"] = spec["description"].strip()
    manifest["sequence_file"] = sequence_relative_path
    manifest["execution_route"] = "experiment_gui_standard_v1"
    manifest["legacy_recipe"] = ""
    manifest.pop("sample_id", None)
    sample_id = str(spec.get("sample_id", "") or "").strip()
    if sample_id:
        manifest["sample_id"] = sample_id
    manifest["allowed_modes"] = ["validate", "dry_run"]
    manifest["catalog_key"] = slug(str(spec.get("catalog_key", manifest_id)))
    manifest["aliases"] = list(spec.get("aliases", []))
    if "scan_defaults" in spec:
        manifest["scan_defaults"] = copy.deepcopy(spec["scan_defaults"])

    requires = copy.deepcopy(manifest.get("requires", {}))
    requires["supervised_until_promoted"] = True
    manifest["requires"] = requires

    notes = list(spec.get("notes", []))
    notes.append(f"Generated from base manifest {spec['base_manifest_id']}.")
    if touched_float_names:
        notes.append("Float defaults overridden: " + ", ".join(sorted(set(touched_float_names))))
    extra_typed = sorted(set(touched_typed_names) - set(touched_float_names))
    if extra_typed:
        notes.append("Typed-only defaults overridden: " + ", ".join(extra_typed))

    manifest["generated_by"] = "openclaw/workspace/design_nv_sequence.py"
    manifest["generated_at"] = datetime.now(timezone.utc).isoformat()
    manifest["generated_from"] = {
        "base_manifest_id": spec["base_manifest_id"],
        "base_sequence_file": base_manifest.get("sequence_file", ""),
        "proposal_type": "manual_xml_text" if isinstance(spec.get("xml_text"), str) and spec.get("xml_text", "").strip() else "template_clone_with_default_overrides",
    }
    manifest["notes"] = notes

    manifest_overrides = spec.get("manifest_overrides")
    if isinstance(manifest_overrides, dict) and manifest_overrides:
        manifest = deep_merge_dicts(manifest, manifest_overrides)
        manifest["id"] = manifest_id
        manifest["sequence_file"] = sequence_relative_path
        manifest["generated_by"] = "openclaw/workspace/design_nv_sequence.py"
        manifest["generated_at"] = datetime.now(timezone.utc).isoformat()
        manifest["generated_from"] = {
            "base_manifest_id": spec["base_manifest_id"],
            "base_sequence_file": base_manifest.get("sequence_file", ""),
            "proposal_type": "manual_xml_text" if isinstance(spec.get("xml_text"), str) and spec.get("xml_text", "").strip() else "template_clone_with_default_overrides",
        }
        merged_notes = manifest.get("notes", [])
        if not isinstance(merged_notes, list):
            merged_notes = []
        for note in notes:
            if note not in merged_notes:
                merged_notes.append(note)
        manifest["notes"] = merged_notes

    return manifest


def build_default_sequence_filename(spec: dict[str, Any]) -> str:
    stem = slug(spec["new_id"])
    return f"{stem}.xml"


def materialize_sequence_spec(
    spec: dict[str, Any],
    *,
    repo_root: Path,
    manifest_root: Path,
    staging_sequence_dir: Path,
    staging_manifest_dir: Path,
    dry_run: bool = False,
) -> dict[str, Any]:
    base_manifest_id = str(spec["base_manifest_id"]).strip()
    base_manifest, base_manifest_path, _ = load_manifest(manifest_root, base_manifest_id)
    validate_spec(spec, base_manifest)

    xml_text_override = spec.get("xml_text")
    xml_text = ""
    base_sequence_path = Path()
    if isinstance(xml_text_override, str) and xml_text_override.strip():
        xml_text = xml_text_override
        base_sequence_path = resolve_repo_path(repo_root, str(base_manifest.get("sequence_file", "")))
    else:
        base_sequence_path = resolve_repo_path(repo_root, str(base_manifest.get("sequence_file", "")))
        if not base_sequence_path.is_file():
            raise ValueError(f"Base sequence file not found: {base_sequence_path}")
        xml_text = base_sequence_path.read_text(encoding="utf-8")

    overrides = spec.get("default_overrides", {})
    updated_manifest_defaults, float_touched, typed_touched = update_manifest_defaults(base_manifest, overrides)
    xml_default_map = build_xml_default_map(updated_manifest_defaults)

    if isinstance(xml_text_override, str) and xml_text_override.strip():
        updated_xml = xml_text
        xml_touched = list(overrides.keys())
        typed_touched_from_xml: list[str] = []
        missing_in_xml: list[str] = []
    else:
        updated_xml, xml_touched, typed_touched_from_xml = replace_variable_defaults(xml_text, xml_default_map)
        missing_in_xml = sorted(set(overrides) - set(xml_touched))
        if missing_in_xml:
            raise ValueError(
                "Some override keys were not rewritten into the XML variables block: " + ", ".join(missing_in_xml)
            )

    sequence_file_name = spec.get("sequence_filename", "") or build_default_sequence_filename(spec)
    sequence_output_path = staging_sequence_dir / sequence_file_name
    sequence_relative_path = relative_to_repo(repo_root, sequence_output_path)

    staging_manifest = build_staging_manifest(
        spec=spec,
        base_manifest=base_manifest,
        sequence_relative_path=sequence_relative_path,
        updated_manifest_defaults=updated_manifest_defaults,
        touched_float_names=float_touched,
        touched_typed_names=sorted(set(typed_touched) | set(typed_touched_from_xml)),
    )
    manifest_output_path = staging_manifest_dir / f"{spec['new_id'].strip()}.json"

    response = {
        "ok": True,
        "dry_run": bool(dry_run),
        "base_manifest_id": base_manifest_id,
        "base_manifest_path": str(base_manifest_path),
        "base_sequence_path": str(base_sequence_path),
        "sequence_output_path": str(sequence_output_path),
        "manifest_output_path": str(manifest_output_path),
        "touched_float_vars": float_touched,
        "touched_typed_vars": sorted(set(typed_touched) | set(typed_touched_from_xml)),
        "staging_manifest": staging_manifest,
        "xml_source": "inline_xml_text" if isinstance(xml_text_override, str) and xml_text_override.strip() else "base_sequence_clone",
    }

    if not dry_run:
        staging_sequence_dir.mkdir(parents=True, exist_ok=True)
        staging_manifest_dir.mkdir(parents=True, exist_ok=True)
        write_text_atomic(sequence_output_path, updated_xml)
        write_json_atomic(manifest_output_path, staging_manifest)

    return response


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a staging NV XML + manifest proposal from a validated template.")
    parser.add_argument("--spec", default="", help="Path to a JSON spec file describing the new sequence proposal.")
    parser.add_argument("--list-base-manifests", action="store_true", help="List validated manifests that can be used as templates.")
    parser.add_argument("--repo-root", default=os.environ.get("NV_SEQUENCE_REPO_ROOT", "") or str(DEFAULT_REPO_ROOT))
    parser.add_argument(
        "--manifest-root",
        default=os.environ.get("NV_SEQUENCE_MANIFEST_ROOT", "") or str(DEFAULT_MANIFEST_ROOT),
    )
    parser.add_argument(
        "--staging-sequence-dir",
        default=os.environ.get("NV_SEQUENCE_STAGING_SEQUENCE_DIR", "") or str(DEFAULT_STAGING_SEQUENCE_DIR),
    )
    parser.add_argument(
        "--staging-manifest-dir",
        default=os.environ.get("NV_SEQUENCE_STAGING_MANIFEST_DIR", "") or str(DEFAULT_STAGING_MANIFEST_DIR),
    )
    parser.add_argument("--dry-run", action="store_true", help="Validate and render outputs without writing files.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    repo_root = normalize_path(args.repo_root, DEFAULT_REPO_ROOT)
    manifest_root = normalize_path(args.manifest_root, DEFAULT_MANIFEST_ROOT)
    staging_sequence_dir = normalize_path(args.staging_sequence_dir, DEFAULT_STAGING_SEQUENCE_DIR)
    staging_manifest_dir = normalize_path(args.staging_manifest_dir, DEFAULT_STAGING_MANIFEST_DIR)

    if args.list_base_manifests:
        print(json.dumps({"base_manifests": list_validated_manifests(manifest_root)}, ensure_ascii=False, indent=2))
        return 0

    if not args.spec:
        parser.error("--spec is required unless --list-base-manifests is used")

    spec_path = normalize_path(args.spec, Path(args.spec))
    spec = load_spec(spec_path)

    response = materialize_sequence_spec(
        spec,
        repo_root=repo_root,
        manifest_root=manifest_root,
        staging_sequence_dir=staging_sequence_dir,
        staging_manifest_dir=staging_manifest_dir,
        dry_run=bool(args.dry_run),
    )
    response["spec_path"] = str(spec_path)

    print(json.dumps(response, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
