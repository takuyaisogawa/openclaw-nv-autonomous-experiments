# Second Ramsey in-progress autosave sanity review

Question: while the det=1.0 MHz Ramsey follow-up is running, is there any hard anomaly or useful preliminary evidence to record before terminal review?

Inputs read:
- Live bridge status for `nv23_ramsey_20260513_204925_image145844_reimage_r03_ramsey_det1p0_8us_8avg`.
- In-progress savedexperiment autosave: `<MATLAB_23C_ROOT>/savedexperiments/NV1/1DExp-seq-ramsey-vary-tau-2026-05-13-204940.mat`.
- Raw export: `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_autosave_raw_export_20260513_2124.json`.
- Prior model/protocol plan: `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_8avg_model_plan_20260513_2042.json`.
- NV research memory `Shot Budget And Data Quality` / `OpenClaw Project Operation` notes on running autosave and non-terminal data.

Action taken:
- Confirmed the bridge job is still running, with monitor `last_error` empty and no stop requested.
- Copied the live status and batch state into `work/bridge_jobs/`.
- Raw-exported the current autosave MAT. The export contains 3 completed averages out of 8 planned averages. This also confirms the known autosave behavior: status may report `autosave_target_exists=false` because the status path omits `.mat`, while the actual MAT exists.
- Made a preliminary raw/readout and frequency-screen artifact plus figure:
  - `work/artifacts/analysis/image145844_reimage_r03_ramsey_det1p0_8us_autosave_review_20260513_2124.json`
  - `work/artifacts/figures/image145844_reimage_r03_ramsey_det1p0_8us_autosave_review_20260513_2124.png`
- Marked the earlier 21:18 autosave review JSON as superseded because the 2-average array shape was ambiguous (`[1,2,2,41]`); the 3-average export resolves `ExperimentDataEachAvg` as `[slice, average, readout, point]`.

Result:
- Status copy at review time: running, message `(3/8) averages completed for 1 scans`, final-count text `Final = 43.331 kcps`.
- Autosave export: 3/8 averages, 41 tau points from 0 to 8 us, 50000 repetitions per average, 150000/400000 planned shots per tau point.
- Raw means in the 3-average autosave: reference 48.79 kcps, Ramsey signal 44.36 kcps, signal/reference mean 0.909.
- Stored average signal means drift downward over the first three averages (48.44, 43.44, 41.20 kcps), but counts remain in the expected range and this is not by itself a hard anomaly or stop condition.
- Preliminary frequency screen on the combined ratio is not claim-grade: top least-squares component is around 0.448 MHz with amplitude about 0.0227 ratio; target amplitudes are about 0.0095 at 1.0 MHz, 0.0072 at 0.615 MHz, 0.0047 at 1.385 MHz, and 0.0067 at the prior 0.884 MHz component.

Checks actually performed:
- `tools_mat_parse.py --pretty` raw export completed successfully on the in-progress MAT.
- Python analysis generated JSON and PNG artifacts and verified the resolved per-average/readout axis order from the 3-average export.
- Live status and batch state were copied, but the bridge queue was not mutated.

Remaining uncertainty:
- This is only an in-progress autosave snapshot with 37.5% of the planned shot budget. It must not support T2star or 13C claims.
- The preliminary downward average-to-average signal/reference trend needs terminal drift/readout review; do not stop for it alone under the running-autosave and drift guidance.

Next pointer:
- Continue waiting for terminal completion of the running Ramsey job. On terminal, copy job/result/status/control and batch state, complete intent `image145844_reimage_r03_ramsey_det1p0_8us_8avg_20260513_2042`, raw-export the final savedexperiment, run scan-order-aware drift, and perform the planned raw/readout + FFT/least-squares + fit-after-signal review before any T2star or 13C claim.
