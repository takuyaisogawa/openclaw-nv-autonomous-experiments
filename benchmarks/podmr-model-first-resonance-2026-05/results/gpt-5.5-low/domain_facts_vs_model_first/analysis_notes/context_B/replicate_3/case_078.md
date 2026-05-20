Case podmr_064_2026-05-17-065956

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The instruction block first performs optical polarization, then detection. This is readout 1, a bright m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The active measurement then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is readout 2, the microwave-pulse signal readout.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- length_rabi_pulse = 52 ns. The XML file defaults include mod_depth = 1, while the saved embedded sequence text has mod_depth = 0.3. The exported Variable_values list gives mod_depth = 1. I evaluated both because either gives a quantitatively detectable signal if a resonance is present.

Physical model calculation:
- Current setup contrast between m_S = 0 and m_S = +1 is about C = 22%.
- Rabi frequency is f_R = 10 MHz * mod_depth.
- Starting in m_S = 0, the resonant microwave pulse transfers population P_1 = sin^2(pi * f_R * tau), with tau = 52 ns.
- For mod_depth = 1: f_R = 10 MHz, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected fluorescence drop is C * P_1 = 0.219, about 22%. At a raw level near 51 counts this is about 11.2 counts.
- For mod_depth = 0.3: f_R = 3 MHz, P_1 = sin^2(pi * 3e6 * 52e-9) = 0.222, so the expected fluorescence drop is C * P_1 = 0.0487, about 4.9%. At a raw level near 51 counts this is about 2.5 counts.

Observed data:
- readout 1 mean = 50.97, standard deviation across scan = 1.12.
- readout 2 mean = 50.92, standard deviation across scan = 1.12.
- Around the active center frequency in the saved sequence, 3.8751 GHz, the sampled point is 3.875 GHz.
- At 3.875 GHz: readout 1 = 48.40, readout 2 = 49.44.
- The normalized signal ratio readout2/readout1 at 3.875 GHz is 1.021, while the scan mean ratio is 0.999 with standard deviation 0.0268. This is not a microwave-induced fluorescence decrease; it is above the mean by about 0.83 sigma.
- The largest low ratio is at 3.890 GHz, not at the expected resonance location, and does not align with a consistent raw-readout dip feature.

Decision:
The relevant model predicts a large dip in readout 2 relative to the bright reference at resonance: about 22% if mod_depth = 1, or still about 4.9% if using the embedded-sequence mod_depth = 0.3. The observed normalized signal has no dip at the relevant frequency and the raw traces show only scan-scale noise/drift. I therefore decide that a pODMR resonance is absent.
