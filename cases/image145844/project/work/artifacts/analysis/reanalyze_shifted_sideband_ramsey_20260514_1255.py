#!/usr/bin/env python3
from __future__ import annotations
import json, math
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT = Path('<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507')
AN = PROJECT/'work/artifacts/analysis'
FIGS = PROJECT/'work/artifacts/figures'
REVIEW_PATH = AN/'image145844_reimage_r03_ramsey_refreshed_center_terminal_review_20260514_0938.json'
TS = datetime.now(ZoneInfo('America/New_York')).strftime('%Y%m%d_%H%M')

review = json.loads(REVIEW_PATH.read_text(encoding='utf-8'))
raw = json.loads(Path(review['raw_export_path']).read_text(encoding='utf-8'))
scan = raw['scan']
edata = np.asarray(scan['ExperimentData'], dtype=float)[0]
eavg = np.asarray(scan['ExperimentDataEachAvg'], dtype=float)[0]
ref_each = eavg[:, 0, :]
sig_each = eavg[:, 1, :]
ref = edata[0]
sig = edata[1]
if not (np.allclose(ref_each.mean(axis=0), ref) and np.allclose(sig_each.mean(axis=0), sig)):
    raise RuntimeError('ExperimentDataEachAvg axis contract check failed')

points = int(scan['vary_points'])
tau = float(scan['vary_begin']) + np.arange(points) * float(scan['vary_step_size'])
tau_us = tau * 1e6
ratio = sig / ref
ref_line = np.polyval(np.polyfit(tau, ref, 1), tau)
sig_over_refline = sig / ref_line
ratio_each = sig_each / ref_each
n_avg = int(eavg.shape[0])

TARGETS = review['targets_hz']
programmed_carrier = float(TARGETS['programmed_carrier_det_1p5MHz'])
low_fixed = float(TARGETS['expected_low_13C_sideband_det_minus_larmor'])
high_fixed = float(TARGETS['expected_high_13C_sideband_det_plus_larmor'])
f13c = (high_fixed - low_fixed) / 2.0
nyquist_hz = float(review['summary_stats']['nyquist_hz'])
median_signal_sem = float(review['summary_stats']['signal_point_sem_kcps']['median'])

# The human-requested alternate hypothesis: the actual Ramsey carrier can be
# shifted by residual mw-frequency calibration error, and 13C sidebands can sit
# around that shifted carrier. One particularly diagnostic case is a carrier
# shifted up by f13C: the lower sideband then lands on the programmed 1.5 MHz
# line and the upper sideband lands near the previously dominant high-edge line.
carrier_shifted_by_larmor = programmed_carrier + f13c
shifted_freqs_global = [carrier_shifted_by_larmor - f13c, carrier_shifted_by_larmor, carrier_shifted_by_larmor + f13c]

def fit_linear(t: np.ndarray, y: np.ndarray):
    X = np.column_stack([np.ones_like(t), t])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ b
    rss = float(np.sum((y - pred) ** 2))
    return {'rss': rss, 'k': 2, 'coef': [float(x) for x in b], 'pred': pred}

def fit_freqs(t: np.ndarray, y: np.ndarray, freqs: list[float], damp_T: float | None = None):
    cols = [np.ones_like(t), t]
    env = np.ones_like(t) if damp_T is None else np.exp(-t / damp_T)
    for f in freqs:
        w = 2 * np.pi * f * t
        cols += [env * np.cos(w), env * np.sin(w)]
    X = np.column_stack(cols)
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ b
    rss = float(np.sum((y - pred) ** 2))
    amps = []
    phases = []
    for i in range(len(freqs)):
        c = float(b[2 + 2*i])
        s = float(b[3 + 2*i])
        amps.append(float(math.hypot(c, s)))
        phases.append(float(math.atan2(-s, c)))
    return {'rss': rss, 'k': X.shape[1], 'coef': [float(x) for x in b], 'pred': pred,
            'amps': amps, 'phases_rad': phases}

def score(n: int, rss: float, k: int):
    rss = max(float(rss), 1e-300)
    return {
        'aic': float(n * math.log(rss / n) + 2 * k),
        'bic': float(n * math.log(rss / n) + k * math.log(n)),
    }

