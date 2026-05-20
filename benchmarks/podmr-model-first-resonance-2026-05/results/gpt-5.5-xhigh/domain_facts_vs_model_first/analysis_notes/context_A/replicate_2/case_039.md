Sequence and readout interpretation:

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sets full_expt = 0, so the optional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true. The active acquisition order is therefore:

1. adj_polarize, then detection: this is the true mS = 0 reference readout.
2. rabi_pulse_mod_wait_time, then detection: this is the microwave-pulse signal readout.

Thus combined readout 1 is the pumped mS = 0 reference, and combined readout 2 is the post-Rabi-pulse signal. The active Rabi pulse uses length_rabi_pulse = 52 ns, rounded at 250 MS/s to the same 52 ns, with mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. If the scanned microwave frequency hits the NV transition, readout 2 should be substantially dimmer than the mS = 0 reference, on the order of the setup contrast scale rather than only a small fluctuation.

Data assessment:

The combined readouts do not show a robust resonance-like dip of readout 2 relative to readout 1. The largest combined deficit is at about 3.895 GHz, where readout 2 is only about 3.1% below readout 1. Other negative differences are similarly small, and many scan points have readout 2 above readout 1. This is far below the roughly 22% contrast expected for a near-pi pulse at mod_depth = 1. The two stored averages sit at different absolute brightness levels, consistent with tracking cadence or drift, and their few-percent readout differences are not a strong independent repeatability test.

Decision:

No pODMR resonance is present in this scan.
