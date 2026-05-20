Active sequence: Rabimodulated.xml varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The XML has full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive despite do_adiabatic_inversion = 1. The executed readouts are therefore:

- readout 1: detection immediately after optical polarization, acting as the mS = 0 reference.
- readout 2: detection after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is essentially a resonant pi pulse. If the sweep crossed a pODMR resonance, readout 2 should show a localized decrease relative to readout 1 on the order of the setup contrast scale, about 22% for a strong transition.

The combined readout 2 / readout 1 ratio stays close to unity. The largest negative deviations are isolated points near 3.855 GHz and 3.910 GHz at only about 5%, and the surrounding points do not form a clean, localized resonance feature. The two stored averages show some similar negative excursions, especially near 3.910 GHz, but stored averages can reflect tracking cadence and the feature is still much smaller and less coherent than expected for a 52 ns pi pulse at mod_depth = 1.

Decision: no convincing pODMR resonance is present.
