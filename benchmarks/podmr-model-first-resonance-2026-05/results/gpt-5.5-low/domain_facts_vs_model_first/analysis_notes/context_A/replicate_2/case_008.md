Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the XML:
- readout 1 is the true m_S = 0 optical reference after adj_polarize and detection.
- readout 2 is the measurement after the rabi_pulse_mod_wait_time microwave pulse and detection.
- full_expt is 0, so the optional m_S = +1 reference block is inactive.

Pulse settings used for the decision:
- mod_depth = 1 from the provided sequence XML and exported variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is close to a pi pulse.

Decision basis:
A near-pi pulse on resonance should produce a substantial fluorescence reduction relative to the m_S = 0 reference, on the order of the setup contrast scale if the resonance is well addressed. The combined readouts instead stay around the mid-40s with only small point-to-point differences. The largest apparent low point in the post-pulse readout is isolated and not convincingly repeated across the two stored averages; those averages also appear affected by tracking/cadence drift. There is no coherent resonance-shaped dip across frequency and no robust contrast near the expected scale.

Conclusion: resonance absent.
