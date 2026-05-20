Case: podmr_023_2026-05-16-174219

Input files used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- SequenceName in raw export: Rabimodulated.xml.
- The provided sequence XML is a Rabi-modulated pODMR sequence varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active variables from the executed export table: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, delay_wrt_1mus = 0.2 us.
- The XML instruction first polarizes and detects the optically initialized mS=0 reference, then skips the intermediate mS=+1 reference block because full_expt = 0, then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detects again.
- Therefore readout 1 is the mS=0 optical reference, and readout 2 is the post-Rabi-pulse signal readout. Stored averages are treated only as tracking-cadence views, not as strong independent repeats.

Physical model calculation:
- Given setup Rabi frequency f_R ~= 10 MHz at mod_depth = 1 and approximately linear scaling, the active pulse has f_R = 10 MHz.
- For a square resonant pulse, transferred population is P = sin^2(pi * f_R * tau), where tau = 52 ns if f_R is expressed as full Rabi-cycle frequency.
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a setup contrast scale of about 22% between mS=0 and mS=+1, the expected resonant fractional readout decrease in the post-pulse signal relative to the 0 reference is about 0.22 * 0.996 = 0.219, i.e. an expected signal/readout ratio near 0.781 at resonance.
- The mean readout 1 level is 47.55 counts, so the expected on-resonance drop is about 10.42 counts.

Data comparison:
- Mean readout 1 = 47.55, mean readout 2 = 47.69, mean readout2/readout1 = 1.003.
- The minimum readout2/readout1 ratio across the scan is 0.949 at 3.835 GHz, much smaller than the expected resonant ratio drop to about 0.781 and not localized at the strongest low-readout point in an otherwise consistent resonance pattern.
- The minimum absolute readout 2 point is 45.38 at 3.895 GHz, but its paired reference is 46.56, giving a ratio of 0.975 and only a 1.17 count decrease.
- The standard deviation of readout2 - readout1 across scan points is 1.42 counts, while the modeled resonant drop is about 10.42 counts. A true resonance under the active pulse settings should be obvious in the raw readout comparison.

Decision:
No pODMR resonance is present. The active pulse should produce nearly full population transfer at resonance, but the measured post-pulse readout remains essentially equal to the 0-reference readout throughout the sweep, with fluctuations far below the expected contrast-scale signal.
