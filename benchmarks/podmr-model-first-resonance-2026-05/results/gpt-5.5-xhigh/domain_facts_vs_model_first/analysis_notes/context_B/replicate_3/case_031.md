Case: podmr_016_2026-05-16-131456

I used inputs/sequence.xml and the raw export values, not labels or outside context.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the "true 0 level reference": optical polarization followed immediately by detection.
- Readout 2 is the signal readout after the active microwave Rabi pulse, followed by detection.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
The setup Rabi frequency is about 10 MHz at mod_depth = 1, so I used Omega_R = 10 MHz. For a square pulse of duration t = 52 ns, the transition probability versus detuning Delta is

P(Delta) = (Omega_R^2 / (Omega_R^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega_R^2 + Delta^2)).

On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated 22% contrast scale, the expected maximum signal/reference drop is 0.22 * 0.996 = 0.219, so the normalized signal readout should be able to fall from about 1.0 to about 0.78 near resonance.

Quantitative comparison to the data:
- Normalized signal readout = readout 2 / readout 1.
- The minimum normalized signal is 0.829 at 3.875 GHz, with adjacent values 0.868 at 3.870 GHz, 0.831 at 3.880 GHz, and 0.850 at 3.885 GHz.
- The off-feature edge median ratio is about 0.993, so the observed maximum drop is about 0.164 relative to that local baseline. This is smaller than the ideal 0.219 but well within a plausible imperfect-pulse/readout scale.
- Fitting the fixed 22% contrast Rabi response above with only center frequency and a scale factor gives best center 3.877158 GHz, scale factor 1.0029, and RMSE 0.0248 in normalized ratio.
- A flat no-resonance model gives RMSE 0.0622 in normalized ratio.
- Letting the dip amplitude float gives a fitted contrast of 0.204, close to the 0.22 expected contrast scale, with center 3.877160 GHz.

Decision:
The second readout shows a frequency-localized dip at the expected scale and width for the 52 ns, mod_depth 1 Rabi pulse, while the first readout remains a reference channel. This is consistent with a pODMR resonance being present.
