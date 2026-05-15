#!/usr/bin/env python3
"""Shared project/item schema helpers for OpenClaw agent-driven planning."""

from __future__ import annotations

import copy
from typing import Any, Callable


VALID_OPTIONAL_MODES = {"", "validate", "dry_run", "execute"}
VALID_BATCH_MODES = {"validate", "dry_run", "execute"}

PLAN_ITEM_STRING_KEYS = {
    "id",
    "job_id",
    "sequence",
    "sequence_manifest_id",
    "recipe",
    "job_id_prefix",
    "job_id_suffix",
    "requested_by",
    "submission_path",
    "intent",
    "reference_data",
}
PLAN_ITEM_DICT_KEYS = {"scan", "float_vars", "bool_vars", "limits", "acquisition", "analysis", "metadata"}
PLAN_ITEM_BOOL_KEYS = {"allow_seed_fallback", "measurement_plan_verified"}
PLAN_ITEM_LIST_KEYS = {"nv_position"}
PLAN_ITEM_INT_KEYS = {"max_attempts"}
PLAN_ITEM_SPECIAL_DICT_KEYS = {"sequence_authoring", "project_branches"}

PLAN_ITEM_OVERRIDE_ALLOWED_KEYS = {
    "sequence",
    "sequence_manifest_id",
    "job_id",
    "recipe",
    "job_id_prefix",
    "job_id_suffix",
    "requested_by",
    "submission_path",
    "intent",
    "reference_data",
    "scan",
    "float_vars",
    "bool_vars",
    "limits",
    "acquisition",
    "analysis",
    "metadata",
    "allow_seed_fallback",
    "measurement_plan_verified",
    "max_attempts",
    "mode",
    "sample_id",
    "sequence_authoring",
    "project_branches",
}
RUNTIME_ITEM_OVERRIDE_ALLOWED_KEYS = {
    "scan",
    "float_vars",
    "bool_vars",
    "limits",
    "acquisition",
    "analysis",
    "metadata",
    "allow_seed_fallback",
    "sequence_authoring",
    "project_branches",
}

PROJECT_BRANCH_KEYS = ("after_accept", "after_continue", "before_rerun", "before_retry")
PROJECT_BRANCH_RULE_EVENTS = ("analysis", "recovery")
PROJECT_BRANCH_RULE_WHEN_LIST_KEYS = {
    "action_in",
    "action_not_in",
    "error_code_in",
    "aux_key_in",
    "fit_kind_in",
}
PROJECT_BRANCH_RULE_WHEN_BOOL_KEYS = {"aux_applied"}
PROJECT_BRANCH_LEGACY_RULES = {
    "after_accept": {"event": "analysis", "action_in": ["accept"]},
    "after_continue": {"event": "analysis", "action_in": ["continue"]},
    "before_rerun": {"event": "analysis", "action_in": ["rerun_item"]},
    "before_retry": {"event": "recovery", "action_in": ["retry"]},
}

SEQUENCE_AUTHORING_STRING_KEYS = {
    "new_id",
    "label",
    "description",
    "base_manifest_id",
    "sample_id",
    "sequence_filename",
    "catalog_key",
    "xml_text",
}
SEQUENCE_AUTHORING_DICT_KEYS = {"default_overrides", "scan_defaults", "manifest_overrides"}
SEQUENCE_AUTHORING_LIST_KEYS = {"aliases", "notes"}

SUPPORTED_PLAN_ITEM_KEYS = sorted(
    PLAN_ITEM_STRING_KEYS
    | PLAN_ITEM_DICT_KEYS
    | PLAN_ITEM_BOOL_KEYS
    | PLAN_ITEM_LIST_KEYS
    | PLAN_ITEM_INT_KEYS
    | PLAN_ITEM_SPECIAL_DICT_KEYS
    | {"mode", "sample_id"}
)


def normalize_optional_mode(value: Any) -> str:
    mode = str(value or "").strip().lower()
    return mode if mode in VALID_OPTIONAL_MODES else ""


