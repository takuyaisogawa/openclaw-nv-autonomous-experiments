Case podmr_038_2026-05-16-214551

I used the provided sequence XML as the active pulse program. The sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active detections are:

1. adj_polarize followed by detection: this is the true m_S = 0 bright reference, corresponding to readout 1.
2. Because full_expt = 0, the optional m_S = 1 reference block is skipped.
3. rabi_pulse_mod_wait_time followed by detection: this is the pODMR signal readout after the microwave pulse, corresponding to readout 2.

The active pulse parameters from the provided sequence XML are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded duration remains 13 samples = 52 ns.

Quantitative signal model:

The stated setup has Rabi frequency about 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so f_R = 10 MHz here. For a rectangular pulse, the transition probability as a function of detuning Delta is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau)

with tau = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected on-resonance normalized pODMR dip is

0.22 * 0.996 = 0.219, or about 21.9%.

The bright-reference mean readout is 46.57 counts, so the expected on-resonance dip is about

46.57 * 0.219 = 10.2 counts.

Observed data:

readout1 mean = 46.57 counts
readout2 mean = 46.23 counts
readout1 - readout2 mean = 0.34 counts
maximum observed normalized dip (readout1 - readout2) / readout1 = 0.060
maximum observed count dip = 2.79 counts

I also fit the observed normalized dip to the Rabi detuning model while allowing the resonance center to vary across the scanned range. The best fit was centered near 3.8475 GHz with fitted amplitude about 0.049, only 22% of the expected 0.22 contrast amplitude. This fit describes a small local fluctuation, not the expected near-pi-pulse pODMR response.

Stored averages were not treated as independent proof because the prompt notes that they often reflect tracking cadence. They show substantial baseline shifts between averages, consistent with tracking or drift, and do not recover a 22% resonance dip.

Decision: resonance_absent. Under the active sequence parameters, a true resonance should be a large readout2 dip relative to the m_S = 0 reference, and the measured signal is far too small.
