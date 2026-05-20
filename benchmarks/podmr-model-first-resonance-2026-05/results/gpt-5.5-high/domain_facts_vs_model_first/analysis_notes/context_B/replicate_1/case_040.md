Case: podmr_026_2026-05-16-182622

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png for visual cross-check only

Sequence interpretation:
- Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence, varying mw_freq.
- The instructions first polarize the NV and immediately perform detection. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The second active readout follows rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so readout 2 is the signal after the microwave Rabi pulse.
- Extracted pulse settings from the provided XML/export values: mod_depth = 1, length_rabi_pulse = 5.2e-08 s = 52 ns, sample_rate = 250 MHz. The rounded duration is still 52 ns because 52 ns * 250 MHz = 13 samples.

Explicit model calculation:
- Domain fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for this measurement.
- For a square resonant pulse, the transferred m_S = +1 population is P = sin^2(pi * f_R * t).
- With t = 52 ns: P = sin^2(pi * 10e6 * 52e-9) = 0.996057.
- Domain fact: the m_S = 0 to m_S = +1 contrast scale is about 22%.
- The mean m_S = 0 reference readout is 49.6108 counts. A resonant 52 ns pulse should therefore darken the post-pulse readout by about 49.6108 * 0.22 * 0.996057 = 10.8713 counts.
- Expected on-resonance post-pulse readout is therefore about 38.7395 counts, or normalized readout2/readout1 about 0.7809.

Observed data comparison:
- Mean readout 1 = 49.6108 counts.
- Mean readout 2 = 49.5833 counts.
- Mean readout2 - readout1 = -0.0275 counts, with point-to-point standard deviation 1.4711 counts.
- The darkest observed combined point has readout2 - readout1 = -3.0962 counts, equivalent to only 5.94% normalized dark contrast.
- Observed normalized readout2/readout1 ranges from 0.9406 to 1.0654, nowhere near the expected 0.7809 on-resonance value.

Frequency-domain model check:
- I evaluated a square-pulse detuned response P(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)) over candidate resonance frequencies across the scan.
- With the physical contrast fixed at 22%, the best candidate resonance gives RSS = 0.09734 in normalized readout2/readout1, worse than a flat no-resonance model RSS = 0.01753.
- If the contrast amplitude is allowed to float, the best fit only wants an effective contrast of 4.38%, far below the expected 22% for this setup and this nearly pi pulse.

Decision:
- The active pulse should produce a large pODMR dip if a resonance is present in the scanned range.
- The measured readout 2 does not show the expected darkening relative to the m_S = 0 reference, and the fixed physical model is strongly inconsistent with the data.
- Stored averages are not treated as a strong independent repeatability test; they mainly support that the visible variations are tracking/noise-scale, not a 22% resonance response.

Conclusion: resonance_absent.
