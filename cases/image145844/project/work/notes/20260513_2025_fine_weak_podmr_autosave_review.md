# Fine weak-pi pODMR autosave review (3/4 averages)

Question: while the fine weak-pi pODMR is still running, is there useful bridge-free evidence for the likely refined center before deciding the next Ramsey design?

Inputs read:
- Bridge running status: `<NV_BRIDGE_ROOT>/running/nv23_pulsed_odmr_rabimodulated_v1_20260513_195437_pulsed_odmr_rabimodulated_v1/status.json`
- Autosave raw export: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-Rabimodulated-vary-mw_freq-2026-05-13-195452.mat` via `tools_mat_parse.py --pretty`
- Running job contract: `<NV_BRIDGE_ROOT>/running/nv23_pulsed_odmr_rabimodulated_v1_20260513_195437_pulsed_odmr_rabimodulated_v1/job.json`
- Sequence XML: `<MATLAB_23C_ROOT>/SavedSequences/SavedSequences-AWG/Rabimodulated.xml`

Action taken:
- Reviewed the in-progress autosave only; did not mutate or stop the bridge queue.
- Confirmed `Rabimodulated.xml` with `full_expt=0` has readout1 as the mS=0 reference detection and readout2 as the post-rabi-pulse signal.
- Compared raw signal, point-wise signal/reference, fitted-reference-line normalization, and per-average signal minima.

Result:
- Status at review: `None`, `None`, `None`.
- Savedexperiment contains 3 of None planned averages.
- Combined raw signal minimum: 3875900000 Hz (-0.100 MHz from 3.876 GHz), drop 13.3% vs edge median.
- Fitted-reference-line-normalized minimum: 3875900000 Hz (-0.100 MHz), drop 13.1% vs edge median.
- Completed-average raw minima are [3876000000, 3875900000, 3875900000] Hz, i.e. offsets [0.0, -0.1, -0.1] MHz.

Checks actually performed:
- Raw/readout-aware data extraction succeeded with no parser warnings.
- Sequence readout role was checked from active XML instructions.
- No queue mutation was performed while the bridge job is running.

Remaining uncertainty:
- This is not terminal evidence. The fourth average and scan-order-aware drift review are still required before selecting a final refined `mw_freq_hz` or designing the next Ramsey.
- Point-wise ratio has denominator-sensitive minima, so raw signal and fitted-reference-line normalization should dominate the terminal center decision.

Next pointer:
- Wait for terminal fine-pODMR result. Then copy terminal job/result/status/batch state into `work/bridge_jobs/`, complete intent `image145844_reimage_r03_fine_weak_podmr_20260513_1950`, rerun raw export plus drift review, and only then choose the next Ramsey settings.

Artifacts:
- `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/analysis/image145844_reimage_r03_fine_weak_podmr_autosave_review_20260513_2025.json`
- `<OPENCLAW_WORKSPACE>/.openclaw/projects/nv23_aligned_nv_t2star_13c_image145844_20260513_1507/work/artifacts/figures/image145844_reimage_r03_fine_weak_podmr_autosave_review_20260513_2025.png`
