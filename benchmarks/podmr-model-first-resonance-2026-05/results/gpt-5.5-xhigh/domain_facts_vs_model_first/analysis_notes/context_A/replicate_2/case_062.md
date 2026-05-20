The active sequence is Rabimodulated.xml. It first polarizes and detects a true m_S = 0 bright reference, then skips the optional m_S = 1 reference because full_expt = 0. The final active readout is after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, so the two stored readouts are:

- readout 1: bright reference before the microwave pulse
- readout 2: post-pulse pODMR signal after the Rabi-modulated microwave pulse

At mod_depth = 1 the provided setup estimate gives a Rabi frequency of about 10 MHz, making 52 ns approximately a pi pulse. If the scan crossed a real resonance, the post-pulse readout should drop strongly relative to the bright reference, on the order of the 22% m_S = 0 to m_S = +1 contrast scale.

The combined normalized post/reference behavior is much smaller and irregular. The deepest combined point is only about a 7.4% drop, with several other dips in the 2-5% range and positive excursions nearby. The apparent depressions are not a clean line shape, and the two stored averages mainly show tracking-level scatter rather than a strong independent repeatability check. Given the near-pi active pulse, the data do not show a convincing pODMR resonance.
