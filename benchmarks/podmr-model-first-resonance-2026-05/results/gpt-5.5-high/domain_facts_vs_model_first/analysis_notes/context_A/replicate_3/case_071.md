Case podmr_057_2026-05-17-051839

Sequence interpretation:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect the bright m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by a second detection. Thus readout 1 is the pre-pulse m_S = 0 reference, and readout 2 is the post-Rabi-pulse signal.
- Provided XML and exported variable values give length_rabi_pulse = 52 ns and mod_depth = 1.

Pulse/contrast expectation:
- With the supplied setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency.
- A 52 ns pulse is therefore approximately a pi pulse on resonance, so if the frequency scan crosses a strong pODMR resonance the post-pulse readout should show a clear fluorescence loss relative to the m_S = 0 reference.
- The stated contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should plausibly be much larger than ordinary few-percent scatter.

Data check:
- The combined readouts have similar means: readout 1 mean about 45.46 and readout 2 mean about 45.42.
- Signal-reference contrast, computed as (readout1 - readout2) / readout1, has mean about 0.07%, standard deviation about 2.1%, and ranges from about -3.9% to +4.5%.
- The largest apparent depletion is at the scan endpoint and is only about 4.5%, far below the expected scale for a near-pi pulse at this modulation depth.
- The sign of the signal-reference difference changes repeatedly across the scan, and the per-average overlays look dominated by tracking/noise rather than a reproducible resonance feature. Stored averages are not a strong independent repeatability test here.

Decision:
The scan does not show a convincing pODMR resonance. The active pulse settings should have produced a strong relative drop if a resonance were present, but the observed deviations are small, inconsistent, and comparable to raw readout scatter.
