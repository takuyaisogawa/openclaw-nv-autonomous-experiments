Case podmr_023_2026-05-16-174219.

Inputs used: inputs/sequence.xml and inputs/raw_export.json. The active sequence is Rabimodulated.xml. The instruction path first polarizes and detects the true m_S = 0 reference, then skips the m_S = +1 reference branch because full_expt = 0, then applies one rabi_pulse_mod_wait_time pulse and detects again. Thus the two active readout roles are:

- readout 1: polarized m_S = 0 reference detection before the microwave pulse.
- readout 2: detection after the modulated Rabi pulse.

The standalone sequence.xml lists length_rabi_pulse = 52 ns and mod_depth = 1. The saved sequence embedded in raw_export.json for this run lists length_rabi_pulse = 52 ns and mod_depth = 0.3, while Variable_values also contains mod_depth = 1. I evaluated both because the decision should not hinge on that ambiguity.

Physical model calculation:

Use Rabi frequency f_R = 10 MHz * mod_depth. For a square resonant pulse of duration t = 52 ns, the transferred population is

P_1 = sin^2(pi * f_R * t).

The fluorescence contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional change of the post-pulse readout relative to the pre-pulse reference is approximately

Delta PL / PL = -0.22 * P_1.

For mod_depth = 1:

f_R = 10 MHz, pi * f_R * t = 1.6336 rad, P_1 = 0.996, expected Delta PL / PL = -0.219, or about -10.5 counts for a 48 count baseline.

For mod_depth = 0.3:

f_R = 3 MHz, pi * f_R * t = 0.4901 rad, P_1 = 0.222, expected Delta PL / PL = -0.0487, or about -2.34 counts for a 48 count baseline.

Observed combined readouts:

- readout 1 mean = 47.55, standard deviation across scan points = 1.05.
- readout 2 mean = 47.69, standard deviation across scan points = 1.00.
- readout2 - readout1 mean = +0.14 counts, standard deviation = 1.46 counts.
- Relative difference mean = +0.34%, standard deviation = 3.09%.
- The largest negative relative difference is -5.06% at 3.835 GHz, but the programmed center region around 3.875 GHz is not a dip: at 3.875 GHz readout2 - readout1 = +3.15 counts (+6.78%).

For a true pODMR resonance with the given sequence, the post-pulse readout should show a negative feature at the resonant microwave frequency. The expected signal is either very large if mod_depth = 1 or still a roughly 5% negative contrast if mod_depth = 0.3. The observed data instead has no centered negative feature; the strongest center-point feature has the opposite sign, and isolated negative points elsewhere are comparable to the point-to-point noise and not supported by the physical resonance model.

Decision: resonance_absent.
