Case podmr_035_2026-05-16-210045

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence, full_expt is 0, so the "Acquire 1 level reference" block is not active. The actual readout roles are therefore:

- readout 1: true m_S = 0 reference after optical polarization and before the microwave pulse.
- readout 2: signal readout after the modulated Rabi microwave pulse.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At the stated setup scale, mod_depth = 1 gives an approximately 10 MHz Rabi frequency, so 52 ns is close to a pi pulse. If the frequency sweep crossed a real pODMR resonance, the pulsed readout should show a clear resonance-shaped reduction relative to the m_S = 0 reference, potentially on the order of the 22 percent contrast scale.

The observed combined readouts instead show both channels drifting upward across the scan, with readout 2 only a few percent below readout 1 at scattered points and sometimes above it. The largest deficits are about 5 to 6 percent and are not centered into a coherent resonance feature. The per-average overlay also does not provide strong independent repeatability because the averages likely reflect tracking cadence and show substantial point-to-point variation.

Decision: resonance_absent. The data are dominated by drift/noise and do not show the distinct pulsed-ODMR contrast expected from a near-pi pulse at mod_depth = 1.