def add_scores(row: dict, n: int, rss0: float):
    row.update(score(n, row['rss'], row['k']))
    row['delta_rss_vs_linear'] = float(rss0 - row['rss'])
    row['r2_improvement'] = float(max(0.0, (rss0 - row['rss']) / rss0)) if rss0 > 0 else 0.0
    return row

def freqs_for_fc(fc: float, include_carrier: bool = True):
    vals = [fc - f13c]
    if include_carrier:
        vals.append(fc)
    vals.append(fc + f13c)
    return vals

def valid_freqs(freqs: list[float], fmin: float = 0.25e6):
    return all(fmin <= f <= nyquist_hz for f in freqs)

def grid_best_triplet(t: np.ndarray, y: np.ndarray, fc_grid: np.ndarray, *, include_carrier: bool = True, damped: bool = False):
    lin = fit_linear(t, y)
    n = len(t)
    best = None
    best_pred = None
    best_scan = []
    T_grid = np.geomspace(0.35e-6, 80e-6, 90) if damped else [None]
    for fc in fc_grid:
        freqs = freqs_for_fc(float(fc), include_carrier=include_carrier)
        if not valid_freqs(freqs):
            continue
        local_best = None
        local_pred = None
        for T in T_grid:
            m = fit_freqs(t, y, freqs, damp_T=T)
            k_eff = 2 + 2 * len(freqs) + 1 + (1 if damped else 0)  # baseline + amp/phase + fc (+T)
            row = {
                'rss': m['rss'], 'k': k_eff, 'fc_hz': float(fc), 'fc_mhz': float(fc/1e6),
                'carrier_shift_hz': float(fc - programmed_carrier),
                'carrier_shift_mhz': float((fc - programmed_carrier)/1e6),
                'sideband_spacing_hz': float(f13c),
                'freqs_hz': [float(x) for x in freqs],
                'freqs_mhz': [float(x/1e6) for x in freqs],
                'amps': m['amps'], 'phases_rad': m['phases_rad'],
                'damped': bool(damped), 'T2star_us': None if T is None else float(T*1e6),
            }
            add_scores(row, n, lin['rss'])
            if local_best is None or row['rss'] < local_best['rss']:
                local_best = row
                local_pred = m['pred']
        if local_best is not None:
            best_scan.append({k: local_best[k] for k in ['fc_hz','fc_mhz','carrier_shift_hz','carrier_shift_mhz','rss','aic','bic','r2_improvement','amps','T2star_us']})
            if best is None or local_best['rss'] < best['rss']:
                best = local_best
                best_pred = local_pred
    return best, best_pred, best_scan

def grid_best_single(t: np.ndarray, y: np.ndarray, f_grid: np.ndarray, *, damped: bool = False):
    lin = fit_linear(t, y)
    n = len(t)
    best = None
    best_pred = None
    T_grid = np.geomspace(0.35e-6, 80e-6, 90) if damped else [None]
    for f in f_grid:
        if not valid_freqs([float(f)]):
            continue
        for T in T_grid:
            m = fit_freqs(t, y, [float(f)], damp_T=T)
            k_eff = 2 + 2 + 1 + (1 if damped else 0)
            row = {
                'rss': m['rss'], 'k': k_eff, 'freq_hz': float(f), 'freq_mhz': float(f/1e6),
                'amp': m['amps'][0], 'phase_rad': m['phases_rad'][0],
                'damped': bool(damped), 'T2star_us': None if T is None else float(T*1e6),
            }
            add_scores(row, n, lin['rss'])
            if best is None or row['rss'] < best['rss']:
                best = row
                best_pred = m['pred']
    return best, best_pred

