Case: podmr_034_2026-05-15-235221

Files used:
- inputs/sequence.xml
- inputs/raw_export.json

Sequence identification and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML sets length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and full_expt = 0.
- Since full_expt = 0, the conditional "Acquire 1 level reference" block is skipped.
- Readout 1 is the bright m_S = 0 reference after polarization and detection.
- Readout 2 is the detection after the modulated Rabi pulse. A pODMR resonance should therefore appear as readout 2 dropping relative to readout 1.

Explicit expected-signal model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, f_R = 10 MHz.
- For a square resonant pulse, the driven population transfer is P = sin^2(pi * f_R * tau), with tau = 52 ns.
- P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With the setup contrast scale between m_S = 0 and m_S = +1 of about 22%, the expected resonant fractional drop in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 22%.
- Off resonance, the transfer should be small and readout 2 should remain near readout 1 apart from noise and tracking drift.

Observed quantitative comparison:
- Normalized contrast was calculated as 1 - readout2/readout1 at each scan point.
- The deepest points are:
  - 3.870 GHz: contrast = 0.193
  - 3.875 GHz: contrast = 0.217
  - 3.880 GHz: contrast = 0.246
- The off-window contrast, excluding 3.870 to 3.885 GHz, has mean 0.024 and standard deviation 0.037.
- The 3.875 and 3.880 GHz points are about 5.25 and 6.05 off-window standard deviations above the off-window mean.
- The observed drop magnitude is close to the physical expectation for a near-pi pulse at mod_depth = 1: expected about 0.219, observed about 0.217 to 0.246.

Decision:
The active sequence and quantitative Rabi/contrast model predict a large resonant drop in readout 2, and the data show a localized drop of the expected scale near 3.875-3.880 GHz. A pODMR resonance is present.
