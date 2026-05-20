Active sequence: Rabimodulated.xml / Rabimodulated sequence while scanning mw_freq from 3.825 GHz to 3.925 GHz.

The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is skipped even though do_adiabatic_inversion is true. The active readouts are therefore:

- readout 1: detection after optical polarization, serving as the m_S = 0 fluorescence reference.
- readout 2: detection after a modulated Rabi microwave pulse, serving as the resonance-sensitive readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, the Rabi period is about 100 ns and a pi pulse is about 50 ns, so a resonant transition should substantially reduce readout 2 relative to the m_S = 0 reference. The stated full contrast scale is about 22%, so a clean full inversion could be large, but real pODMR data may show smaller apparent contrast.

The combined raw readouts do not show a smooth broad line, and the stored averages are not a strong repeatability test because they may reflect tracking cadence. However, the within-point comparison is most relevant here. At 3.860 GHz, readout 2 is 48.846 versus readout 1 at 53.442, a reduction of about 8.6%. Both stored averages show the same local reduction at this point: roughly 54.42 to 50.12 and 52.46 to 47.58. Several other frequencies have smaller reductions, but 3.860 GHz is the clearest resonance-like feature.

Decision: resonance_present. The contrast is weaker and noisier than the nominal 22% scale, but the active sequence uses a near-pi pulse at full modulation depth, and there is a reproducible same-frequency drop in the post-pulse readout relative to the polarized reference.
