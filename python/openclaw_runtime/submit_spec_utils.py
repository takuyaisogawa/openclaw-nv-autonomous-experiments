#!/usr/bin/env python3
"""Shared helpers for the Python-facing submit-spec contract."""

from __future__ import annotations

import copy
from typing import Any


SUBMIT_SPEC_STRING_KEYS = (
    "job_id",
    "job_id_prefix",
    "job_id_suffix",
    "mode",
    "recipe",
    "sample_id",
    "sequence",
    "sequence_manifest_id",
    "simulation_manifest_id",
    "requested_by",
    "submission_path",
    "intent",
    "reference_data",
)
SUBMIT_SPEC_DICT_KEYS = ("scan", "float_vars", "bool_vars", "limits", "metadata", "acquisition", "simulation")
BATCH_ITEM_DICT_KEYS = SUBMIT_SPEC_DICT_KEYS + ("analysis",)
SUBMIT_SPEC_LIST_KEYS = ("nv_position",)
SUBMIT_SPEC_BOOL_KEYS = ("allow_seed_fallback", "measurement_plan_verified")


def merge_dicts(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = merge_dicts(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def _text(value: Any) -> str:
    return str(value or "").strip()


def _copy_dict(value: Any) -> dict[str, Any]:
    return copy.deepcopy(value) if isinstance(value, dict) and value else {}


def _copy_list(value: Any) -> list[Any]:
    return copy.deepcopy(list(value)) if isinstance(value, (list, tuple)) and value else []


def build_submit_spec_from_batch_item(
    item: dict[str, Any],
    batch_spec: dict[str, Any] | None = None,
    *,
    submission_path: str = "",
    measurement_plan_verified: bool | None = None,
) -> dict[str, Any]:
    item = item if isinstance(item, dict) else {}
    batch_spec = batch_spec if isinstance(batch_spec, dict) else {}

    spec: dict[str, Any] = {}
    item_id = _text(item.get("id", ""))

    for key in ("job_id", "job_id_prefix", "job_id_suffix"):
        value = _text(item.get(key, ""))
        if value:
            spec[key] = value

    mode = _text(item.get("mode", "") or batch_spec.get("mode", "") or "execute")
    if mode:
        spec["mode"] = mode

    recipe = _text(item.get("recipe", "") or "xml_generic_v1")
    if recipe:
        spec["recipe"] = recipe

    sample_id = _text(item.get("sample_id", "") or batch_spec.get("requested_sample_id", ""))
    if sample_id:
        spec["sample_id"] = sample_id

    simulation_manifest_id = _text(item.get("simulation_manifest_id", ""))
    sequence_manifest_id = _text(item.get("sequence_manifest_id", ""))
    sequence = _text(item.get("sequence", ""))
    if simulation_manifest_id:
        spec["simulation_manifest_id"] = simulation_manifest_id
    if sequence_manifest_id:
        spec["sequence_manifest_id"] = sequence_manifest_id
    elif sequence:
        spec["sequence"] = sequence

    requested_by = _text(item.get("requested_by", "") or batch_spec.get("requested_by", ""))
    if requested_by:
        spec["requested_by"] = requested_by

    resolved_submission_path = _text(submission_path or item.get("submission_path", ""))
    if resolved_submission_path:
        spec["submission_path"] = resolved_submission_path

    for key in SUBMIT_SPEC_DICT_KEYS:
        value = _copy_dict(item.get(key))
        if value:
            spec[key] = value

    metadata = _copy_dict(spec.get("metadata"))

    intent = _text(item.get("intent", "") or metadata.get("intent", ""))
    if intent:
        spec["intent"] = intent

    reference_data = _text(item.get("reference_data", "") or metadata.get("reference_data", ""))
    if reference_data:
        spec["reference_data"] = reference_data

    nv_position = _copy_list(item.get("nv_position"))
    if not nv_position:
        nv_position = _copy_list(metadata.get("nv_position"))
    if nv_position:
        spec["nv_position"] = nv_position

    allow_seed_fallback = item.get("allow_seed_fallback")
    if not isinstance(allow_seed_fallback, bool):
        allow_seed_fallback = metadata.get("allow_seed_fallback")
    if isinstance(allow_seed_fallback, bool):
        spec["allow_seed_fallback"] = allow_seed_fallback

    if measurement_plan_verified is not None:
        spec["measurement_plan_verified"] = bool(measurement_plan_verified)
    elif isinstance(item.get("measurement_plan_verified"), bool):
        spec["measurement_plan_verified"] = bool(item.get("measurement_plan_verified"))

    if "job_id" not in spec and "job_id_suffix" not in spec and item_id:
        spec["job_id_suffix"] = item_id

    return spec


def build_batch_item_from_submit_spec(
    submit_spec: dict[str, Any],
    *,
    item_id: str = "",
    job_id_prefix: str = "",
    job_id_suffix: str = "",
    include_job_id: bool = False,
    extra_fields: dict[str, Any] | None = None,
) -> dict[str, Any]:
    submit_spec = submit_spec if isinstance(submit_spec, dict) else {}
    item: dict[str, Any] = {}

    resolved_item_id = _text(item_id or submit_spec.get("id", "") or submit_spec.get("job_id_suffix", "") or submit_spec.get("sequence_manifest_id", "") or submit_spec.get("sequence", "") or "item")
    item["id"] = resolved_item_id

    copy_keys = (
        "mode",
        "recipe",
        "sample_id",
        "sequence",
        "sequence_manifest_id",
        "simulation_manifest_id",
        "requested_by",
        "submission_path",
        "intent",
        "reference_data",
        "measurement_plan_verified",
        "allow_seed_fallback",
    )
    for key in copy_keys:
        value = submit_spec.get(key)
        if isinstance(value, bool):
            item[key] = value
        else:
            text = _text(value)
            if text:
                item[key] = text

    for key in BATCH_ITEM_DICT_KEYS:
        value = _copy_dict(submit_spec.get(key))
        if value:
            item[key] = value

    nv_position = _copy_list(submit_spec.get("nv_position"))
    if nv_position:
        item["nv_position"] = nv_position

    resolved_prefix = _text(job_id_prefix or submit_spec.get("job_id_prefix", ""))
    if resolved_prefix:
        item["job_id_prefix"] = resolved_prefix

    resolved_suffix = _text(job_id_suffix or submit_spec.get("job_id_suffix", ""))
    if resolved_suffix:
        item["job_id_suffix"] = resolved_suffix

    if include_job_id:
        job_id = _text(submit_spec.get("job_id", ""))
        if job_id:
            item["job_id"] = job_id

    if isinstance(extra_fields, dict) and extra_fields:
        item = merge_dicts(item, extra_fields)
    return item
