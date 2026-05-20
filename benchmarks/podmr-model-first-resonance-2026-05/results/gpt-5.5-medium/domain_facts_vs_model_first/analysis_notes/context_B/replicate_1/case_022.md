Case: podmr_007_2026-05-16-013306

Sequence and readout roles:
- The provided XML is Rabimodulated.xml.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is acquired immediately after optical polarization and is the bright m_S = 0 reference.
- Readout 2 is acquired after the active microwave Rabi-modulated pulse and is the pODMR signal readout.
- Active pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Quantitative physical model:
- Given setup contrast scale from m_S = 0 to m_S = +1 is about 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore this sequence uses f_R = 10 MHz.
- On resonance, the pulse population transfer for a square pulse is
  P = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The expected fluorescence ratio on resonance is therefore approximately
  1 - 0.22 * 0.996 = 0.781, or a 21.9% drop from readout 1 to readout 2.

Data check:
- The combined readout-2/readout-1 ratio has its minimum at 3.880 GHz:
  readout1 = 36.9038, readout2 = 28.2115, ratio = 0.7645, drop = 23.6%.
- Nearby points also show the expected broadened square-pulse response:
  3.870 GHz ratio = 0.8684, 3.875 GHz ratio = 0.8163, 3.885 GHz ratio = 0.8783.
- Excluding the central dip region, the off-resonance ratio mean is about 0.980 with standard deviation about 0.051, so the deepest point is about 4.2 sigma below the off-resonance level.
- A square-pulse Rabi response model,
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t),
  fitted as ratio = B - A * P gives center 3.8785 GHz, baseline B = 0.9917, and amplitude A = 0.2165.
- This fitted amplitude agrees with the independently expected 0.22 contrast scale.
- The two stored averages both have their minimum at 3.880 GHz with drops of about 24.6% and 22.6%, although stored averages are treated mainly as tracking cadence rather than a strong repeatability test.

Decision:
The observed dip has the correct readout role, sign, magnitude, width, and fitted amplitude for the active 52 ns mod_depth 1 Rabi-modulated pODMR pulse. A pODMR resonance is present.
