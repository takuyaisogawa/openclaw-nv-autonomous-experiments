Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The active instructions first polarize and detect, then skip the optional 1-level reference block because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and detect again. Therefore readout 1 is the bright m_S = 0 reference for each scan point, and readout 2 is the post-microwave signal readout. The provided sequence file and exported active variable values set mod_depth = 1 and length_rabi_pulse = 52 ns. The embedded sequence text in raw_export.json contains an older/default-looking mod_depth = 0.3 line, but the local sequence XML and active Variable_values indicate mod_depth = 1.

At this setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is near a strong pi-like pulse. If a resonance were present in the scanned frequency range, the post-microwave readout should show a localized reduction approaching the setup contrast scale, roughly 22% between m_S = 0 and m_S = +1 for a single NV under strong transfer. With raw counts near 50, that would be a much larger dip than the observed point-to-point differences.

The measured readout 2 minus readout 1 differences are only a few counts at most, alternate in sign, and both readouts share a slow upward drift across the scan. The most negative normalized points are about 4-5%, far below the expected strong-pulse contrast and not a clean localized resonance. The two stored averages are not enough to establish independent repeatability and likely reflect tracking cadence, so I do not treat the faint per-average variations as a resonance.

Decision: resonance absent.
