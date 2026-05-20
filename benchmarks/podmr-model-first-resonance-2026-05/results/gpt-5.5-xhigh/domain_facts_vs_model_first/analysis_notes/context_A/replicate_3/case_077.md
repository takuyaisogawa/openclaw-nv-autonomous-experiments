Active sequence assessment:

The supplied XML is Rabimodulated.xml. It polarizes first, then performs a detection readout that serves as the true m_S = 0 reference. The full_expt variable is 0, so the optional m_S = +1 reference block is not active. The second active readout is after rabi_pulse_mod_wait_time and is therefore the post-pulse signal readout.

The active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If the microwave frequency crossed the NV transition, the post-pulse signal readout should drop strongly relative to the 0-reference readout, on the order of the setup contrast scale of about 22%.

The measured post-pulse signal/reference contrast only fluctuates by a few percent across the sweep and alternates sign. The largest signal deficit relative to the reference is about 5%, and there is also a shared downward trend in both raw readouts at the high-frequency end, which is not a selective post-pulse resonance feature. The two stored averages are not a strong repeatability test because they can reflect tracking cadence, but they also do not reveal a coherent resonance-like dip.

Decision: resonance absent.
