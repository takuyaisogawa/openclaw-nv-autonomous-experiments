Case: podmr_078_2026-05-17-102220

Inputs used:
- Sequence: exported executed sequence in inputs/raw_export.json, SequenceName Rabimodulated.xml.
- Standalone inputs/sequence.xml is consistent in sequence structure, but the exported sequence records the run-specific values.

Active pulse sequence and readout roles:
- Active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference branch is inactive.
- The actual readout pair is therefore:
  1. readout 1: true m_S = 0 reference after optical polarization.
  2. readout 2: signal readout after a modulated microwave Rabi pulse.
- The microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Explicit physical model calculation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- Pulse duration t = 52 ns.
- On resonance, the driven population transfer is P_flip = sin^2(pi f_R t).
- P_flip = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Setup contrast between m_S = 0 and m_S = +1 is about 22%, so expected fractional fluorescence reduction on resonance is 0.22 * 0.996 = 0.219, about 21.9%.
- The pre-drop raw baseline is about 52.16 for readout 1 and 52.35 for readout 2, so the expected on-resonance signal scale is about 11.4 raw-readout units.

Observed data check:
- Combined readout 2 spans 49.5 to 53.73 raw units, a total range of only 4.23 units.
- Comparing the first 15 points to the last 6 points gives a readout 2 reduction of about 2.07 units, or about 4.0% of baseline.
- Readout 1, which is the polarized reference and should not carry the microwave resonance, also shifts downward by about 1.16 units over the same region.
- Stored averages show only two averages, and these likely reflect tracking cadence rather than a strong independent repeatability test.

Decision:
- A real resonance under this pulse condition should be a near-pi-pulse effect with an expected raw suppression around 11 counts.
- The observed variation is much smaller, broad/drifty, and partially shared by the reference readout.
- Therefore I decide resonance_absent.
