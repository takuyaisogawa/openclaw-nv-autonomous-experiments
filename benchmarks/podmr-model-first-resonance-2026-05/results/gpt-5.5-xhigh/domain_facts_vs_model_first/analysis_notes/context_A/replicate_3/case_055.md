Sequence check: inputs/sequence.xml is the Rabimodulated sequence with mw_freq as the scanned variable. The active instructions are polarize, detection, wait, rabi_pulse_mod_wait_time, detection, and final wait. The first detection is the true mS = 0 reference/readout 1, and the final detection after the microwave pulse is the signal/readout 2. The optional 1-level reference branch is disabled because full_expt = 0.

The active microwave pulse uses length_rabi_pulse = 52 ns, rounded at 250 MS/s to the same 52 ns, with mod_depth = 1. Using the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so the pi time is about 50 ns. This pulse should therefore produce near-full inversion on resonance, with an expected fluorescence change comparable to the roughly 22% mS = 0 to mS = +1 contrast scale.

The paired raw readouts do not show that scale of response. The largest combined contrast, computed as (readout 1 - readout 2) / readout 1, is only about 5.6%, and the trace has scattered positive and negative deviations rather than a clean resonance-shaped dip. The stored averages sit on different count baselines, consistent with tracking cadence, so I do not treat them as a strong independent repeatability test.

Decision: resonance_absent.
