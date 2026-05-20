Active sequence assessment:

The provided sequence XML is Rabimodulated.xml. It sets mod_depth = 1 and length_rabi_pulse = 5.2e-08 s, rounded at a 250 MHz sample rate. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a 52 ns pulse, close to a pi pulse scale.

Readout roles:

The sequence first calls adj_polarize and detection, labeled in the XML as acquiring the true 0 level reference. The optional 1 level reference block is gated by full_expt, and full_expt = 0, so that block is inactive. The second active detection occurs after rabi_pulse_mod_wait_time using length_rabi_pulse and mod_depth, so it is the microwave-pulsed signal readout rather than an independent stored 1 reference.

Expected resonance behavior:

For a single NV pODMR resonance with a near-pi pulse, the pulsed signal readout should drop relative to the 0 reference at the resonant microwave frequency. The known contrast scale is about 22%, so even allowing for imperfect drive and noise, the relevant evidence should be a localized and physically consistent suppression in the pulsed readout compared with the reference.

Observed data:

The two combined raw readouts both show a broad downward drift across the scan. The pulsed readout is often higher than the 0 reference, crosses it inconsistently, and does not show a stable localized dip of the expected sign. The per-average traces show large opposing baseline/tracking changes between stored averages, so the average overlays are not strong independent repeatability evidence. Apparent low points occur in both readouts and are not cleanly tied to a microwave-induced contrast feature.

Decision:

I do not find convincing evidence for a pODMR resonance in this scan. The data are better explained by baseline/tracking drift and readout noise than by a localized resonant reduction of the pulsed signal relative to the 0 reference.
