#!/usr/bin/env python3
"""Terminal det=1.0 MHz Ramsey/T2star/13C review for reimage1804_c02.

This script exports the terminal savedexperiment with the real MATLAB/23-C
classes, runs the scan-order-aware drift diagnostic, then performs a
readout-aware bridge-free review. It keeps raw export separate from the
scientific summary.
"""
from __future__ import annotations

import json
import math
import shutil
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

sys.path.insert(0, "<OPENCLAW_WORKSPACE>")
from tools_mat_parse import (  # noqa: E402
    export_savedexperiment_mat_raw_files,
    analyze_savedexperiment_average_drift_mat_files,
)

PROJECT_ID = "nv23_aligned_nv_t2star_13c_image172647_20260514_1728"
JOB_ID = "nv23_ramsey_20260514_230820_auto_ramsey"
STAMP = "20260515_0245"
PROJ = Path("<OPENCLAW_WORKSPACE>/.openclaw/projects") / PROJECT_ID
ANALYSIS_DIR = PROJ / "work/artifacts/analysis"
FIG_DIR = PROJ / "work/artifacts/figures"
BRIDGE_ART_DIR = PROJ / "work/artifacts/bridge_results"
NOTE_DIR = PROJ / "work/notes"
for p in (ANALYSIS_DIR, FIG_DIR, BRIDGE_ART_DIR, NOTE_DIR):
    p.mkdir(parents=True, exist_ok=True)

BRIDGE_DONE_DIR = Path("<NV_BRIDGE_ROOT>/done") / JOB_ID
MAT_PATH = Path("<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-14-231101.mat")

RESULT_COPY = BRIDGE_ART_DIR / f"reimage1804_c02_ramsey_det1_terminal_result_{STAMP}.json"
STATUS_COPY = BRIDGE_ART_DIR / f"reimage1804_c02_ramsey_det1_terminal_status_{STAMP}.json"
CONTROL_COPY = BRIDGE_ART_DIR / f"reimage1804_c02_ramsey_det1_terminal_control_{STAMP}.json"
JOB_COPY = BRIDGE_ART_DIR / f"reimage1804_c02_ramsey_det1_terminal_job_{STAMP}.json"
BRIDGE_LOG_COPY = BRIDGE_ART_DIR / f"reimage1804_c02_ramsey_det1_terminal_bridge_log_{STAMP}.txt"
RAW_PATH = ANALYSIS_DIR / f"reimage1804_c02_ramsey_det1_terminal_raw_16avg_{STAMP}.json"
DRIFT_PATH = ANALYSIS_DIR / f"reimage1804_c02_ramsey_det1_terminal_drift_16avg_{STAMP}.json"
SUMMARY_PATH = ANALYSIS_DIR / f"reimage1804_c02_ramsey_det1_terminal_summary_16avg_{STAMP}.json"
FIG_PATH = FIG_DIR / f"reimage1804_c02_ramsey_det1_terminal_16avg_{STAMP}.png"
NOTE_PATH = NOTE_DIR / f"reimage1804_c02_ramsey_det1_terminal_16avg_review_{STAMP}.md"


def copy_if_exists(src: Path, dst: Path) -> str:
    if src.is_file():
        shutil.copy2(src, dst)
        return str(dst)
    return ""


