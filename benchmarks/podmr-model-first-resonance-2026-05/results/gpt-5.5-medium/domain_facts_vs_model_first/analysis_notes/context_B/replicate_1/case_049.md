Case podmr_035_2026-05-16-210045 analysis note

Sequence identification:
- Active sequence: Rabimodulated.xml / rabi_pulse_mod_wait_time with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout roles from the XML instructions:
  - readout 1 is the first detection after adj_polarize, before any microwave pulse, so it is the true mS=0 / bright reference.
  - full_expt is 0, so the optional mS=1 reference branch is inactive.
  - readout 2 is the detection after the active Rabi-modulated microwave pulse, so it is the pODMR signal readout.
- Pulse parameters used for the decision: mod_depth = 1, length_rabi_pulse = 52 ns, sample_rate = 250 MHz, rounded pulse duration remains 52 ns.

Quantitative physical model:
The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse with detuning delta, I used

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz and t = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated 22% contrast between mS=0 and mS=+1, the expected pODMR resonance at this pulse length is therefore an approximately

0.22 * 0.996 = 0.219

fractional decrease of the signal readout relative to the mS=0 reference, if a resonance is in the swept frequency range.

Observed data comparison:
The observed signal/reference ratios readout2/readout1 are:

0.9775, 0.9435, 1.0216, 0.9898, 0.9687, 0.9823, 0.9738, 1.0198, 0.9455, 0.9944, 0.9835, 0.9869, 0.9858, 0.9757, 0.9993, 0.9962, 1.0150, 0.9896, 0.9728, 0.9729, 0.9563.

The full observed ratio span is about 0.078, far smaller than the approximately 0.219 fractional on-resonance dip expected from the active pulse model. A free fit of the square-pulse resonance template to the ratio data gives a positive coefficient (+0.0296) rather than the negative coefficient required for a fluorescence dip. A known-contrast 22% dip model fits much worse than a simple weak baseline/trend model, because the data do not contain the predicted deep localized decrease.

Decision:
The active sequence should produce a large readout2 dip relative to readout1 on resonance, but the measured ratios show only small scatter/drift and no quantitatively compatible dip. I therefore decide that a pODMR resonance is absent.
