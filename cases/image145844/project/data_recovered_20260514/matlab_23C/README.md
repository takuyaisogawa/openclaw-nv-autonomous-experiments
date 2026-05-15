# Recovered MATLAB Data Snapshot

This snapshot adds raw MATLAB `.mat` files referenced by the `image145844`
case artifacts that were not present in the cold-archive project copy.

Included:

- `savedexperiments/NV1/`: 12 `1DExp-...mat` savedexperiment files for pODMR
  and Ramsey analyses.
- `SavedImages/`: 1 `3DXYZ-Image-2026-05-13-145844.mat` imaging scan.
- `RECOVERED_MAT_FILES.csv`: public-path and source-relative manifest.

The case records also mention several `nv23_...mat` or job-named `.mat`
strings. Those were not found as source raw files in the checked
`23-C/savedexperiments/NV1` or `23-C/SavedImages` source locations and appear
to be generated job/intent artifact names rather than the raw MATLAB data
inputs needed for analysis replay.
