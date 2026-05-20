Case podmr_042_2026-05-16-225623

I used the sequence embedded in raw_export.json as the active pulse sequence snapshot. The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executable part is:

- adj_polarize, then detection: this is the true m_S = 0/reference readout, reported as readout 1.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 0.3, then detection: this is the microwave-affected pODMR readout, reported as readout 2.

The standalone sequence.xml has default-like values including mod_depth = 1, but the saved experiment's active sequence text shows mod_depth = 0.3. I therefore used mod_depth = 0.3 for the physical expectation.

Quantitative model:

Given the domain fact f_R ~= 10 MHz at mod_depth = 1, linear scaling gives f_R ~= 3 MHz at mod_depth = 0.3. For a resonant rectangular pulse of duration t = 52 ns, the two-level transfer probability is

P = sin^2(pi f_R t) = sin^2(pi * 3e6 * 52e-9) = 0.222.

With the setup contrast scale between m_S = 0 and m_S = +1 of about 22%, the expected resonant fluorescence reduction in the pulsed readout is

0.222 * 0.22 = 0.0487, or about 4.9%.

The mean combined raw readout level is 46.79 counts, so the expected resonant dip size is about

46.79 * 0.0487 = 2.28 raw-count units.

Data comparison:

The average of the two stored readouts has its deepest point at 3.875 GHz, the scan center and the saved mw_freq value, with value 44.45 counts. A linear detrend of the combined average leaves the 3.875 GHz point as the strongest negative residual, -2.34 counts. The local depth versus neighboring points is about 3.04 counts in the combined average.

Because readout 1 is the pre-pulse reference and readout 2 is the post-pulse measurement, readout 2 is the more direct pODMR channel. At 3.875 GHz readout 2 is 43.54 counts, while neighboring readout 2 values at 3.870 and 3.880 GHz are 47.83 and 46.85 counts. This gives a local readout-2 dip of about 3.80 counts, close to and somewhat larger than the 2.28-count model expectation. The point is also close to the mw_freq center 3.8751 GHz recorded in the active sequence.

The stored averages show substantial drift/tracking structure, so I do not treat the two averages as a strong independent repeatability test. Even with that limitation, the expected model signal size and the observed center-frequency post-pulse dip are consistent with a pODMR resonance.

Decision: resonance_present.