def normalize_batch_mode(value: Any, default_mode: str) -> str:
    mode = str(value or "").strip().lower()
    if mode in VALID_BATCH_MODES:
        return mode
    fallback = str(default_mode or "").strip().lower()
    return fallback if fallback in VALID_BATCH_MODES else "execute"


def normalize_sequence_authoring_spec(raw_payload: Any, default_sample_id: str) -> dict[str, Any]:
    if not isinstance(raw_payload, dict):
        return {}

    normalized: dict[str, Any] = {}
    for key in SEQUENCE_AUTHORING_STRING_KEYS:
        value = raw_payload.get(key)
        if key == "sample_id":
            text = str(value or "").strip().upper()
        else:
            text = str(value or "").strip()
        if text:
            normalized[key] = text

    for key in SEQUENCE_AUTHORING_DICT_KEYS:
        value = raw_payload.get(key)
        if isinstance(value, dict) and value:
            normalized[key] = copy.deepcopy(value)

    for key in SEQUENCE_AUTHORING_LIST_KEYS:
        value = raw_payload.get(key)
        if isinstance(value, (list, tuple)) and value:
            normalized[key] = copy.deepcopy(list(value))

    required = ("new_id", "label", "description", "base_manifest_id")
    if any(not str(normalized.get(field, "") or "").strip() for field in required):
        return {}
    return normalized


def item_identity_hint(item_spec: dict[str, Any]) -> str:
    return str(
        item_spec.get("id", "")
        or item_spec.get("sequence_manifest_id", "")
        or item_spec.get("sequence", "")
        or ((item_spec.get("sequence_authoring") or {}) if isinstance(item_spec.get("sequence_authoring"), dict) else {}).get("new_id", "")
        or "item"
    )


def _normalize_text_list(value: Any) -> list[str]:
    if not isinstance(value, (list, tuple, set)):
        return []
    normalized: list[str] = []
    for entry in value:
        text = str(entry or "").strip()
        if text:
            normalized.append(text)
    return normalized


def _normalize_project_branch_rule_when(raw_when: Any) -> dict[str, Any]:
    if not isinstance(raw_when, dict):
        return {}
    normalized: dict[str, Any] = {}
    for key in PROJECT_BRANCH_RULE_WHEN_LIST_KEYS:
        values = _normalize_text_list(raw_when.get(key))
        if values:
            normalized[key] = values
    for key in PROJECT_BRANCH_RULE_WHEN_BOOL_KEYS:
        value = raw_when.get(key)
        if isinstance(value, bool):
            normalized[key] = value
    return normalized


def _normalize_project_branch_rule(
    raw_rule: Any,
    *,
    default_mode: str,
    default_sample_id: str,
    normalize_analysis: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
    use_default_mode: bool = False,
    max_branch_items: int = 12,
) -> dict[str, Any]:
    if not isinstance(raw_rule, dict):
        return {}

    event = str(raw_rule.get("event", "") or "").strip().lower()
    if event not in PROJECT_BRANCH_RULE_EVENTS:
        return {}

    raw_items = raw_rule.get("items", raw_rule.get("insert_items", []))
    if not isinstance(raw_items, list):
        return {}

    items: list[dict[str, Any]] = []
    for raw_item in raw_items[:max_branch_items]:
        item = normalize_item_spec(
            raw_item,
            require_sequence=True,
            default_mode=default_mode,
            default_sample_id=default_sample_id,
            allow_id=True,
            normalize_analysis=normalize_analysis,
            use_default_mode=use_default_mode,
            max_branch_items=max_branch_items,
        )
        if item:
            items.append(item)
    if not items:
        return {}

    normalized: dict[str, Any] = {
        "event": event,
        "items": items,
    }
    rule_id = str(raw_rule.get("id", "") or "").strip()
    if rule_id:
        normalized["id"] = rule_id
    when = _normalize_project_branch_rule_when(raw_rule.get("when", {}))
    if when:
        normalized["when"] = when
    return normalized


