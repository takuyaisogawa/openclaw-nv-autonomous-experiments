Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Sequence/readout roles:
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- readout 1 is the true m_S = 0 reference after optical polarization and detection with no microwave pulse.
- readout 2 is the signal detection after the modulated Rabi pulse.

Pulse settings:
- mod_depth = 1.
- length_rabi_pulse = 52 ns.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is approximately a pi pulse on resonance. A real resonance should therefore produce a sizeable post-pulse signal loss relative to the m_S = 0 reference, on the order of the available 22% contrast scale if the pulse is effective.

Data assessment:
The combined raw readouts show both channels drifting downward toward the high-frequency end, especially near 3.920-3.925 GHz. That common-mode drop is not by itself evidence for ODMR contrast because the reference channel drops with the signal channel.

Comparing readout 2 against readout 1, the deficits are small and irregular. The signal/reference ratios range roughly from 0.955 to 1.040, with isolated minima around 3.855 GHz and 3.905-3.925 GHz rather than a clear localized dip. The largest combined deficit is about 4.5%, far below the expected contrast scale for a near-pi pulse at full modulation depth. The two stored averages do not provide strong independent confirmation, and their apparent minima do not define a consistent resonance feature.

Decision: no credible pODMR resonance is present in this scan.
