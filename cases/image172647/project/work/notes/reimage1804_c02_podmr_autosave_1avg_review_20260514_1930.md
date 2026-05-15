# reimage1804_c02 pODMR first autosave review

Created: 2026-05-14T19:32:30-04:00

Bridge job: `nv23_pulsed_odmr_rabimodulated_v1_20260514_191847_reimage1804_c02_strong_podmr`

## Status

- Job is still running/nonterminal; no bridge queue mutation was performed.
- One saved average was available from autosave `2026-05-14-192106`.
- This review is provisional only. The requested job is 4 averages x 50000 reps; wait for terminal 4-average review before claiming alignment or starting Ramsey/T2star/13C work.

## Readout roles

`Rabimodulated.xml` with `full_expt=0`: readout 1 is the mS=0 reference; readout 2 is the signal after `length_rabi_pulse`.

## First-average observation

The exported first average shows a signal-only depression centered at about 3.875000 GHz:

- signal minimum: 37.923 kcps
- linear off-resonant signal baseline at the minimum: 49.465 kcps
- raw signal depression: 23.3%
- fitted-reference ratio depression: 23.4%
- pointwise signal/reference ratio depression: 23.5%
- reference depression at the signal minimum: -0.6% (reference is not depressed)
- expected strong-pi contrast reference: about 22%

## Interpretation

This is encouraging because the effect is near the expected resonance and has the expected contrast scale, while the reference readout does not show a matching dip. However, it is one running autosave average only. Keep the current verdict as `promising but nonterminal`; the next decision must be based on the terminal 4-average raw/readout-aware review.

## Artifacts

- Raw export: `work/artifacts/analysis/reimage1804_c02_podmr_autosave_raw_1avg_20260514_1930.json`
- Summary: `work/artifacts/analysis/reimage1804_c02_podmr_autosave_1avg_summary_20260514_1930.json`
- Figure: `work/artifacts/figures/reimage1804_c02_podmr_autosave_1avg_20260514_1930.png`
