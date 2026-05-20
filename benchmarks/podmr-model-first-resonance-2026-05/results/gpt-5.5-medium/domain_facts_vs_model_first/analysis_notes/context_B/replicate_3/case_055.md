Case: podmr_041_2026-05-16-224136

Sequence/readout identification:
- Active sequence: Rabimodulated.xml / Rabimodulated scan varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction flow first runs adj_polarize followed by detection: this is readout 1, the true m_S = 0 optical reference.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) followed by detection: this is readout 2, the MW-pulsed pODMR signal.
- Active pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- Active mod_depth: 1 from the provided sequence XML and exported Variable_values.

Quantitative expected signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling, f_R = 10 MHz here.
- For a resonant square pulse, transition probability P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pi-like pulse should reduce the pulsed readout by about 0.22 * 0.996 = 21.9% relative to the m_S = 0 reference.
- Around the observed readout level of about 46 counts, this corresponds to an expected drop of about 10.1 counts, giving an on-resonance readout 2 near 35.9 counts if the transition is driven.

Observed data check:
- Combined readout 1 mean = 46.35 counts, readout 2 mean = 46.14 counts.
- The largest combined readout2 - readout1 drop is at 3.895 GHz: -2.60 counts, only 5.6% of readout 1.
- The combined ratio readout2/readout1 ranges from 0.944 to 1.048 with standard deviation about 0.030, so the deepest dip is a small fluctuation on this noisy scale rather than the modeled 0.781 ratio expected for a resonant pi-like pODMR response.
- The stored per-average traces have large baseline shifts consistent with tracking cadence; they do not supply a strong independent repeatability test. One average has its strongest ratio dip at 3.830 GHz, while the other has it at 3.895 GHz.

Decision:
The active pulse should produce a large, roughly 22% optical contrast drop on resonance, but the observed scan shows only shallow, inconsistent few-percent excursions. I therefore decide that a pODMR resonance is absent in this data.
