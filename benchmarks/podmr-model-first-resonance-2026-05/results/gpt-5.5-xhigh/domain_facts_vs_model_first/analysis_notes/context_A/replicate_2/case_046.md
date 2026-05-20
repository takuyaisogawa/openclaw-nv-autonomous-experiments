Sequence XML review:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional 1-level reference block is inactive despite do_adiabatic_inversion being true.
- Readout roles: readout 1 is the true m_S = 0 reference after optical polarization; readout 2 is after the modulated Rabi microwave pulse.
- mod_depth is 1.
- length_rabi_pulse is 52 ns after sample-rate rounding at 250 MHz.

Decision reasoning:

At the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the swept microwave crosses the m_S = 0 to m_S = +1 resonance, readout 2 should show a substantial dark response relative to readout 1, on the order of the stated 22% contrast scale.

The combined raw readouts do not show that behavior. The largest readout2/readout1 excursion is a positive change of about +7.3% at 3.875 GHz, not a dark post-pulse readout. Other negative excursions are only a few percent and are not a clear resonant feature. The per-average traces also mainly reflect offset/tracking changes, so they do not provide a strong independent repeatability check.

Conclusion: resonance_absent.
