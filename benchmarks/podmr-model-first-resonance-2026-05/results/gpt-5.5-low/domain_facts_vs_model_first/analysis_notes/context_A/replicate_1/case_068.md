Sequence inspection:

- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Applied sequence values in the export: mod_depth = 1, length_rabi_pulse = 52 ns, full_expt = 0.
- With full_expt = 0, the "Acquire 1 level reference" block is inactive. The executed readouts are:
  - readout 1: true m_S = 0 reference after optical polarization and detection.
  - readout 2: signal after the modulated microwave Rabi pulse and detection.
- Given the supplied setup facts, mod_depth = 1 implies roughly 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi-scale pulse. On resonance it should produce a substantial fluorescence reduction in the signal readout relative to the 0 reference, with a possible contrast scale up to about 22%.

Data assessment:

The combined raw readouts fluctuate around 41-44 counts. readout 2 does not show a clear, localized dip relative to readout 1 at a candidate resonance frequency. The largest point-to-point excursions are comparable between the two readouts and are not centered or shaped like a pODMR line. The per-average overlay shows strong average-to-average baseline drift/tracking behavior, and the stored averages are not a strong independent repeatability test. Normalized differences between the signal readout and the reference are only a few percent and change sign across the scan, far below the expected scale for a near-pi pulse on a single NV with the stated contrast.

Decision:

No credible pODMR resonance is present in this scan.
