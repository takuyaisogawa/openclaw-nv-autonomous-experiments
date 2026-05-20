Case podmr_050_2026-05-17-005655

Inputs used:
- sequence XML from inputs/sequence.xml and the saved sequence/variables in inputs/raw_export.json.
- raw readouts from inputs/raw_export.json.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active detections are therefore:
  1. readout 1: true m_S = 0 fluorescence reference after optical polarization.
  2. readout 2: fluorescence after one rabi_pulse_mod_wait_time pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns after sample-rate rounding.

Explicit signal model:
- Given setup Rabi frequency f_Rabi = 10 MHz at mod_depth = 1, scaling linearly with mod_depth, the active pulse has f_Rabi = 10 MHz.
- For a resonant two-level Rabi pulse starting in m_S = 0, transferred population to m_S = +1 is
  P1 = sin^2(pi * f_Rabi * t).
- With t = 52 ns:
  P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance readout-2/readout-1 ratio should be
  1 - 0.22 * P1 = 0.7809.
- The measured readout-1 mean is 53.2866 raw units, so the expected on-resonance drop is
  53.2866 * (1 - 0.7809) = 11.68 raw units.

Observed data:
- Mean readout 1 = 53.2866.
- Mean readout 2 = 52.9295.
- Mean difference readout2 - readout1 = -0.3571 raw units.
- Mean readout2/readout1 ratio = 0.9936.
- The lowest readout2/readout1 ratio occurs at 3.865 GHz:
  readout 1 = 55.5769, readout 2 = 52.1538, difference = -3.4231 raw units, ratio = 0.9384.

Decision:
- The expected resonant signal for the active pulse is a near-pi-pulse contrast dip of about 11.7 raw units, or a ratio near 0.781.
- The observed scan shows only small fluctuations around equal readouts. The largest apparent dip is far smaller than the model expectation and the stored averages are not a strong independent repeatability test because they can reflect tracking cadence.
- I therefore decide that a pODMR resonance is absent in this scan.
