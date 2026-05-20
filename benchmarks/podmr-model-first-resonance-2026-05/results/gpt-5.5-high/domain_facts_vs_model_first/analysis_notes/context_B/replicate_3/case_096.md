Case podmr_082_2026-05-17-111957

I used the provided sequence XML and raw export, without using labels or sibling cases.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions first polarize the NV and call detection; the XML comment identifies this as "Acquiring true 0 level reference". This is readout 1, the m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. There is no independent m_S = +1 reference in this run.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is readout 2, the post-Rabi-pulse signal readout.
- mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given the setup fact f_Rabi ~= 10 MHz at mod_depth = 1, the square-pulse transition probability versus detuning is
  P1(df) = (f_Rabi^2 / (f_Rabi^2 + df^2)) * sin^2(pi * sqrt(f_Rabi^2 + df^2) * tau),
  with f_Rabi and df in cycles/s and tau = 52 ns.
- On resonance, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the m_S = 0 to m_S = +1 contrast scale of 22%, a full resonance should reduce the signal readout by about 0.22 * 0.996 = 21.9% relative to the m_S = 0 reference.
- The mean readout 1 level is 50.38 counts, so the expected on-resonance dip in readout 2 is about 11.04 counts, giving an expected signal near 39.34 counts.
- The scan step is 5 MHz. Even if the resonance center falls halfway between sampled points, df = 2.5 MHz at the nearest point gives P1 = 0.929 and an expected dip of about 10.30 counts. At df = 5 MHz, the expected dip is still about 8.30 counts.

Data comparison:
- Measured readout 1 mean = 50.38 counts, readout 2 mean = 50.03 counts.
- The measured signal-minus-reference differences have mean -0.35 counts, standard deviation 1.53 counts, minimum -3.46 counts, and maximum +2.65 counts.
- The minimum normalized signal/reference ratio is 0.934, a 6.6% dip. The expected resonance ratio at the nearest scan point should be about 0.796 or lower for a resonance within the sweep range, which is far larger than observed.
- Fitting the expected square-pulse line shape over possible resonance centers does not find a positive-contrast dip consistent with the model; the best unconstrained fit prefers the opposite sign near 3.870 GHz.
- The stored averages are not treated as a strong repeatability test because they can reflect tracking cadence, but the combined raw readouts still lack the amplitude required by the physical model.

Decision: resonance_absent. The active pulse is essentially a pi pulse for this setup, so a pODMR resonance in the scanned range should produce an order-10-count dip in readout 2 relative to the m_S = 0 reference; the observed deviations are only a few counts and do not match the expected line shape.
