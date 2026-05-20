Case podmr_051_2026-05-17-011109

Sequence and roles:
- The active sequence is Rabimodulated.xml.
- The active branch has full_expt = 0, so the optional mS = +1 reference block is skipped.
- The first detection after adj_polarize is therefore the mS = 0 reference readout.
- The second detection is after rabi_pulse_mod_wait_time and is the pODMR signal readout.
- The provided sequence XML uses mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this remains 52 ns after rounding.

Physical model calculation:
- The setup Rabi frequency is approximately 10 MHz at mod_depth = 1.
- For a rectangular Rabi pulse, the resonant transition probability is P = sin^2(pi * f_R * tau).
- With f_R = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% mS = 0 to mS = +1 contrast scale, the expected on-resonance readout reduction is 0.22 * 0.996 = 0.219, or about 21.9%.
- For a reference level near 48 raw counts, that corresponds to an expected dip of about 10.5 counts for an ideal resonant point.
- Using the off-resonant rectangular-pulse expression P(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)), the expected drops at 48 counts are about 7.9 counts at 5 MHz detuning, 2.9 counts at 10 MHz detuning, and 0.5 counts at 20 MHz detuning.

Observed data:
- The scan covers 3.825 to 3.925 GHz in 5 MHz steps.
- Combined readout 1 mean/std is 48.33/1.11 counts.
- Combined readout 2 mean/std is 47.86/1.13 counts.
- The largest reference-normalized dip, (readout1 - readout2) / readout1, is 0.092 at 3.895 GHz.
- At this point readout 1 is 50.0 counts and readout 2 is 45.38 counts, a drop of 4.62 counts.
- The same point is the largest normalized dip in both stored averages: about 10.0% in average 1 and 8.5% in average 2. These averages are not treated as strong independent repeatability tests because stored averages can reflect tracking cadence, but their agreement supports that the feature is not purely from one stored trace.

Decision:
The observed dip is smaller than the ideal 21.9% pi-pulse contrast predicted from the simple model, but it has the correct readout role, sign, frequency-localized shape, and appears consistently at 3.895 GHz in both stored averages. I therefore classify this case as resonance_present with low-to-moderate practical confidence, while noting that the measured contrast is substantially reduced relative to the ideal expected signal.
