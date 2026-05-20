Active sequence: Rabimodulated.xml.

The provided sequence XML uses a modulated Rabi pulse experiment while sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables give mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse on resonance. Given the stated 22% mS=0 to mS=+1 contrast scale, a true resonance should produce a sizable drop in the post-microwave readout relative to the bright reference.

Readout roles from the active instructions:
- The first detection follows adj_polarize and is the true mS=0 bright reference.
- full_expt = 0, so the optional mS=1 reference block is skipped.
- The second detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the frequency-dependent signal readout after the microwave pulse.

The combined data do not show the expected strong post-pulse fluorescence loss. The readout-2 vs readout-1 contrast only reaches roughly 3% at its strongest points, and the apparent low region near the high-frequency side is also accompanied by motion in the reference/readout-1 trace and by per-average variability. Stored averages are only two averages and can reflect tracking cadence, so the per-average overlay is not strong independent confirmation. Overall the structure is small compared with the expected pi-pulse contrast and is not coherent enough to call a pODMR resonance.

Decision: resonance_absent.
