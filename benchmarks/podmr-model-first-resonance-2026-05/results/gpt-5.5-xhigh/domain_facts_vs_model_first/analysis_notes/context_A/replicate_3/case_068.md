Sequence/readout analysis:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS = +1 reference branch is inactive.
- Readout 1 is the bright mS = 0 reference after optical polarization and before the microwave pulse.
- Readout 2 is the signal after rabi_pulse_mod_wait_time followed by detection.
- The provided sequence has mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so a real resonance should drive a large drop of readout 2 relative to readout 1, on the order of the 22% contrast scale.

Data assessment:
The combined readout-2/readout-1 ratios stay close to unity. The deepest combined drop is about 0.947 at 3.840 GHz, only about a 5% decrease, while positive excursions of similar size also occur. The per-average traces show tracking-related offsets and shallow local differences near 3.84-3.85 GHz, but stored averages are not a strong independent repeatability test and the feature is far smaller than expected for this near-pi pulse.

Decision:
resonance_absent. The observed readout differences are small and comparable to scan/tracking fluctuations rather than a clear pODMR resonance response.
