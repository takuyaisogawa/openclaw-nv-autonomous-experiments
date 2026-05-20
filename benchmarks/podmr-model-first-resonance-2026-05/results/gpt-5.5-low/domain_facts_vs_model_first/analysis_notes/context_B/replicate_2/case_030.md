Case podmr_015_2026-05-16-130043

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with a scan over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first performs adj_polarize followed by detection. This is the true m_S = 0 optical reference, corresponding to readout 1 in the two stored readouts.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped. Therefore readout 2 is not a stored m_S = +1 reference. It is the detection after the active Rabi microwave pulse.
- The active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- From the provided sequence XML and exported variable values: mod_depth = 1, length_rabi_pulse = 5.2e-08 s, sample_rate = 250 MHz. Rounding to the sample grid leaves 52 ns because 52 ns * 250 MHz = 13 samples.

Physical model calculation:
- Setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, so f_R = 10 MHz here.
- For a resonant rectangular pulse, transferred population can be modeled as P_1 = sin^2(pi * f_R * t), using f_R as the population oscillation frequency. With t = 52 ns and f_R = 10 MHz:
  P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected resonant fluorescence drop relative to the m_S = 0 readout is therefore 0.22 * 0.996 = 0.219, or 21.9%.

Measured comparison:
- At the minimum point, mw_freq = 3.875 GHz, readout 1 = 46.2115 and readout 2 = 35.8654.
- The normalized readout ratio there is readout2/readout1 = 0.7761, i.e. a 22.4% drop.
- The expected readout 2 at that point from the model is 46.2115 * (1 - 0.219) = 36.09, very close to the measured 35.87.
- Away from the central dip, excluding the five points centered on the minimum, the mean readout2/readout1 ratio is 0.9698 with standard deviation 0.0270. The central dip is lower than that off-resonant mean by 0.1937, about 7.2 off-resonant standard deviations.
- The dip is also frequency-localized across adjacent scan points around 3.87 to 3.885 GHz rather than being a single isolated outlier.

Decision:
The pulse sequence and quantitative signal model predict a large pODMR dip when the microwave frequency is resonant, and the measured normalized readout drop matches the expected 22% contrast-scale transfer. A pODMR resonance is present.
