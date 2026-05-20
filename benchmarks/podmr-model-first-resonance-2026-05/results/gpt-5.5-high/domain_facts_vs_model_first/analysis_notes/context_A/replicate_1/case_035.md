Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The XML has full_expt = 0, so only two detection windows are active. Readout 1 is the optically pumped m_S = 0 reference acquired immediately after polarization. The m_S = +1 reference block is skipped. Readout 2 is the signal acquired after the microwave Rabi pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so 52 ns is approximately a pi pulse. On resonance this should drive substantial population from m_S = 0 to m_S = +1, giving a signal readout noticeably lower than the 0 reference, on the order of the stated 22% contrast scale.

The combined paired contrast, computed as (readout1 - readout2) / readout1, is small and inconsistent: it ranges from about -4% to +7%, with a mean near +1.4%. The largest apparent dips are isolated and not a coherent localized resonance over the frequency scan. Several high-frequency points have readout 2 greater than readout 1, which is opposite the expected on-resonance sign for this pulse. The per-average traces show strong drifting/opposite trends consistent with tracking cadence effects rather than independent repeatability.

Decision: resonance_absent.
