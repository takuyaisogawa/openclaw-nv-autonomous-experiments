import argparse
import hashlib
import json
import math
import os
import struct
import subprocess
import sys
import zlib
from pathlib import Path
from typing import Any

miINT8=1; miUINT8=2; miINT16=3; miUINT16=4; miINT32=5; miUINT32=6; miSINGLE=7; miDOUBLE=9; miINT64=12; miUINT64=13; miMATRIX=14; miCOMPRESSED=15; miUTF8=16; miUTF16=17; miUTF32=18
mxCELL_CLASS=1; mxSTRUCT_CLASS=2; mxOBJECT_CLASS=3; mxCHAR_CLASS=4; mxSPARSE_CLASS=5; mxDOUBLE_CLASS=6; mxSINGLE_CLASS=7; mxINT8_CLASS=8; mxUINT8_CLASS=9; mxINT16_CLASS=10; mxUINT16_CLASS=11; mxINT32_CLASS=12; mxUINT32_CLASS=13; mxINT64_CLASS=14; mxUINT64_CLASS=15

NUMERIC_DTYPES = {
    miDOUBLE: ('<d', 8), miSINGLE: ('<f', 4), miINT8: ('<b', 1), miUINT8: ('<B', 1),
    miINT16: ('<h', 2), miUINT16: ('<H', 2), miINT32: ('<i', 4), miUINT32: ('<I', 4),
    miINT64: ('<q', 8), miUINT64: ('<Q', 8)
}

class Reader:
    def __init__(self, data):
        self.data=data
        self.pos=0
    def read(self,n):
        out=self.data[self.pos:self.pos+n]
        self.pos+=n
        return out
    def align8(self):
        if self.pos%8:
            self.pos += 8-(self.pos%8)


def read_tag(r):
    raw=r.read(4)
    if len(raw)<4: return None
    a,b=struct.unpack('<HH', raw)
    if b!=0:
        # small data element format
        dt=a; n=b
        payload=r.read(4)
        return dt,n,payload[:n],True
    else:
        dt=a
        n=struct.unpack('<I', r.read(4))[0]
        payload=r.read(n)
        pad=(8-(n%8))%8
        if pad: r.read(pad)
        return dt,n,payload,False


