Case podmr_036_2026-05-16-211536

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName/active XML: Rabimodulated.xml.
- The instructions first call adj_polarize, then detection. This is the true m_S = 0 optical reference readout.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second readout is the pODMR signal after the microwave pulse.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the microwave-pulsed signal readout.

Relevant pulse parameters:
- scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this already corresponds to exactly 13 samples, so no rounding change is introduced.
- mod_depth = 1.
- full_expt = 0, so no independent m_S = 1 reference is acquired.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1 is about 10 MHz, the resonant transition probability for a square pulse is
  P_excited = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns:
  P_excited = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given the current setup contrast between m_S = 0 and m_S = +1 is about 22%, a resonant point should reduce the signal readout by approximately
  0.22 * 0.996 = 0.219 of the m_S = 0 optical level.
- The measured readout 1 mean is 50.99 counts, so the expected resonant dip is about
  50.99 * 0.219 = 11.17 counts.

Data comparison:
- Combined readout 1 mean = 50.99 counts, standard deviation across scan points = 0.81 counts.
- Combined readout 2 mean = 50.48 counts, standard deviation across scan points = 0.93 counts.
- Signal-reference difference, readout2 - readout1: mean = -0.51 counts, standard deviation = 1.36 counts.
- The largest combined drop is at 3.920 GHz: readout1 = 51.69, readout2 = 48.90, difference = -2.79 counts, only 5.5% of the reference level.
- This is far smaller than the expected approximately 11.2-count, 21.9% resonant dip for the active 52 ns, mod_depth 1 pulse.
- Per-average minima do not give a strong independent repeatability check here because averages can reflect tracking cadence; nevertheless they are not aligned in frequency: average 1 minimum is at 3.920 GHz, average 2 minimum is at 3.845 GHz.

Decision:
The active pulse should produce a large pODMR contrast if it hits resonance, but the observed readout differences are small, noisy, and not consistent with the expected resonant signal. I decide that a pODMR resonance is absent.
