Active sequence and readout interpretation

The scan is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the "Acquire 1 level reference" branch is inactive. The executed readouts are therefore:

1. readout 1: after adj_polarize and before the microwave pulse, a true m_S = 0 optical reference.
2. readout 2: after one modulated Rabi microwave pulse, the pODMR signal readout.

The active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The XML/variable values give length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model

Using the supplied setup scale, the Rabi frequency is f_R = 10 MHz at mod_depth = 1. For a rectangular resonant pulse of duration t = 52 ns,

theta = 2*pi*f_R*t = 2*pi*10e6*52e-9 = 1.04*pi.

The on-resonance transition probability is therefore

P0 = sin^2(theta/2) = sin^2(0.52*pi) = 0.996.

With the supplied m_S = 0 to m_S = +1 contrast scale C = 0.22, the expected on-resonance normalized fluorescence drop in readout 2 relative to readout 1 is

C*P0 = 0.22*0.996 = 0.219.

For finite detuning I used the driven two-level rectangular-pulse model

P(delta_f) = (Omega^2/(Omega^2 + Delta^2))*sin^2(0.5*t*sqrt(Omega^2 + Delta^2)),

where Omega = 2*pi*10 MHz and Delta = 2*pi*delta_f. If the resonance were centered at 3.880 GHz, the expected normalized contrast profile at 3.870, 3.875, 3.880, 3.885, and 3.890 GHz would be approximately 0.060, 0.165, 0.219, 0.165, and 0.060. In counts, using the observed readout 1 levels, this corresponds to roughly 3.0, 8.0, 10.9, 8.1, and 2.9 counts of drop.

Observed data check

The measured normalized contrast (readout1 - readout2)/readout1 has mean 0.010, standard deviation 0.034, and maximum 0.075 at 3.880 GHz. Around that maximum, the measured contrasts are:

3.870 GHz: -0.008
3.875 GHz: -0.013
3.880 GHz: 0.075
3.885 GHz: 0.003
3.890 GHz: -0.019

This does not match the expected pi-pulse resonance shape. The central point is about one third of the expected 0.219 contrast, and the two adjacent 5 MHz points, which should still be large drops near 0.165, are essentially absent or negative.

I also fit the measured contrast to the same rectangular-pulse profile. A baseline-only model has RMSE 0.0338. The best in-range fixed-amplitude physical model with C = 0.22 has RMSE 0.0625, worse than baseline-only. Allowing a nonnegative fitted amplitude improves only slightly to RMSE 0.0326 with amplitude 0.0308, far below the expected 0.22 contrast scale. The unconstrained best fit prefers a negative amplitude, which is not a physical pODMR dip.

Decision

Given the active 52 ns, mod_depth = 1 pulse, a real resonance should produce a large, structured readout-2 dip. The observed readout differences are small, isolated, and not consistent with the expected physical lineshape. I therefore classify this case as resonance_absent.
