Case: podmr_029_2026-05-16-193002

Input basis used:
- Used only inputs/sequence.xml and inputs/raw_export.json in this isolated workspace.
- The active sequence is Rabimodulated.xml / Rabi-modulated pODMR with vary_prop = mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence interpretation:
- The instructions first polarize and detect: this is the true m_S = 0 / bright reference readout, corresponding to readout 1 in the two stored readouts.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive. There is no independent m_S = +1 reference in this scan.
- The active spectroscopy operation is one rabi_pulse_mod_wait_time pulse followed by detection, corresponding to readout 2.
- From inputs/sequence.xml, length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1. The raw export also contains an embedded older-looking sequence string with mod_depth = 0.3, but the provided sequence XML and Variable_values report mod_depth = 1, so I used mod_depth = 1 for the decision.

Expected signal model:
- Given the stated setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant transition probability for a square pulse is
  P = sin^2(pi * f_R * t).
- With t = 52 ns and f_R = 10 MHz:
  P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant post-pulse fluorescence reduction is
  0.22 * 0.996 = 0.219, or about 21.9% of the bright reference.
- The readout level is about 45 counts, so an on-resonance dip should be approximately
  45 * 0.219 = 9.9 counts in readout2 relative to readout1.
- Even if the conflicting embedded mod_depth = 0.3 were used, the model would give P = sin^2(pi * 3e6 * 52e-9) = 0.222 and an expected dip of about 2.2 counts.

Observed quantitative comparison:
- Mean readout 1 = 44.929 counts.
- Mean readout 2 = 44.908 counts.
- Mean(readout2 - readout1) = -0.021 counts.
- Standard deviation of readout2 - readout1 across scan points = 1.273 counts.
- The most negative point is at 3.855 GHz, where readout2 - readout1 = -2.558 counts, about -5.6% of readout1.
- Around the nominal high-frequency end and across the scan, there is no localized dip remotely close to the approximately -9.9 count expected pi-pulse response for mod_depth = 1.
- The small negative excursions are comparable to point-to-point scatter and are not a strong independent repeatability test because the two stored averages can reflect tracking cadence.

Decision:
The physically expected resonant contrast for the active 52 ns, mod_depth = 1 pulse is large, but the measured post-pulse readout does not show a corresponding localized reduction relative to the 0-reference. I therefore decide resonance_absent.
