Case podmr_021_2026-05-16-171244.

Used only the provided XML/raw export for this case. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect, giving readout 1 as the true m_S = 0 bright reference. Because full_expt = 0, the optional m_S = 1 reference branch is skipped. The active experimental branch is then one rabi_pulse_mod_wait_time pulse followed by detection, so readout 2 is the pulse-affected readout. The relevant pulse parameters are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, switch_delay = 100 ns.

Quantitative expected signal model:

Given the stated calibration, Rabi frequency at mod_depth = 1 is about 10 MHz, scaling linearly with mod_depth. For a resonant square pulse of duration T = 52 ns, the transition probability is

P_1(Delta=0) = sin^2(pi * Omega_R * T)

with Omega_R = 10 MHz. This gives pi * Omega_R * T = 1.6336 rad and P_1 = 0.996. With the setup contrast between m_S = 0 and m_S = +1 of about 22%, a resonant point should reduce the pulsed readout by about 0.22 * 0.996 = 21.9% of the bright readout. The mean reference readout is 46.49 counts, so the expected on-resonance drop is about 10.19 counts, putting readout 2 near 36.3 counts if the pulse is resonant and the model applies.

I also evaluated the detuned square-pulse response

P_1(Delta) = (Omega_R^2 / (Omega_R^2 + Delta^2)) * sin^2(pi * sqrt(Omega_R^2 + Delta^2) * T)

at the sampled frequency points. If the resonance were near a sampled point such as 3.880 GHz, the expected pulsed-readout drop would be about 10.2 counts at the center and about 7.7 counts one 5 MHz step away. Thus a true resonance in this scan range should produce a large, localized decrease of readout 2 relative to readout 1 over one to several scan points.

Observed data:

Readout 1 mean = 46.49 counts, standard deviation across scan points = 1.03.
Readout 2 mean = 46.41 counts, standard deviation across scan points = 1.24.
The pointwise difference readout2 - readout1 has mean -0.074 counts, standard deviation 1.21 counts, minimum -2.27 counts, and maximum +1.81 counts.

The largest observed pulsed-readout deficit is only 2.27 counts, far below the approximately 10-count deficit expected from the calibrated pulse model for a resonance. Around the visually low region near 3.880 to 3.885 GHz the deficits are only about 1.08 and 1.19 counts, while neighboring points do not form the expected square-pulse resonance profile. Stored averages differ substantially in slow baseline/tracking behavior, so I did not treat them as a strong independent repeatability test.

Decision: resonance_absent. The active pulse sequence and calibrated Rabi/contrast model predict a much larger and more structured readout-2 suppression than is present in the raw data.
