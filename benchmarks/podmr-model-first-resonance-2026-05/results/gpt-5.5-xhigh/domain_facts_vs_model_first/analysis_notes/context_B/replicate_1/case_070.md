Case: podmr_056_2026-05-17-050447

I used the provided sequence XML and the exported numeric readouts only.

Active sequence and roles:
- The active sequence is Rabimodulated.xml with `full_expt = 0`, so the conditional 1-level reference block is inactive.
- The executed cycle is: optical polarization, detection, wait, one modulated Rabi pulse, detection, wait.
- Therefore readout 1 is the true m_S = 0 reference after optical pumping, and readout 2 is the signal after the microwave pulse.
- `mod_depth = 1`.
- `length_rabi_pulse = 5.2e-08 s`; at the 250 MHz sample rate it rounds to 13 samples, still 52 ns.

Quantitative model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant pulse rotation is pi * f_R * t = pi * 10e6 * 52e-9 = 1.6336 rad in the sin^2 convention.
- Resonant transfer probability is sin^2(1.6336) = 0.996.
- With the setup contrast scale C = 0.22, an on-resonance pi pulse should reduce readout 2 relative to readout 1 by about C * 0.996 = 0.219, or 21.9%.
- For a square pulse, I used
  P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),
  with Omega = 2*pi*10 MHz and t = 52 ns. This gives expected contrast of 21.9% at zero detuning, 20.4% at 2.5 MHz detuning, 16.5% at 5 MHz detuning, 6.0% at 10 MHz detuning, and 1.1% at 20 MHz detuning.
- Since the scan step is 5 MHz, any resonance inside the scanned range should put at least one sampled point within 2.5 MHz of resonance and should produce about a 20% readout-2 deficit, with visible shoulders at neighboring points.

Data comparison:
- Combined readout 1 mean = 43.77 and readout 2 mean = 43.93; readout 2 is not globally lower.
- The normalized ratio readout2/readout1 has mean 1.0043 and point-to-point standard deviation 0.0323.
- The largest combined readout-2 deficit is at 3.900 GHz: (readout1 - readout2) / readout1 = 0.0572, only 5.7%.
- Neighboring points do not show the required pulse response: at 3.895 GHz the deficit is 0.09%, and at 3.905 GHz readout 2 is higher than readout 1 by 3.1%.
- A fixed-contrast 22% finite-pulse model fit within the sweep is much worse than a constant-ratio null model (RSS 0.0780 vs 0.0209). A nonnegative contrast fit within the sweep prefers only about 3.9% contrast, far below the expected 22%.

Decision:
The data do not contain the quantitative signature expected for a pODMR resonance under the active pulse sequence. The apparent small point deficits are at the noise/drift scale and lack the required finite-pulse line shape, so I decide resonance_absent.
