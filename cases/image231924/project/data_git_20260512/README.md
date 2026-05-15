# Data snapshot for nv23_aligned_nv_t2star_13c_image231924_20260511_2319

This directory is a self-contained git snapshot of the completed OpenClaw NV project and the lab data/config files used by the run.

- `matlab_23C/` contains copied files from the MATLAB 23-C tree, including the source SavedImage, saved experiment MAT files, sequence XML, and sequence manifests referenced by the project.
- `nv_bridge/` contains copied bridge job directories from `<NV_BRIDGE_ROOT>` for this project.
- `MANIFEST.json` records source paths, snapshot paths, sizes, and SHA-256 hashes.
- `FILES.tsv` is a tabular version of the copied-file manifest.

The original MATLAB data directories are ignored by the MATLAB repository's `.gitignore`; this snapshot preserves the exact files inside the OpenClaw project so the project can be committed without staging unrelated MATLAB repo state.
