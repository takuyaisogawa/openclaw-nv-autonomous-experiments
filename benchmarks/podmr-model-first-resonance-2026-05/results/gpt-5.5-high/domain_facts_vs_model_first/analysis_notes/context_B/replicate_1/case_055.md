Case: podmr_041_2026-05-16-224136

I used the provided sequence.xml and the raw export values without labels or external case context.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The active instructions polarize the NV, then perform detection immediately. This first readout is the mS = 0 fluorescence reference.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection. This second readout is the pODMR signal after the scanned microwave pulse.
- Active mod_depth = 1 and pulse duration = 52 ns. The sample rate is 250 MHz, so 52 ns is exactly 13 samples after rounding.

Physical signal model:
- Given f_Rabi = 10 MHz at mod_depth = 1 and approximately linear scaling, the active Rabi frequency is f_R = 10 MHz.
- For a square pulse with detuning Delta in Hz, I modeled the mS = +1 transfer probability as
  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
- At Delta = 0 and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% contrast scale between mS = 0 and mS = +1, the expected normalized signal readout on resonance is 1 - 0.22 * 0.996 = 0.781, i.e. about a 21.9% dip in readout 2 relative to the mS = 0 reference.
- The observed mS = 0 reference mean is 46.354 counts, so the expected on-resonance drop is about 10.16 counts, to roughly 36.2 counts. Since the scan step is 5 MHz, a resonance inside the scan range would be within 2.5 MHz of a sampled point; the same model still predicts a near-pi-pulse dip of about 20% at that nearest point.

Data check:
- Combined readout 1 mean = 46.354 counts, standard deviation = 0.459 counts.
- Combined readout 2 mean = 46.142 counts, standard deviation = 1.363 counts.
- The normalized readout 2/readout 1 ratios have mean 0.9955, standard deviation 0.0310, minimum 0.9437 at 3.895 GHz, and maximum 1.0484.
- The deepest combined dip is only 5.6% relative to readout 1, much smaller than the expected 21.9% dip and not localized with the fixed-contrast Rabi lineshape.
- A fixed 22% contrast Rabi model gives a worse residual than a flat ratio model; its best placement is at the scan edge and predicts a 0.781 ratio at resonance, which is not observed.
- Allowing the amplitude to float gives a best dip amplitude of about 0.053 rather than the expected 0.22, consistent with ordinary point-to-point readout scatter rather than the expected pODMR response.
- The stored averages have different offsets, consistent with tracking cadence, so I do not treat them as a strong independent repeatability test.

Decision:
The expected quantitative pODMR signal for the active sequence is a large readout-2 dip from an almost-pi pulse. The measured trace lacks such a dip and is better described as small fluctuations around the reference. I therefore decide that a pODMR resonance is absent.
