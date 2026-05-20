Case podmr_058_2026-05-17-053345

I used the provided sequence XML and raw export, not any labels or prior outputs. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true bright-state / m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped even though the adiabatic inversion flag is present. The final active block is a modulated Rabi microwave pulse followed by detection, so readout 1 is the bright reference and readout 2 is the signal after the microwave pulse.

The provided XML/variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so 52 ns is approximately a pi pulse. If the sweep crossed a well-coupled resonance, the signal readout should show a clear drop relative to the bright reference, with a contrast scale approaching the approximately 22 percent m_S = 0 to m_S = +1 separation, allowing for imperfections.

The combined raw readout ratio readout2/readout1 has several negative excursions, with the lowest points around 0.93 near 3.885-3.890 GHz and additional isolated negative points near 3.910 and 3.925 GHz. These are much smaller than the expected near-pi-pulse contrast and are not a clean single resonance feature; the trace also has comparable positive excursions. The per-average overlay shows strong baseline/tracking offsets between averages, and the stored averages are not a strong independent repeatability test. The apparent dips are therefore better treated as noise/tracking structure rather than a defensible pODMR resonance.

Decision: resonance_absent.
