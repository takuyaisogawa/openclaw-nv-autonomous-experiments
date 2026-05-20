Case: podmr_014_2026-05-16-124559

Sequence identification:
- The provided XML is Rabimodulated.xml.
- Active variables include length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Because full_expt = 0, the optional m_S = +1 reference block is inactive. The active readouts are:
  - readout 1: after adj_polarize and detection, the true m_S = 0 bright reference.
  - readout 2: after the modulated Rabi pulse and detection, the pODMR signal readout.

Physical model calculation:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For this sequence, f_Rabi = 10 MHz and pulse duration t = 52 ns.
- Resonant transfer probability for a driven two-level Rabi pulse is P = sin^2(pi f_Rabi t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected resonant fractional fluorescence drop is 0.22 * 0.996 = 0.219, about 21.9%.
- The off-resonant readout-2 baseline excluding the dip region is about 46.71 raw counts, so the expected resonant drop is about 10.24 counts and the expected resonant minimum is about 36.48 counts under full contrast.

Observed data check:
- readout 2 has a clear dip at the scanned center region:
  - 3.870 GHz: 42.33
  - 3.875 GHz: 39.12
  - 3.880 GHz: 39.56
  - 3.885 GHz: 43.04
- The minimum readout-2 value is 39.12 at 3.875 GHz.
- Relative to the off-resonant readout-2 baseline of 46.71, the observed drop is 7.60 counts, or 16.3%.
- The off-resonant readout-2 standard deviation is about 1.00 count, so the dip minimum is about 7.6 standard deviations below the off-resonant baseline.
- The stored per-average traces both show the same dip region: average 1 minimum 38.46 near 3.880 GHz, average 2 minimum 39.04 near 3.875 GHz. These averages may reflect tracking cadence rather than independent repeatability, but they are still consistent with a real resonance feature.

Decision:
The active sequence should produce a large pODMR dip when the microwave is resonant, and the observed readout-2 trace shows a quantitatively compatible, localized dip near 3.875 GHz while readout 1 remains a bright reference. A pODMR resonance is present.
