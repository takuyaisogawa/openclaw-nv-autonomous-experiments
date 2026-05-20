Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the optional m_S = +1 reference block is inactive. The active readouts are therefore:

1. Readout 1: fluorescence after optical polarization, serving as the m_S = 0 reference.
2. Readout 2: fluorescence after a Rabi-modulated microwave pulse, serving as the driven-state readout.

The active Rabi pulse is length_rabi_pulse = 52 ns with mod_depth = 1. Given the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse. If the scan crossed a pODMR resonance, the post-pulse readout should show a strong localized fluorescence reduction relative to the m_S = 0 reference, on the order of the setup contrast scale of about 22%.

The measured readout-2 minus readout-1 differences are small and irregular, ranging roughly from -5.4% to +5.7% relative to readout 1. The two traces mostly share the same slow drift/tracking structure, and the small negative excursions are not a clean resonance-like suppression. Stored averages are not treated as a strong independent repeatability test here because they can reflect tracking cadence.

Decision: resonance_absent.
