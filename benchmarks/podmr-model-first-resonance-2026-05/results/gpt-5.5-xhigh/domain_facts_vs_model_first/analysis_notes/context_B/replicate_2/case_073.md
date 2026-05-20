Analysis note for podmr_059_2026-05-17-054846

Sequence identification:

The provided sequence is Rabimodulated.xml. The active path is:

1. adj_polarize for 1 us.
2. detection: readout 1, the bright mS = 0 reference after optical polarization.
3. wait_for_awg for 2 us.
4. The "Acquire 1 level reference" block is skipped because full_expt = 0.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns.
6. detection: readout 2, the frequency-dependent readout after the microwave/Rabi pulse.
7. wait_for_awg for 1 us.

The sample rate is 250 MHz, so round(52 ns * 250 MHz) = 13 samples and the active pulse remains 52 ns. The microwave scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:

The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1. For a square pulse, using frequencies in cycles/s,

P1(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * T * sqrt(f_R^2 + detuning^2)).

With f_R = 10 MHz and T = 52 ns, the on-resonance transfer probability is sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated 22% mS = 0 to mS = +1 contrast, an on-resonance point should reduce readout 2 relative to the bright reference by about 0.22 * 0.996 = 21.9%. Because the scan step is 5 MHz, any resonance whose center lies inside the scan would have at least one sampled point with P1 >= 0.929, implying at least a 20.4% normalized dip.

Observed data:

The combined readout means are readout 1 = 42.670 and readout 2 = 42.108. The normalized ratio readout2/readout1 has mean 0.987, standard deviation 0.025, and minimum 0.936 at 3.880 GHz. The largest raw drop is therefore 2.865 counts, or 6.4% of the local readout 1 level. If a resonance were centered at 3.880 GHz, the fixed model would predict readout 2 = 34.78 counts from the local readout 1 value, while the observed readout 2 is 41.67 counts.

I also fit the detuned Rabi lineshape to the normalized ratios. A constant-ratio model has RMSE 0.0247. The fixed physical model with f_R = 10 MHz, T = 52 ns, contrast = 22%, and a resonance constrained inside the scan has RMSE 0.0560, worse because it predicts a deep dip that is not present. Allowing only a nonnegative apparent dip amplitude inside the scan gives an apparent amplitude of 0.0416 against an expected 0.2188, about 19% of the expected response. The best fixed-contrast fit over a wider center range moves the center outside the scan and produces only a weak edge response.

The per-average traces show large baseline shifts consistent with tracking cadence: average 0 has ratio mean 0.979 and average 1 has ratio mean 0.998, with their minima at different scan points. I do not treat those stored averages as a strong independent repeatability test, but they also do not show the required deep near-pi-pulse notch.

Decision:

Given the active 52 ns, mod_depth = 1 pulse, the expected pODMR response is a roughly 20-22% dip at at least one sampled point for any in-scan resonance. The measured ratios only show a small few-percent fluctuation and do not match the fixed physical model. I therefore classify this case as resonance_absent.
