Case: podmr_076_2026-05-17-095337

Sequence interpretation:

The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. From the provided sequence XML, length_rabi_pulse is 52 ns and mod_depth is 1. The full_expt variable is 0, so the "Acquire 1 level reference" branch is inactive.

Readout roles:

Readout 1 is the true bright m_S = 0 reference: adj_polarize followed by detection before the microwave probe pulse.

Readout 2 is the pODMR signal readout: a modulated Rabi microwave pulse with length 52 ns and mod_depth 1, followed by detection. A resonance should therefore appear as readout 2 dropping below readout 1.

Quantitative expected signal model:

Use a driven two-level model for the addressed m_S = 0 to m_S = +1 transition. With the stated setup, the Rabi frequency is approximately

f_R = 10 MHz * mod_depth = 10 MHz.

For a square pulse of duration tau = 52 ns, the transfer probability at detuning delta is

P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

On resonance, P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated 22% fluorescence contrast, the expected resonant fractional drop is

0.22 * 0.996 = 0.219, or about 21.9%.

The bright reference mean is 51.03 raw counts, so an on-resonance point should lose about

51.03 * 0.219 = 11.18 counts.

Even if the line center falls halfway between scan points, the nearest point is only 2.5 MHz detuned. The same model gives P_1(2.5 MHz) about 0.929, so the expected drop would still be about 20.4%, or about 10.4 counts.

Observed data:

Mean readout 1 = 51.03 counts.
Mean readout 2 = 50.82 counts.
Mean readout2 - readout1 = -0.21 counts.
Standard deviation across scan points of readout2 - readout1 = 1.42 counts.
The deepest normalized loss is about -5.2%, with readout2 - readout1 about -2.73 counts at 3.825 GHz and about -2.63 counts at 3.905 GHz.

Decision:

The observed losses are far smaller than the 10 to 11 count drop expected from the active 52 ns, mod_depth 1 near-pi pulse. The small troughs are comparable to point-to-point fluctuation and tracking-scale variation, and the stored averages should not be treated as a strong independent repeatability test. I therefore classify this scan as resonance_absent.
