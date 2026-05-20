Case podmr_038_2026-05-16-214551

Sequence identification:
- SequenceName in raw_export.json is Rabimodulated.xml.
- The provided XML has full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active readouts are therefore:
  1. Initial polarize + detection: true mS = 0 fluorescence reference.
  2. Rabi-modulated microwave pulse + detection: signal after the scanned microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s. This is exactly 13 samples, so the active pulse duration remains 52 ns.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the on-resonance transition probability for a square pulse is
  P = sin^2(pi * f_R * tau), with tau = 52 ns.
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The contrast scale between mS = 0 and mS = +1 is about 22%.
- The measured mS = 0 reference readout mean is 46.57 counts.
- Expected on-resonance fluorescence drop in readout 2 relative to readout 1 is therefore:
  46.57 * 0.22 * 0.996 = 10.20 counts.
- Thus a real resonant point should be near readout2 - readout1 = -10.2 counts, modulo noise and slow drift.

Observed data comparison:
- Observed readout2 - readout1 has mean -0.34 counts, standard deviation about 1.17 counts, minimum -2.79 counts, and maximum +1.81 counts.
- The largest observed drop is only 27% of the expected on-resonance drop.
- A detuned square-pulse model centered at the most favorable observed point would predict a broad local pattern around that point, with values approximately [-2.8, -7.7, -10.2, -7.7, -2.8] counts across nearby 5 MHz-spaced scan points. The actual neighboring points do not show this structure.
- The per-average traces differ enough to reflect tracking/cadence fluctuations, and those stored averages are not a strong independent repeatability test.

Decision:
The active sequence should produce a large negative differential dip if a pODMR resonance were in the scan window. The measured differential signal is small, sign-changing, and lacks the expected resonance-shaped contrast. I decide resonance_absent.
