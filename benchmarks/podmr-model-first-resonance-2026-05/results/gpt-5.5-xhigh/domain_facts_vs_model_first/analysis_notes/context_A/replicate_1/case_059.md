Case podmr_045_2026-05-16-234216

Sequence interpretation:
- The provided sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional m_S=+1 reference block is inactive. The do_adiabatic_inversion flag is not used in the active branch.
- The two active detections are therefore:
  1. readout 1: true m_S=0 fluorescence reference after optical polarization.
  2. readout 2: fluorescence after the modulated Rabi microwave pulse.
- The active microwave pulse is length_rabi_pulse = 52 ns with mod_depth = 1.

Expected scale:
- With the supplied setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency. A 52 ns pulse is close to a pi pulse.
- If the swept microwave frequency hits a real pODMR resonance, the post-pulse readout should show a substantial fluorescence reduction relative to the m_S=0 reference, with an available contrast scale of roughly 22% for m_S=0 versus m_S=+1.

Observed data:
- Combined mean readout 1 is about 48.85 and combined mean readout 2 is about 48.77.
- The mean signal-reference difference is only about -0.08 counts, and the pointwise readout-2/readout-1 ratio ranges from about 0.964 to 1.051.
- The largest signal deficit is about 3.6%, far smaller than the expected near-pi-pulse contrast. Other frequencies show positive excursions of similar or larger size, including the high-frequency end.
- The per-average overlay is dominated by average-to-average offset/drift, consistent with tracking cadence rather than an independent repeatability check. It does not show a stable resonant dip in the post-pulse readout.

Decision:
No convincing pODMR resonance is present in this scan.
