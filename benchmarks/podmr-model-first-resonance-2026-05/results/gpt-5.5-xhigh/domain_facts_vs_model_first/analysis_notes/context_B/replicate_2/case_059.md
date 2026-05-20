Case podmr_045_2026-05-16-234216

Sequence interpretation:

The active XML sequence is Rabimodulated with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction order is:

1. adj_polarize for 1 us.
2. detection: this is the true mS = 0 optical reference, corresponding to readout 1.
3. wait_for_awg for 2 us.
4. The optional "Acquire 1 level reference" block is skipped because full_expt = 0. The do_adiabatic_inversion boolean is therefore not active for the acquired data.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
6. detection: this is the post-microwave-pulse readout, corresponding to readout 2.
7. final wait.

Thus the relevant pODMR observable is whether readout 2 is reduced relative to readout 1 as a function of scanned microwave frequency.

Quantitative physical model:

Use the supplied setup facts: contrast between mS = 0 and mS = +1 is approximately C = 0.22, and the Rabi frequency is approximately f_R = 10 MHz at mod_depth = 1. For a square resonant microwave pulse of duration T = 52 ns, the expected transferred population versus detuning df is

P1(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * T * sqrt(f_R^2 + df^2)).

The expected fractional optical reduction in readout 2 is C * P1(df).

Numerical values:

- On resonance, P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996, so the expected fractional dip is 21.9%.
- Because the scan step is 5 MHz, any resonance inside the scan range should be within 2.5 MHz of a sampled point. At df = 2.5 MHz, P1 = 0.929 and the expected fractional dip is 20.4%.
- With the measured readout-1 mean of 48.85 counts, the expected on-resonance dip is about 10.7 counts.
- Even at df = 5 MHz, the model still predicts a 16.5% dip, about 8.0 counts.

Measured data check:

The combined readout-1 mean is 48.85 counts and the combined readout-2 mean is 48.77 counts. The pointwise contrast estimate (readout1 - readout2) / readout1 has mean 0.14%, standard deviation 2.09%, minimum -5.10%, and maximum +3.65%. The largest observed readout-2 suppression is 1.83 counts at 3.845 GHz, far below the approximately 10-count suppression expected from a mod_depth = 1, 52 ns near-pi pulse on resonance. Several high-frequency points show the opposite sign, with readout 2 brighter than readout 1.

A least-squares comparison to the resonant square-pulse model also does not support a resonance: fixing the expected contrast at 22% gives a much worse fit than a flat baseline, while allowing the contrast amplitude to float prefers a negative amplitude near the high-frequency edge, meaning a brightening rather than the expected dark resonance.

Decision:

No pODMR resonance is present in this scan. The expected resonance signature for the active pulse parameters is large and broad enough that it should be unmistakable on this frequency grid, but the observed readout-2/readout-1 differences are small, noisy, and not shaped like the physical model.
