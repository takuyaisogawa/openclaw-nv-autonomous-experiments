Active sequence and parameters:

The saved scan uses Rabimodulated.xml while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active sequence has full_expt = 0, so the optional "1 level reference" block is skipped. Each shot first polarizes and detects the true m_S = 0 reference, then applies a rabi_pulse_mod_wait_time pulse and detects the MW-pulsed signal. Thus readout 1 is the bright/reference readout and readout 2 is the post-MW signal readout.

The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is near a pi pulse. On resonance this should transfer population toward m_S = +1 and reduce fluorescence by a large fraction of the available contrast scale, about 22% between m_S = 0 and m_S = +1.

Data assessment:

The raw readouts are noisy at the single-average level and the two stored averages should mainly be treated as tracking cadence, not as a strong repeatability check. The combined readouts do not show a stable resonance-like fluorescence dip of the MW-pulsed signal relative to the reference. The most visible excursions are isolated or shared fluctuations: both readouts peak near the low-frequency side around 3.83 GHz, and the signal-reference difference changes sign several times across the sweep. The largest negative signal-minus-reference points are not a coherent dip with neighboring support, and their size is far smaller and less structured than expected for a near-pi pulse on a single NV with the stated contrast scale.

Decision:

I do not find a credible pODMR resonance in this scan. The apparent structure is consistent with readout noise and tracking drift rather than a frequency-localized ODMR contrast feature.
