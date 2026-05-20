I used the provided sequence XML and raw export for this case only.

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence has full_expt = 0, so the optional mS = +1 reference block is skipped. The two active detections are therefore:

- readout 1: polarized no-microwave bright reference after adj_polarize
- readout 2: signal after a scanned microwave rabi_pulse_mod_wait_time pulse, followed by detection

The active microwave pulse is length_rabi_pulse = 52 ns after rounding at 250 MS/s, with mod_depth = 1. Using the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is near a pi pulse. If a clean pODMR resonance were present, the signal readout should show a strong localized drop relative to the bright reference, on the order of the stated 22% mS = 0 to mS = +1 contrast scale.

The combined readouts instead show strong common drift upward across the frequency scan. The signal/reference contrast is small, mostly within about plus or minus 5%, and changes sign multiple times. There are dip-like points, including around 3.89 GHz, but their depth is far below the expected near-pi-pulse contrast and is comparable to the scan drift and stored-average variation. The stored averages also mainly reflect tracking cadence, so they do not provide a strong independent repeatability check.

Decision: resonance_absent. The data do not show a convincing pODMR resonance under the active near-pi pulse conditions.
