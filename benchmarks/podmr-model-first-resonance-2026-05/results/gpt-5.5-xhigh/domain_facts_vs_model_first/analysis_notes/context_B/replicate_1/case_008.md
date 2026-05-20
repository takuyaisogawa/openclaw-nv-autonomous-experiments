Case podmr_014_2026-05-12-081841

Input sequence and active roles:

- Sequence: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" branch is inactive despite do_adiabatic_inversion being true.
- There are two active detections per repetition. Readout 1 is the true m_S = 0 bright reference after optical pumping. Readout 2 is the signal after the Rabi-modulated microwave pulse.
- The active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 5.2e-8 s. At sample_rate = 250 MHz this is exactly 13 samples, so the active pulse duration remains 52 ns.
- mod_depth = 1 from the provided sequence XML and the exported active Variable_values.

Quantitative expected-signal model:

Use the stated setup values: contrast C = 0.22 between m_S = 0 and m_S = +1, and resonant Rabi frequency f_R = 10 MHz at mod_depth = 1. For a square pulse with detuning df in cycles/s, the transition probability is

P1(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * t * sqrt(f_R^2 + df^2)).

At resonance, t = 52 ns gives

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Thus a resonance in the scanned range should produce an expected fractional readout-2 dip of

C * P1(0) = 0.22 * 0.996 = 0.219.

At the observed bright-reference scale mean(readout 1) = 46.62 raw units, that corresponds to about 10.22 raw units of suppression in the signal readout. The detuned Rabi model has an approximate half-maximum width of 15.2 MHz for this pulse, so the 5 MHz scan step should sample a strong dip if the resonance is present in range.

Data comparison:

- Combined readout 1 mean = 46.62, standard deviation = 1.14.
- Combined readout 2 mean = 46.32, standard deviation = 1.08.
- The readout-2/readout-1 ratio has mean 0.9938 and minimum 0.9370, a maximum observed normalized dip of about 5.7% from the ratio mean.
- The largest raw readout-2 suppression relative to readout 1 is 3.13 units, much smaller than the approximately 10.22 units expected for this pulse.
- A least-squares fit of the fixed physical model with C = 0.22 does not explain a dip in the scan interior; when forced to use the expected contrast at candidate interior dips, it predicts ratios near 0.80 where the observed ratios are about 0.94 to 0.96.
- Allowing the contrast amplitude to float gives a best apparent fractional contrast of about 0.038, far below the expected 0.219.
- The two stored averages have ratio minima at different frequencies (3.865 GHz and 3.905 GHz), consistent with tracking/noise variations rather than a stable pODMR feature. These averages are not treated as a strong independent repeatability test.

Decision:

The active sequence should create a large, resolvable readout-2 dip on resonance, but the measured data only show small, non-repeating fluctuations. I therefore classify this case as resonance absent.
