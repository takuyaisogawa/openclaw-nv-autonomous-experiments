Sequence/readout interpretation:

The provided sequence is Rabimodulated.xml with mw_freq swept over the scan.  The active branch has full_expt = 0, so the optional m_S = +1 reference branch is skipped even though do_adiabatic_inversion is true.  The first detection after adj_polarize is therefore the true m_S = 0 reference/readout 1.  After that, the sequence applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detects readout 2 as the microwave-driven measurement.

Pulse expectation:

Using the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse.  On resonance this should move population from m_S = 0 toward m_S = +1 and reduce fluorescence in readout 2 relative to the m_S = 0 reference.  The full setup contrast scale is about 22%, but an observed raw pODMR feature can be smaller because the data are noisy and only two stored averages are present.

Data assessment:

The combined normalized difference readout2/readout1 shows a localized darkening cluster near 3.880-3.895 GHz: readout 2 is lower than readout 1 by about 5.7%, 4.4%, 6.4%, and 3.5% across consecutive points.  Both stored averages show darkening in this same region, especially around 3.88-3.89 GHz, while other excursions such as 3.910 GHz look more isolated.  Since stored averages can reflect tracking cadence, I do not treat them as a strong independent repeatability test, but they do not contradict the resonance-like feature.

Decision:

A pODMR resonance is present.  The feature is weaker than the full 22% contrast scale, but its sign, approximate width for a 52 ns pulse, and repeated contrast around 3.88-3.89 GHz support a resonance call.
