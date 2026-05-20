The provided sequence is Rabimodulated.xml. With full_expt = 0, the inactive mS=+1 reference block is skipped, so the active cycle is a polarize/detect mS=0 reference followed by a modulated rabi pulse and a second detection. Thus readout 1 is the no-microwave mS=0 reference and readout 2 is the post-pulse signal readout.

The sequence uses mod_depth = 1 and length_rabi_pulse = 52 ns. Given the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. If a pODMR resonance were being hit cleanly, the signal readout should show a large drop relative to the reference, on the order of the stated 22% mS=0 to mS=+1 contrast scale.

Instead, readout 2 divided by readout 1 stays near unity, with point-to-point fluctuations of only a few percent and no convincing resonance-shaped dip. The lowest combined ratios are around 0.95, and similar-sized deviations of both signs occur across the scan. The per-average overlays show tracking/noise-level variation rather than a stable independent resonance feature, and the common downward drift in both readouts near the high-frequency end is not diagnostic of spin contrast.

Decision: resonance absent.
