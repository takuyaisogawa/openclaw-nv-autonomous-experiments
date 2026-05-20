Case podmr_017_2026-05-16-132945

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml with a microwave-frequency scan. The executable instruction block first polarizes the NV and performs detection, then waits. Because full_expt is 0, the optional m_S=+1 reference block is skipped. The final active operation is a rabi_pulse_mod_wait_time followed by detection. Therefore readout 1 is the polarized m_S=0 optical reference and readout 2 is the post-Rabi-pulse signal. The active pulse duration is length_rabi_pulse = 52 ns, and mod_depth = 1 from the provided XML variable values.

Quantitative model:

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. Thus the pulse area for t = 52 ns is f_R * t = 10e6 * 52e-9 = 0.52 cycles. For a resonant two-level drive starting in m_S=0, the transfer probability is

P_1(Delta=0) = sin^2(pi * f_R * t) = sin^2(pi * 0.52) = 0.996.

With a stated optical contrast scale of about 22%, a resonant point should reduce the post-pulse readout by approximately 0.22 * 0.996 = 21.9% relative to the m_S=0 reference. The mean readout-1 reference is 44.562 counts, giving an expected resonant readout of

44.562 * (1 - 0.22 * 0.996) = 34.797 counts.

The measured readout-2 minimum occurs at 3.875 GHz. At that point readout 1 is 45.404 and readout 2 is 34.173, giving a paired contrast of

1 - 34.173 / 45.404 = 24.7%.

This is close to the expected 21.9% contrast scale for a near-pi pulse. The surrounding points also follow the expected Rabi-detuning shape for f_R = 10 MHz and t = 52 ns: using

P_1(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),

the expected transition probabilities around the center are approximately 0.749 at +/-5 MHz, 0.273 at +/-10 MHz, and 0.012 at +/-15 MHz. The observed readout-2 trace has the same localized deep minimum centered near 3.875 GHz, while readout 1 stays near the reference level. The two stored averages both show the same central dip, but I treat this only as consistency with the tracking cadence rather than as a strong independent repeatability test.

Decision: a pODMR resonance is present.