def model_table_for_view(t: np.ndarray, y: np.ndarray, include_damped: bool = True):
    lin = fit_linear(t, y)
    n = len(t)
    rows = []
    preds = {'linear': lin['pred']}
    def add(name: str, row: dict, pred):
        row = dict(row)
        row['name'] = name
        rows.append(row)
        preds[name] = pred
    add('linear_baseline_only', add_scores({'rss': lin['rss'], 'k': 2}, n, lin['rss']), lin['pred'])

    # Existing fixed models for comparison.
    fixed_carrier = fit_freqs(t, y, [programmed_carrier])
    add('undamped_fixed_programmed_carrier_1p5MHz', add_scores({
        'rss': fixed_carrier['rss'], 'k': fixed_carrier['k'], 'freqs_hz': [programmed_carrier],
        'freqs_mhz': [programmed_carrier/1e6], 'amps': fixed_carrier['amps']}, n, lin['rss']), fixed_carrier['pred'])
    fixed_trip = fit_freqs(t, y, [low_fixed, programmed_carrier, high_fixed])
    add('undamped_fixed_original_carrier_plus_13C_sidebands', add_scores({
        'rss': fixed_trip['rss'], 'k': fixed_trip['k'], 'freqs_hz': [low_fixed, programmed_carrier, high_fixed],
        'freqs_mhz': [low_fixed/1e6, programmed_carrier/1e6, high_fixed/1e6], 'amps': fixed_trip['amps']}, n, lin['rss']), fixed_trip['pred'])

    # Human-advised shifted-carrier 13C model: diagnostic fixed shift of +f13C.
    shifted_freqs = freqs_for_fc(carrier_shifted_by_larmor, include_carrier=True)
    shifted = fit_freqs(t, y, shifted_freqs)
    add('undamped_shifted_carrier_plus_13C_sidebands_fc_eq_det_plus_f13C', add_scores({
        'rss': shifted['rss'], 'k': shifted['k'], 'fc_hz': carrier_shifted_by_larmor,
        'fc_mhz': carrier_shifted_by_larmor/1e6,
        'carrier_shift_hz': carrier_shifted_by_larmor-programmed_carrier,
        'carrier_shift_mhz': (carrier_shifted_by_larmor-programmed_carrier)/1e6,
        'sideband_spacing_hz': f13c,
        'freqs_hz': shifted_freqs, 'freqs_mhz': [f/1e6 for f in shifted_freqs],
        'amps': shifted['amps'], 'phases_rad': shifted['phases_rad']}, n, lin['rss']), shifted['pred'])

    # Free shifted-carrier search. Coarse then fine for undamped triplet and sideband pair.
    fc_grid = np.arange(1.10e6, min(2.12e6, nyquist_hz - f13c) + 1, 2e3)
    best_trip, pred_trip, scan_trip = grid_best_triplet(t, y, fc_grid, include_carrier=True, damped=False)
    add('undamped_free_shifted_carrier_plus_13C_sidebands', best_trip, pred_trip)
    best_pair, pred_pair, scan_pair = grid_best_triplet(t, y, fc_grid, include_carrier=False, damped=False)
    add('undamped_free_shifted_13C_sideband_pair_no_carrier', best_pair, pred_pair)

    f_grid = np.arange(0.75e6, min(2.31e6, nyquist_hz) + 1, 2e3)
    best_single, pred_single = grid_best_single(t, y, f_grid, damped=False)
    add('undamped_single_free_frequency', best_single, pred_single)
    # Damped grids at lower resolution because they are descriptive with more parameters.
    scan_trip_d = []
    if include_damped:
        f_grid_d = np.arange(0.75e6, min(2.31e6, nyquist_hz) + 1, 10e3)
        best_single_d, pred_single_d = grid_best_single(t, y, f_grid_d, damped=True)
        add('damped_single_free_frequency', best_single_d, pred_single_d)
        fc_grid_d = np.arange(1.10e6, min(2.12e6, nyquist_hz - f13c) + 1, 10e3)
        best_trip_d, pred_trip_d, scan_trip_d = grid_best_triplet(t, y, fc_grid_d, include_carrier=True, damped=True)
        add('damped_free_shifted_carrier_plus_13C_sidebands_common_T2', best_trip_d, pred_trip_d)

    best_bic = min(r['bic'] for r in rows)
    best_aic = min(r['aic'] for r in rows)
    for r in rows:
        r['delta_bic_vs_best'] = float(r['bic'] - best_bic)
        r['delta_aic_vs_best'] = float(r['aic'] - best_aic)
    rows.sort(key=lambda r: r['bic'])
    return rows, preds, {'triplet_scan': scan_trip, 'pair_scan': scan_pair, 'triplet_damped_scan': scan_trip_d}

