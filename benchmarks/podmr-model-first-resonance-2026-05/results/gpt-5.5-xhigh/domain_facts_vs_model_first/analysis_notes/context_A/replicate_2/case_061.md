Active sequence: Rabimodulated.xml.

The provided sequence first polarizes the NV and performs detection before any microwave pulse, so readout 1 is the true m_S = 0 bright reference. The `full_expt` value is 0, so the optional m_S = +1 reference block is skipped. The active measurement then applies `rabi_pulse_mod_wait_time` followed by detection, so readout 2 is the post-microwave-pulse readout.

The active pulse uses `length_rabi_pulse = 5.2e-08 s` and `mod_depth = 1`. With the given setup calibration, the Rabi frequency is about 10 MHz at mod_depth 1, making 52 ns approximately a pi pulse. If a pODMR resonance were present, the post-pulse readout should show a large contrast-scale response, roughly on the order of the stated 22% m_S = 0 to m_S = +1 contrast, not just a few percent of noisy variation.

The scan data show both combined raw readouts staying near 50 counts across the 3.825-3.925 GHz sweep. Readout 2 does not show a clear, localized suppression relative to the bright reference, and the per-average overlay mainly shows offsets and point-to-point scatter consistent with tracking cadence rather than a stable resonance feature. The high-frequency changes are not a convincing resonance response for a near-pi pulse.

Decision: pODMR resonance absent.