def normalize_project_branches(
    raw_branches: Any,
    *,
    default_mode: str,
    default_sample_id: str,
    normalize_analysis: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
    use_default_mode: bool = False,
    max_branch_items: int = 12,
) -> dict[str, Any]:
    if not isinstance(raw_branches, dict):
        return {}

    normalized_rules: list[dict[str, Any]] = []
    for branch_key in PROJECT_BRANCH_KEYS:
        raw_items = raw_branches.get(branch_key)
        if not isinstance(raw_items, list):
            continue
        legacy_rule = {
            "event": PROJECT_BRANCH_LEGACY_RULES[branch_key]["event"],
            "when": {"action_in": copy.deepcopy(PROJECT_BRANCH_LEGACY_RULES[branch_key]["action_in"])},
            "items": raw_items,
        }
        rule = _normalize_project_branch_rule(
            legacy_rule,
            default_mode=default_mode,
            default_sample_id=default_sample_id,
            normalize_analysis=normalize_analysis,
            use_default_mode=use_default_mode,
            max_branch_items=max_branch_items,
        )
        if rule:
            normalized_rules.append(rule)

    raw_rules = raw_branches.get("rules", [])
    if isinstance(raw_rules, list):
        for raw_rule in raw_rules:
            rule = _normalize_project_branch_rule(
                raw_rule,
                default_mode=default_mode,
                default_sample_id=default_sample_id,
                normalize_analysis=normalize_analysis,
                use_default_mode=use_default_mode,
                max_branch_items=max_branch_items,
            )
            if rule:
                normalized_rules.append(rule)

    if normalized_rules:
        return {"rules": normalized_rules}
    return {}


def normalize_item_spec(
    raw_item: Any,
    *,
    require_sequence: bool,
    default_mode: str,
    default_sample_id: str,
    allow_id: bool,
    normalize_analysis: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
    use_default_mode: bool = False,
    allowed_keys: set[str] | None = None,
    max_branch_items: int = 12,
) -> dict[str, Any]:
    if not isinstance(raw_item, dict):
        return {}

    selected_keys = allowed_keys if isinstance(allowed_keys, set) else (
        PLAN_ITEM_STRING_KEYS | PLAN_ITEM_DICT_KEYS | PLAN_ITEM_BOOL_KEYS | PLAN_ITEM_LIST_KEYS | PLAN_ITEM_INT_KEYS | PLAN_ITEM_SPECIAL_DICT_KEYS | {"mode", "sample_id"}
    )
    normalized: dict[str, Any] = {}

    if allow_id and "id" in selected_keys:
        item_id = str(raw_item.get("id", "") or "").strip()
        if item_id:
            normalized["id"] = item_id

    if "mode" in selected_keys:
        mode = normalize_batch_mode(raw_item.get("mode", ""), default_mode) if use_default_mode else normalize_optional_mode(raw_item.get("mode", ""))
        if mode:
            normalized["mode"] = mode

    effective_mode = str(normalized.get("mode", "") or (normalize_batch_mode("", default_mode) if use_default_mode else "")).strip().lower()

    if "sample_id" in selected_keys:
        sample_id = str(raw_item.get("sample_id", "") or default_sample_id or "").strip().upper()
        if sample_id:
            normalized["sample_id"] = sample_id

    for key in PLAN_ITEM_STRING_KEYS:
        if key not in selected_keys:
            continue
        value = str(raw_item.get(key, "") or "").strip()
        if value:
            normalized[key] = value

    for key in PLAN_ITEM_DICT_KEYS:
        if key not in selected_keys:
            continue
        value = raw_item.get(key)
        if not isinstance(value, dict) or not value:
            continue
        if key == "analysis" and normalize_analysis is not None:
            if effective_mode not in {"validate", "dry_run"}:
                normalized_analysis = normalize_analysis(value)
                if normalized_analysis:
                    normalized[key] = normalized_analysis
            continue
        normalized[key] = copy.deepcopy(value)

    for key in PLAN_ITEM_BOOL_KEYS:
        if key not in selected_keys:
            continue
        value = raw_item.get(key)
        if isinstance(value, bool):
            normalized[key] = value

    for key in PLAN_ITEM_LIST_KEYS:
        if key not in selected_keys:
            continue
        value = raw_item.get(key)
        if isinstance(value, (list, tuple)) and value:
            normalized[key] = copy.deepcopy(list(value))

    for key in PLAN_ITEM_INT_KEYS:
        if key not in selected_keys:
            continue
        value = raw_item.get(key)
        if value is None:
            continue
        try:
            normalized[key] = int(value)
        except (TypeError, ValueError):
            continue

    if "sequence_authoring" in selected_keys:
        authoring = normalize_sequence_authoring_spec(raw_item.get("sequence_authoring"), normalized.get("sample_id", default_sample_id))
        if authoring:
            normalized["sequence_authoring"] = authoring

    if "project_branches" in selected_keys:
        branches = normalize_project_branches(
            raw_item.get("project_branches"),
            default_mode=effective_mode or default_mode,
            default_sample_id=normalized.get("sample_id", default_sample_id),
            normalize_analysis=normalize_analysis,
            use_default_mode=use_default_mode,
            max_branch_items=max_branch_items,
        )
        if branches:
            normalized["project_branches"] = branches

    if require_sequence and not (
        normalized.get("sequence_manifest_id")
        or normalized.get("sequence")
        or normalized.get("sequence_authoring")
    ):
        return {}

    if allow_id and require_sequence and not normalized.get("id"):
        normalized["id"] = item_identity_hint(normalized)
    return normalized


