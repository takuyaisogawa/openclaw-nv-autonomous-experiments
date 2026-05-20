Active sequence: Rabimodulated.xml / Rabimodulated, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The sequence first polarizes the NV and detects a true mS=0 reference. Because full_expt = 0, the optional mS=+1 reference block is skipped. The second acquired readout is therefore the measurement after a rabi_pulse_mod_wait_time pulse.

Relevant active pulse settings from the provided sequence/export are mod_depth = 1 and length_rabi_pulse = 52 ns, rounded at 250 MS/s. Given the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is essentially a pi pulse duration. If the microwave frequency crossed a real pODMR resonance, the post-pulse readout should show a strong contrast change relative to the mS=0 reference, on the order of the setup's 22% mS=0 to mS=+1 contrast scale.

The two combined raw readouts stay close to each other over the scan, with differences of only a few counts and no reproducible resonance-shaped drop in the post-pulse readout. The per-average traces show substantial tracking/cadence offsets between averages, and those offsets dominate over any candidate spectral feature. Since stored averages are not a strong independent repeatability test here, the relevant evidence is that the expected pi-pulse contrast is not visible in the active signal readout.

Decision: resonance_absent.
