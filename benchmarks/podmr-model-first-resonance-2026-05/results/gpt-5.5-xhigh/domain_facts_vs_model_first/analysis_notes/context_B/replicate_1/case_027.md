Case: podmr_012_2026-05-16-121601

Sequence interpretation from inputs/sequence.xml:

The active sequence is Rabimodulated.xml. It first polarizes the NV and performs a detection readout before any microwave pulse; this is the true m_S = 0 bright reference. The optional m_S = +1 reference block is not active because full_expt = 0, even though do_adiabatic_inversion is set. The second active detection occurs after PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on), so readout 2 is the pODMR readout after the microwave pulse. The provided XML has length_rabi_pulse = 5.2e-08 s and mod_depth = 1. With sample_rate = 250 MHz, the pulse is rounded to 13 samples, still 52 ns.

Quantitative model calculation:

For a square microwave pulse, using the stated setup facts, f_R = 10 MHz at mod_depth = 1 and the transition probability versus detuning is

P(delta f) = f_R^2 / (f_R^2 + delta f^2) * sin^2(pi * tau * sqrt(f_R^2 + delta f^2)).

With tau = 52 ns, the on-resonance probability is sin^2(pi * 10e6 * 52e-9) = 0.996. The mean bright reference readout is 42.075 counts. Using the stated contrast scale of 22%, the expected on-resonance drop from readout 1 to readout 2 is 42.075 * 0.22 * 0.996 = 9.22 counts, or about 21.9% of the bright level.

Observed data:

The combined difference readout1 - readout2 has a localized positive feature near the center of the scan:

0.673, -0.346, 0.962, 0.500, -0.769, 0.769, 0.942, -1.115, 0.192, 5.538, 5.231, 7.308, 5.654, 1.327, -0.404, 0.096, 1.250, 2.269, 0.538, 0.038, 3.058 counts.

The largest drop is 7.31 counts at 3.880 GHz, equal to 17.7% of readout 1 at that point. This is smaller than the ideal 9.22 count prediction but close in scale for a real single-NV pODMR measurement.

I fitted the difference signal to a no-resonance linear drift model and to the physical square-pulse response with a linear drift term:

d(f) = b0 + b1 f + A P(f - f0).

The no-resonance linear model gave SSE = 108.04 and RMSE = 2.38 counts. The resonance model gave best f0 = 3.87845 GHz, A = 7.28 counts, SSE = 20.81, and RMSE = 1.08 counts. The fitted amplitude is 17.3% of the mean bright readout, about 0.79 of the ideal 22% contrast prediction. A fixed-contrast model using the 22% physical scale still strongly improves the fit, with f0 = 3.8784 GHz, SSE = 25.16, and SSE ratio 0.233 relative to the no-resonance model.

The two stored averages both show the same central depletion region, although stored averages can reflect tracking cadence and are not a strong independent repeatability test.

Decision:

The active readout roles and the square-pulse pODMR model predict a localized depletion in readout 2 relative to the m_S = 0 reference, and the observed depletion has the expected sign, frequency-localized shape, and near-expected magnitude. I decide that a pODMR resonance is present.
