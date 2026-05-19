<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_013

I used the provided sequence XML as the deciding sequence. The active sequence is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz. The sequence first acquires a true mS = 0 reference after optical polarization and detection. Because full_expt = 0, the optional mS = +1 reference block is skipped. The second acquired readout is therefore the signal after a Rabi-modulated microwave pulse followed by detection.

Relevant pulse settings from the provided XML: mod_depth = 1, length_rabi_pulse = 52 ns, mw_ampl = -5 dBm, ampIQ = 5 dBm, freqIQ = 50 MHz. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, a 52 ns pulse is approximately a pi pulse on resonance, so a real resonance should produce a readout-2 reduction relative to the mS = 0 readout on the order of the setup contrast scale, about 22%.

The combined raw readouts show the strongest contrast near 3.880 GHz. At that point readout 1 is about 35.65 and readout 2 is about 29.31, giving readout2/readout1 about 0.822, an approximately 18% reduction. Neighboring points around 3.870-3.880 GHz also trend low in readout 2 compared with the reference, while much of the scan is closer to parity or above. This is the expected sign and approximate size for ODMR depletion under a near-pi pulse.

The two stored averages have strong opposite drifts, consistent with tracking cadence effects rather than a clean repeatability test, so I do not treat them as independent resonance confirmations. Even with that caveat, the combined reference-normalized dip is large enough and aligned with the expected pulse behavior to call a pODMR resonance present.
