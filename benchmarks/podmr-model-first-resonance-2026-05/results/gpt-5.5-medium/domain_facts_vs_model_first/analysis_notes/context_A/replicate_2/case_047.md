<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The sequence first performs optical polarization and detection, so readout 1 is the bright mS=0 reference for each scan point. Because full_expt is 0, the optional mS=1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth from the provided sequence XML set to 1, followed by the second detection, so readout 2 is the post-microwave signal readout.

With the provided setup facts, mod_depth = 1 implies about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. On resonance this should transfer population out of mS=0 and produce a strong fluorescence loss in the signal readout, on the order of the 22 percent contrast scale for this setup. Even if using the embedded saved sequence text in raw_export.json, which shows mod_depth = 0.3 in one place, the expected on-resonance loss from a 52 ns pulse would still be a coherent dip in readout 2 relative to the reference, not a broad positive excursion.

The combined raw readouts do not show a clear resonance-shaped dip. Readout 2 is generally comparable to or higher than readout 1, with a high point near 3.915 GHz rather than a fluorescence loss. The per-average overlays mostly show tracking-like offsets between averages and both readouts drifting together; the stored averages are not a strong independent repeatability test. Given the readout roles and the expected sign/magnitude of a resonance response, the data do not support a pODMR resonance.
