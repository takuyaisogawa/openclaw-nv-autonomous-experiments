Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Sequence/readout roles:
- readout 1 is the initial polarized bright m_S = 0 reference, acquired after adj_polarize and detection.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- readout 2 is acquired after rabi_pulse_mod_wait_time using length_rabi_pulse, then detection.

Pulse settings:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s but unchanged at this value.
- With the provided setup facts, the Rabi frequency is about 10 MHz at mod_depth 1, so 52 ns is near a pi pulse.
- If the microwave frequency were resonant, the post-pulse readout should show a clear, frequency-localized drop approaching a sizable fraction of the stated 22% m_S = 0 to m_S = +1 contrast scale.

Data assessment:
The combined readouts are noisy and the average readout 2 level is only slightly below readout 1: about 50.82 versus 51.03, roughly 0.4% mean contrast. The largest pointwise normalized drop of readout 2 relative to readout 1 is only about 5.2%, and similar positive and negative excursions occur at other frequencies. The lowest readout 2 point near 3.905 GHz is not compelling because the stored per-average traces show large tracking-like shifts and the averages are only two stored averages, which should not be treated as a strong repeatability test. Since the active pulse is near a pi pulse at full modulation depth, a real resonance should be much stronger and more coherent than this scattered pattern.

Decision: pODMR resonance absent.
