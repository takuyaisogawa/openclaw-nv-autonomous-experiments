Case: podmr_044_2026-05-16-232730

Sequence and roles:
- The provided XML is Rabimodulated.xml.
- Active settings from the XML are full_expt = 0, do_adiabatic_inversion = 1 but not active because the 1-level reference block is inside if abs(full_expt)>1e-12, length_rabi_pulse = 52 ns, sample_rate = 250 MHz, mod_depth = 1, mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps.
- With full_expt = 0, the executed detections are:
  1. after optical polarization, before the microwave pulse: true m_S = 0 reference;
  2. after the modulated Rabi pulse: pODMR signal readout.

Quantitative model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling, f_R = 10 MHz here.
- The rounded pulse duration is round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- For a rectangular pulse, use transition probability
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).
- On resonance, P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant signal change is -0.22 * 0.996 = -21.9% of the reference readout.
- The mean reference readout is 48.56 counts, so the expected on-resonance deficit is about -10.64 counts.
- Even if the resonance falls halfway between two 5 MHz scan points, the nearest sampled detuning is 2.5 MHz, P = 0.929, and the expected deficit is about -9.93 counts. At 5 MHz detuning it is still about -8.00 counts.

Data comparison:
- Combined readout 1 mean: 48.56.
- Combined readout 2 mean: 48.69.
- Post-pulse minus reference has mean +0.13 counts, minimum -2.42 counts, and maximum +2.06 counts.
- The most negative point is only -4.8% of the local reference, far below the expected roughly -22% resonant contrast.
- A finite-detuning rectangular-pulse fit of diff = baseline - A * P(delta) gives a best drop amplitude A about 2.06 counts, with positive excursions of comparable size elsewhere. This is much smaller than the expected 10.6-count pi-pulse deficit and is not a credible pODMR resonance signature.

Decision:
The active pulse should produce a large negative post-pulse readout feature if a resonance is present in the swept range. The observed differences are small, sign-changing, and consistent with drift/noise rather than the expected contrast. Therefore I classify this case as resonance_absent.