def normalize_override_spec(
    raw_overrides: Any,
    *,
    default_mode: str,
    default_sample_id: str,
    allowed_keys: set[str],
    normalize_analysis: Callable[[dict[str, Any]], dict[str, Any]] | None = None,
    use_default_mode: bool = False,
    max_branch_items: int = 12,
) -> dict[str, Any]:
    return normalize_item_spec(
        raw_overrides,
        require_sequence=False,
        default_mode=default_mode,
        default_sample_id=default_sample_id,
        allow_id=False,
        normalize_analysis=normalize_analysis,
        use_default_mode=use_default_mode,
        allowed_keys=allowed_keys,
        max_branch_items=max_branch_items,
    )


def summarize_sequence_authoring(item_spec: dict[str, Any]) -> dict[str, Any]:
    authoring = item_spec.get("sequence_authoring", {}) if isinstance(item_spec, dict) else {}
    if not isinstance(authoring, dict) or not authoring:
        return {}
    return {
        "new_id": str(authoring.get("new_id", "") or ""),
        "base_manifest_id": str(authoring.get("base_manifest_id", "") or ""),
        "label": str(authoring.get("label", "") or ""),
        "description": str(authoring.get("description", "") or ""),
        "sample_id": str(authoring.get("sample_id", "") or ""),
        "sequence_filename": str(authoring.get("sequence_filename", "") or ""),
        "catalog_key": str(authoring.get("catalog_key", "") or ""),
        "default_override_keys": sorted((authoring.get("default_overrides") or {}).keys()) if isinstance(authoring.get("default_overrides"), dict) else [],
        "manifest_override_keys": sorted((authoring.get("manifest_overrides") or {}).keys()) if isinstance(authoring.get("manifest_overrides"), dict) else [],
        "has_xml_text": bool(str(authoring.get("xml_text", "") or "").strip()),
    }


