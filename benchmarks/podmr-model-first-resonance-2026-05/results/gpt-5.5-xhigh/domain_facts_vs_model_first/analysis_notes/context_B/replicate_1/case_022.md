Case: podmr_007_2026-05-16-013306

Inputs inspected:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png as a visual check only

Active sequence and readout roles:
- Sequence name in the export is Rabimodulated.xml, with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize the NV, then call detection before any microwave pulse. This is readout 1, the true m_S = 0 level reference.
- full_expt = 0, so the "Acquire 1 level reference" branch is skipped. do_adiabatic_inversion is set but no active adiabatic inversion is executed in this branch.
- The active microwave operation is one rabi_pulse_mod_wait_time call followed by detection. This is readout 2, the post-Rabi-pulse signal.
- From the provided XML and exported variable values, mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MS/s, 52 ns is exactly 13 samples, so rounding does not change the pulse duration.

Quantitative physical model:
- Given setup facts: contrast between m_S = 0 and m_S = +1 is about C = 0.22, and Rabi frequency is about f_R = 10 MHz at mod_depth = 1.
- For a rectangular resonant pulse with detuning delta, using frequencies in cycles/s:

  P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

  with tau = 52 ns.

- Expected normalized post-pulse readout:

  readout2 / readout1 = 1 - C * P_transfer(delta)

- On resonance, P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961. Therefore the expected fractional readout drop is 0.22 * 0.9961 = 0.2191, so a reference near 36 counts should fall to about 36 * (1 - 0.2191) = 28.1 counts.
- Model samples around resonance:
  - delta = 0 MHz: expected drop 21.9%
  - delta = +/-5 MHz: expected drop 16.5%
  - delta = +/-10 MHz: expected drop 6.0%
  - delta = +/-15 MHz: expected drop 0.3%

Observed normalized signal:
- readout1 is approximately flat: mean 35.99 counts, population standard deviation 0.80 counts.
- readout2 has a pronounced dip: minimum 28.21 counts.
- Normalized fractional drops, 1 - readout2/readout1:
  - 3.870 GHz: 13.2%
  - 3.875 GHz: 18.4%
  - 3.880 GHz: 23.6%
  - 3.885 GHz: 12.2%
  - 3.890 GHz: 4.9%
- The observed minimum at 3.880 GHz gives readout2/readout1 = 0.7645, a 23.6% drop. This is very close to the 21.9% drop expected for a near-pi pulse at mod_depth = 1.

Explicit fit/check:
- I fit the normalized data to y = b - A * P_transfer(freq - f0), using f_R = 10 MHz and tau = 52 ns fixed.
- Best grid fit over the resonance region:
  - f0 = 3.8784 GHz
  - b = 0.9917
  - A = 0.2165
  - SSE = 0.0432
- A flat no-resonance normalized-ratio model gives mean y = 0.9532 and SSE = 0.1206, about 2.8 times worse.
- The fitted amplitude A = 21.7% agrees with the stated 22% contrast scale.
- The stored per-average overlays are not treated as an independent repeatability test because averages can reflect tracking cadence, but both averages still place their largest normalized drop at 3.880 GHz.

Decision:
- The active sequence is exactly capable of producing a contrast-scale pODMR dip when mw_freq crosses resonance.
- The observed dip has the expected magnitude, width, and center behavior for a 52 ns, mod_depth = 1 Rabi pulse with about 10 MHz Rabi frequency.
- Therefore a pODMR resonance is present.
