Analysis note for podmr_074_2026-05-17-092418

Input use and active sequence:
- The provided sequence XML is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the XML instructions, the active readouts are:
  - readout 1: true mS = 0 reference, acquired after adj_polarize(...) and detection(...), before the microwave pulse.
  - readout 2: pulsed signal, acquired after rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...) and detection(...).
- full_expt = 0, so the separate mS = +1 reference block is disabled. do_adiabatic_inversion = 1 is therefore not active in the disabled reference block.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the pulse is rounded to 13 samples, still 52 ns.

Physical model calculation:
- Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the on-resonance Rabi frequency here is f_R = 10 MHz.
- For a square microwave pulse starting in mS = 0, I used
  P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau),
  where tau = 52 ns and delta is frequency detuning in Hz.
- On resonance, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS = 0 to mS = +1 contrast scale of 22%, the expected normalized pulsed fluorescence at resonance is
  readout2/readout1 = 1 - 0.22 * 0.996 = 0.781.
- Even if the resonance falls midway between 5 MHz scan points, the closest sampled point has P1 about 0.929 and expected readout2/readout1 about 0.796.
- With the observed reference level near 49.1 counts, that model predicts an in-scan resonant deficit of about 10.0 to 10.8 counts.

Observed data check:
- Combined readout1 mean: 49.077 counts.
- Combined readout2 mean: 48.785 counts.
- Observed readout2/readout1 ratios have mean 0.994, standard deviation 0.035, minimum 0.923 at 3.900 GHz.
- The largest combined deficit, readout1 - readout2, is 3.923 counts at 3.900 GHz, far below the expected roughly 10 count resonant deficit.
- The two stored averages show fluctuations and drift, but these averages are not treated as a strong independent repeatability test because stored averages can reflect tracking cadence.

Model comparison:
- A flat normalized baseline gives SSE = 0.0241 and RMSE = 0.0339 for readout2/readout1.
- A resonance model with the physically expected fixed contrast C = 0.22, allowing the resonance center and baseline to vary over the scan, gives best SSE = 0.0734 and RMSE = 0.0591. This is worse than the flat baseline because it predicts a much deeper dip than observed.
- Allowing the contrast amplitude to be fit with a nonnegative resonance dip gives best C about 0.048, much smaller than the expected 0.22 for this pulse and setup.

Decision:
The expected pODMR signal for this active sequence is a large readout2 dip relative to the mS = 0 reference. The measured data only show small fluctuations with no dip on the expected scale, and the quantitative resonance model is disfavored. I therefore decide that a pODMR resonance is absent.
