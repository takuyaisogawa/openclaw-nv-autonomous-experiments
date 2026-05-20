Case: podmr_004_2026-05-16-005019

I used the provided sequence XML to identify the active sequence and readout roles before deciding. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect, then skip the "1 level reference" block because full_expt = 0, then apply rabi_pulse_mod_wait_time and detect again. Therefore readout 1 is the optically polarized m_S = 0 reference, and readout 2 is the signal after the microwave Rabi pulse. The pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 52 ns; at 250 MHz sample rate this is 13 samples, so rounding leaves it at 52 ns.

Physical model calculation:

For a square microwave pulse, with Rabi frequency f_R and detuning df in cycles/s,

P_transfer(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * t * sqrt(f_R^2 + df^2)).

The setup facts give f_R about 10 MHz at mod_depth = 1. With t = 52 ns,

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance readout-2 reduction relative to readout 1 is

0.22 * 0.996 = 0.219, or about 8.85 counts for a 40.4 count reference.

Observed combined readouts:

- At 3.875 GHz, readout1 = 41.2885 and readout2 = 32.4231, giving ratio 0.7853 and fractional drop 0.2147.
- At 3.880 GHz, readout1 = 40.4231 and readout2 = 31.8077, giving ratio 0.7869 and fractional drop 0.2131.
- Away from the central feature, the median readout2/readout1 ratio excluding 3.870 to 3.885 GHz is 0.9751, so the central excess ratio drop is about 0.19.

If the resonance center is between the two deepest grid points, around 3.8775 GHz, the same square-pulse model predicts readout2/readout1 ratios of about 0.796 at +/-2.5 MHz and 0.888 at +/-7.5 MHz. The observed ratios at 3.875/3.880 GHz are about 0.786, and the neighboring ratios at 3.870/3.885 GHz are 0.868 and 0.881, which is consistent with that model at the measurement grid spacing.

The two stored averages both show a central dip, but I do not treat the averages as a strong independent repeatability test because stored averages can reflect tracking cadence. The decision rests on the active readout roles and the quantitative agreement between the expected near-pi-pulse contrast and the observed readout-2 dip.

Decision: a pODMR resonance is present.
