Case podmr_082_2026-05-17-111957 analysis.

I used only the provided isolated inputs. The provided sequence XML is Rabimodulated.xml. Its active instructions polarize the NV, take a detection, wait, skip the optional "Acquire 1 level reference" branch because full_expt = 0, apply one rabi_pulse_mod_wait_time pulse, and take a second detection. Therefore readout 1 is the bright m_S = 0 optical reference after polarization, and readout 2 is the signal after the scanned microwave Rabi pulse. The active microwave pulse has length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz, mod_depth = 1, and the scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:

For a rectangular resonant Rabi pulse, with the supplied setup fact f_R = 10 MHz at mod_depth = 1 and linear scaling, the active Rabi frequency is 10 MHz. The on-resonance transfer probability is

P_1(0) = sin^2(pi f_R tau)
       = sin^2(pi * 10e6 * 52e-9)
       = 0.996.

Using the supplied contrast scale of 22% between m_S = 0 and m_S = +1, a true resonance should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219 of the bright reference. With a bright readout near 50 counts, the expected resonant signal is about 50 * (1 - 0.219) = 39.0 counts, a drop of about 11 counts relative to readout 1.

I also evaluated the finite-detuning rectangular-pulse response

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi tau sqrt(f_R^2 + delta^2)).

This gives expected contrast drops of 21.9% at 0 MHz detuning, 20.4% at 2.5 MHz, 16.5% at 5 MHz, 6.0% at 10 MHz, 1.1% at 20 MHz, and 0.7% at 50 MHz. Since the scan step is 5 MHz, an in-range resonance should create a pronounced one- or few-point dip in readout 2 relative to readout 1.

Data comparison:

The combined readout 1 mean is 50.38 counts and readout 2 mean is 50.03 counts. The normalized ratio readout2/readout1 has mean 0.993, standard deviation 0.029, and minimum 0.934. The largest negative point-by-point difference is -3.46 counts at 3.850 GHz, far smaller than the approximately -11 count resonant drop expected from the active pulse. The lowest absolute readout 2 value is 47.90 at 3.905 GHz, but its corresponding normalized ratio is 0.951, still much higher than the approximately 0.81 expected at resonance.

I fit the same rectangular-pulse response to the normalized readouts. With the physical 22% contrast fixed and the resonance center constrained inside the scan, the best fit still predicts a normalized minimum near 0.811 and has RMS residual 0.058, worse than an absent-resonance constant model RMS of 0.029. Allowing the contrast amplitude to float does not recover a physical dip: the best fit chooses a negative contrast amplitude, meaning the data around the best center look more like a small peak than a dip.

Conclusion:

The active pulse sequence should produce a large, easily visible resonant dip if a pODMR resonance were present within the scanned frequency range. The observed fluctuations are only a few counts, are not consistent with the expected line shape or amplitude, and stored averages are not a strong independent repeatability test. I therefore decide that a pODMR resonance is absent.
