Case podmr_058_2026-05-17-053345.

I used the provided sequence.xml and the raw export values. The active sequence is Rabimodulated.xml with full_expt = 0, so the "Acquire 1 level reference" block is skipped. The active readout roles are therefore:

- readout 1: bright m_S = 0 reference, after adj_polarize and before any microwave pulse.
- readout 2: signal readout after the Rabi-modulated microwave pulse.

Active pulse parameters from sequence.xml:

- mod_depth = 1
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns
- scan variable = mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps

Physical model calculation:

The setup Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so this sequence should have f_R = 10 MHz. For a square pulse, the driven transition probability at detuning Delta is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * T * sqrt(f_R^2 + Delta^2))

with T = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

The m_S = 0 to m_S = +1 contrast scale is about 22%, so an on-resonance point should reduce readout 2 relative to readout 1 by about 0.22 * 0.996 = 21.9%, giving an expected readout2/readout1 ratio near 0.781. With the 5 MHz scan grid, a resonance lying between scan points should still be within 2.5 MHz of a sampled point. At 2.5 MHz detuning the model gives P = 0.929, or an expected fractional drop of 20.4%, ratio about 0.796. At 5 MHz detuning the expected ratio is still about 0.835.

Observed data:

- combined readout1 mean = 45.681, readout2 mean = 45.584
- combined readout2 - readout1 mean = -0.097 with standard deviation 1.834
- combined readout2/readout1 mean = 0.998
- minimum combined readout2/readout1 ratio = 0.931, at 3.890 GHz, with similar shallow fluctuations elsewhere

The per-average traces show shallow dips at some points, but stored averages here mainly reflect tracking cadence. They do not provide a strong independent repeatability test. More importantly, the active-pulse model predicts a much larger near-resonant response than any observed dip. A real resonance within this scan should have produced a point around 0.78 to 0.80 in readout2/readout1, while the deepest combined point is only 0.931 and the mean difference is essentially zero.

Decision: resonance_absent.