def summarize_exact_shift(rows: list[dict]):
    by_name = {r['name']: r for r in rows}
    exact = by_name['undamped_shifted_carrier_plus_13C_sidebands_fc_eq_det_plus_f13C']
    free = by_name['undamped_free_shifted_carrier_plus_13C_sidebands']
    single = by_name.get('damped_single_free_frequency') or by_name['undamped_single_free_frequency']
    original = by_name['undamped_fixed_original_carrier_plus_13C_sidebands']
    return {
        'best_model_name': rows[0]['name'],
        'exact_shift_delta_bic_vs_best': exact['delta_bic_vs_best'],
        'exact_shift_r2_improvement': exact['r2_improvement'],
        'exact_shift_freqs_mhz': exact['freqs_mhz'],
        'exact_shift_amps': exact['amps'],
        'free_shifted_triplet_fc_mhz': free['fc_mhz'],
        'free_shifted_triplet_delta_bic_vs_best': free['delta_bic_vs_best'],
        'single_free_delta_bic_vs_best': single['delta_bic_vs_best'],
        'original_fixed_triplet_delta_bic_vs_best': original['delta_bic_vs_best'],
    }

views = {
    'ratio_full': (tau, ratio),
    'signal_over_refline_full': (tau, sig_over_refline),
    'raw_signal_kcps_full': (tau, sig),
    'ratio_skip_first4': (tau[4:], ratio[4:]),
    'signal_over_refline_skip_first4': (tau[4:], sig_over_refline[4:]),
}

results = {}
preds_for_plot = {}
scans_for_plot = {}
for name, (t, y) in views.items():
    rows, preds, scans = model_table_for_view(t, y)
    results[name] = {'n_points': len(t), 'tau_start_us': float(t[0]*1e6), 'tau_stop_us': float(t[-1]*1e6),
                     'model_table_sorted_by_bic': rows, 'summary': summarize_exact_shift(rows)}
    preds_for_plot[name] = preds
    scans_for_plot[name] = scans

# Bootstrap: resample stored averages, fit the free shifted-triplet FC in the ratio and signal/refline views.
rng = np.random.default_rng(20260514)
boot_rows = []
fc_grid_boot = np.arange(1.10e6, min(2.12e6, nyquist_hz - f13c) + 1, 5e3)
for b in range(160):
    idx = rng.integers(0, n_avg, size=n_avg)
    br = ref_each[idx].mean(axis=0)
    bs = sig_each[idx].mean(axis=0)
    bratio = bs / br
    bref_line = np.polyval(np.polyfit(tau, br, 1), tau)
    brefline = bs / bref_line
    row = {'bootstrap_index': b}
    for label, y in [('ratio_full', bratio), ('signal_over_refline_full', brefline)]:
        rows, _, _ = model_table_for_view(tau, y, include_damped=False)
        exact = [r for r in rows if r['name'] == 'undamped_shifted_carrier_plus_13C_sidebands_fc_eq_det_plus_f13C'][0]
        free = [r for r in rows if r['name'] == 'undamped_free_shifted_carrier_plus_13C_sidebands'][0]
        by = {r['name']: r for r in rows}
        single = by.get('damped_single_free_frequency') or by['undamped_single_free_frequency']
        row[f'{label}_best_model'] = rows[0]['name']
        row[f'{label}_exact_shift_delta_bic_vs_best'] = exact['delta_bic_vs_best']
        row[f'{label}_exact_shift_r2'] = exact['r2_improvement']
        row[f'{label}_exact_shift_amps'] = exact['amps']
        row[f'{label}_free_shift_fc_mhz'] = free['fc_mhz']
        row[f'{label}_free_shift_delta_bic_vs_best'] = free['delta_bic_vs_best']
        row[f'{label}_single_delta_bic_vs_best'] = single['delta_bic_vs_best']
    boot_rows.append(row)

