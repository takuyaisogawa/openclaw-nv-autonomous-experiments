Sequence and readout roles

The provided sequence is Rabimodulated.xml. The active instructions first polarize and detect a true m_S = 0 reference, then wait. The m_S = +1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion is true. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth and performs the second detection. Thus readout 1 is the m_S = 0 reference and readout 2 is the signal after the modulated Rabi pulse.

Relevant pulse parameters

The stored scan variables give length_rabi_pulse = 52 ns and mod_depth = 1. The sample rate is 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical expectation

Using the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the driven population transfer versus detuning can be modeled as

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * tau),

where Omega is in cycles/s and tau = 52 ns. On resonance this gives

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant signal/readout-reference ratio is therefore lower by about

0.22 * 0.996 = 0.219,

so a real resonance from this pulse should appear as an approximately 22% dip in readout 2 relative to readout 1 near resonance, broadened on the order of the 10 MHz Rabi rate.

Data calculation

I normalized the signal readout by the 0-reference readout at each scan point. The signal/reference ratios are:

3.825 GHz 1.0047
3.830 GHz 1.0137
3.835 GHz 0.9954
3.840 GHz 1.0175
3.845 GHz 0.9111
3.850 GHz 0.9705
3.855 GHz 0.9695
3.860 GHz 0.9798
3.865 GHz 1.0422
3.870 GHz 0.9898
3.875 GHz 1.0177
3.880 GHz 1.0209
3.885 GHz 1.0325
3.890 GHz 1.0041
3.895 GHz 0.9913
3.900 GHz 1.0028
3.905 GHz 0.9955
3.910 GHz 0.9710
3.915 GHz 0.9935
3.920 GHz 1.0431
3.925 GHz 0.9920

The lowest normalized point is 0.911 at 3.845 GHz, an 8.9% drop from unity. A least-squares fit of ratio = baseline - A * P1(delta) over possible center frequencies gives the best center near 3.848 GHz, baseline 1.009, and fitted contrast A = 0.065. This is only about 30% of the physically expected 0.219 contrast. A model with the contrast fixed to the expected 0.22 gives SSE = 0.01668, only slightly better than a flat ratio model with SSE = 0.01719, and its best center is pushed outside the scan range. The free-amplitude fit improves the SSE to 0.00995, but only by using a much smaller contrast than the sequence and calibration predict.

Decision

The data contain a small low feature near 3.845 to 3.855 GHz, but the explicit Rabi/contrast model predicts a much deeper pODMR dip for this 52 ns, mod_depth 1 pulse. Because the expected 22% normalized drop is not present and the fixed physical model does not meaningfully outperform a flat baseline, I classify this case as resonance_absent.
