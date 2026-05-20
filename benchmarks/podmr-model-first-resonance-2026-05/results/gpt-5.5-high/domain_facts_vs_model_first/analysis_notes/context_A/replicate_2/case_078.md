The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. Because full_expt is 0, the optional 1-level reference block is inactive. The two active readouts are therefore the initial polarized m_S = 0 reference detection followed by the post-Rabi-pulse signal detection. The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Using the stated setup calibration, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. A real pODMR resonance should therefore create a substantial post-pulse fluorescence reduction relative to the 0-reference readout, on the order of the setup contrast scale when well driven.

The combined raw readouts do not show such a feature. The largest post-pulse deficit relative to the reference is around 3.890 GHz at roughly -5.4%, with other negative excursions near -3% and -4%, but there is also a comparable positive excursion near 3.915 GHz of about +6.1%. The feature is not a coherent resonance-shaped dip and is small compared with the expected roughly 22% contrast scale for a near-pi pulse. The stored two averages show tracking-like drift and inconsistent point excursions rather than a strong independent repeatability signature.

Decision: resonance_absent.
