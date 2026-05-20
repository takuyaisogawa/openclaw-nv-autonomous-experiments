Case: podmr_067_2026-05-17-074342

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, sibling cases, previous outputs, or external context.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml; the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML has full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- There are therefore two active detections:
  1. readout 1 follows adj_polarize and is the bright m_S = 0 reference.
  2. readout 2 follows one rabi_pulse_mod_wait_time pulse and is the microwave-sensitive pODMR signal.
- The active pulse settings from the provided XML / variable values are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the sequence rounding keeps 52 ns exactly.

Quantitative expected-signal model:
Using the supplied setup facts, the on-resonance Rabi frequency is about 10 MHz at mod_depth = 1. For a square microwave pulse, the transfer probability is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * tau * sqrt(Omega^2 + delta^2)),

where Omega and delta are in cycles/s and tau is the pulse duration. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance fractional dip in the second readout relative to the bright reference is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean bright reference readout is 48.92 counts, so the expected on-resonance readout-2 suppression is about

48.92 * 0.219 = 10.7 counts.

Observed data check:
- readout 1 mean = 48.920 counts, standard deviation across scan = 0.804 counts.
- readout 2 mean = 48.757 counts, standard deviation across scan = 1.250 counts.
- readout2 - readout1 has mean -0.163 counts, standard deviation 1.568 counts, minimum -2.346 counts.
- The normalized apparent contrast, 1 - readout2/readout1, has mean 0.0030, standard deviation 0.0323, and maximum 0.0477.

Thus the deepest observed normalized dip is only 4.8%, corresponding to about 2.35 counts, far below the approximately 21.9% / 10.7-count dip predicted for the active near-pi pulse.

I also compared the scan to the explicit square-pulse detuning response above. Fitting contrast = offset + A * P(delta) over possible resonance centers gives the best center near 3.8845 GHz, but with A = 0.0455 instead of the expected A = 0.22. Holding A fixed at the expected 0.22 gives almost no improvement over a constant null model. The weak feature near 3.88-3.89 GHz is therefore much too small for the active physical sequence and is not a convincing pODMR resonance.

Decision: resonance_absent.
