Case: podmr_014_2026-05-16-124559

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first optically polarizes the NV and immediately detects; this is the true mS = 0 reference readout.
- full_expt = 0, so the optional mS = 1 reference block is not executed.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection; this second readout is the pODMR signal after the microwave pulse.
- Pulse duration used after sample-rate rounding is 52 ns at 250 MS/s.

Quantitative model:
- Given f_Rabi ~= 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the driven Rabi frequency here is about 10 MHz.
- For a square resonant pulse, the transition probability is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between mS = 0 and mS = +1 is about 22%, so the expected resonant pODMR signal reduction is 0.22 * 0.996 = 0.219, or about 21.9% of the local bright signal.
- For a signal baseline near 46.7 raw counts, this corresponds to an expected dip of about 10.2 counts for a full-contrast isolated resonance, before allowing for linewidth, detuning grid placement, and measurement noise.

Observed data:
- Readout 1, the mS = 0 reference, remains around 46.9 counts with no matching dip at the candidate resonance. At 3.875 GHz it is 48.54 counts, above its mean.
- Readout 2, the post-pulse signal, has a localized minimum of 39.12 counts at 3.875 GHz.
- Using nearby non-dip signal points as baseline gives about 46.71 counts, so the observed dip depth is 7.60 counts, or 16.3%.
- The reference-normalized signal ratio at 3.875 GHz is 0.806, while the median ratio over the scan is about 0.986.
- The two stored averages both show the same central depression in the signal readout, but I treat this mainly as consistency with the tracking cadence rather than a strong independent repeatability test.

Decision:
The active physical model predicts a large signal-only pODMR dip for this near-pi pulse, and the measured data show a localized signal-channel depression near 3.875 GHz with no corresponding reference-channel artifact. The observed depth is somewhat smaller than the ideal 21.9% expectation but is of the right sign, scale, and readout role. I therefore decide that a pODMR resonance is present.
