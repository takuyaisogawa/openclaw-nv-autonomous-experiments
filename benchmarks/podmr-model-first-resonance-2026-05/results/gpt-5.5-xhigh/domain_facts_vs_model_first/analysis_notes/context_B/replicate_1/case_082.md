Case: podmr_068_2026-05-17-075825

Sequence/readout interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The first detection occurs immediately after adj_polarize, so readout 1 is the true m_S = 0 fluorescence reference.
- full_expt = 0, so the optional 1-level reference block is skipped; do_adiabatic_inversion is not active in the executed path.
- The relevant driven readout is readout 2, after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- At sample_rate = 250 MHz, the sequence rounds 52 ns to exactly 13 samples, still 52 ns.

Quantitative model:
- Given the setup calibration, f_Rabi ~= 10 MHz * mod_depth = 10 MHz.
- For a rectangular resonant drive, the expected +1 population after pulse duration tau is:
  P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),
  using f_R and detuning delta in cycles/s.
- With tau = 52 ns and f_R = 10 MHz, on resonance P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected fluorescence ratio for readout 2 relative to the m_S = 0 reference is 1 - C * P1, with C = 0.22.
- Thus on resonance the expected ratio is 0.7809, a 21.9% loss. For a median readout 1 level of 49.5 counts, this is an expected drop of about 10.85 counts.
- The frequency grid spacing is 5 MHz, so any resonance within the swept range should be within 2.5 MHz of at least one sampled point. At 2.5 MHz detuning the model gives P1 = 0.929 and an expected loss of 20.4%. Even at 5 MHz detuning the expected loss is 16.5%.

Measured comparison:
- The measured normalized contrast values 1 - readout2/readout1 range from -3.99% to +4.47%.
- The largest measured loss is at 3.855 GHz: readout1 = 51.1923, readout2 = 48.9038, ratio = 0.9553, loss = 4.47%.
- The high-frequency raw-count decrease appears in both readouts: for example readout1 falls to about 45.5 at 3.920-3.925 GHz while readout2 also falls, so this is common-mode drift rather than the predicted post-pulse-only resonance contrast.
- A flat normalized-ratio model has SSE 0.00786. A fixed 22% contrast Rabi-response model is much worse, with best sampled-center SSE 0.0655. Allowing the contrast to vary between 0 and 22% gives a best fitted contrast of only 1.9%, far below the expected setup contrast.
- I did not treat the two stored averages as strong independent repeatability evidence, because stored averages often track acquisition cadence rather than independent repeats.

Decision:
The expected driven response from the active 52 ns, mod_depth 1 pulse is a large roughly 20-22% normalized loss if a resonance is present in the sweep. The observed normalized losses are small, irregular, and dominated by common-mode drift. Therefore the pODMR resonance is absent.
