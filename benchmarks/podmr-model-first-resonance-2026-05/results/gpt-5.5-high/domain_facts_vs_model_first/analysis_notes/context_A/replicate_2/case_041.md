Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The instruction block first polarizes and detects, then waits; because full_expt = 0, the optional +1 reference block is disabled. It then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection. Thus readout 1 is the bright m_S = 0 reference for each frequency point, and readout 2 is the post-microwave-pulse signal readout.

From the provided sequence XML/exported variable values, length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. A true resonance should therefore produce a substantial transfer toward the darker m_S = +1 state, on the order of the setup's roughly 22% contrast scale if well driven.

The measured readout 2 values are not consistently or strongly darkened relative to readout 1. The largest pointwise deficits are only a few counts, roughly several percent of the raw readout level, and similarly sized excursions and sign changes occur across the scan. The two stored averages show noticeable tracking/noise-like scatter rather than a stable, localized frequency feature. Given the expected near-pi pulse strength, this is too small and inconsistent to call a pODMR resonance.

Decision: resonance absent.
