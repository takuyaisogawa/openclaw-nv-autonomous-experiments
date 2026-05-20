Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence performs an adjusted polarization pulse and immediate detection first. That first detection is the bright m_S = 0 reference/readout 1. Because full_expt is 0, the optional m_S = +1 reference branch is skipped even though do_adiabatic_inversion is true. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection; readout 2 is therefore the microwave-pulsed signal readout.

The active pulse is length_rabi_pulse = 52 ns at mod_depth = 1, rounded exactly to 13 samples at the 250 MHz sample rate. Using the stated setup calibration, this is approximately a pi pulse for a 10 MHz Rabi frequency. With a 22% m_S = 0 to m_S = +1 contrast scale, an on-resonance pi pulse should produce a substantial readout 2 dip relative to readout 1, not just a few percent.

The two raw traces share a slow downward drift across the scan, so the relevant evidence is the readout 1/readout 2 differential. The normalized contrast (readout1 - readout2) / readout1 has mean about -0.35% and standard deviation about 3.0%. The point at 3.875 GHz is a 4.0% signal reduction, but comparable or larger excursions also occur at unrelated frequencies such as 3.830 GHz and 3.840 GHz, with sign reversals elsewhere. The feature is not a coherent resonance-like dip over neighboring 5 MHz samples, and the per-average overlay mainly reflects the same tracking/drift behavior rather than a strong repeatability test.

Decision: resonance absent.
