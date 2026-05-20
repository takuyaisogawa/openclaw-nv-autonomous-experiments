Active sequence: Rabimodulated.xml, scanning mw_freq.

The provided sequence XML sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is essentially a pi-scale pulse. The active instruction flow is: polarize, detect the true m_S = 0 reference, wait, skip the +1 reference block because full_expt = 0, apply rabi_pulse_mod_wait_time with the scanned microwave frequency, then detect again. Thus readout 1 is the polarized 0-level reference and readout 2 is the post-microwave-pulse signal, not an independent +1 reference.

For a real pODMR resonance under this pulse, readout 2 should show a clear localized fluorescence reduction relative to readout 1, with the possible contrast scale set by the approximately 22% m_S = 0 to m_S = +1 contrast. The raw data only show small and scattered readout-2 suppressions: the largest is around 3.86 GHz at about 4.6 counts below the reference, roughly 9%, with other smaller dips spread across the scan. The per-average traces vary strongly with tracking cadence and do not establish a clean, localized resonance feature.

Decision: resonance_absent.
