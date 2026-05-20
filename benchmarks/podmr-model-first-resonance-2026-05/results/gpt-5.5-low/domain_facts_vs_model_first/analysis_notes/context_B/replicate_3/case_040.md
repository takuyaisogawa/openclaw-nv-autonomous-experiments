Case: podmr_026_2026-05-16-182622

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with vary_prop mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first polarize, then acquire a detection readout before the microwave pulse. This is the true mS = 0 reference readout.
- full_expt = 0, so the optional mS = 1 reference block is not executed.
- The active experimental block then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second readout is the post-Rabi-pulse pODMR signal readout.
- mod_depth = 1 and length_rabi_pulse = 52 ns from the provided sequence XML / exported variable values.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1 is about 10 MHz and scales linearly with mod_depth, the relevant Rabi frequency is 10 MHz.
- For a resonant square Rabi pulse, the spin-transfer probability is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The current mS = 0 to mS = +1 contrast scale is about 22%, so an on-resonance post-pulse readout should be reduced by about 0.22 * 0.996 = 0.219, i.e. about 21.9% of the reference fluorescence.
- The measured reference baseline is about 49.61 raw counts, so the expected on-resonance signal drop is about 49.61 * 0.219 = 10.87 raw counts.

Observed data:
- Combined readout 1 mean = 49.61 counts; combined readout 2 mean = 49.58 counts.
- The pointwise post-pulse minus reference differences have mean -0.03 counts, standard deviation 1.44 counts, minimum -3.10 counts, and maximum +3.17 counts.
- The largest observed relative post-pulse deficit is only about 5.9%, much smaller than the approximately 21.9% drop predicted for a resonant 52 ns pulse at mod_depth = 1.
- Stored averages differ by a slow offset pattern consistent with tracking cadence and do not provide a strong independent repeatability check.

Decision:
The expected resonant pODMR feature should be a large post-pulse fluorescence dip relative to the reference readout, roughly 10.9 counts at this baseline. No such dip is present in the mw_freq scan; the readout differences are small, sign-changing, and noise/tracking-scale compared with the model expectation. Therefore the pODMR resonance is absent.
