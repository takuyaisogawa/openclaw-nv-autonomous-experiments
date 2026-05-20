Case podmr_072_2026-05-17-085551

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instruction path first polarizes the NV and performs detection. This is the bright m_S = 0 reference readout.
- full_expt is 0, so the optional "Acquire 1 level reference" branch is inactive; there is no separate stored dark reference from that branch.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), followed by detection. This is the microwave-pulsed signal readout.
- Therefore readout 1 is the bright/reference readout and readout 2 is the post-microwave signal readout.
- Provided sequence.xml values: length_rabi_pulse = 52 ns, mod_depth = 1, mw_freq scan 3.825 to 3.925 GHz in 5 MHz steps. The raw export also embeds the same active sequence structure; its stored template text shows mod_depth = 0.3, but the exported Variable_values and the standalone sequence.xml provided for this case list mod_depth = 1.

Quantitative model:
- Use the driven two-level response for a square microwave pulse:
  P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * t),
  where Omega / 2pi = 10 MHz * mod_depth and t = 52 ns.
- The optical readout contrast scale is 22%, so the expected fractional signal reduction in the pulsed readout is 0.22 * P1(delta), relative to the m_S = 0 reference.
- With mod_depth = 1, Omega / 2pi = 10 MHz. On resonance, theta = 2*pi*10e6*52e-9 = 3.267 rad, P1 = sin^2(theta/2) = 0.996. The expected resonant optical dip is 0.22*0.996 = 21.9%, or about 11 counts for a 50-count bright readout.
- Even using the raw-export template value mod_depth = 0.3 as a conservative cross-check, Omega / 2pi = 3 MHz gives theta = 0.980 rad, P1 = 0.222, and the expected on-resonance optical dip is 4.87%, or about 2.4 counts for a 50-count bright readout.

Observed data:
- Combined readout 1 mean = 50.17, readout 2 mean = 49.54.
- Pointwise readout2/readout1 mean = 0.9877 with standard deviation 0.0239.
- Pointwise readout2-readout1 mean = -0.63 counts with standard deviation 1.20 counts.
- The largest apparent suppression occurs at the high-frequency scan edge, 3.925 GHz, with readout2/readout1 = 0.952 and readout2-readout1 = -2.44 counts. Nearby points do not form a clear resonance-shaped dip: 3.910 GHz is high (ratio 1.023), 3.915 GHz is near baseline (0.991), and 3.920 GHz is 0.970.

Decision:
- For the active mod_depth = 1 sequence, a real resonance should produce a large, localized approximately 22% pulsed-readout reduction, much larger than the observed fluctuations. No such feature is present.
- The endpoint-only low value is not enough to establish a resonance shape, and stored averages are not a strong independent repeatability test because they can reflect tracking cadence.
- I therefore decide resonance_absent.
