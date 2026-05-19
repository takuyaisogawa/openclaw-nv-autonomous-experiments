<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_094

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, scanned mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active exported sequence values are the relevant values: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0.
- Because full_expt = 0, the optional m_S = +1 reference block is skipped. The two stored readouts are therefore the initial polarized m_S = 0 detection reference and the detection after the Rabi-modulated microwave pulse.

Physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, the active pulse has f_R = 10 MHz.
- For a resonant square Rabi pulse, P(+1) = sin^2(pi * f_R * tau).
- With tau = 52 ns, pi * f_R * tau = 1.6336 rad and P(+1) = 0.9961, essentially a pi pulse.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant normalized fluorescence drop is 0.22 * 0.9961 = 0.2191, or about 11.3 raw-readout units around the observed 51.7-count baseline.

Data/model comparison:
- The observed mean readouts are 51.671 for readout 1 and 51.700 for readout 2, with mean difference +0.028 rather than a negative post-pulse drop.
- The normalized ratio readout2/readout1 has mean 1.0007, point-to-point noise estimate about 0.0134, minimum 0.9654 at 3.895 GHz, and full observed span only 0.0644.
- The deepest observed suppression is therefore about 3.5%, far below the approximately 21.9% drop predicted for an on-resonance pi pulse.
- I also fit the detuned square-pulse Rabi transition model P = (f_R/f_eff)^2 sin^2(pi f_eff tau), f_eff = sqrt(f_R^2 + detuning^2), to the normalized data. An unconstrained baseline-plus-amplitude fit preferred an amplitude of -0.032, the wrong sign for a pODMR dip. A fixed 22% contrast fit only improved over a flat model by placing the resonance outside the scan, where the expected tail is weak.

Decision:
The active pulse should have produced a large resonance dip if an addressed pODMR transition were present in the scan. The measured readout differences are small, noisy, and not consistent with the expected sign or magnitude of the physical model. I classify this case as resonance_absent.
