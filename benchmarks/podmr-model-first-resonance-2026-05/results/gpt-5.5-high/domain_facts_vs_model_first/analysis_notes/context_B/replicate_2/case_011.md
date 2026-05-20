Case: podmr_028_2026-05-13-100213

Active sequence and readout roles:
- The provided sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first polarizes the NV and immediately performs detection. This is the bright-state m_S = 0 reference readout.
- full_expt = 0, so the separate "Acquire 1 level reference" branch is inactive despite do_adiabatic_inversion being true.
- The active signal operation is then one rabi_pulse_mod_wait_time pulse followed by detection. This second readout is the microwave-pulsed signal readout.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse duration remains 52 ns.
- mod_depth = 1 in the provided XML and active variable values.

Physical model calculation:
- Given setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For a rectangular resonant Rabi pulse, the population transfer probability is
  P(delta) = Omega^2/(Omega^2 + delta^2) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),
  using Omega and delta as cycle frequencies in Hz.
- With Omega = 10 MHz and t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance signal drop in readout2/readout1 is 0.22 * 0.996 = 0.219, or about 21.9%.
- At +/-5 MHz detuning the same model gives P = 0.749, for an expected drop of about 16.5%; at +/-10 MHz it gives P = 0.273, for an expected drop of about 6.0%. Therefore, a resonance within the scan should appear as a clear, physically shaped multi-point depression, not only a one-point fluctuation.

Observed quantitative comparison:
- The relevant normalized observable is readout2/readout1, since readout1 is the bright-state reference in the same scan point.
- The mean readout2/readout1 ratio is 0.985.
- The minimum ratio is 0.873 at 3.905 GHz, corresponding to a 12.7% apparent drop.
- Neighboring ratios are 0.936 at 3.900 GHz and 1.018 at 3.910 GHz. A true 10 MHz Rabi-line response centered near 3.905 GHz would predict substantial drops on both neighboring 5 MHz points.
- A constant-ratio model has SSE = 0.07458. A Rabi-line fit with frequency and amplitude free but amplitude constrained to the physical contrast range improves SSE only to 0.06717 and selects an effective amplitude of 0.066, far below the expected 0.219. Forcing the physical 0.219 resonant amplitude does not identify a credible in-scan line.
- Stored per-average traces are not treated as strong independent repeatability evidence, but the combined normalized trace itself lacks the expected amplitude and line shape.

Decision:
The data do not show a quantitatively consistent pODMR resonance. The lone dip near 3.905 GHz is too shallow and too narrow/asymmetric compared with the expected 52 ns, mod_depth = 1 Rabi response.
