Case: podmr_047_2026-05-17-001223

Active sequence and readout roles:
- The scan uses Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction flow first polarizes the NV and immediately calls detection. This is readout 1, the true ms=0 fluorescence reference.
- full_expt is 0, so the optional one-level reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) followed by detection. This is readout 2, the post-MW pODMR signal.
- The provided sequence XML and exported variable values give mod_depth = 1 and length_rabi_pulse = 5.2e-8 s. With sample_rate = 250 MHz, 52 ns is exactly 13 samples, so rounding does not change the pulse length. The embedded sequence text in raw_export.json contains an older/default mod_depth = 0.3 line, but the provided XML and active variable table both indicate mod_depth = 1.

Quantitative signal model:
- Use a square-pulse two-level Rabi model:
  P1(delta) = (Omega_R^2 / (Omega_R^2 + delta^2)) * sin^2(pi * tau * sqrt(Omega_R^2 + delta^2)),
  where frequencies are in cycles/s.
- Given the setup fact Omega_R = 10 MHz at mod_depth = 1 and tau = 52 ns:
  P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% ms=0 to ms=+1 contrast scale, the expected on-resonance readout2/readout1 ratio is
  1 - 0.22 * 0.996 = 0.781.
- For a 50-count reference this is an expected drop of about 11.0 counts.
- If the resonance were halfway between adjacent 5 MHz scan points, the nearest sampled point would be 2.5 MHz detuned. The model gives P1(2.5 MHz) = 0.929, expected ratio = 0.796, and expected drop about 10.2 counts.

Observed data comparison:
- Mean readout 1 = 50.383 counts; mean readout 2 = 50.062 counts.
- readout2/readout1 ratios have mean 0.994, standard deviation 0.0279, minimum 0.947, and maximum 1.051.
- The raw readout2 - readout1 differences have mean -0.32 counts, minimum -2.73 counts, and maximum +2.54 counts.
- No scan point approaches the expected physical ratio near 0.78 or the expected approximately 10 to 11 count fluorescence loss.
- A linear no-dip baseline fit to the normalized ratio has SSE = 0.01545. A model with the physical 22% Rabi dip forced at the best half-grid center has SSE = 0.03553, about 2.30 times worse. Letting the dip amplitude float gives a best amplitude of only 0.0655, far below the 0.22 contrast expected for the active pulse and not a credible pODMR resonance under this pulse model.

Decision:
The physically expected pODMR signal for this sequence would be a large, readily visible post-pulse fluorescence dip, but the data show only small tracking/noise-scale fluctuations. Resonance is absent.
