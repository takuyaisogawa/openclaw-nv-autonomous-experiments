Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes the NV and immediately detects; this is the true mS = 0 reference readout. The "Acquire 1 level reference" block is guarded by full_expt, and full_expt = 0, so that block is inactive. The second active detection is after rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, so readout 2 is the post-Rabi signal. At 250 MHz sample rate, 52 ns is 13 samples and does not round away.

Domain expectation: with mod_depth = 1 the Rabi frequency is about 10 MHz, so a 52 ns pulse is approximately a pi pulse. If the microwave sweep hits a real pODMR resonance, the post-Rabi readout should show a sizable spin-dependent drop toward the mS = +1 fluorescence level, on the order of the stated 22% contrast scale relative to the mS = 0 reference.

Observed behavior: readout 2 divided by readout 1 stays close to unity across the sweep. The deepest local combined-ratio dip is about 0.955 at 3.855 GHz, and another endpoint dip is about 0.966 at 3.925 GHz, far smaller than the expected near-pi-pulse contrast. The large downward trend near the high-frequency end is shared by both readouts, which is consistent with optical/tracking drift rather than a spin-selective resonance. The stored average traces are useful context but not a strong independent repeatability test here, and the small pointwise dips are not enough to overcome the mismatch with the expected 52 ns full-depth response.

Decision: resonance_absent.
