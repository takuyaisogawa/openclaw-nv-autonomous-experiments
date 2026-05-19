<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence assessment:

The provided XML is Rabimodulated.xml with mw_freq as the swept parameter. The sequence first polarizes and detects the true mS = 0 bright reference. Because full_expt = 0, the optional mS = +1 reference block is skipped. It then applies one modulated Rabi pulse and performs the second detection, so readout 1 is the mS = 0 reference and readout 2 is the post-pulse signal.

The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse on resonance. Given the about 22% mS = 0 to mS = +1 contrast scale, a real resonance should cause a clear, localized reduction of the post-pulse readout relative to the reference near the resonant microwave frequency.

The raw readouts do not show that behavior. Both readouts track a similar slow downward drift over the scan, and the per-average traces show substantial point-to-point variation. The post-pulse readout is sometimes below and sometimes above the reference, without a stable localized dip of the expected contrast scale. Stored averages are only two and likely reflect tracking cadence rather than a strong repeatability check, so I do not treat the two average traces as independent confirmation.

Decision: resonance_absent.
