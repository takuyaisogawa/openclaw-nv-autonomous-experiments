Case: podmr_069_2026-05-17-081236

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence name in the export: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence XML, full_expt = 0, so the "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is set.
- Readout 1 is the first detection immediately after adj_polarize, so it is the bright m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time, so it is the pODMR signal after the microwave pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1.
- With sample_rate = 250 MHz, the pulse length rounds to 13 samples / 250 MHz = 52 ns, unchanged.

Explicit model calculation:
- Given the setup fact f_Rabi = 10 MHz at mod_depth = 1, the active pulse has f_Rabi = 10 MHz.
- For a square pulse, the transition probability versus detuning df is:
  P(df) = (f_Rabi^2 / (f_Rabi^2 + df^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + df^2)).
- On resonance with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the given m_S = 0 to m_S = +1 contrast scale C = 0.22, the expected signal/reference ratio on resonance is:
  1 - C * P(0) = 0.781.
- The expected resonant drop is therefore 21.9% of readout 1. The mean readout 1 level is 46.686 counts, so the expected drop is about 10.23 counts.
- The 5 MHz frequency grid is fine enough for this pulse: even if the resonance lies halfway between two sampled points, P(2.5 MHz) = 0.929 and the expected ratio is 0.796, still about a 20.4% drop.

Observed quantitative comparison:
- Combined readout 1 mean = 46.686 counts; readout 2 mean = 46.582 counts.
- The readout2/readout1 ratio has mean 0.998, standard deviation 0.029, and minimum 0.911.
- The deepest observed signal drop is at 3.845 GHz: readout 1 = 48.231, readout 2 = 43.942, ratio = 0.911, drop = 8.89% or 4.29 counts.
- This is less than half of the expected 21.9% resonant drop for the active 52 ns, mod_depth 1 pulse.
- A fixed 22% contrast square-pulse resonance model with free center frequency in the scanned interval fits worse than no resonance: SSE for ratio = 1 is 0.0173, while the best fixed-contrast resonance gives SSE = 0.0769 at 3.8481 GHz.
- If the resonance amplitude is allowed to float, the best fitted contrast amplitude is only 5.1%, far below the expected 22% scale.
- The two stored averages have different overall baselines, consistent with tracking cadence, so I used the normalized readout2/readout1 comparison rather than treating the averages as a strong repeatability test.

Decision:
The physical model predicts a large near-pi-pulse pODMR dip that is not present in the normalized data. I therefore classify this scan as resonance_absent.