def q(vals):
    arr = np.asarray(vals, dtype=float)
    return {'median': float(np.nanmedian(arr)), 'q16': float(np.nanquantile(arr, .16)),
            'q84': float(np.nanquantile(arr, .84)), 'q05': float(np.nanquantile(arr, .05)),
            'q95': float(np.nanquantile(arr, .95)), 'min': float(np.nanmin(arr)), 'max': float(np.nanmax(arr))}
boot_summary = {}
for label in ['ratio_full', 'signal_over_refline_full']:
    boot_summary[f'{label}_free_shift_fc_mhz'] = q([r[f'{label}_free_shift_fc_mhz'] for r in boot_rows])
    boot_summary[f'{label}_exact_shift_delta_bic_vs_best'] = q([r[f'{label}_exact_shift_delta_bic_vs_best'] for r in boot_rows])
    boot_summary[f'{label}_exact_shift_r2'] = q([r[f'{label}_exact_shift_r2'] for r in boot_rows])
    boot_summary[f'{label}_fraction_best_is_exact_shift'] = float(np.mean([r[f'{label}_best_model'] == 'undamped_shifted_carrier_plus_13C_sidebands_fc_eq_det_plus_f13C' for r in boot_rows]))
    boot_summary[f'{label}_fraction_best_is_any_shifted_triplet'] = float(np.mean(['shifted_carrier_plus_13C_sidebands' in r[f'{label}_best_model'] for r in boot_rows]))
    vals = np.asarray([r[f'{label}_free_shift_fc_mhz'] for r in boot_rows])
    hist, edges = np.histogram(vals, bins=np.arange(1.10, 2.13, 0.05))
    boot_summary[f'{label}_free_shift_fc_histogram_0p05MHz_bins'] = {'edges_mhz': [float(x) for x in edges], 'counts': [int(x) for x in hist]}

# Interpretation synthesis. Keep claims scoped: this is bridge-free reanalysis of one Ramsey branch.
ratio_summary = results['ratio_full']['summary']
refline_summary = results['signal_over_refline_full']['summary']
raw_summary = results['raw_signal_kcps_full']['summary']
exact_ratio = [r for r in results['ratio_full']['model_table_sorted_by_bic'] if r['name'] == 'undamped_shifted_carrier_plus_13C_sidebands_fc_eq_det_plus_f13C'][0]
exact_refline = [r for r in results['signal_over_refline_full']['model_table_sorted_by_bic'] if r['name'] == 'undamped_shifted_carrier_plus_13C_sidebands_fc_eq_det_plus_f13C'][0]
exact_raw = [r for r in results['raw_signal_kcps_full']['model_table_sorted_by_bic'] if r['name'] == 'undamped_shifted_carrier_plus_13C_sidebands_fc_eq_det_plus_f13C'][0]

# Decide whether interpretation changes. Criteria are deliberately conservative: the shifted-sideband model must be model-competitive in both normalized views and explain the known frequency pattern.
changed_interpretation = (
    exact_ratio['delta_bic_vs_best'] <= 6.0 and
    exact_refline['delta_bic_vs_best'] <= 6.0 and
    exact_ratio['r2_improvement'] > 0.45 and
    exact_refline['r2_improvement'] > 0.45
)

if changed_interpretation:
    t2 = 'The shifted-carrier/13C-sideband model gives a plausible carrier-shifted Ramsey-frequency interpretation, but it is still not a claim-grade numeric T2star because the model is multi-frequency, BIC competition/normalization dependence remain, and the fitted envelope was not uniquely established.'
    c13 = 'The previous negative 13C wording is too strong. Reanalysis supports a plausible nearby-13C candidate pattern under a residual calibration shift: carrier fc ~= det + f13C (%.6f MHz) with sidebands at %.6f and %.6f MHz, matching the programmed 1.5 MHz line and high-edge %.3f MHz feature. This should be reported as candidate/conditional evidence, not a confirmed coupling claim.' % (carrier_shifted_by_larmor/1e6, (carrier_shifted_by_larmor-f13c)/1e6, (carrier_shifted_by_larmor+f13c)/1e6, (carrier_shifted_by_larmor+f13c)/1e6)
    closeout_action = 'Rewrite closeout report: aligned NV found; numeric T2star remains non-claim-grade; 13C conclusion changes from unsupported/negative to plausible shifted-sideband candidate requiring confirmation if operator wants to continue, with no further measurements in this wake.'
