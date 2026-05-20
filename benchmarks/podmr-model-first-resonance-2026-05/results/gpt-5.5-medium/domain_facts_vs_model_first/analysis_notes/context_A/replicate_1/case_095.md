Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The active instructions first polarize and detect a true m_S = 0 bright reference, then wait, then apply one rabi_pulse_mod_wait_time pulse, then detect again. Because full_expt = 0, the optional m_S = 1 reference block is skipped. Thus readout 1 is the bright reference/tracking readout and readout 2 is the post-microwave-pulse pODMR signal readout.

The provided sequence XML and variable values indicate mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi-like pulse on resonance. Given the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a true resonance should produce a clear signal-readout contrast change relative to the bright reference, substantially larger and more localized than the few-count tracking-scale fluctuations.

The combined raw readouts do not show a convincing signal-specific resonance. Readout 2 sometimes lies below readout 1, but the separation changes sign and size irregularly, and both channels show slow drift across the scan. The largest apparent low values occur toward the high-frequency edge where both readouts are also lower, which is more consistent with drift/tracking behavior than a resolved pODMR dip. The per-average traces mainly show offset changes between averages, matching the warning that stored averages reflect tracking cadence rather than a strong repeatability test.

Decision: resonance_absent.
