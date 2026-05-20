Case: podmr_027_2026-05-16-184117

I used the provided sequence XML and the raw export values, without using labels or any outside cases.

Active pulse sequence and readout roles:
- Sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first performs optical polarization, then detection. This is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the conditional m_S = +1 reference block is inactive.
- The active microwave-dependent part is one rabi_pulse_mod_wait_time call followed by detection. This is readout 2, the post-microwave readout.
- The provided sequence and active variable values give mod_depth = 1 and length_rabi_pulse = 52 ns. At 250 MHz sample rate, 52 ns rounds to 13 samples, still 52 ns.

Quantitative physical model:
- Given setup contrast C = 0.22 between m_S = 0 and m_S = +1.
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a square resonant pulse, use P_exc(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)), with tau = 52 ns and delta in Hz.
- On resonance, P_exc(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected readout ratio at resonance is R2/R1 = 1 - C * P_exc = 1 - 0.22 * 0.996 = 0.781.
- Since the scan step is 5 MHz, any resonance inside the scan should be within 2.5 MHz of a sampled point. At delta = 2.5 MHz, P_exc = 0.929, so expected R2/R1 = 0.796.
- In counts, using the mean readout 1 level of 53.79, the expected resonant drop is about 11.8 counts at a sampled resonance and about 11.0 counts at a worst-case halfway-between-points resonance.

Observed data:
- Mean readout 1 = 53.794; mean readout 2 = 52.947.
- Observed R2/R1 ratios range from 0.937 to 1.032.
- The deepest observed ratio, 0.937 at 3.835 GHz, corresponds to only a 6.3% drop, about 3.46 counts.
- That is far smaller than the expected 20.4% to 21.9% drop for the active 52 ns, mod_depth = 1 pulse if a resonance were present in this scan.
- The apparent dips are not strongly repeatable across the two stored averages; the stored averages are also not a strong independent repeatability test because they often reflect tracking cadence.

I also fit the normalized ratios to the fixed-contrast physical lineshape above. A flat-ratio model had SSE 0.01475, while the best fixed-contrast resonance model had SSE 0.01409 and placed its center outside the scan near 3.940 GHz, giving only a negligible improvement. Allowing the contrast amplitude to float put the best in-scan amplitude near 0.038, far below the expected 0.22.

Decision: resonance_absent. The active sequence should have produced a large post-pulse fluorescence loss if a pODMR resonance were present, but the measured readout ratios show only small noisy fluctuations.
