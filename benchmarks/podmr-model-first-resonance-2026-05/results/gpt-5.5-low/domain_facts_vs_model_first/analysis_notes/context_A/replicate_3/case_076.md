Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion = 1. The active readouts are the initial polarized/detected bright m_S = 0 reference, then the post-microwave Rabi-pulse detection.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is approximately a pi pulse. If the scan crosses a pODMR resonance, readout 2 should show a clear fluorescence reduction relative to the bright reference, with contrast on the order of the stated 22% scale for a well-driven transition.

Data assessment:

The combined readout 1 and readout 2 traces remain close together, mostly near raw readout 48-51, with no stable, resonance-like dip in the post-pulse readout across neighboring frequency points. The strongest low point in readout 2 near the high-frequency end is isolated and not a convincing line shape; the per-average traces show substantial tracking/noise variation, and the stored averages are not a strong independent repeatability test. There is no clear feature approaching the expected pODMR contrast for a near-pi pulse.

Decision: resonance_absent.
