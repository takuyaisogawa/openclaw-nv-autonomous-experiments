# Recovered MATLAB Data Snapshot

This snapshot adds raw MATLAB `.mat` files referenced by the `image172647`
case artifacts that were not embedded in the sanitized project-folder copy.

Included:

- `SavedImages/`: the initial saved image used to start the project.
- `nv_bridge/status/openclaw_imaging/`: the fresh re-image MAT file produced
  after the stale initial candidate failure.
- `nv_bridge/status/openclaw_imaging_exports/`: MATLAB export files used by the
  candidate-selection artifacts.
- `savedexperiments/NV1/`: eight `1DExp-...mat` savedexperiment files for pODMR,
  Ramsey, and CPMG analyses.
- `RECOVERED_MAT_FILES.csv`: public-path and source-relative manifest.

The case records may mention job/intent artifact names in addition to these
raw data files. The files here are the recovered MATLAB data inputs needed for
case audit and analysis replay.
