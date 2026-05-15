# MATLAB

Public MATLAB subset for inspecting data export and analysis used in the case
studies.

- `analysis/`: savedexperiment export, savedexperiment summary, saved scan
  analysis, and image-axis normalization.
- `manifests/`: case-relevant sequence manifests.
- `sequences/`: sequence XML files referenced by the public manifests and case
  records.

Live hardware execution and the MATLAB lab backend source are not included in
this release. Instrument control and live bridge queue mutation are outside the
public execution surface.
