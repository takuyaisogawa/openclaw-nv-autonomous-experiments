# reimage1804_c02 pODMR third autosave review

Created: 2026-05-14T19:50:00-04:00

Bridge job: `nv23_pulsed_odmr_rabimodulated_v1_20260514_191847_reimage1804_c02_strong_podmr`

## Status

- Job is still running/nonterminal; no bridge queue mutation was performed.
- Status had advanced to `(3/4) averages completed` with no monitor/control/stop anomaly.
- Three saved averages were raw-exported from autosave `2026-05-14-192106`.
- This is an odd intermediate autosave under snake scan order, so it is useful provenance but not a final balanced verdict. The planned job uses 4 averages.

## Three-average observation

The three-average mean still has its signal minimum at 3.875000 GHz:

- signal minimum: 41.795 kcps
- raw signal depression vs linear off-resonant signal baseline: 13.5%
- fitted-reference ratio depression: 13.9%
- reference depression at the signal minimum: -2.0% (reference is not depressed)
- expected strong-pi contrast reference: about 22%

Per-average check at/near 3.875 GHz:

- avg 1: strong ~23% raw signal depression at 3.875 GHz.
- avg 2: weaker ~7.7% raw signal depression at 3.875 GHz, with a noisy lower point elsewhere.
- avg 3: signal minimum is near 3.878 GHz; at exactly 3.875 GHz the depression is about 9.3%.

## Interpretation

The feature remains signal-only and near the expected ms=+1 resonance, but the running mean has weakened from the one-average view and is below the expected ~22% strong-pi contrast. Keep the verdict provisional. The terminal 4-average review must decide whether this is a clear usable resonance or not; do not claim magnetic-field alignment or start Ramsey/T2star/13C from this autosave.

## Artifacts

- Raw export: `work/artifacts/analysis/reimage1804_c02_podmr_autosave_raw_3avg_20260514_1949.json`
- Summary: `work/artifacts/analysis/reimage1804_c02_podmr_autosave_3avg_summary_20260514_1949.json`
- Figure: `work/artifacts/figures/reimage1804_c02_podmr_autosave_3avg_20260514_1949.png`
- Status snapshot: `work/artifacts/bridge_results/reimage1804_c02_strong_podmr_running_status_20260514_1950.json`
