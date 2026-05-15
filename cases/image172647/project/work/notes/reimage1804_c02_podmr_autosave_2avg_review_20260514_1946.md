# reimage1804_c02 pODMR second autosave review

Created: 2026-05-14T19:46:30-04:00

Bridge job: `nv23_pulsed_odmr_rabimodulated_v1_20260514_191847_reimage1804_c02_strong_podmr`

## Status

- Job is still running/nonterminal; no bridge queue mutation was performed.
- Status snapshot at 2026-05-14T19:46 EDT showed `(2/4) averages completed`, final count text `Final = 39.971 kcps`, and no monitor/control/stop anomaly.
- Two saved averages were raw-exported from autosave `2026-05-14-192106`.
- This remains provisional. The requested job is 4 averages x 50000 reps; terminal 4-average raw/readout-aware review is required before alignment, Ramsey/T2star, or 13C claims.

## Readout roles

`Rabimodulated.xml` with `full_expt=0`: readout 1 is the mS=0 reference; readout 2 is the signal after `length_rabi_pulse`.

## Two-average observation

The two-average mean still has its signal minimum at 3.875000 GHz:

- signal minimum: 40.192 kcps
- linear off-resonant signal baseline at the minimum: 47.673 kcps
- raw signal depression: 15.7%
- fitted-reference ratio depression: 16.1%
- pointwise signal/reference ratio depression: 16.1%
- reference depression at the signal minimum: -0.6% (reference is not depressed)
- expected strong-pi contrast reference: about 22%

Per-average check at 3.875 GHz:

- avg 1: about 23.2% raw signal depression, consistent with the earlier promising one-average review.
- avg 2: about 7.7% raw signal depression at 3.875 GHz; its lowest signal point is elsewhere and looks noisy/provisional.

## Interpretation

This is still encouraging enough to keep waiting: the mean dip is signal-only, centered near the expected ms=+1 resonance, and the reference readout is not depressed. However, the two-average depth is now weaker than the expected ~22% strong-pi contrast because average 2 is less clear. Do not claim magnetic-field alignment from this autosave. The terminal 4-average review must decide whether the resonance is clear and usable.

## Artifacts

- Raw export: `work/artifacts/analysis/reimage1804_c02_podmr_autosave_raw_2avg_20260514_1943.json`
- Summary: `work/artifacts/analysis/reimage1804_c02_podmr_autosave_2avg_summary_20260514_1943.json`
- Figure: `work/artifacts/figures/reimage1804_c02_podmr_autosave_2avg_20260514_1943.png`
- Status snapshot: `work/artifacts/bridge_results/reimage1804_c02_strong_podmr_running_status_20260514_1946.json`
