# reimage1804_c01 terminal pODMR review: reject for alignment branch

Created: 2026-05-14T19:00:00-04:00

## Terminal bridge result

- Job: `nv23_pulsed_odmr_rabimodulated_v1_20260514_182054_pulsed_odmr_rabimodulated_v1`
- Status: completed, finished 2026-05-14T18:58:55
- Savedexperiment: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-14-182326.mat`
- In-run alignment count: 39.053 kcps; post-run final count: 39.612 kcps
- Acquisition: 31 mw_freq points from 3.825 to 3.925 GHz, 4 averages x 50000 reps

## Readout roles

`Rabimodulated.xml` with `full_expt=0` uses readout 1 as the mS=0 reference and readout 2 as the signal after the 52 ns, mod_depth=1 pulse. The terminal raw export preserves `ScanOrderMode=snake`; data are saved in frequency order with per-average acquisition order recorded.

## Expected signal

The pre-enqueue model expected a strong-pi resonant dip of about 22% over a sinc-like width around 15.4 MHz. The scan spacing was 3.3 MHz, so a usable in-window resonance should be visible across multiple frequency points in raw/readout-aware views.

## Observed terminal data

- Raw signal max depression vs high-percentile signal baseline: 4.4% at 3.848333 GHz.
- Pointwise signal/reference max depression: 8.3% at 3.838333 GHz.
- Signal divided by fitted reference max depression: 5.1% at 3.848333 GHz.
- These are far below the expected ~22% strong-pi contrast. Normalization-only/weak features are not enough to claim a usable resonance.

## Verdict

Reject `reimage1804_c01` for the magnetic-field-aligned NV search branch because terminal strong-pi pODMR completed but did not show a clear usable resonance. This is a resonance/alignment-screen rejection, not a tracking failure; counts stayed healthy.

## Next step

Move to fallback candidate `reimage1804_c02` from the fresh re-image ranking, starting with standalone TrackCenter before any pODMR.

Artifact summary: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/analysis/reimage1804_c01_podmr_terminal_summary_4avg_20260514_1859.json`
Figure: `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image172647_20260514_1728/work/artifacts/figures/reimage1804_c01_podmr_terminal_4avg_20260514_1859.png`