def summarize_project_branches(item_spec: dict[str, Any]) -> dict[str, Any]:
    branches = item_spec.get("project_branches", {}) if isinstance(item_spec, dict) else {}
    if not isinstance(branches, dict) or not branches:
        return {}

    rules = branches.get("rules", [])
    if isinstance(rules, list) and rules:
        summarized_rules: list[dict[str, Any]] = []
        for rule in rules:
            if not isinstance(rule, dict):
                continue
            rule_items = rule.get("items", [])
            if not isinstance(rule_items, list) or not rule_items:
                continue
            summarized_rules.append(
                {
                    "id": str(rule.get("id", "") or ""),
                    "event": str(rule.get("event", "") or ""),
                    "when": copy.deepcopy(rule.get("when", {})) if isinstance(rule.get("when"), dict) else {},
                    "items": [
                        {
                            "id": str(item.get("id", "") or ""),
                            "sequence_manifest_id": str(item.get("sequence_manifest_id", "") or ""),
                            "sequence": str(item.get("sequence", "") or ""),
                            "sequence_authoring_new_id": str(((item.get("sequence_authoring") or {}) if isinstance(item.get("sequence_authoring"), dict) else {}).get("new_id", "") or ""),
                        }
                        for item in rule_items
                        if isinstance(item, dict)
                    ],
                }
            )
        if summarized_rules:
            return {"rules": summarized_rules}

    summary: dict[str, Any] = {}
    for branch_key in PROJECT_BRANCH_KEYS:
        raw_items = branches.get(branch_key)
        if not isinstance(raw_items, list) or not raw_items:
            continue
        summary[branch_key] = [
            {
                "id": str(item.get("id", "") or ""),
                "sequence_manifest_id": str(item.get("sequence_manifest_id", "") or ""),
                "sequence": str(item.get("sequence", "") or ""),
                "sequence_authoring_new_id": str(((item.get("sequence_authoring") or {}) if isinstance(item.get("sequence_authoring"), dict) else {}).get("new_id", "") or ""),
            }
            for item in raw_items
            if isinstance(item, dict)
        ]
    return summary


def select_project_branch_items(
    item_spec: dict[str, Any],
    *,
    event: str,
    action: str = "",
    error_code: str = "",
    aux_key: str = "",
    aux_applied: bool | None = None,
    fit_kind: str = "",
) -> list[dict[str, Any]]:
    branches = item_spec.get("project_branches", {}) if isinstance(item_spec, dict) else {}
    if not isinstance(branches, dict) or not branches:
        return []

    normalized_event = str(event or "").strip().lower()
    normalized_action = str(action or "").strip().lower()
    normalized_error_code = str(error_code or "").strip()
    normalized_aux_key = str(aux_key or "").strip()
    normalized_fit_kind = str(fit_kind or "").strip()
    selected: list[dict[str, Any]] = []

    for branch_key, legacy_rule in PROJECT_BRANCH_LEGACY_RULES.items():
        raw_items = branches.get(branch_key)
        if not isinstance(raw_items, list) or not raw_items:
            continue
        if legacy_rule["event"] != normalized_event:
            continue
        allowed_actions = {str(value).strip().lower() for value in legacy_rule.get("action_in", [])}
        if allowed_actions and normalized_action not in allowed_actions:
            continue
        selected.extend(copy.deepcopy(item) for item in raw_items if isinstance(item, dict))

    raw_rules = branches.get("rules", [])
    if not isinstance(raw_rules, list):
        return selected

    for rule in raw_rules:
        if not isinstance(rule, dict):
            continue
        if str(rule.get("event", "") or "").strip().lower() != normalized_event:
            continue

        when = rule.get("when", {})
        if not isinstance(when, dict):
            when = {}

        action_in = {str(value).strip().lower() for value in when.get("action_in", []) if str(value).strip()}
        if action_in and normalized_action not in action_in:
            continue
        action_not_in = {str(value).strip().lower() for value in when.get("action_not_in", []) if str(value).strip()}
        if action_not_in and normalized_action in action_not_in:
            continue

        error_code_in = {str(value).strip() for value in when.get("error_code_in", []) if str(value).strip()}
        if error_code_in and normalized_error_code not in error_code_in:
            continue

        aux_key_in = {str(value).strip() for value in when.get("aux_key_in", []) if str(value).strip()}
        if aux_key_in and normalized_aux_key not in aux_key_in:
            continue

        fit_kind_in = {str(value).strip() for value in when.get("fit_kind_in", []) if str(value).strip()}
        if fit_kind_in and normalized_fit_kind not in fit_kind_in:
            continue

        if "aux_applied" in when and isinstance(when.get("aux_applied"), bool):
            if aux_applied is None or bool(aux_applied) != bool(when.get("aux_applied")):
                continue

        rule_items = rule.get("items", [])
        if isinstance(rule_items, list):
            selected.extend(copy.deepcopy(item) for item in rule_items if isinstance(item, dict))

    return selected
