Case podmr_054_2026-05-17-043636

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual check of the exported arrays

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions polarize the NV, take a first detection, wait, then apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then take a second detection.
- full_expt is 0, so the conditional "Acquire 1 level reference" block is inactive.
- Therefore readout 1 is the laser-polarized m_S = 0 reference readout with no preceding MW pulse, and readout 2 is the signal readout after the Rabi-modulated MW pulse.
- The relevant active pulse duration is length_rabi_pulse = 52 ns. The exported active Variable_values list reports mod_depth = 1. The embedded sequence text contains a stale-looking default mod_depth = 0.3, but the provided sequence XML and exported Variable_values both indicate the run value is mod_depth = 1.

Quantitative physical model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, with linear scaling, the on-resonance transition probability for a square pulse is:
  P = sin^2(pi * f_R * t)
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected signal/readout-reference ratio at resonance is:
  ratio_expected = 1 - 0.22 * P = 0.7809.
- For a raw baseline near 42.5 counts, this corresponds to an expected on-resonance signal drop of about 9.31 counts in readout 2 relative to the m_S = 0 reference scale.

Observed data check:
- The combined readout 2 / readout 1 ratios across the scan have mean 0.9945 and sample standard deviation 0.0276.
- The minimum observed ratio is 0.9468 at 3.840 GHz, a 5.3% dip, corresponding to only about 2.33 counts below readout 1 at that point.
- Near the high-frequency end where an NV transition might plausibly appear in this scan, the ratios remain close to 1.0: 3.905 GHz = 0.9834, 3.910 GHz = 1.0065, 3.915 GHz = 1.0032, 3.920 GHz = 1.0042, 3.925 GHz = 0.9991.
- Stored per-average traces show substantial baseline/tracking drift, consistent with the warning that stored averages mostly reflect tracking cadence rather than independent repeatability.

Decision:
The expected on-resonance signature for the active 52 ns, mod_depth 1 pulse is an approximately 22% drop in the signal readout. The observed data show only small few-percent fluctuations and no frequency-localized feature with the expected amplitude. I therefore decide that a pODMR resonance is absent.