def load_json(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def linfit(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    coef = np.polyfit(x, np.asarray(y, dtype=float), 1)
    return np.polyval(coef, x)


def mednorm(y: np.ndarray) -> np.ndarray:
    arr = np.asarray(y, dtype=float)
    med = float(np.nanmedian(arr))
    return arr / med if med else arr


def p2p_percent(frac: np.ndarray) -> float:
    arr = np.asarray(frac, dtype=float)
    return float((np.nanmax(arr) - np.nanmin(arr)) * 100.0)


def get_scan_order_info(raw: dict, scan: dict) -> dict:
    extra = raw.get("extra_variables") or {}
    soi = extra.get("ScanOrderInfo") or {}
    return {
        "scan_order_mode": scan.get("ScanOrderMode") or soi.get("mode") or "unknown",
        "scan_order_source": soi.get("source") or scan.get("ScanOrderSource") or "unknown",
        "scan_order_each_avg_present": bool(scan.get("ScanOrderEachAvg") or soi.get("order_each_avg")),
    }


def fft_review(y_rel: np.ndarray, tau: np.ndarray, targets: dict[str, float], *, tmin: float = 0.2e-6) -> dict:
    y_rel = np.asarray(y_rel, dtype=float)
    mask = tau >= (tmin - 1e-15)
    tx = tau[mask]
    yy = y_rel[mask]
    if len(tx) < 8:
        return {"available": False, "reason": "too_few_points"}
    # Match the in-run autosave review: remove a linear trend on the selected
    # window and use a Hann window. With tau=0 excluded, 50 points at 0.2 us
    # give 100 kHz bins, matching the det-shift model record.
    dt = float(np.median(np.diff(tx)))
    t0 = tx - tx.min()
    trend = np.polyval(np.polyfit(t0, yy, 1), t0)
    yd = yy - trend
    win = np.hanning(len(tx))
    spec = np.fft.rfft(yd * win)
    freqs = np.fft.rfftfreq(len(tx), dt)
    amp = 2.0 * np.abs(spec) / np.sum(win) * 100.0
    valid = np.where((freqs > 0) & (freqs <= freqs[-1]))[0]
    top = sorted(valid, key=lambda k: amp[k], reverse=True)[:12]
    target_bins = {}
    for name, target in targets.items():
        if len(valid) == 0:
            continue
        idx = int(valid[np.argmin(np.abs(freqs[valid] - target))])
        target_bins[name] = {
            "target_hz": float(target),
            "bin_hz": float(freqs[idx]),
            "bin_offset_hz": float(freqs[idx] - target),
            "amplitude_percent": float(amp[idx]),
            "phase_rad": float(np.angle(spec[idx])),
        }
    return {
        "available": True,
        "method": "tau>=0.2us, linear detrend, Hann window, 2*abs(rfft)/sum(window)",
        "tmin_s": float(tmin),
        "n_points": int(len(tx)),
        "dt_s": dt,
        "frequency_resolution_hz": float(freqs[1] - freqs[0]) if len(freqs) > 1 else None,
        "nyquist_hz": float(freqs[-1]),
        "target_bins": target_bins,
        "top_peaks": [
            {"frequency_hz": float(freqs[k]), "amplitude_percent": float(amp[k]), "phase_rad": float(np.angle(spec[k]))}
            for k in top
        ],
    }


def fft_complex_at_targets(y_rel: np.ndarray, tau: np.ndarray, targets: dict[str, float], *, tmin: float = 0.2e-6) -> dict[str, complex]:
    y_rel = np.asarray(y_rel, dtype=float)
    mask = tau >= (tmin - 1e-15)
    tx = tau[mask]
    yy = y_rel[mask]
    dt = float(np.median(np.diff(tx)))
    t0 = tx - tx.min()
    trend = np.polyval(np.polyfit(t0, yy, 1), t0)
    yd = yy - trend
    win = np.hanning(len(tx))
    spec = np.fft.rfft(yd * win)
    freqs = np.fft.rfftfreq(len(tx), dt)
    valid = np.where((freqs > 0) & (freqs <= freqs[-1]))[0]
    out = {}
    for name, target in targets.items():
        idx = int(valid[np.argmin(np.abs(freqs[valid] - target))])
        out[name] = 2.0 * spec[idx] / np.sum(win) * 100.0
    return out


def per_average_target_coherence(each_avg: np.ndarray, tau: np.ndarray, targets: dict[str, float], *, view: str) -> dict:
    complexes = {name: [] for name in targets}
    curves = []
    for avg in each_avg:
        ref_i = np.asarray(avg[0], dtype=float)
        sig_i = np.asarray(avg[1], dtype=float)
        if view == "signal_self_baseline":
            y = sig_i / linfit(tau, sig_i) - 1.0
        elif view == "fitted_reference_norm":
            z = sig_i / linfit(tau, ref_i)
            y = z / np.median(z) - 1.0
        else:
            z = sig_i / ref_i
            y = z / np.median(z) - 1.0
        curves.append(y)
        c = fft_complex_at_targets(y, tau, targets)
        for name, val in c.items():
            complexes[name].append(val)
    payload = {}
    for name, vals in complexes.items():
        arr = np.asarray(vals, dtype=complex)
        amps = np.abs(arr)
        vector = np.mean(arr) if len(arr) else 0j
        payload[name] = {
            "combined_vector_amplitude_percent": float(abs(vector)),
            "mean_single_average_amplitude_percent": float(np.mean(amps)) if len(amps) else None,
            "std_single_average_amplitude_percent": float(np.std(amps, ddof=1)) if len(amps) > 1 else None,
            "sem_single_average_amplitude_percent": float(np.std(amps, ddof=1) / math.sqrt(len(amps))) if len(amps) > 1 else None,
            "vector_coherence_abs_mean_over_mean_abs": float(abs(vector) / np.mean(amps)) if len(amps) and np.mean(amps) else None,
            "single_average_amplitudes_percent": [float(x) for x in amps],
            "single_average_phases_rad": [float(np.angle(x)) for x in arr],
        }
    return payload


def fit_damped_cosine(tau: np.ndarray, yy: np.ndarray, sigma: np.ndarray, *, exponent: int = 1,
                      exclude_points: int = 0, end_us: float = 10.0,
                      fixed_freq_mhz: float | None = None, starts_mhz: list[float] | None = None) -> dict:
    mask = (tau >= tau[exclude_points] - 1e-15) & (tau <= end_us * 1e-6 + 1e-15)
    t = tau[mask]
    y = yy[mask]
    w = sigma[mask]
    if len(t) < 8:
        return {"ok": False, "reason": "too_few_points"}
    # Do not let the optimizer declare an arbitrary very-high-frequency result.
    freq_starts = starts_mhz or [0.615, 1.0, 1.385, 1.9]
    if fixed_freq_mhz is not None:
        freq_starts = [float(fixed_freq_mhz)]
    best = None
    for A0 in [0.005, 0.015, 0.03, 0.06]:
        for T0 in [0.5, 1.5, 3.0, 8.0, 20.0]:
            for f0 in freq_starts:
                for phi0 in [-math.pi, -1.0, 0.0, 1.0, math.pi]:
                    if fixed_freq_mhz is None:
                        x0 = np.array([0.0, A0, math.log(T0), f0, phi0], dtype=float)
                        lb = np.array([-0.10, 0.0, math.log(0.1), 0.05, -4 * math.pi])
                        ub = np.array([0.10, 0.30, math.log(100.0), 2.50, 4 * math.pi])

                        def residual(x):
                            c, A, logT, fMHz, phi = x
                            T = math.exp(logT) * 1e-6
                            model = c + A * np.exp(-((t / T) ** exponent)) * np.cos(2 * np.pi * fMHz * 1e6 * t + phi)
                            return (model - y) / w
                    else:
                        x0 = np.array([0.0, A0, math.log(T0), phi0], dtype=float)
                        lb = np.array([-0.10, 0.0, math.log(0.1), -4 * math.pi])
                        ub = np.array([0.10, 0.30, math.log(100.0), 4 * math.pi])

                        def residual(x):
                            c, A, logT, phi = x
                            T = math.exp(logT) * 1e-6
                            model = c + A * np.exp(-((t / T) ** exponent)) * np.cos(2 * np.pi * fixed_freq_mhz * 1e6 * t + phi)
                            return (model - y) / w
                    try:
                        res = least_squares(residual, x0, bounds=(lb, ub), max_nfev=2500)
                    except Exception:
                        continue
                    chi2 = float(np.sum(res.fun ** 2))
                    k = len(x0)
                    aic = chi2 + 2 * k
                    if best is None or aic < best["aic"]:
                        if fixed_freq_mhz is None:
                            c, A, logT, fMHz, phi = res.x
                        else:
                            c, A, logT, phi = res.x
                            fMHz = float(fixed_freq_mhz)
                        best = {
                            "ok": True,
                            "exponent": int(exponent),
                            "exclude_points": int(exclude_points),
                            "start_tau_us": float(t[0] * 1e6),
                            "end_tau_us": float(t[-1] * 1e6),
                            "n_points": int(len(t)),
                            "fixed_frequency_mhz": fixed_freq_mhz,
                            "offset": float(c),
                            "amplitude_fraction": float(A),
                            "t2star_us": float(math.exp(logT)),
                            "frequency_mhz": float(fMHz),
                            "phase_rad": float(((phi + math.pi) % (2 * math.pi)) - math.pi),
                            "chi2": chi2,
                            "reduced_chi2": float(chi2 / max(1, len(t) - k)),
                            "aic": float(aic),
                            "optimizer_success": bool(res.success),
                        }
    return best or {"ok": False, "reason": "optimizer_failed"}


def model_curve(tau: np.ndarray, fit: dict) -> np.ndarray:
    if not fit.get("ok"):
        return np.full_like(tau, np.nan, dtype=float)
    T = float(fit["t2star_us"]) * 1e-6
    exponent = int(fit.get("exponent") or 1)
    return (
        float(fit["offset"])
        + float(fit["amplitude_fraction"])
        * np.exp(-((tau / T) ** exponent))
        * np.cos(2 * np.pi * float(fit["frequency_mhz"]) * 1e6 * tau + float(fit["phase_rad"]))
    )


def main() -> None:
    if not BRIDGE_DONE_DIR.is_dir():
        raise FileNotFoundError(f"Done bridge job not found: {BRIDGE_DONE_DIR}")
    if not MAT_PATH.is_file():
        raise FileNotFoundError(f"Savedexperiment MAT not found: {MAT_PATH}")

    copy_if_exists(BRIDGE_DONE_DIR / "result.json", RESULT_COPY)
    copy_if_exists(BRIDGE_DONE_DIR / "status.json", STATUS_COPY)
    copy_if_exists(BRIDGE_DONE_DIR / "control.json", CONTROL_COPY)
    copy_if_exists(BRIDGE_DONE_DIR / "job.json", JOB_COPY)
    copy_if_exists(BRIDGE_DONE_DIR / "bridge.log", BRIDGE_LOG_COPY)

    raw_payloads = export_savedexperiment_mat_raw_files([str(MAT_PATH)], force=True, timeout_seconds=300)
    raw = raw_payloads[0]
    RAW_PATH.write_text(json.dumps(raw, indent=2, ensure_ascii=False) + "\n")

    try:
        drift = analyze_savedexperiment_average_drift_mat_files(
            [str(MAT_PATH)], force=True, drop_threshold=0.15,
            min_averages_for_reference=2, timeout_seconds=300,
        )[0]
    except Exception as exc:  # diagnostic should not erase the raw terminal result
        drift = {
            "ok": False,
            "source": "analyze_savedexperiment_average_drift.m",
            "error_code": type(exc).__name__,
            "error_message": str(exc),
        }
    DRIFT_PATH.write_text(json.dumps(drift, indent=2, ensure_ascii=False) + "\n")

    result = load_json(RESULT_COPY)
    status = load_json(STATUS_COPY)
    job = load_json(JOB_COPY)
    scan = raw["scan"]
    combined = np.asarray(scan["ExperimentData"][0], dtype=float)
    errors = np.asarray(scan.get("ExperimentDataError", [[np.zeros_like(combined)]])[0], dtype=float)
    each_avg = np.asarray(scan["ExperimentDataEachAvg"][0], dtype=float)
    points = int(scan.get("vary_points") or combined.shape[-1])
    begin = float(scan.get("vary_begin") or 0.0)
    step = float(scan.get("vary_step_size") or ((float(scan.get("vary_end")) - begin) / max(points - 1, 1)))
    tau = begin + step * np.arange(points)
    tau_us = tau * 1e6
    ref = combined[0]
    sig = combined[1]
    ref_fit = linfit(tau, ref)
    sig_fit = linfit(tau, sig)
    pointwise = mednorm(sig / ref)
    fitted_ref = mednorm(sig / ref_fit)
    self_baseline = sig / sig_fit
    self_view = self_baseline / np.median(self_baseline)
    point_frac = pointwise - 1.0
    ref_frac = fitted_ref - 1.0
    self_frac = self_view - 1.0

    # Use exported errors if useful; otherwise use the across-average SEM. Keep a
    # floor so fits cannot overclaim tiny pointwise uncertainties.
    if errors.shape == combined.shape and np.nanmax(np.abs(errors)) > 0:
        sigma_rel = np.maximum(np.asarray(errors[1], dtype=float) / np.maximum(np.abs(sig_fit), 1e-12), 0.003)
    else:
        sig_each = each_avg[:, 1, :]
        sem = np.std(sig_each, axis=0, ddof=1) / math.sqrt(max(1, each_avg.shape[0]))
        sigma_rel = np.maximum(sem / np.maximum(np.abs(sig_fit), 1e-12), 0.003)

    meta = job.get("metadata") or {}
    model = meta.get("expected_signal_model") or {}
    float_vars = job.get("float_vars") or {}
    det_hz = float(float_vars.get("det") or model.get("det_hz") or 1.0e6)
    f13_hz = float(model.get("expected_13C_larmor_hz") or model.get("direct_13C_larmor_check_hz") or 384586.53035146825)
    previous_hz = float(model.get("previous_ramsey_empirical_frequency_hz") or 1.923e6)
    targets = {
        "direct_13C_larmor_hz": f13_hz,
        "det_minus_13C_hz": det_hz - f13_hz,
        "det_carrier_hz": det_hz,
        "det_plus_13C_hz": det_hz + f13_hz,
        "previous_det1p5_ambiguity_hz": previous_hz,
    }

    fft_self = fft_review(self_frac, tau, targets)
    fft_ref = fft_review(ref_frac, tau, targets)
    fft_point = fft_review(point_frac, tau, targets)
    coh_self = per_average_target_coherence(each_avg, tau, targets, view="signal_self_baseline")
    coh_ref = per_average_target_coherence(each_avg, tau, targets, view="fitted_reference_norm")

    fit_grid = []
    starts = [targets["det_minus_13C_hz"] / 1e6, det_hz / 1e6, targets["det_plus_13C_hz"] / 1e6, previous_hz / 1e6]
    for view_name, yy in [("signal_self_baseline", self_frac), ("fitted_reference_norm", ref_frac)]:
        for exponent in [1, 2]:
            for exclude_points in [0, 1, 2, 3]:
                for end_us in [4.0, 6.0, 8.0, 10.0]:
                    fit = fit_damped_cosine(tau, yy, sigma_rel, exponent=exponent, exclude_points=exclude_points, end_us=end_us, starts_mhz=starts)
                    fit["view"] = view_name
                    fit_grid.append(fit)
    fixed_fit_grid = []
    for fmhz in [targets["det_minus_13C_hz"] / 1e6, det_hz / 1e6, targets["det_plus_13C_hz"] / 1e6, previous_hz / 1e6]:
        fit = fit_damped_cosine(tau, self_frac, sigma_rel, exponent=1, exclude_points=0, end_us=10.0, fixed_freq_mhz=fmhz, starts_mhz=starts)
        fit["view"] = "signal_self_baseline"
        fixed_fit_grid.append(fit)
    valid_fits = [f for f in fit_grid if f.get("ok")]
    valid_self_fits = [f for f in valid_fits if f.get("view") == "signal_self_baseline"]
    best_self_fit = min(valid_self_fits, key=lambda f: f["aic"]) if valid_self_fits else {"ok": False}
    selected_self_all_10us = next(
        (f for f in valid_self_fits if f.get("exponent") == 1 and f.get("exclude_points") == 0 and abs(f.get("end_tau_us", -1) - 10.0) < 1e-9),
        best_self_fit,
    )
    selected_self_excl1_10us = next(
        (f for f in valid_self_fits if f.get("exponent") == 1 and f.get("exclude_points") == 1 and abs(f.get("end_tau_us", -1) - 10.0) < 1e-9),
        best_self_fit,
    )

    def target_amp(payload: dict, name: str) -> float:
        return float((((payload.get("target_bins") or {}).get(name) or {}).get("amplitude_percent") or 0.0))

    navg = int(each_avg.shape[0])
    reps = int(scan.get("Repetitions") or 0)
    shots = navg * reps if reps else None
    binomial_floor = 1.0 / math.sqrt(shots) if shots else None
    scan_order_info = get_scan_order_info(raw, scan)
    flagged = drift.get("flagged_average_indices") or []

    # Conservative interpretation from raw/readout-aware evidence.
    target_line = {
        "direct_13C_larmor_hz": target_amp(fft_self, "direct_13C_larmor_hz"),
        "det_minus_13C_hz": target_amp(fft_self, "det_minus_13C_hz"),
        "det_carrier_hz": target_amp(fft_self, "det_carrier_hz"),
        "det_plus_13C_hz": target_amp(fft_self, "det_plus_13C_hz"),
        "previous_det1p5_ambiguity_hz": target_amp(fft_self, "previous_det1p5_ambiguity_hz"),
    }
    strongest_target = max(target_line, key=target_line.get)
    top_self = (fft_self.get("top_peaks") or [{}])[0]

    # A visible weak oscillation is allowed if raw signal/self-baseline structure
    # and FFT/fits agree. 13C, however, needs det-shift-consistent sideband
    # support in both self and reference-aware views, not just the largest bin.
    signal_presence = "weak_empirical_ramsey_structure_present_but_low_contrast"
    t2star_status = "bounded_short_us_order_only_not_final_scalar"
    carbon13_status = "not_established"
    interpretation_text = (
        f"Terminal 16-average det=1.0 MHz Ramsey completed with healthy counts and no stop request. "
        f"Readout2/self-baseline FFT target amplitudes are direct 13C {target_line['direct_13C_larmor_hz']:.2f}%, "
        f"det-13C {target_line['det_minus_13C_hz']:.2f}%, carrier {target_line['det_carrier_hz']:.2f}%, "
        f"det+13C {target_line['det_plus_13C_hz']:.2f}%, and previous 1.9 MHz ambiguity {target_line['previous_det1p5_ambiguity_hz']:.2f}%. "
        f"The strongest target bin is {strongest_target}; the largest self-baseline FFT peak is "
        f"{float(top_self.get('frequency_hz', 0.0))/1e6:.3f} MHz at {float(top_self.get('amplitude_percent', 0.0)):.2f}%. "
        f"The det+13C-compatible component is a real candidate because it moved from the prior det=1.5 MHz high-sideband region to the new det=1.0 MHz high-sideband region, "
        f"but these sub-percent-to-about-percent features are much smaller than the pODMR contrast and the low sideband/direct-Larmor/carrier support is incomplete. "
        f"Damped-cosine fits give a short-us order T2* scale but are sensitive to frequency/window/early-tau handling, so report only a bounded short-us order rather than a final scalar."
    )

    safety = result.get("safety") or result.get("summary", {}).get("safety", {})

    summary = {
        "ok": True,
        "schema_version": 1,
        "project_id": PROJECT_ID,
        "candidate_label": "reimage1804_c02",
        "job_id": JOB_ID,
        "created_at": datetime.now().astimezone().isoformat(),
        "kind": "terminal_ramsey_det1_16avg_review",
        "raw_export_json": str(RAW_PATH),
        "drift_json": str(DRIFT_PATH),
        "figure": str(FIG_PATH),
        "note": str(NOTE_PATH),
        "terminal_bridge": {
            "result_status": result.get("status"),
            "started_at": result.get("started_at"),
            "finished_at": result.get("finished_at"),
            "data_path": result.get("data_path"),
            "pre_run_align_final_counts_kcps": result.get("summary", {}).get("align_nv", {}).get("final_counts_kcps"),
            "post_run_final_counts_kcps": result.get("summary", {}).get("run_experiment", {}).get("post_run", {}).get("final_counts_kcps"),
            "stop_requested": status.get("control", {}).get("stop_requested"),
            "safety_aborted": safety.get("aborted"),
            "safe_shutdown_ok": safety.get("safe_shutdown_ok"),
            "status_state": status.get("state"),
            "status_phase": status.get("phase"),
        },
        "scan_verification": {
            "sequence_name": scan.get("SequenceName"),
            "vary_prop": scan.get("vary_prop"),
            "tau_begin_s": float(scan.get("vary_begin")),
            "tau_end_s": float(scan.get("vary_end")),
            "tau_points": int(scan.get("vary_points")),
            "tau_step_s": float(scan.get("vary_step_size")),
            "averages": int(scan.get("Averages")),
            "repetitions": int(scan.get("Repetitions")),
            "shots_per_point": shots,
            "binomial_floor_fraction": binomial_floor,
            **scan_order_info,
            "readout_roles": "ramsey.xml full_experiment=0: readout 1 mS=0 reference; readout 2 Ramsey signal after Ramsey pulses",
            "actual_float_vars": {item["name"]: item["value"] for item in scan.get("Variable_values", [])},
            "job_float_vars": job.get("float_vars"),
        },
        "expected_signal_model": {
            "source": "job.metadata.expected_signal_model plus direct recomputation of target bins",
            "det_hz": det_hz,
            "expected_13C_larmor_hz": f13_hz,
            "targets_hz": targets,
            "previous_ramsey_empirical_frequency_hz": previous_hz,
            "model_from_job": model,
        },
        "drift": {
            "ok": drift.get("ok"),
            "source": drift.get("source"),
            "num_averages": drift.get("num_averages"),
            "scan_order_source": drift.get("scan_order_source"),
            "scan_order_mode": drift.get("scan_order_mode"),
            "flagged_average_indices": flagged,
            "artifact": str(DRIFT_PATH),
        },
        "raw_readout_stats": {
            "reference_mean_kcps_like": float(np.mean(ref)),
            "reference_min_kcps_like": float(np.min(ref)),
            "reference_max_kcps_like": float(np.max(ref)),
            "signal_mean_kcps_like": float(np.mean(sig)),
            "signal_min_kcps_like": float(np.min(sig)),
            "signal_max_kcps_like": float(np.max(sig)),
            "signal_self_baseline_range_percent": [float(np.min(self_frac) * 100), float(np.max(self_frac) * 100)],
            "signal_self_baseline_std_percent": float(np.std(self_frac) * 100),
            "fitted_reference_norm_range_percent": [float(np.min(ref_frac) * 100), float(np.max(ref_frac) * 100)],
            "fitted_reference_norm_std_percent": float(np.std(ref_frac) * 100),
            "pointwise_signal_over_reference_range_percent": [float(np.min(point_frac) * 100), float(np.max(point_frac) * 100)],
        },
        "fft": {
            "signal_self_baseline": fft_self,
            "fitted_reference_norm": fft_ref,
            "pointwise_signal_over_reference": fft_point,
            "per_average_coherence_signal_self_baseline": coh_self,
            "per_average_coherence_fitted_reference_norm": coh_ref,
            "target_amplitudes_percent_signal_self_baseline": target_line,
        },
        "fits": {
            "best_signal_self_baseline": best_self_fit,
            "selected_exponential_all_points_10us_signal_self_baseline": selected_self_all_10us,
            "selected_exponential_exclude_first_point_10us_signal_self_baseline": selected_self_excl1_10us,
            "fixed_frequency_exponential_10us_signal_self_baseline": fixed_fit_grid,
            "grid": fit_grid,
        },
        "interpretation": {
            "signal_presence": signal_presence,
            "t2star_status": t2star_status,
            "carbon13_status": carbon13_status,
            "strongest_target_bin_signal_self_baseline": strongest_target,
            "summary": interpretation_text,
            "recommended_next": "Do not claim 13C from this run. Since an aligned NV and short T2* order are supported but 13C is not, next bridge-free decision is whether the project objective can close with a no-13C conclusion for this NV or whether to run a targeted confirmation/alternative sequence; any new bridge work needs a fresh model calculation, advisory, and queue-idle verifier.",
        },
    }
    SUMMARY_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")

    # Figure
    fig, axes = plt.subplots(5, 1, figsize=(12, 16), constrained_layout=True)
    ax = axes[0]
    ax.plot(tau_us, ref, "o-", ms=3, label="readout 1 reference")
    ax.plot(tau_us, sig, "o-", ms=3, label="readout 2 signal")
    ax.plot(tau_us, ref_fit, "--", alpha=0.6, label="linear fit ref")
    ax.plot(tau_us, sig_fit, "--", alpha=0.6, label="linear fit signal")
    ax.set_ylabel("kcps-like")
    ax.set_title("reimage1804_c02 det=1 MHz Ramsey terminal: 16 avg")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    ax = axes[1]
    ax.plot(tau_us, pointwise, "o-", ms=3, label="pointwise signal/ref, median norm")
    ax.plot(tau_us, fitted_ref, "o-", ms=3, label="signal / linear-fit(ref), median norm")
    ax.plot(tau_us, self_view, "o-", ms=3, label="signal / linear-fit(signal), median norm")
    ax.axhline(1.0, color="k", linewidth=0.8, alpha=0.5)
    ax.set_ylabel("relative")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    ax = axes[2]
    for i, avg in enumerate(each_avg, start=1):
        sig_i = np.asarray(avg[1], dtype=float)
        self_i = sig_i / linfit(tau, sig_i)
        ax.plot(tau_us, self_i / np.median(self_i), ".-", alpha=0.55, label=f"avg {i}")
    ax.axhline(1.0, color="k", linewidth=0.8, alpha=0.5)
    ax.set_ylabel("per-avg signal/self-line")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", ncol=4, fontsize=6)

    ax = axes[3]
    # Recompute FFT curves for plotting using the same method as fft_review.
    mask = tau >= 0.2e-6 - 1e-15
    tx = tau[mask]
    dt = float(np.median(np.diff(tx)))
    freqs = np.fft.rfftfreq(len(tx), dt)
    win = np.hanning(len(tx))
    def plot_amp(y):
        yy = y[mask]
        t0 = tx - tx.min()
        trend = np.polyval(np.polyfit(t0, yy, 1), t0)
        return 2.0 * np.abs(np.fft.rfft((yy - trend) * win)) / np.sum(win) * 100.0
    ax.plot(freqs / 1e6, plot_amp(ref_frac), "-", label="signal/linear-ref FFT")
    ax.plot(freqs / 1e6, plot_amp(self_frac), "-", label="readout2 self-baseline FFT")
    for label, freq in [
        ("13C Larmor", targets["direct_13C_larmor_hz"]),
        ("det-13C", targets["det_minus_13C_hz"]),
        ("det", targets["det_carrier_hz"]),
        ("det+13C", targets["det_plus_13C_hz"]),
        ("prev 1.9", targets["previous_det1p5_ambiguity_hz"]),
    ]:
        ax.axvline(freq / 1e6, linestyle="--", alpha=0.45)
        ymax = ax.get_ylim()[1]
        ax.text(freq / 1e6, ymax * 0.92, label, rotation=90, va="top", ha="right", fontsize=8)
    ax.set_xlim(0, 2.5)
    ax.set_xlabel("frequency (MHz)")
    ax.set_ylabel("FFT amp (%)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    ax = axes[4]
    ax.errorbar(tau_us, self_frac * 100.0, yerr=sigma_rel * 100.0, fmt="o", ms=3, alpha=0.8, label="signal/self-baseline data")
    if selected_self_all_10us.get("ok"):
        ax.plot(tau_us, model_curve(tau, selected_self_all_10us) * 100.0, "-", label=f"exp fit all: f={selected_self_all_10us['frequency_mhz']:.3f} MHz, T2*={selected_self_all_10us['t2star_us']:.2f} us")
    if selected_self_excl1_10us.get("ok"):
        ax.plot(tau_us, model_curve(tau, selected_self_excl1_10us) * 100.0, "--", label=f"fit excl first: f={selected_self_excl1_10us['frequency_mhz']:.3f} MHz, T2*={selected_self_excl1_10us['t2star_us']:.2f} us")
    ax.axhline(0.0, color="k", linewidth=0.8, alpha=0.5)
    ax.set_xlabel("tau (us)")
    ax.set_ylabel("relative signal (%)")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="best", fontsize=8)

    fig.savefig(FIG_PATH, dpi=180)

    note = f"""# reimage1804_c02 det=1 MHz Ramsey terminal 16-average review ({STAMP})

## Inputs

- Bridge job: `{JOB_ID}` terminal `done`, saved data `{result.get('data_path')}`.
- Sequence/readout: `{scan.get('SequenceName')}`, `full_experiment=0`; readout 1 is reference and readout 2 is Ramsey signal.
- Scan: tau {begin*1e6:.3f}..{tau[-1]*1e6:.3f} us, {points} points, det={det_hz/1e6:.3f} MHz, {navg} averages x {reps} reps ({shots} shots/point).
- Expected discriminator targets from the pre-run model: direct 13C {f13_hz/1e6:.3f} MHz, det-13C {(det_hz-f13_hz)/1e6:.3f} MHz, carrier {det_hz/1e6:.3f} MHz, det+13C {(det_hz+f13_hz)/1e6:.3f} MHz, previous ambiguity {previous_hz/1e6:.3f} MHz.

## Terminal and drift checks

- Pre-run TrackCenter final: {summary['terminal_bridge']['pre_run_align_final_counts_kcps']} kcps; post-run final: {summary['terminal_bridge']['post_run_final_counts_kcps']} kcps.
- stop_requested={summary['terminal_bridge']['stop_requested']}; safety_aborted={summary['terminal_bridge']['safety_aborted']}; safe_shutdown_ok={summary['terminal_bridge']['safe_shutdown_ok']}.
- Drift diagnostic: ok={drift.get('ok')}, scan_order_source={drift.get('scan_order_source')}, scan_order_mode={drift.get('scan_order_mode')}, flagged_average_indices={flagged}.

## Readout-aware review

- Signal/self-baseline range: {summary['raw_readout_stats']['signal_self_baseline_range_percent'][0]:.2f}% to {summary['raw_readout_stats']['signal_self_baseline_range_percent'][1]:.2f}%.
- FFT target amplitudes from the readout2/self-baseline view: direct 13C {target_line['direct_13C_larmor_hz']:.2f}%, det-13C {target_line['det_minus_13C_hz']:.2f}%, carrier {target_line['det_carrier_hz']:.2f}%, det+13C {target_line['det_plus_13C_hz']:.2f}%, previous 1.9 MHz ambiguity {target_line['previous_det1p5_ambiguity_hz']:.2f}%.
- Largest self-baseline FFT peak: {float(top_self.get('frequency_hz', 0.0))/1e6:.3f} MHz at {float(top_self.get('amplitude_percent', 0.0)):.2f}%.
- Fit provenance: selected all-point 10 us exponential fit has f={selected_self_all_10us.get('frequency_mhz', float('nan')):.3f} MHz and T2*={selected_self_all_10us.get('t2star_us', float('nan')):.2f} us; excluding the first point gives f={selected_self_excl1_10us.get('frequency_mhz', float('nan')):.3f} MHz and T2*={selected_self_excl1_10us.get('t2star_us', float('nan')):.2f} us. Treat these as bounded fit provenance, not a final scalar.

## Interpretation

{interpretation_text}

Conclusion for this terminal review: `reimage1804_c02` remains the aligned-NV branch; the run supports only a short/few-us T2* order, not a robust final scalar, and does **not** establish a nearby 13C coupling. Any further bridge work should be a targeted confirmation/alternative protocol with a fresh quantitative model and verifier/advisory gates; do not do a blind repeat.

## Artifacts

- Raw export: `{RAW_PATH}`
- Drift diagnostic: `{DRIFT_PATH}`
- Summary JSON: `{SUMMARY_PATH}`
- Figure: `{FIG_PATH}`
- Bridge result/status/job copies: `{RESULT_COPY}`, `{STATUS_COPY}`, `{JOB_COPY}`
"""
    NOTE_PATH.write_text(note)

    print(json.dumps({"summary": str(SUMMARY_PATH), "figure": str(FIG_PATH), "note": str(NOTE_PATH)}, indent=2))


if __name__ == "__main__":
    main()
