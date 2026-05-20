Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the "Acquire 1 level reference" block is disabled. The active readouts are therefore:
- readout 1: true m_S = 0 reference after optical polarization and detection.
- readout 2: signal detection after rabi_pulse_mod_wait_time.

Relevant pulse settings from the active XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns. With the stated setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. If a resonance were present, the signal readout should move substantially toward the m_S = +1 fluorescence level, on the order of the setup contrast scale of about 22% relative to the m_S = 0 reference.

The combined raw readouts do not show that behavior. Across the sweep, readout 2 minus readout 1 ranges from about -5.9% to +6.5% of the reference, with no isolated or resolved resonance-like drop approaching the expected contrast. The per-average overlay mainly shows tracking-scale baseline shifts between stored averages, which are not a strong independent repeatability test here. The apparent small deviations are comparable to point-to-point scatter and do not form a convincing pODMR resonance.

Decision: resonance_absent.
