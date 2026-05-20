Case: podmr_057_2026-05-17-051839

I used only the provided local inputs for this case. The active pulse sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first runs adj_polarize and detection to acquire a true m_S = 0 fluorescence reference, then waits. The optional "Acquire 1 level reference" block is skipped because full_expt = 0, so no independent m_S = +1 calibration readout is acquired in this scan. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns, followed by the second detection. Therefore readout 1 is the pre-microwave m_S = 0 reference and readout 2 is the post-pulse signal readout. The do_adiabatic_inversion flag is not active because the skipped full_expt block is not entered.

Quantitative model:

For a square resonant pulse on a two-level transition, I used

P_transfer(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with frequencies in cycles/s, t = 52 ns, contrast C = 0.22, and f_R = 10 MHz * mod_depth = 10 MHz. The expected post-pulse fluorescence is reference * (1 - C * P_transfer).

At exact resonance, P_transfer = sin^2(pi * 10 MHz * 52 ns) = 0.9961, so the expected fluorescence drop is 0.22 * 0.9961 = 0.2191, about 21.9 percent. The mean readout 1 reference is 45.455 counts, so this corresponds to an expected dip of about 9.96 counts in readout 2. Even if the resonance lay halfway between two 5 MHz scan points, the largest sampled transfer probability would be about 0.929, giving an expected dip of about 9.29 counts.

Observed data:

Readout 1 mean/min/max/std = 45.455 / 43.654 / 46.923 / 0.972 counts.
Readout 2 mean/min/max/std = 45.420 / 43.827 / 47.750 / 1.283 counts.
The readout2/readout1 ratio has mean 0.9993, minimum 0.9550, maximum 1.0395, and standard deviation 0.0216. Thus the largest observed pointwise post-pulse suppression is only about 4.5 percent, or about 2.04 counts after fitting a global readout scale.

I also compared an explicit fixed-contrast resonance model to a no-resonance model. The no-resonance model readout2 = a * readout1 gives a = 0.99917, SSE = 19.40, RMSE = 0.96 counts. Scanning the resonance center anywhere inside the measured frequency range and fitting only the global scale gives the best fixed-contrast resonance model at the scan edge, with SSE = 140.79 and RMSE = 2.59 counts, which is 7.26 times worse than the no-resonance model. The expected resonant dip is therefore absent from the data.

Decision: resonance_absent.
