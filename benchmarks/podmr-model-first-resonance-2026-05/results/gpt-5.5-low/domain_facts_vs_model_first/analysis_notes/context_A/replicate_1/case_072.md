Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects a true mS=0 reference, then waits, applies a rabi_pulse_mod_wait_time pulse, and detects again. Because full_expt = 0, the intermediate mS=1 reference block is skipped. Therefore readout 1 is the pre-microwave bright reference and readout 2 is the post-pulse signal readout.

Relevant pulse parameters from the provided XML and active variable values:
- mod_depth = 1
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns
- expected Rabi frequency is about 10 MHz at this modulation depth, so the pulse is close to a pi pulse

If an ODMR resonance were present, the near-pi microwave pulse should transfer population out of mS=0 near resonance and produce a clear decrease in the post-pulse signal readout relative to the bright reference, on the order of the setup contrast scale. The combined readouts do not show such a coherent dip: readout 2 fluctuates above and below readout 1, has a high point near 3.900 GHz rather than a depression, and its low points are isolated and not reproducible across the two stored averages. The stored averages also differ mostly by baseline/tracking drift, so they do not provide strong independent confirmation.

Decision: resonance absent.
