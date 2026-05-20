Analysis note for podmr_080_2026-05-17-105113

Sequence and readout roles:
- Provided XML sequence: Rabimodulated.xml.
- Active sequence path has full_expt = 0, so the "Acquire 1 level reference" block is skipped.
- Readout 1 is the initial detection immediately after optical polarization, i.e. the true m_S = 0 reference.
- Readout 2 is the detection after the active microwave Rabi pulse.
- Active pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: t = 52 ns.
- On-resonance transition probability for a rectangular Rabi pulse:
  P = sin^2(pi * f_R * t)
    = sin^2(pi * 10e6 * 52e-9)
    = sin^2(0.52 pi)
    = 0.996.
- Given m_S = 0 to m_S = +1 contrast scale C = 0.22, the expected on-resonance fluorescence ratio for the post-pulse readout relative to the m_S = 0 reference is:
  1 - C * P = 1 - 0.22 * 0.996 = 0.781.
- With the observed readout 1 mean of 51.67 counts, the expected resonant drop is approximately:
  51.67 * 0.219 = 11.32 counts.

Observed quantitative comparison:
- Readout 1 mean = 51.67 counts, readout 2 mean = 51.70 counts.
- Readout 2 / readout 1 ratios across the scan have mean 1.0007 and range 0.9654 to 1.0298.
- The largest observed negative difference, readout 2 minus readout 1, is -1.81 counts, much smaller than the expected approximately -11.3 count resonant response.
- A detuned rectangular-pulse model over possible resonance centers in the scanned range still predicts a deep local ratio minimum near 0.781 at resonance, which is not present in the data.
- The two stored averages differ in baseline level and are consistent with tracking cadence effects, so they are not treated as an independent strong repeatability test.

Decision:
The expected pODMR signal for this pulse and mod_depth would be a large dip in the post-pulse readout relative to the m_S = 0 reference. The measured readouts show only small scan-to-scan fluctuations around unity ratio and no physically expected resonant drop. Therefore the resonance is absent.
