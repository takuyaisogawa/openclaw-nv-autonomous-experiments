Case podmr_049_2026-05-17-004217

Active sequence and roles:
- The scan uses Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes and detects a true m_S = 0 reference. This is readout 1.
- full_expt = 0, so the optional m_S = 1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection. This is readout 2, the microwave-pulse signal readout.
- The active values are mod_depth = 1 and length_rabi_pulse = 52 ns. At 250 MS/s this rounds to 52 ns.

Expected scale:
- With the stated setup, Rabi frequency is about 10 MHz at mod_depth = 1, so the Rabi period is about 100 ns and a pi pulse is about 50 ns.
- The 52 ns pulse is therefore approximately a pi pulse. If the microwave sweep hits a real pODMR resonance, the post-pulse readout should show a clear fluorescence drop relative to the m_S = 0 reference, on a scale comparable to the available contrast. The stated m_S = 0 to m_S = +1 contrast scale is about 22%, which would be roughly an 11-count effect around a 50-count baseline for strong inversion.

Observed data:
- Combined readout 2 minus readout 1 is small and changes sign across the scan.
- The largest combined negative deviations are about -2.6 counts near 3.850 GHz and about -2.2 counts near 3.855 GHz, only about 5% of the reference level.
- There are also positive deviations of similar or larger magnitude, including about +3.5 counts near 3.890 GHz.
- The two stored averages show large baseline offsets consistent with tracking cadence. Their readout-difference features are not a clean repeatable resonance signature; negative excursions appear at different points and are interspersed with positive excursions.

Decision:
Given a near-pi pulse at full modulation depth, a real resonance should create a much clearer post-pulse PL dip relative to the true m_S = 0 reference. The observed deviations are too small, sign-changing, and not cleanly repeatable relative to the expected contrast scale. I therefore classify this case as resonance_absent.
