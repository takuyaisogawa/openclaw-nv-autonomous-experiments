Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The executed instruction path first performs adj_polarize, then detection, then wait_for_awg. Since full_expt = 0, the optional mS = +1 reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. Therefore readout 1 is the pre-microwave polarized mS = 0 fluorescence reference, and readout 2 is the post-microwave signal readout after the Rabi pulse.

The relevant pulse parameters from the provided XML/raw variable values are:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- scanned mw_freq = 3.825 to 3.925 GHz in 5 MHz steps
- full_expt = 0, so there is no active +1 calibration readout

Expected physical signal calculation

Given the supplied setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant rectangular Rabi pulse, the transition probability is

P = sin^2(pi * f_R * t).

With f_R = 10 MHz and t = 52 ns:

f_R * t = 10e6 * 52e-9 = 0.52 cycles
P = sin^2(pi * 0.52) = 0.996

The current mS = 0 to mS = +1 contrast scale is about 22%, so an on-resonance pODMR response should produce an approximate fractional fluorescence drop of

0.22 * 0.996 = 0.219, or about 22%.

Using the standard detuned Rabi response

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

a resonance centered near the low point at 3.895 GHz should also produce large drops at neighboring 5 MHz offsets. The predicted fractional drops are approximately:
- 3.890 GHz: -16.5%
- 3.895 GHz: -21.9%
- 3.900 GHz: -16.5%
- 3.885 and 3.905 GHz: about -6.0%

Data comparison

I normalized the post-microwave signal by the pre-microwave reference as readout2/readout1 - 1. The observed normalized values around the candidate feature are:
- 3.885 GHz: -0.69%
- 3.890 GHz: -1.60%
- 3.895 GHz: -5.27%
- 3.900 GHz: -2.11%
- 3.905 GHz: -0.90%

Across all 21 points, the normalized contrast has mean -0.13% and standard deviation 2.39%. The largest dip is only -5.27%, and it is not accompanied by the broad neighboring response expected from the 52 ns, mod_depth = 1 pulse. A least-squares fit allowing the resonance amplitude to float gives an amplitude of only about 4.8%, far below the expected physical contrast of about 22%. A fixed-contrast physical model with C = 0.22 fits substantially worse than a flat baseline.

Decision

The isolated low point near 3.895 GHz is much smaller and narrower than the expected pODMR signal for this pulse. Because stored averages mainly reflect tracking cadence rather than a strong repeatability test, the single-point dip is not sufficient evidence. I decide that a pODMR resonance is absent.
