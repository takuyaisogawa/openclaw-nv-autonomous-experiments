Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- The first detection occurs immediately after optical polarization and is the true mS=0/readout reference.
- full_expt is 0, so the optional mS=+1 reference block is skipped.
- The active experimental pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence/variable values, followed by the second detection; this second readout is the MW-affected signal.
- With the setup facts, mod_depth = 1 implies roughly 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance. A real resonance should therefore make the second readout noticeably lower than the first readout, potentially on the order of the stated 22% contrast scale, and should be frequency-localized rather than just average-to-average scatter.

Data assessment:
The two combined readouts fluctuate by about one to two raw-count units and cross each other multiple times across the sweep. There is a low point in the second readout near 3.895 GHz, but it is isolated and the stored per-average traces show large tracking-like offsets and inconsistent point-to-point structure rather than a repeatable resonance-shaped dip. The expected on-resonance effect for a near-pi pulse at mod_depth 1 would be substantially clearer than the observed noisy excursions.

Decision: resonance_absent. The raw signal does not show a robust, localized post-MW readout loss relative to the mS=0 reference.
