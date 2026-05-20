Case podmr_038_2026-05-16-214551

Sequence and readout roles:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML has full_expt = 0, so the conditional "1 level reference" block is inactive.
- The executed readouts are therefore:
  1. readout 1: after adj_polarize and detection, a bright m_S = 0 reference.
  2. readout 2: after one rabi_pulse_mod_wait_time and detection, the signal readout.
- The active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.
- mod_depth = 1.

Quantitative expected-signal model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1 and approximately linear scaling with mod_depth, the active pulse has f_R = 10 MHz.
- For a resonant two-level Rabi drive, the transferred population is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce the signal readout relative to the bright reference by 0.22 * 0.996 = 0.219, or about 21.9%.
- Using the measured readout 1 mean of 46.568 counts, the expected resonant signal readout is 46.568 * (1 - 0.219) = 36.36 counts, a drop of about 10.20 counts from the bright reference.

Measured comparison:
- readout 1 mean = 46.568 counts, standard deviation across scan points = 1.000 counts.
- readout 2 mean = 46.231 counts, standard deviation across scan points = 1.141 counts.
- readout2/readout1 ratio mean = 0.993, standard deviation = 0.025, minimum = 0.940.
- readout2 - readout1 mean = -0.337 counts, standard deviation = 1.168 counts, minimum = -2.788 counts.
- The deepest measured signal/reference reduction is about 6.0%, far smaller than the about 21.9% reduction expected from the active 52 ns, mod_depth 1 resonant pulse.
- A true resonance would require a localized dip near the expected signal level of about 36 counts, or at least a drop of order 10 counts. No point approaches that scale; the observed variations are at the 1-3 count level and are comparable to tracking/noise fluctuations. The two stored averages should not be treated as a strong independent repeatability test.

Decision:
The active sequence should produce a large pODMR dip if the swept microwave frequency hits resonance, but the measured signal readout remains essentially equal to the bright reference throughout the sweep. I therefore decide that a pODMR resonance is absent.
