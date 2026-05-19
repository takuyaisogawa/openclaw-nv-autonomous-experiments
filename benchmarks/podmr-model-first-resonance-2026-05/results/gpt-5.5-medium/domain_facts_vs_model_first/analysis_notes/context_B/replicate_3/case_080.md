<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_080

I used the provided sequence XML as the active sequence definition. The active sequence is Rabimodulated.xml. It first polarizes and detects a true m_S = 0 reference, then because full_expt = 0 it skips the optional m_S = 1 reference block. It then applies one rabi_pulse_mod_wait_time pulse and performs the second detection. Thus readout 1 is the pre-microwave m_S = 0 reference and readout 2 is the post-Rabi-pulse signal readout. The active pulse duration is length_rabi_pulse = 52 ns and the active mod_depth is 1.

Quantitative model:

The given setup has Rabi frequency about 10 MHz at mod_depth = 1, approximately linear with mod_depth, so the relevant Rabi frequency here is 10 MHz. For a square pulse, the on-resonance transition probability is

P = sin^2(pi * f_R * tau)

with f_R = 10 MHz and tau = 52 ns. This gives

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant frequency point should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219 of the reference. The mean readout 1 level is about 45.90 counts, so the expected resonant dip in readout 2 relative to readout 1 is about 10.06 counts. Off resonance the detuned square-pulse model

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

predicts the dip should be localized to the resonance with a width set by the roughly 10 MHz Rabi rate, easily resolvable on the 5 MHz scan grid if the resonance lies in the scanned range.

Observed data:

The combined readout2 - readout1 differences across the 21 scan points range from -3.06 to +2.40 counts, with mean -0.53 counts. The most negative points are far smaller than the roughly -10 count dip expected for a resonant pi pulse under the stated contrast and Rabi-frequency calibration. The two stored averages show broad tracking offsets between averages, so I did not treat the average overlay as strong independent repeatability evidence.

Decision:

No pODMR resonance is present. The post-pulse readout lacks the quantitatively expected resonant depletion for the active 52 ns, mod_depth 1 Rabi pulse.
