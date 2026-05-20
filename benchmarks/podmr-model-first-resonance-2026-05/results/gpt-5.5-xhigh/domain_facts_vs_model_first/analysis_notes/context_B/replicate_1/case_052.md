Sequence and roles

The XML sequence is Rabimodulated.xml with mw_freq as the scanned variable from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active path has full_expt = 0, so the "1 level reference" block is skipped despite do_adiabatic_inversion = 1. The executed sequence is:

1. Polarize.
2. Detect the bright m_S = 0 reference. This is readout 1.
3. Wait.
4. Apply rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1.
5. Detect after the microwave pulse. This is readout 2, the pODMR signal.

The sample rate is 250 MHz, so the rounding in the XML gives round(52 ns * 250 MHz) = 13 samples, or exactly 52 ns.

Quantitative model

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is approximately 10 MHz and the bright-to-dark fluorescence contrast scale is about 22%. For a rectangular microwave pulse, the expected transfer probability versus detuning is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

with f_R = 10 MHz and t = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Thus an on-resonance pODMR point should have readout2/readout1 approximately

1 - 0.22 * 0.996 = 0.781,

or about a 21.9% drop. With the measured reference level near 46.57 counts, this is an expected drop of about 10.20 counts.

Because the scan step is 5 MHz, any resonance lying inside the scan range should be within at most 2.5 MHz of a sampled point. The same model gives:

- delta = 0 MHz: P = 0.996, expected drop = 10.20 counts.
- delta = 2.5 MHz: P = 0.929, expected drop = 9.52 counts.
- delta = 5 MHz: P = 0.749, expected drop = 7.67 counts.

Observed data comparison

The combined readout means are readout1 = 46.568 and readout2 = 46.231. The mean readout2/readout1 ratio is 0.993. Across the 21 scan points, readout2 - readout1 ranges from -2.788 to +1.808 counts, with the largest observed drop equal to 2.788 counts at 3.845 GHz. That largest drop is only about 6.0%, far below the approximately 20-22% drop expected at the nearest sampled point for an in-range resonance.

A least-squares comparison also disfavors the physical resonance model. The null model readout2 = alpha * readout1 has RMS residual 1.14 counts. A fixed-contrast resonance model constrained to place the resonance inside the scanned frequency range has best RMS residual 2.51 counts, substantially worse, because it requires a large dip that is not present. If the contrast is allowed to float, the best fitted contrast scale is only about 0.049 rather than the expected 0.22.

Stored averages show different absolute count levels, consistent with tracking cadence, but neither average contains a stable 20% pODMR-scale dip.

Decision

The active pulse should produce a large, broad, easily visible pODMR dip if a resonance were present within this scan. The measured readout2 trace stays close to the reference readout and the quantitative model fit does not support an in-range resonance. I therefore classify this case as resonance_absent.