else:
    t2 = 'No claim-grade numeric T2star; shifted-sideband reanalysis does not make the carrier/decay model unique enough to quote T2star.'
    c13 = 'No supported nearby-13C claim; shifted-sideband model was checked but is not competitive/robust enough to revise the negative conclusion.'
    closeout_action = 'Keep closeout report interpretation, optionally append the shifted-sideband check.'

synthesis = {
    'changed_interpretation': bool(changed_interpretation),
    'T2star_conclusion': t2,
    'nearby_13C_conclusion': c13,
    'basis': {
        'programmed_carrier_mhz': programmed_carrier/1e6,
        'f13c_mhz': f13c/1e6,
        'shifted_carrier_det_plus_f13c_mhz': carrier_shifted_by_larmor/1e6,
        'shifted_triplet_freqs_mhz': [float(x/1e6) for x in shifted_freqs_global],
        'ratio_exact_shift_delta_bic_vs_best': exact_ratio['delta_bic_vs_best'],
        'ratio_exact_shift_r2': exact_ratio['r2_improvement'],
        'ratio_exact_shift_amps': exact_ratio['amps'],
        'signal_over_refline_exact_shift_delta_bic_vs_best': exact_refline['delta_bic_vs_best'],
        'signal_over_refline_exact_shift_r2': exact_refline['r2_improvement'],
        'signal_over_refline_exact_shift_amps': exact_refline['amps'],
        'raw_signal_exact_shift_delta_bic_vs_best': exact_raw['delta_bic_vs_best'],
        'raw_signal_exact_shift_r2': exact_raw['r2_improvement'],
        'raw_signal_exact_shift_amps_kcps': exact_raw['amps'],
        'median_signal_sem_kcps': median_signal_sem,
        'bootstrap_summary': boot_summary,
    },
    'advice_respected': 'Bridge-free only; no bridge queue mutation or measurement submission. Stored-average disagreement was used only as uncertainty/provenance, not as the sole rejection criterion.',
    'closeout_action': closeout_action,
}

out = {
    'ok': True,
    'created_at': datetime.now(ZoneInfo('America/New_York')).isoformat(),
    'question': 'Reanalyze terminal refreshed-center Ramsey allowing a residual-calibration shifted carrier and 13C sidebands around that shifted carrier.',
    'project_id': PROJECT.name,
    'terminal_review_path': str(REVIEW_PATH),
    'raw_export_path': review['raw_export_path'],
    'axis_contract_check': 'ExperimentDataEachAvg readout/average axes verified by averaging per-average readouts back to ExperimentData.',
    'human_advice_path': str(PROJECT/'advice/inbox/2026-05-14_resume_bridge_free_shifted_sideband_report.md'),
    'model_definitions': {
        'programmed_carrier_hz': programmed_carrier,
        'f13c_hz': f13c,
        'shifted_carrier_det_plus_f13C_hz': carrier_shifted_by_larmor,
        'shifted_triplet_det_plus_f13C_freqs_hz': shifted_freqs_global,
        'free_shifted_triplet_fc_search_hz': [1.10e6, float(min(2.12e6, nyquist_hz - f13c)), 2e3],
        'nyquist_hz': nyquist_hz,
    },
    'views': results,
    'bootstrap_replicates': len(boot_rows),
    'bootstrap_rows_path': str(AN/f'image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_bootstrap_rows_{TS}.jsonl'),
    'bootstrap_summary': boot_summary,
    'synthesis': synthesis,
}

out_path = AN/f'image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_{TS}.json'
boot_path = AN/f'image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_bootstrap_rows_{TS}.jsonl'
fig_path = FIGS/f'image145844_reimage_r03_ramsey_refreshed_center_shifted_sideband_reanalysis_{TS}.png'

