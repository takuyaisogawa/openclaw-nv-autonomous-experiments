Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The standalone sequence XML and exported variable values identify mod_depth = 1 and length_rabi_pulse = 52 ns. At the given setup scale, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so 52 ns is close to a pi pulse. The sequence has full_expt = 0, so the optional m_S = +1 reference block is skipped. The acquired readouts are therefore the initial polarized m_S = 0 reference detection followed by the detection after the microwave Rabi pulse.

For a real pODMR resonance with this sequence, the final post-pulse readout should drop relative to the initial reference near the resonant mw_freq. The combined normalized contrast (readout1 - readout2) / readout1 has its strongest local drop at 3.845 GHz, about 8.9%, with neighboring positive contrast around 3.850 to 3.860 GHz. Both stored averages show a same-sign drop at 3.845 GHz, though the averages also reflect tracking cadence and should not be treated as a strong independent repeatability test.

The observed contrast is weaker than the nominal 22% m_S = 0 to m_S = +1 contrast expected for a perfect pi pulse, and the line shape is noisy. Still, the sign, frequency-localized dip, and near-pi pulse condition support classifying this case as a weak pODMR resonance rather than no resonance.
