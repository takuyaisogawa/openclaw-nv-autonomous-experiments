<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_057 analysis

Sequence identification:
- Provided sequence file is Rabimodulated.xml.
- Active branch: full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- Readout roles: readout 1 is the true m_S = 0 reference after optical polarization; readout 2 is the detection after the Rabi-modulated microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples after rounding.
- mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical signal model:
Use the square-pulse two-level Rabi response

P_transfer(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * t)

with Omega = 10 MHz at mod_depth = 1, pulse duration t = 52 ns, and optical contrast scale C = 0.22 between m_S = 0 and m_S = +1. A resonant transition should reduce the post-pulse fluorescence relative to the 0-reference by C * P_transfer.

Quantitative expected signal:
- On resonance, P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected resonant fractional drop = 0.22 * 0.996 = 0.219.
- With the measured readout 1 baseline near 47.11 counts, the expected on-resonance dip is about 10.32 counts.
- At 5 MHz detuning, expected fractional drop is about 0.165, or 7.76 counts.
- At 10 MHz detuning, expected fractional drop is about 0.060, or 2.83 counts.

Observed data:
- readout 1 mean = 47.11 counts; readout 2 mean = 47.55 counts.
- readout2 - readout1 mean = +0.44 counts, standard deviation = 0.92 counts.
- Normalized (readout2 - readout1) / readout1 mean = +0.0095, standard deviation = 0.0196.
- The most negative normalized point is only -0.0243 at 3.885 GHz, far smaller than the approximately -0.219 resonant expectation and not shaped like the model.
- A least-squares fit y = baseline - A * P_transfer gives best A = -0.036, i.e. the opposite sign from a fluorescence dip. A fixed A = 0.22 model is much worse than a flat baseline.

Decision:
The active sequence and pulse settings should produce a large pODMR dip if the sweep crosses a resonance. The data show no such dip, only small tracking/noise-scale fluctuations. Therefore the pODMR resonance is absent.