# Figure: model comparison, data+fits, frequency scan, bootstrap fc distribution.
fig, axes = plt.subplots(2, 2, figsize=(14, 10), constrained_layout=True)
ratio_rows = results['ratio_full']['model_table_sorted_by_bic']
axes[0,0].barh([r['name'] for r in reversed(ratio_rows)], [r['delta_bic_vs_best'] for r in reversed(ratio_rows)])
axes[0,0].set_xlabel('Delta BIC vs best')
axes[0,0].set_title('Ratio full-span model comparison')

pred_exact = preds_for_plot['ratio_full']['undamped_shifted_carrier_plus_13C_sidebands_fc_eq_det_plus_f13C']
pred_single = preds_for_plot['ratio_full']['damped_single_free_frequency']
axes[0,1].plot(tau_us, ratio, 'o-', label='ratio data', ms=4)
axes[0,1].plot(tau_us, fit_linear(tau, ratio)['pred'], '--', label='linear baseline', alpha=.8)
axes[0,1].plot(tau_us, pred_exact, '-', label='shifted carrier + 13C triplet', lw=2)
axes[0,1].plot(tau_us, pred_single, ':', label='best single damped freq', lw=2)
for f, lab in zip(shifted_freqs_global, ['low sideband', 'shifted carrier', 'high sideband']):
    axes[0,1].text(0.01, 0.97 - 0.07*['low sideband','shifted carrier','high sideband'].index(lab), f'{lab}: {f/1e6:.3f} MHz', transform=axes[0,1].transAxes, fontsize=8, va='top')
axes[0,1].set_xlabel('tau (us)')
axes[0,1].set_ylabel('signal/reference')
axes[0,1].legend(fontsize=8)
axes[0,1].set_title('Full-span ratio fit')

scan_trip = scans_for_plot['ratio_full']['triplet_scan']
scan_fc = np.array([r['fc_mhz'] for r in scan_trip])
scan_bic = np.array([r['bic'] for r in scan_trip])
axes[1,0].plot(scan_fc, scan_bic - np.nanmin(scan_bic), label='free shifted triplet')
axes[1,0].axvline(programmed_carrier/1e6, color='k', ls='--', label='programmed det')
axes[1,0].axvline(carrier_shifted_by_larmor/1e6, color='C3', ls=':', label='det + f13C')
axes[1,0].set_xlabel('assumed shifted carrier fc (MHz)')
axes[1,0].set_ylabel('Delta BIC within triplet scan')
axes[1,0].set_title('Shifted triplet fc scan (ratio)')
axes[1,0].legend(fontsize=8)

for label, color in [('ratio_full', 'C0'), ('signal_over_refline_full', 'C1')]:
    vals = [r[f'{label}_free_shift_fc_mhz'] for r in boot_rows]
    axes[1,1].hist(vals, bins=np.arange(1.10, 2.13, 0.05), alpha=.55, label=label, color=color)
axes[1,1].axvline(carrier_shifted_by_larmor/1e6, color='C3', ls=':', label='det + f13C')
axes[1,1].set_xlabel('bootstrap free shifted-triplet fc (MHz)')
axes[1,1].set_ylabel('count')
axes[1,1].set_title('Stored-average bootstrap (uncertainty, not sole rejection)')
axes[1,1].legend(fontsize=8)

fig.savefig(fig_path, dpi=150)
out['figure_path'] = str(fig_path)
out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
with boot_path.open('w', encoding='utf-8') as f:
    for row in boot_rows:
        f.write(json.dumps(row, sort_keys=True) + '\n')

print(json.dumps({
    'ok': True,
    'out_path': str(out_path),
    'figure_path': str(fig_path),
    'changed_interpretation': synthesis['changed_interpretation'],
    'T2star_conclusion': synthesis['T2star_conclusion'],
    'nearby_13C_conclusion': synthesis['nearby_13C_conclusion'],
    'ratio_summary': ratio_summary,
    'signal_over_refline_summary': refline_summary,
    'raw_signal_summary': raw_summary,
}, indent=2))
