Case: podmr_016_2026-05-12-120649

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The sequence is Rabimodulated.xml / Rabimodulated.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- The active detections are therefore:
  1. readout 1: after optical polarization, a true m_S = 0 / no-microwave reference.
  2. readout 2: after one modulated Rabi microwave pulse, the pODMR signal readout.
- The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding to the sample grid gives 13 samples = 52 ns.
- mod_depth = 1 from the provided sequence XML and exported variable values.

Quantitative expected signal model:
- Given domain fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Thus f_R = 10 MHz for this sequence.
- For a square pulse, the transition probability versus detuning is modeled as
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau),
  using f_R and Delta in cycles/s and tau in seconds.
- On resonance with tau = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fractional drop in the signal readout relative to the no-microwave reference is about
  0.22 * 0.996 = 0.219, or 21.9%.
- At a reference level near 26 raw-count units, this corresponds to an expected dip of about 5.7 raw-count units in readout 2 relative to readout 1.
- The model is still broad enough that if a resonance fell halfway between 5 MHz-spaced scan points, P(2.5 MHz) = 0.929 and the expected dip would still be about 20.4%, or about 5.3 counts.
- At 5 MHz detuning, P(5 MHz) = 0.749 and the expected dip is still about 16.5%, or about 4.3 counts.

Observed data check:
- readout 1 is the reference and readout 2 is the post-pulse signal, so I compared readout2/readout1 across the scan.
- The observed ratios range from about 0.9467 to 1.0963.
- The largest observed negative excursion is only about 5.3%, corresponding to about 1.37 raw-count units, much smaller than the expected 21.9% / 5.7-count resonant response.
- The low points are not accompanied by the neighboring-point structure expected from the finite-width Rabi response. For example, a resonance near 3.915 GHz would predict a ratio near 0.84 at the center and still depressed neighboring points, but the observed ratio there is about 0.947 and nearby points include higher values rather than a coherent dip.
- A least-squares check of ratio = linear baseline - A * P(Delta) over in-range resonance centers preferred a negative A, i.e. a bump rather than a dip. For a fixed physical amplitude A = 0.219, the best in-range resonance model fits worse than the simple baseline.

Decision:
The active pulse should produce a large, readily visible pODMR dip if the scan crossed resonance. The measured post-pulse signal does not show the required amplitude or coherent Rabi-response shape. I therefore decide that a pODMR resonance is absent.
