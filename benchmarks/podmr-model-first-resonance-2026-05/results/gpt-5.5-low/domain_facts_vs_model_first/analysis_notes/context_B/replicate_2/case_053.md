Case podmr_039_2026-05-16-221215

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, previous outputs, sibling cases, or external context.

Sequence and readout roles:
- Active sequence: Rabimodulated.xml / Rabi-modulated pODMR while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first calls adj_polarize, then detection. This is the true mS = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional "1 level reference" branch is skipped.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. This is the post-pulse signal, corresponding to readout 2.
- The adiabatic inversion variable is not active because the full_expt branch is skipped and the active pulse is the Rabi-modulated pulse.

Quantitative physical model:
- Given setup Rabi frequency f_R ~= 10 MHz at mod_depth = 1.
- Pulse duration t = 52 ns.
- On-resonance transfer probability for a square Rabi pulse is P = sin^2(pi f_R t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With mS = 0 to mS = +1 contrast scale C ~= 22%, the expected on-resonance readout-2/readout-1 ratio is 1 - C P = 0.781, i.e. an expected dip of about 21.9%.
- Including detuning with P(delta) = (f_R^2/(f_R^2 + delta^2)) sin^2(pi t sqrt(f_R^2 + delta^2)), the expected dips are about 16.5% at 5 MHz detuning and 6.0% at 10 MHz detuning. Since the scan step is 5 MHz, any resonance inside the scan range should usually have a nearest sampled point within 2.5 MHz and therefore should remain close to the full contrast-scale dip.

Measured data comparison:
- The paired combined contrast (readout2 - readout1)/readout1 has mean -0.26% and standard deviation 3.31% across scan points.
- The most negative combined point is only -4.91% at 3.850 GHz; nearby behavior is not a clear resonance-shaped dip, and another shallow negative region near 3.910 to 3.925 GHz is also only about -2.6% to -4.8%.
- Per-average overlays vary substantially and are consistent with tracking/noise cadence rather than a robust repeated resonance signature; stored averages are not treated as a strong independent repeatability test.

Decision:
The expected resonant response from the active 52 ns, mod_depth 1 Rabi pulse is about a 22% fluorescence drop in readout 2 relative to the mS = 0 reference, but the observed paired changes are only a few percent and lack a convincing resonance line shape. I therefore decide that a pODMR resonance is absent in this scan.