def parse_numeric(dt, payload):
    fmt,size=NUMERIC_DTYPES[dt]
    if len(payload)%size: payload=payload[:len(payload)//size*size]
    vals=[x[0] for x in struct.iter_unpack(fmt, payload)]
    return vals


def reshape_col_major(vals, dims):
    total=1
    for d in dims: total*=max(1,d)
    vals=vals[:total]
    if len(dims)==2:
        m,n=dims
        out=[[None]*n for _ in range(m)]
        k=0
        for j in range(n):
            for i in range(m):
                out[i][j]=vals[k]; k+=1
        return out
    return vals


def parse_matrix(payload):
    r=Reader(payload)
    tag=read_tag(r)  # flags
    dt,n,pl,_=tag
    flags=parse_numeric(miUINT32, pl)
    class_type=flags[0] & 0xFF if flags else None
    tag=read_tag(r)  # dims
    dims=parse_numeric(dt, pl:=tag[2])
    dims=[int(x) for x in dims]
    tag=read_tag(r)  # name
    name_bytes=tag[2]
    try:
        name=name_bytes.decode('utf-8').rstrip('\x00')
    except:
        name=''
    if class_type==mxSTRUCT_CLASS or class_type==mxOBJECT_CLASS:
        # field name length
        tag=read_tag(r)
        field_name_length=parse_numeric(tag[0], tag[2])[0]
        tag=read_tag(r)
        raw=tag[2]
        field_names=[]
        for i in range(0, len(raw), int(field_name_length)):
            s=raw[i:i+int(field_name_length)].split(b'\x00',1)[0].decode('utf-8','ignore')
            if s: field_names.append(s)
        nfields=len(field_names)
        nelems=1
        for d in dims: nelems*=d
        elems=[]
        for _ in range(nelems):
            item={}
            for fname in field_names:
                tag=read_tag(r)
                if tag[0]!=miMATRIX:
                    item[fname]=None
                else:
                    item[fname]=parse_matrix(tag[2])
            elems.append(item)
        value=elems[0] if nelems==1 else elems
        if class_type==mxOBJECT_CLASS and isinstance(value, dict):
            value['__class__']='object'
        return {'name':name,'class':class_type,'dims':dims,'value':value}
    if class_type==mxCELL_CLASS:
        nelems=1
        for d in dims: nelems*=d
        cells=[]
        for _ in range(nelems):
            tag=read_tag(r)
            cells.append(parse_matrix(tag[2]) if tag and tag[0]==miMATRIX else None)
        return {'name':name,'class':class_type,'dims':dims,'value':cells}
    if class_type==mxCHAR_CLASS:
        tag=read_tag(r)
        chars=tag[2]
        try:
            if tag[0] in (miUINT16, miUTF16):
                txt=chars.decode('utf-16le','ignore')
            else:
                txt=chars.decode('utf-8','ignore')
        except:
            txt=''
        return {'name':name,'class':class_type,'dims':dims,'value':txt.rstrip('\x00')}
    # numeric/logical
    real=[]
    imag=[]
    while True:
        tag=read_tag(r)
        if tag is None: break
        dt,n,pl,_=tag
        if dt in NUMERIC_DTYPES:
            if not real: real=parse_numeric(dt, pl)
            else: imag=parse_numeric(dt, pl)
    value=reshape_col_major(real, dims)
    return {'name':name,'class':class_type,'dims':dims,'value':value}


def loadmat_simple(path):
    data=Path(path).read_bytes()
    pos=128
    vars={}
    while pos+8<=len(data):
        dt,n=struct.unpack('<II', data[pos:pos+8]); pos+=8
        payload=data[pos:pos+n]; pos+=n
        if pos%8: pos += 8-(pos%8)
        if dt==miCOMPRESSED:
            payload=zlib.decompress(payload)
            rr=Reader(payload)
            while rr.pos < len(payload):
                tag=read_tag(rr)
                if tag is None: break
                if tag[0]==miMATRIX:
                    obj=parse_matrix(tag[2])
                    vars[obj['name']]=obj['value']
        elif dt==miMATRIX:
            obj=parse_matrix(payload)
            vars[obj['name']]=obj['value']
    return vars


DEFAULT_C23_ROOT = Path(os.environ.get("MATLAB_23C_ROOT", "../matlab")).expanduser()
DEFAULT_CACHE_ROOT = Path(os.environ.get("OPENCLAW_MAT_CACHE_ROOT", ".openclaw/savedexperiment_mat_cache")).expanduser()
DEFAULT_RAW_EXPORT_CACHE_ROOT = Path(
    os.environ.get("OPENCLAW_MAT_RAW_EXPORT_CACHE_ROOT", ".openclaw/savedexperiment_mat_raw_cache")
).expanduser()
DEFAULT_DRIFT_CACHE_ROOT = Path(os.environ.get("OPENCLAW_DRIFT_CACHE_ROOT", ".openclaw/savedexperiment_drift_cache")).expanduser()
DEFAULT_ARTIFACT_ROOT = Path(os.environ.get("OPENCLAW_MAT_ARTIFACT_ROOT", ".openclaw/savedexperiment_mat_artifacts")).expanduser()
DEFAULT_RAW_ARTIFACT_ROOT = Path(
    os.environ.get("OPENCLAW_MAT_RAW_ARTIFACT_ROOT", ".openclaw/savedexperiment_mat_raw_artifacts")
).expanduser()
DEFAULT_MATLAB_EXE_CANDIDATES = tuple(
    Path(item).expanduser()
    for item in os.environ.get("MATLAB_EXE_CANDIDATES", "matlab").split(os.pathsep)
    if item
)
JSON_BEGIN_MARKER = "OPENCLAW_JSON_BEGIN"
JSON_END_MARKER = "OPENCLAW_JSON_END"
DEFAULT_SUMMARY_TIMEOUT_SECONDS = 240.0
LEGACY_SUMMARY_ENV = "OPENCLAW_ALLOW_LEGACY_MAT_SUMMARY"


def env_flag_enabled(name: str) -> bool:
    text = str(os.environ.get(name, "") or "").strip().lower()
    return text in {"1", "true", "yes", "on", "allow", "allowed"}


def normalize_agent_path(path_value: Any) -> str:
    text = str(path_value or "").strip()
    if not text:
        return ""
    unc_host = os.environ.get("WSL_UNC_HOST", "wsl.localhost")
    unc_distro = os.environ.get("WSL_DISTRO_NAME", "<WSL_DISTRO>")
    unc_prefix = "\\\\" + unc_host + "\\" + unc_distro + "\\"
    if text.lower().startswith(unc_prefix.lower()):
        rest = text[len(unc_prefix):].replace("\\", "/").lstrip("/")
        return f"/{rest}"
    if len(text) >= 3 and text[1:3] in (":\\", ":/"):
        drive = text[0].lower()
        rest = text[2:].replace("\\", "/").lstrip("/")
        return f"/mnt/{drive}/{rest}"
    return text


def to_wsl_path(path_value: Any) -> Path:
    return Path(normalize_agent_path(path_value)).expanduser().resolve()


def to_windows_path(path_value: Any) -> str:
    text = str(path_value or "").strip()
    if not text:
        return ""
    if len(text) >= 3 and text[1:3] in (":\\", ":/"):
        drive = text[0].upper()
        rest = text[2:].replace("/", "\\").lstrip("\\")
        return f"{drive}:\\{rest}"
    if text.startswith("/mnt/") and len(text) > 6:
        drive = text[5].upper()
        rest = text[7:].replace("/", "\\")
        return f"{drive}:\\{rest}"
    return text.replace("/", "\\")


def matlab_quote(text: str) -> str:
    return "'" + str(text).replace("'", "''") + "'"


def resolve_matlab_exe(matlab_exe: str | Path | None = None) -> Path:
    candidates = []
    if matlab_exe:
        candidates.append(Path(str(matlab_exe)).expanduser())
    candidates.extend(DEFAULT_MATLAB_EXE_CANDIDATES)
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("MATLAB executable was not found for savedexperiment MAT extraction.")


def extract_json_between_markers(stdout_text: str) -> Any:
    start = stdout_text.find(JSON_BEGIN_MARKER)
    end = stdout_text.rfind(JSON_END_MARKER)
    if start < 0 or end < 0 or end <= start:
        raise ValueError("Savedexperiment MAT extraction command did not emit JSON markers.")
    payload = stdout_text[start + len(JSON_BEGIN_MARKER):end].strip()
    if not payload:
        raise ValueError("Savedexperiment MAT extraction command emitted empty JSON payload.")
    return json.loads(payload)


def cache_key_for_summary(path_value: Any) -> str:
    resolved = to_wsl_path(path_value)
    stat = resolved.stat()
    raw = f"savedexperiment-summary-v3|{resolved}|{stat.st_mtime_ns}|{stat.st_size}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def cache_key_for_raw_export(path_value: Any) -> str:
    resolved = to_wsl_path(path_value)
    stat = resolved.stat()
    raw = f"savedexperiment-raw-export-v1|{resolved}|{stat.st_mtime_ns}|{stat.st_size}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def cache_key_for_average_drift(
    path_value: Any,
    *,
    drop_threshold: float,
    slice_index: int,
    min_averages_for_reference: int,
) -> str:
    resolved = to_wsl_path(path_value)
    stat = resolved.stat()
    raw = (
        "savedexperiment-average-drift-v4-common-mode-scan-order-aware|"
        f"{resolved}|{stat.st_mtime_ns}|{stat.st_size}|"
        f"drop_threshold={float(drop_threshold):.12g}|"
        f"slice_index={int(slice_index)}|"
        f"min_averages_for_reference={int(min_averages_for_reference)}"
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def artifact_key_for_savedexperiment(path_value: Any) -> str:
    resolved = to_wsl_path(path_value)
    stat = resolved.stat()
    raw = f"savedexperiment-artifact-v1|{resolved}|{stat.st_mtime_ns}|{stat.st_size}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def raw_artifact_key_for_savedexperiment(path_value: Any) -> str:
    resolved = to_wsl_path(path_value)
    stat = resolved.stat()
    raw = f"savedexperiment-raw-artifact-v1|{resolved}|{stat.st_mtime_ns}|{stat.st_size}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def artifact_path_for_savedexperiment(path_value: Any, artifact_root: str | Path = DEFAULT_ARTIFACT_ROOT) -> Path:
    artifact_root_path = Path(str(artifact_root)).expanduser()
    return artifact_root_path / f"{artifact_key_for_savedexperiment(path_value)}.json"


def raw_artifact_path_for_savedexperiment(
    path_value: Any,
    artifact_root: str | Path = DEFAULT_RAW_ARTIFACT_ROOT,
) -> Path:
    artifact_root_path = Path(str(artifact_root)).expanduser()
    return artifact_root_path / f"{raw_artifact_key_for_savedexperiment(path_value)}.json"


def normalize_summary_payload(summary: Any) -> dict[str, Any]:
    payload = dict(summary) if isinstance(summary, dict) else {}
    if "data_path" in payload:
        payload["data_path"] = normalize_agent_path(payload.get("data_path", ""))
    diagnostics = payload.get("diagnostic_figures", {})
    if isinstance(diagnostics, dict):
        if "png_path" in diagnostics:
            diagnostics["png_path"] = normalize_agent_path(diagnostics.get("png_path", ""))
        if "png_path_wsl" in diagnostics:
            diagnostics["png_path_wsl"] = normalize_agent_path(diagnostics.get("png_path_wsl", ""))
        payload["diagnostic_figures"] = diagnostics
    scan = payload.get("scan", {})
    if isinstance(scan, dict) and "position" in scan:
        scan["position"] = scan.get("position", [])
        payload["scan"] = scan
    return payload


def normalize_raw_export_payload(raw_export: Any) -> dict[str, Any]:
    payload = dict(raw_export) if isinstance(raw_export, dict) else {}
    if "data_path" in payload:
        payload["data_path"] = normalize_agent_path(payload.get("data_path", ""))
    diagnostics = payload.get("diagnostic_figures", {})
    if isinstance(diagnostics, dict):
        if "png_path" in diagnostics:
            diagnostics["png_path"] = normalize_agent_path(diagnostics.get("png_path", ""))
        if "png_path_wsl" in diagnostics:
            diagnostics["png_path_wsl"] = normalize_agent_path(diagnostics.get("png_path_wsl", ""))
        payload["diagnostic_figures"] = diagnostics
    return payload


def normalize_drift_payload(summary: Any) -> dict[str, Any]:
    payload = dict(summary) if isinstance(summary, dict) else {}
    if "data_path" in payload:
        payload["data_path"] = normalize_agent_path(payload.get("data_path", ""))
    if "source_file" in payload:
        payload["source_file"] = normalize_agent_path(payload.get("source_file", ""))
    entries = payload.get("entries", [])
    if isinstance(entries, dict):
        entries = [entries]
    payload["entries"] = entries if isinstance(entries, list) else []
    payload.setdefault("scan_order_source", "")
    payload.setdefault("scan_order_mode", "")
    payload.setdefault("data_order_for_score", "")
    payload.setdefault("scan_order_used_count", 0)
    warnings = payload.get("scan_order_warnings", [])
    if isinstance(warnings, str):
        warnings = [warnings]
    payload["scan_order_warnings"] = warnings if isinstance(warnings, list) else []
    return payload


def read_cached_summary(cache_root: Path, path_value: Any) -> dict[str, Any] | None:
    key = cache_key_for_summary(path_value)
    cache_path = cache_root / f"{key}.json"
    if not cache_path.is_file():
        return None
    try:
        payload = normalize_summary_payload(json.loads(cache_path.read_text(encoding="utf-8")))
        if payload.get("ok", False) and "diagnostic_figures" not in payload:
            return None
        diagnostics = payload.get("diagnostic_figures", {})
        if isinstance(diagnostics, dict):
            contents = diagnostics.get("contents", [])
            if isinstance(contents, list) and any(str(item).lower() == "derived signal preview" for item in contents):
                return None
        return payload
    except (OSError, json.JSONDecodeError):
        return None


def read_cached_raw_export(cache_root: Path, path_value: Any) -> dict[str, Any] | None:
    key = cache_key_for_raw_export(path_value)
    cache_path = cache_root / f"{key}.json"
    if not cache_path.is_file():
        return None
    try:
        return normalize_raw_export_payload(json.loads(cache_path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError):
        return None


def read_cached_average_drift(
    cache_root: Path,
    path_value: Any,
    *,
    drop_threshold: float,
    slice_index: int,
    min_averages_for_reference: int,
) -> dict[str, Any] | None:
    key = cache_key_for_average_drift(
        path_value,
        drop_threshold=drop_threshold,
        slice_index=slice_index,
        min_averages_for_reference=min_averages_for_reference,
    )
    cache_path = cache_root / f"{key}.json"
    if not cache_path.is_file():
        return None
    try:
        return normalize_drift_payload(json.loads(cache_path.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError):
        return None


def write_cached_summary(cache_root: Path, path_value: Any, payload: dict[str, Any]) -> None:
    key = cache_key_for_summary(path_value)
    cache_root.mkdir(parents=True, exist_ok=True)
    cache_path = cache_root / f"{key}.json"
    cache_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_cached_raw_export(cache_root: Path, path_value: Any, payload: dict[str, Any]) -> None:
    key = cache_key_for_raw_export(path_value)
    cache_root.mkdir(parents=True, exist_ok=True)
    cache_path = cache_root / f"{key}.json"
    cache_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_cached_average_drift(
    cache_root: Path,
    path_value: Any,
    payload: dict[str, Any],
    *,
    drop_threshold: float,
    slice_index: int,
    min_averages_for_reference: int,
) -> None:
    key = cache_key_for_average_drift(
        path_value,
        drop_threshold=drop_threshold,
        slice_index=slice_index,
        min_averages_for_reference=min_averages_for_reference,
    )
    cache_root.mkdir(parents=True, exist_ok=True)
    cache_path = cache_root / f"{key}.json"
    cache_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_savedexperiment_artifact(artifact_root: Path, path_value: Any, payload: dict[str, Any]) -> Path:
    artifact_path = artifact_path_for_savedexperiment(path_value, artifact_root)
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return artifact_path


def write_savedexperiment_raw_artifact(artifact_root: Path, path_value: Any, payload: dict[str, Any]) -> Path:
    artifact_path = raw_artifact_path_for_savedexperiment(path_value, artifact_root)
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    artifact_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return artifact_path


def build_matlab_summary_command(c23_root: str, windows_paths: list[str]) -> str:
    matlab_paths = "{" + ",".join(matlab_quote(path) for path in windows_paths) + "};"
    return (
        f"root={matlab_quote(c23_root)}; "
        "addpath(root); "
        "addpath(fullfile(root,'claw')); "
        "addpath(fullfile(root,'experiment')); "
        "addpath(fullfile(root,'experiment','Functions')); "
        f"paths={matlab_paths}; "
        "summaries=cell(1,numel(paths)); "
        "for k=1:numel(paths); summaries{k}=claw_summarize_savedexperiment_mat(paths{k}); end; "
        f"disp('{JSON_BEGIN_MARKER}'); "
        "disp(jsonencode(summaries)); "
        f"disp('{JSON_END_MARKER}');"
    )


def build_matlab_raw_export_command(c23_root: str, windows_paths: list[str]) -> str:
    matlab_paths = "{" + ",".join(matlab_quote(path) for path in windows_paths) + "};"
    return (
        f"root={matlab_quote(c23_root)}; "
        "addpath(root); "
        "addpath(fullfile(root,'claw')); "
        "addpath(fullfile(root,'experiment')); "
        "addpath(fullfile(root,'experiment','Functions')); "
        f"paths={matlab_paths}; "
        "exports=cell(1,numel(paths)); "
        "for k=1:numel(paths); exports{k}=claw_export_savedexperiment_mat_raw(paths{k}); end; "
        f"disp('{JSON_BEGIN_MARKER}'); "
        "disp(jsonencode(exports)); "
        f"disp('{JSON_END_MARKER}');"
    )


def build_matlab_average_drift_command(
    c23_root: str,
    windows_paths: list[str],
    *,
    drop_threshold: float,
    slice_index: int,
    min_averages_for_reference: int,
) -> str:
    matlab_paths = "{" + ",".join(matlab_quote(path) for path in windows_paths) + "};"
    return (
        f"root={matlab_quote(c23_root)}; "
        "addpath(root); "
        "addpath(fullfile(root,'claw')); "
        "addpath(fullfile(root,'experiment')); "
        "addpath(fullfile(root,'experiment','Functions')); "
        f"paths={matlab_paths}; "
        f"dropThreshold={float(drop_threshold):.12g}; "
        f"sliceIndex={int(slice_index)}; "
        f"minAvgRef={int(min_averages_for_reference)}; "
        "summaries=cell(1,numel(paths)); "
        "for k=1:numel(paths); "
        "s=struct('ok',false,'source','analyze_savedexperiment_average_drift.m','data_path',paths{k},"
        "'source_file','','sequence_name','','slice_index',sliceIndex,'num_averages',0,'num_traces',0,"
        "'num_points',0,'drop_threshold',dropThreshold,'min_averages_for_reference',minAvgRef,"
        "'reference_method','','trace_aggregation_method','','drift_score_method','','scan_order_source','','scan_order_mode','','data_order_for_score','','scan_order_used_count',0,'scan_order_warnings',{{}},'entries',[],'flagged_average_indices',[],'error_code','','error_message',''); "
        "try; "
        "d=analyze_savedexperiment_average_drift(paths{k},'SliceIndex',sliceIndex,'DropThreshold',dropThreshold,'MinAveragesForReference',minAvgRef); "
        "idx=(1:double(d.num_averages)).'; "
        "scanOrderUsed=false(size(idx)); if isfield(d,'scan_order_used'); scanOrderUsed=logical(d.scan_order_used(:)); end; "
        "entries=struct('average_index',num2cell(idx),"
        "'drift_score',num2cell(double(d.drift_score(:))),"
        "'flagged',num2cell(logical(d.flagged(:))),"
        "'scan_order_used',num2cell(scanOrderUsed),"
        "'common_mode_end_minus_start_fraction',num2cell(double(d.common_mode_end_minus_start_fraction(:))),"
        "'common_mode_edge_end_minus_start_fraction',num2cell(double(d.common_mode_edge_end_minus_start_fraction(:))),"
        "'worst_drop_score',num2cell(double(d.worst_drop_score(:))),"
        "'worst_trace_index',num2cell(double(d.worst_trace_index(:))),"
        "'worst_trace_end_minus_start_fraction',num2cell(double(d.worst_trace_end_minus_start_fraction(:))),"
        "'worst_residual_end_minus_start_fraction',num2cell(double(d.worst_residual_end_minus_start_fraction(:))),"
        "'worst_edge_end_minus_start_fraction',num2cell(double(d.worst_edge_end_minus_start_fraction(:)))); "
        "s.ok=true; s.source_file=d.source_file; s.sequence_name=d.sequence_name; "
        "s.slice_index=double(d.slice_index); s.num_averages=double(d.num_averages); "
        "s.num_traces=double(d.num_traces); s.num_points=double(d.num_points); "
        "s.drop_threshold=double(d.drop_threshold); "
        "s.min_averages_for_reference=double(d.min_averages_for_reference); "
        "s.reference_method=d.reference_method; s.trace_aggregation_method=d.trace_aggregation_method; "
        "if isfield(d,'drift_score_method'); s.drift_score_method=d.drift_score_method; end; "
        "if isfield(d,'scan_order_source'); s.scan_order_source=d.scan_order_source; end; "
        "if isfield(d,'scan_order_mode'); s.scan_order_mode=d.scan_order_mode; end; "
        "if isfield(d,'data_order_for_score'); s.data_order_for_score=d.data_order_for_score; end; "
        "if isfield(d,'scan_order_used'); s.scan_order_used_count=double(nnz(d.scan_order_used)); end; "
        "if isfield(d,'scan_order_warnings'); s.scan_order_warnings=cellstr(d.scan_order_warnings); end; "
        "s.entries=entries; "
        "s.flagged_average_indices=reshape(double(d.flagged_average_indices),1,[]); "
        "catch ME; s.error_code=ME.identifier; s.error_message=ME.message; end; "
        "summaries{k}=s; "
        "end; "
        f"disp('{JSON_BEGIN_MARKER}'); "
        "disp(jsonencode(summaries)); "
        f"disp('{JSON_END_MARKER}');"
    )


def run_matlab_savedexperiment_summaries(
    path_values: list[str],
    *,
    c23_root: str | Path = DEFAULT_C23_ROOT,
    matlab_exe: str | Path | None = None,
    timeout_seconds: float = DEFAULT_SUMMARY_TIMEOUT_SECONDS,
) -> list[dict[str, Any]]:
    if not path_values:
        return []
    matlab_path = resolve_matlab_exe(matlab_exe)
    windows_c23_root = to_windows_path(c23_root)
    windows_paths = [to_windows_path(path_value) for path_value in path_values]
    command = build_matlab_summary_command(windows_c23_root, windows_paths)
    completed = subprocess.run(
        [str(matlab_path), "-batch", command],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_seconds,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "MATLAB savedexperiment summary command failed.\n"
            f"Return code: {completed.returncode}\n"
            f"STDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    payload = extract_json_between_markers(completed.stdout)
    if isinstance(payload, dict):
        payload = [payload]
    if not isinstance(payload, list):
        raise ValueError("Savedexperiment summary JSON payload was not a list.")
    if len(payload) != len(path_values):
        raise ValueError("Savedexperiment summary count did not match the requested paths.")
    return [normalize_summary_payload(item) for item in payload]


def run_matlab_savedexperiment_raw_exports(
    path_values: list[str],
    *,
    c23_root: str | Path = DEFAULT_C23_ROOT,
    matlab_exe: str | Path | None = None,
    timeout_seconds: float = DEFAULT_SUMMARY_TIMEOUT_SECONDS,
) -> list[dict[str, Any]]:
    if not path_values:
        return []
    matlab_path = resolve_matlab_exe(matlab_exe)
    windows_c23_root = to_windows_path(c23_root)
    windows_paths = [to_windows_path(path_value) for path_value in path_values]
    command = build_matlab_raw_export_command(windows_c23_root, windows_paths)
    completed = subprocess.run(
        [str(matlab_path), "-batch", command],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_seconds,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "MATLAB savedexperiment raw export command failed.\n"
            f"Return code: {completed.returncode}\n"
            f"STDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    payload = extract_json_between_markers(completed.stdout)
    if isinstance(payload, dict):
        payload = [payload]
    if not isinstance(payload, list):
        raise ValueError("Savedexperiment raw export JSON payload was not a list.")
    if len(payload) != len(path_values):
        raise ValueError("Savedexperiment raw export count did not match the requested paths.")
    return [normalize_raw_export_payload(item) for item in payload]


def run_matlab_savedexperiment_average_drift(
    path_values: list[str],
    *,
    c23_root: str | Path = DEFAULT_C23_ROOT,
    matlab_exe: str | Path | None = None,
    timeout_seconds: float = DEFAULT_SUMMARY_TIMEOUT_SECONDS,
    drop_threshold: float = 0.15,
    slice_index: int = 1,
    min_averages_for_reference: int = 3,
) -> list[dict[str, Any]]:
    if not path_values:
        return []
    matlab_path = resolve_matlab_exe(matlab_exe)
    windows_c23_root = to_windows_path(c23_root)
    windows_paths = [to_windows_path(path_value) for path_value in path_values]
    command = build_matlab_average_drift_command(
        windows_c23_root,
        windows_paths,
        drop_threshold=drop_threshold,
        slice_index=slice_index,
        min_averages_for_reference=min_averages_for_reference,
    )
    completed = subprocess.run(
        [str(matlab_path), "-batch", command],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout_seconds,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "MATLAB savedexperiment average drift command failed.\n"
            f"Return code: {completed.returncode}\n"
            f"STDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    payload = extract_json_between_markers(completed.stdout)
    if isinstance(payload, dict):
        payload = [payload]
    if not isinstance(payload, list):
        raise ValueError("Savedexperiment average drift JSON payload was not a list.")
    if len(payload) != len(path_values):
        raise ValueError("Savedexperiment average drift count did not match the requested paths.")
    return [normalize_drift_payload(item) for item in payload]


def summarize_savedexperiment_mat_files(
    path_values: list[str],
    *,
    cache_root: str | Path = DEFAULT_CACHE_ROOT,
    c23_root: str | Path = DEFAULT_C23_ROOT,
    matlab_exe: str | Path | None = None,
    timeout_seconds: float = DEFAULT_SUMMARY_TIMEOUT_SECONDS,
    force: bool = False,
) -> list[dict[str, Any]]:
    cache_root_path = Path(str(cache_root)).expanduser()
    ordered_paths = [normalize_agent_path(path_value) for path_value in path_values if str(path_value or "").strip()]
    if not ordered_paths:
        return []

    results: list[dict[str, Any] | None] = [None] * len(ordered_paths)
    missing_by_index: list[tuple[int, str]] = []
    for index, path_value in enumerate(ordered_paths):
        cached = None if force else read_cached_summary(cache_root_path, path_value)
        if cached is not None:
            results[index] = cached
        else:
            missing_by_index.append((index, path_value))

    if missing_by_index:
        unique_missing: list[str] = []
        missing_map: dict[str, list[int]] = {}
        for index, path_value in missing_by_index:
            missing_map.setdefault(path_value, []).append(index)
            if path_value not in unique_missing:
                unique_missing.append(path_value)
        try:
            fetched = run_matlab_savedexperiment_summaries(
                unique_missing,
                c23_root=c23_root,
                matlab_exe=matlab_exe,
                timeout_seconds=timeout_seconds,
            )
        except Exception:
            fetched = []
            for path_value in unique_missing:
                try:
                    single = run_matlab_savedexperiment_summaries(
                        [path_value],
                        c23_root=c23_root,
                        matlab_exe=matlab_exe,
                        timeout_seconds=timeout_seconds,
                    )[0]
                except Exception as exc:
                    single = {
                        "ok": False,
                        "source": "savedexperiment_mat",
                        "data_path": normalize_agent_path(path_value),
                        "sequence_name": "",
                        "date_time": "",
                        "position": [],
                        "scan": {},
                        "signal": {},
                        "warnings": [],
                        "notes": [],
                        "error_code": "SavedExperimentSummaryFailed",
                        "error_message": str(exc),
                    }
                fetched.append(single)
        for path_value, payload in zip(unique_missing, fetched):
            normalized = normalize_summary_payload(payload)
            write_cached_summary(cache_root_path, path_value, normalized)
            for index in missing_map.get(path_value, []):
                results[index] = dict(normalized)

    finalized: list[dict[str, Any]] = []
    for index, payload in enumerate(results):
        if isinstance(payload, dict):
            finalized.append(payload)
        else:
            finalized.append(
                {
                    "ok": False,
                    "source": "savedexperiment_mat",
                    "data_path": ordered_paths[index],
                    "sequence_name": "",
                    "date_time": "",
                    "position": [],
                    "scan": {},
                    "signal": {},
                    "warnings": [],
                    "notes": [],
                    "error_code": "SavedExperimentSummaryMissing",
                    "error_message": "Summary payload was not available.",
                }
            )
    return finalized


def export_savedexperiment_mat_raw_files(
    path_values: list[str],
    *,
    cache_root: str | Path = DEFAULT_RAW_EXPORT_CACHE_ROOT,
    c23_root: str | Path = DEFAULT_C23_ROOT,
    matlab_exe: str | Path | None = None,
    timeout_seconds: float = DEFAULT_SUMMARY_TIMEOUT_SECONDS,
    force: bool = False,
) -> list[dict[str, Any]]:
    cache_root_path = Path(str(cache_root)).expanduser()
    ordered_paths = [normalize_agent_path(path_value) for path_value in path_values if str(path_value or "").strip()]
    if not ordered_paths:
        return []

    results: list[dict[str, Any] | None] = [None] * len(ordered_paths)
    missing_by_index: list[tuple[int, str]] = []
    for index, path_value in enumerate(ordered_paths):
        cached = None if force else read_cached_raw_export(cache_root_path, path_value)
        if cached is not None:
            results[index] = cached
        else:
            missing_by_index.append((index, path_value))

    if missing_by_index:
        unique_missing: list[str] = []
        missing_map: dict[str, list[int]] = {}
        for index, path_value in missing_by_index:
            missing_map.setdefault(path_value, []).append(index)
            if path_value not in unique_missing:
                unique_missing.append(path_value)
        try:
            fetched = run_matlab_savedexperiment_raw_exports(
                unique_missing,
                c23_root=c23_root,
                matlab_exe=matlab_exe,
                timeout_seconds=timeout_seconds,
            )
        except Exception:
            fetched = []
            for path_value in unique_missing:
                try:
                    single = run_matlab_savedexperiment_raw_exports(
                        [path_value],
                        c23_root=c23_root,
                        matlab_exe=matlab_exe,
                        timeout_seconds=timeout_seconds,
                    )[0]
                except Exception as exc:
                    single = {
                        "ok": False,
                        "source": "savedexperiment_mat_raw_export",
                        "data_path": normalize_agent_path(path_value),
                        "mat_variables": [],
                        "scan": {},
                        "extra_variables": {},
                        "diagnostic_figures": {},
                        "warnings": [],
                        "error_code": "SavedExperimentRawExportFailed",
                        "error_message": str(exc),
                    }
                fetched.append(single)
        for path_value, payload in zip(unique_missing, fetched):
            normalized = normalize_raw_export_payload(payload)
            write_cached_raw_export(cache_root_path, path_value, normalized)
            for index in missing_map.get(path_value, []):
                results[index] = dict(normalized)

    finalized: list[dict[str, Any]] = []
    for index, payload in enumerate(results):
        if isinstance(payload, dict):
            finalized.append(payload)
        else:
            finalized.append(
                {
                    "ok": False,
                    "source": "savedexperiment_mat_raw_export",
                    "data_path": ordered_paths[index],
                    "mat_variables": [],
                    "scan": {},
                    "extra_variables": {},
                    "diagnostic_figures": {},
                    "warnings": [],
                    "error_code": "SavedExperimentRawExportMissing",
                    "error_message": "Raw export payload was not available.",
                }
            )
    return finalized


def analyze_savedexperiment_average_drift_mat_files(
    path_values: list[str],
    *,
    cache_root: str | Path = DEFAULT_DRIFT_CACHE_ROOT,
    c23_root: str | Path = DEFAULT_C23_ROOT,
    matlab_exe: str | Path | None = None,
    timeout_seconds: float = DEFAULT_SUMMARY_TIMEOUT_SECONDS,
    force: bool = False,
    drop_threshold: float = 0.15,
    slice_index: int = 1,
    min_averages_for_reference: int = 3,
) -> list[dict[str, Any]]:
    cache_root_path = Path(str(cache_root)).expanduser()
    ordered_paths = [normalize_agent_path(path_value) for path_value in path_values if str(path_value or "").strip()]
    if not ordered_paths:
        return []

    results: list[dict[str, Any] | None] = [None] * len(ordered_paths)
    missing_by_index: list[tuple[int, str]] = []
    for index, path_value in enumerate(ordered_paths):
        cached = None if force else read_cached_average_drift(
            cache_root_path,
            path_value,
            drop_threshold=drop_threshold,
            slice_index=slice_index,
            min_averages_for_reference=min_averages_for_reference,
        )
        if cached is not None:
            results[index] = cached
        else:
            missing_by_index.append((index, path_value))

    if missing_by_index:
        unique_missing: list[str] = []
        missing_map: dict[str, list[int]] = {}
        for index, path_value in missing_by_index:
            missing_map.setdefault(path_value, []).append(index)
            if path_value not in unique_missing:
                unique_missing.append(path_value)
        try:
            fetched = run_matlab_savedexperiment_average_drift(
                unique_missing,
                c23_root=c23_root,
                matlab_exe=matlab_exe,
                timeout_seconds=timeout_seconds,
                drop_threshold=drop_threshold,
                slice_index=slice_index,
                min_averages_for_reference=min_averages_for_reference,
            )
        except Exception:
            fetched = []
            for path_value in unique_missing:
                try:
                    single = run_matlab_savedexperiment_average_drift(
                        [path_value],
                        c23_root=c23_root,
                        matlab_exe=matlab_exe,
                        timeout_seconds=timeout_seconds,
                        drop_threshold=drop_threshold,
                        slice_index=slice_index,
                        min_averages_for_reference=min_averages_for_reference,
                    )[0]
                except Exception as exc:
                    single = {
                        "ok": False,
                        "source": "analyze_savedexperiment_average_drift.m",
                        "data_path": normalize_agent_path(path_value),
                        "source_file": normalize_agent_path(path_value),
                        "sequence_name": "",
                        "slice_index": int(slice_index),
                        "num_averages": 0,
                        "num_traces": 0,
                        "num_points": 0,
                        "drop_threshold": float(drop_threshold),
                        "min_averages_for_reference": int(min_averages_for_reference),
                        "reference_method": "",
                        "trace_aggregation_method": "",
                        "drift_score_method": "",
                        "scan_order_source": "",
                        "scan_order_mode": "",
                        "data_order_for_score": "",
                        "scan_order_used_count": 0,
                        "scan_order_warnings": [],
                        "entries": [],
                        "flagged_average_indices": [],
                        "error_code": "SavedExperimentAverageDriftFailed",
                        "error_message": str(exc),
                    }
                fetched.append(single)
        for path_value, payload in zip(unique_missing, fetched):
            normalized = normalize_drift_payload(payload)
            write_cached_average_drift(
                cache_root_path,
                path_value,
                normalized,
                drop_threshold=drop_threshold,
                slice_index=slice_index,
                min_averages_for_reference=min_averages_for_reference,
            )
            for index in missing_map.get(path_value, []):
                results[index] = dict(normalized)

    finalized: list[dict[str, Any]] = []
    for index, payload in enumerate(results):
        if isinstance(payload, dict):
            finalized.append(payload)
        else:
            finalized.append(
                {
                    "ok": False,
                    "source": "analyze_savedexperiment_average_drift.m",
                    "data_path": ordered_paths[index],
                    "source_file": ordered_paths[index],
                    "sequence_name": "",
                    "slice_index": int(slice_index),
                    "num_averages": 0,
                    "num_traces": 0,
                    "num_points": 0,
                    "drop_threshold": float(drop_threshold),
                    "min_averages_for_reference": int(min_averages_for_reference),
                    "reference_method": "",
                    "trace_aggregation_method": "",
                    "drift_score_method": "",
                    "scan_order_source": "",
                    "scan_order_mode": "",
                    "data_order_for_score": "",
                    "scan_order_used_count": 0,
                    "scan_order_warnings": [],
                    "entries": [],
                    "flagged_average_indices": [],
                    "error_code": "SavedExperimentAverageDriftMissing",
                    "error_message": "Average drift payload was not available.",
                }
            )
    return finalized


def materialize_savedexperiment_mat_artifacts(
    path_values: list[str],
    *,
    artifact_root: str | Path = DEFAULT_ARTIFACT_ROOT,
    cache_root: str | Path = DEFAULT_CACHE_ROOT,
    c23_root: str | Path = DEFAULT_C23_ROOT,
    matlab_exe: str | Path | None = None,
    timeout_seconds: float = DEFAULT_SUMMARY_TIMEOUT_SECONDS,
    force: bool = False,
) -> list[dict[str, Any]]:
    ordered_paths = [normalize_agent_path(path_value) for path_value in path_values if str(path_value or "").strip()]
    if not ordered_paths:
        return []

    payloads = summarize_savedexperiment_mat_files(
        ordered_paths,
        cache_root=cache_root,
        c23_root=c23_root,
        matlab_exe=matlab_exe,
        timeout_seconds=timeout_seconds,
        force=force,
    )

    artifact_root_path = Path(str(artifact_root)).expanduser()
    artifacts: list[dict[str, Any]] = []
    for path_value, payload in zip(ordered_paths, payloads):
        normalized = normalize_summary_payload(payload)
        artifact_path = write_savedexperiment_artifact(artifact_root_path, path_value, normalized)
        artifacts.append(
            {
                "data_path": normalize_agent_path(path_value),
                "artifact_path": normalize_agent_path(str(artifact_path)),
                "ok": bool(normalized.get("ok", False)),
                "error_code": str(normalized.get("error_code", "") or ""),
                "error_message": str(normalized.get("error_message", "") or ""),
            }
        )
    return artifacts


def materialize_savedexperiment_mat_raw_artifacts(
    path_values: list[str],
    *,
    artifact_root: str | Path = DEFAULT_RAW_ARTIFACT_ROOT,
    cache_root: str | Path = DEFAULT_RAW_EXPORT_CACHE_ROOT,
    c23_root: str | Path = DEFAULT_C23_ROOT,
    matlab_exe: str | Path | None = None,
    timeout_seconds: float = DEFAULT_SUMMARY_TIMEOUT_SECONDS,
    force: bool = False,
) -> list[dict[str, Any]]:
    ordered_paths = [normalize_agent_path(path_value) for path_value in path_values if str(path_value or "").strip()]
    if not ordered_paths:
        return []

    payloads = export_savedexperiment_mat_raw_files(
        ordered_paths,
        cache_root=cache_root,
        c23_root=c23_root,
        matlab_exe=matlab_exe,
        timeout_seconds=timeout_seconds,
        force=force,
    )

    artifact_root_path = Path(str(artifact_root)).expanduser()
    artifacts: list[dict[str, Any]] = []
    for path_value, payload in zip(ordered_paths, payloads):
        normalized = normalize_raw_export_payload(payload)
        artifact_path = write_savedexperiment_raw_artifact(artifact_root_path, path_value, normalized)
        diagnostics = normalized.get("diagnostic_figures", {}) if isinstance(normalized.get("diagnostic_figures"), dict) else {}
        artifacts.append(
            {
                "data_path": normalize_agent_path(path_value),
                "artifact_path": normalize_agent_path(str(artifact_path)),
                "plot_path": normalize_agent_path(diagnostics.get("png_path_wsl") or diagnostics.get("png_path") or ""),
                "ok": bool(normalized.get("ok", False)),
                "error_code": str(normalized.get("error_code", "") or ""),
                "error_message": str(normalized.get("error_message", "") or ""),
            }
        )
    return artifacts


def build_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export savedexperiment .mat raw data for agent-friendly JSON output.")
    parser.add_argument("paths", nargs="+", help="One or more savedexperiment .mat paths.")
    parser.add_argument("--force", action="store_true", help="Ignore cache and rerun MATLAB extraction.")
    parser.add_argument("--pretty", action="store_true", help="Pretty-print the JSON output.")
    parser.add_argument(
        "--summary",
        action="store_true",
        help=(
            "Deprecated legacy compact summary extractor. Blocked for normal hooks unless "
            "--allow-legacy-summary is also passed or OPENCLAW_ALLOW_LEGACY_MAT_SUMMARY=1 is set."
        ),
    )
    parser.add_argument(
        "--allow-legacy-summary",
        action="store_true",
        help="Explicitly allow deprecated --summary compatibility mode for this manual invocation.",
    )
    parser.add_argument("--timeout-seconds", type=float, default=DEFAULT_SUMMARY_TIMEOUT_SECONDS)
    parser.add_argument("--matlab-exe", default="")
    parser.add_argument("--c23-root", default=str(DEFAULT_C23_ROOT))
    parser.add_argument("--cache-root", default="")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_cli_parser()
    args = parser.parse_args(argv)
    if bool(args.summary):
        if not bool(args.allow_legacy_summary) and not env_flag_enabled(LEGACY_SUMMARY_ENV):
            parser.error(
                "Deprecated --summary mode is disabled for normal hooks. "
                "Use the default raw export, or pass --allow-legacy-summary / set "
                f"{LEGACY_SUMMARY_ENV}=1 for intentional compatibility work."
            )
        payload = summarize_savedexperiment_mat_files(
            args.paths,
            cache_root=args.cache_root or DEFAULT_CACHE_ROOT,
            c23_root=args.c23_root,
            matlab_exe=args.matlab_exe or None,
            timeout_seconds=float(args.timeout_seconds),
            force=bool(args.force),
        )
        legacy_notice = {
            "legacy_deprecated": True,
            "legacy_notice": "This is deprecated --summary output. Normal hooks should use raw export plus plots.",
        }
        for item in payload:
            if isinstance(item, dict):
                item.update(legacy_notice)
    else:
        payload = export_savedexperiment_mat_raw_files(
            args.paths,
            cache_root=args.cache_root or DEFAULT_RAW_EXPORT_CACHE_ROOT,
            c23_root=args.c23_root,
            matlab_exe=args.matlab_exe or None,
            timeout_seconds=float(args.timeout_seconds),
            force=bool(args.force),
        )
    output: Any = payload[0] if len(payload) == 1 else payload
    if args.pretty:
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print(json.dumps(output, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
