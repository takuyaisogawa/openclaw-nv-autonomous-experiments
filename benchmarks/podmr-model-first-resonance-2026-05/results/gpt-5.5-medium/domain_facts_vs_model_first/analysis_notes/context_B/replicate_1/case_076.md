Case podmr_062_2026-05-17-063134

I used the provided sequence XML, not prior labels or sibling cases. The active pulse sequence is Rabimodulated.xml / Rabimodulated: it polarizes the NV, detects the true m_S = 0 level, waits, then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection of the pulsed state. The full_expt variable is 0, so the optional "Acquire 1 level reference" block is inactive. Thus the two readouts are: readout 1 = m_S = 0 optical reference after polarization, and readout 2 = signal after the modulated microwave pulse. The relevant pulse duration is length_rabi_pulse = 52 ns, and mod_depth = 1 in the provided XML.

Quantitative model:

The supplied setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For this case, f_R = 10 MHz and tau = 52 ns. Using the standard driven two-level rectangular-pulse response in cycles/s,

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

On resonance, P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996. With the stated current setup contrast scale of 22% between m_S = 0 and m_S = +1, the expected on-resonance pODMR fluorescence decrease in the active readout is 0.22 * 0.996 = 0.219, or about 21.9%. At the observed active-readout level of about 49.44 counts, this corresponds to an expected resonant dip of about 10.8 counts. At detunings of 5 MHz and 10 MHz the same model predicts about 16.5% and 6.0% fractional dips respectively, so a real resonance sampled on this 5 MHz grid should produce a clear broad depression with a very large central point if the resonance lies within the scan.

Data comparison:

The scan covers 3.825 to 3.925 GHz in 5 MHz steps. The combined readout statistics are:

- readout 1 mean 49.41, standard deviation 1.15, range 46.98 to 51.23
- readout 2 mean 49.44, standard deviation 0.87, range 47.25 to 50.87
- readout2/readout1 mean 1.001, standard deviation 0.0247, minimum 0.937

The deepest normalized active-readout point is at 3.920 GHz: readout 1 = 50.40, readout 2 = 47.25, ratio = 0.937, a 6.3% drop relative to readout 1. That is far smaller than the 21.9% on-resonance signal expected for a 52 ns pulse at mod_depth 1, and it is not supported by the adjacent 3.925 GHz point, where the ratio returns to about 1.009. The stored averages are only two and can reflect tracking cadence, so I do not treat per-average variation as a strong repeatability test.

Decision: resonance_absent. The active readout does not show the quantitatively expected pODMR response for the XML pulse parameters.
