Case podmr_017_2026-05-16-132945

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz. In the provided sequence, full_expt = 0, so the "Acquire 1 level reference" block is skipped. The first detection immediately after adj_polarize is therefore the true m_S = 0 reference readout, and the later detection after the modulated Rabi pulse is the pODMR signal readout.

The relevant pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The provided sequence and exported variable values give length_rabi_pulse = 5.2e-08 s and mod_depth = 1. With sample_rate = 250 MHz, the rounded pulse length remains 52 ns. Given the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse, so an on-resonance response should drive population toward m_S = +1 and reduce fluorescence by roughly the setup contrast scale.

The combined signal readout has a pronounced dip centered at about 3.875 GHz: readout 2 falls to 34.17 while the m_S = 0 reference readout remains about 45.40, giving a signal/reference ratio near 0.753. Neighboring signal points form the same broad trough from roughly 3.865 to 3.885 GHz, and both stored averages show the dip at the same center, though stored averages should mainly be treated as tracking cadence. The depth is consistent with the expected approximately 22% contrast for a near-pi pulse rather than with noise or a reference fluctuation.

Decision: pODMR resonance is present.
