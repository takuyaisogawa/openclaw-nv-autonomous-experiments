# Ramsey/T2star scout autosave avg1 review (2026-05-12 01:39 EDT)

## Question
Does the first saved average from the running c01 Ramsey/T2star scout show useful in-progress signal or any hard reason to intervene?

## Inputs read
- Running bridge status for `nv23_image231924_c01_ramsey_t2star_scout_20260512_012010_image231924_c01_ramsey_t2star_scout_20260512_0118_execute`.
- Autosave MAT: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-12-012318.mat`.
- Raw export: `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_autosave_avg1_raw_export.json`.
- Route/readout-role review and the Ramsey FFT expectation note.

## Action taken
Raw-exported the in-progress savedexperiment after one stored average and generated a compact review/figure using raw readouts, fitted-reference normalization, and FFT on the actual tau grid.

## Result
- Export succeeded; saved data contains 1 stored average, 51 tau points from 0 to 8 us, and `ScanOrderMode = snake` with data saved in tau order.
- Assumed readout roles from route review: readout 1 is the `mS=0` reference, readout 2 is the post-Ramsey signal.
- Raw readout 1 has a slow downward trend across the scan; fitted-reference normalization is therefore the safer plotting/FFT view than point-wise normalization alone.
- The one-average normalized signal is oscillatory enough to justify waiting for terminal 4-average data.
- FFT on the one-average fitted-reference-normalized trace shows power in the expected lower-13C-sideband/carrier region, including bins near 1.59 MHz and 1.96 MHz, but this is not enough for a T2star or 13C claim.

## Checks actually performed
- Confirmed the autosave MAT exists before export.
- Confirmed export `ok=true` with no warnings.
- Confirmed current bridge control has no stop request and monitor has no last error in the latest status check.

## Remaining uncertainty
- This is one stored average only while the bridge job is still running; average-to-average stability and final SNR are unknown.
- No T2star fit or 13C conclusion should be made from this in-progress autosave.

## Next pointer
Leave the bridge job running. On terminal completion, raw-export the final savedexperiment, redo the raw/readout-aware FFT analysis across all saved averages, then decide separately whether T2star and 13C are supported or whether a redesigned Ramsey repeat is needed.

## Artifacts
- `work/artifacts/analysis/image231924_c01_ramsey_t2star_scout_autosave_avg1_review.json`
- `work/artifacts/figures/image231924_c01_ramsey_t2star_scout_autosave_avg1_review.png`
- `work/artifacts/figures/image231924_c01_ramsey_t2star_scout_autosave_avg1_raw_readouts.png`
