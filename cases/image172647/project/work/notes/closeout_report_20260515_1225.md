# Closeout report bundle - 2026-05-15 12:25 EDT

Human advice requested: create a LaTeX/PDF closeout report.

Artifacts:
- LaTeX source: `work/reports/closeout_20260515_1225/nv23_image172647_closeout_report_20260515.tex`
- PDF report: `work/reports/closeout_20260515_1225/nv23_image172647_closeout_report_20260515.pdf`
- Copied figure assets: `work/reports/closeout_20260515_1225/figures/`
- Tectonic build log: `work/reports/closeout_20260515_1225/nv23_image172647_closeout_report_20260515.log`

Verification:
- PDF exists: `True`
- PDF size bytes: `1257827`
- PDF header: `%PDF-`

Build note:
- The LaTeX source was created and a normal local OpenClaw Tectonic build was attempted with `latex_report_build.py`.
- Tectonic could not complete because the local font bundle was incomplete and network/DNS fetches for required fonts failed (`lmmonolt10-bold.otf`, later `cmr17.pfb`).
- To satisfy the PDF closeout deliverable in this no-network state, the PDF was rendered from the same extracted report content and copied figures using a Matplotlib/PdfPages fallback. This choice is recorded here per the LaTeX tooling guidance.

Scientific closeout summary:
- Accepted aligned branch: `reimage1804_c02`.
- T2star conclusion: short/few-us order, about 2-3 us but method-sensitive; not a precise scalar.
- 13C conclusion: likely weak/moderate nearby-13C-like signature from det-shift Ramsey plus terminal CPMG N=8 target-region corroboration; no precise coupling extraction.
- No further bridge-touching work is required by default.

Manager summary copies:
- `summaries/nv23_image172647_closeout_report_20260515.tex`
- `summaries/nv23_image172647_closeout_report_20260515.pdf`
