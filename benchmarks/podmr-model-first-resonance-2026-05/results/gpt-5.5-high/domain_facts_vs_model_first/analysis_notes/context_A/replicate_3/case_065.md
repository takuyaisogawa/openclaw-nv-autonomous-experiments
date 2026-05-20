Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided XML has full_expt = 0, so the optional m_S = +1 reference block is disabled. The first detection after adj_polarize is the active m_S = 0 / bright reference readout. The second detection follows the modulated Rabi pulse and is the frequency-dependent signal readout. There is no independent dark-state reference in this scan.

The pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, the pulse is close to a pi pulse on resonance. A true resonance should therefore reduce the post-pulse signal relative to the polarized reference, with an upper contrast scale around 22 percent for this setup.

The combined readouts show the post-pulse/readout-reference ratio dipping most strongly at 3.895 GHz: readout 1 is 50.0 and readout 2 is 45.3846, a normalized drop of about 9.2 percent. The two stored averages both show a similar drop at that point, with ratios about 0.900 and 0.915, though these averages may reflect tracking cadence and are not a strong repeatability test. Other frequency points fluctuate by a few percent, and there are weaker negative excursions, but this is the clearest resonant-looking feature and it is in the expected direction for the active pulse sequence.

Decision: resonance_present.
