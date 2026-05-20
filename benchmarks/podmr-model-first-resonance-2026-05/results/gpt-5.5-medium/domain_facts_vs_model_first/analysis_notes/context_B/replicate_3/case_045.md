Case podmr_031_2026-05-16-195907

Sequence interpretation:
- SequenceName is Rabimodulated.xml.
- The provided sequence has full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive.
- Active readout roles are therefore:
  - readout 1: polarized true m_S = 0 reference after adj_polarize and detection.
  - readout 2: detection after one modulated Rabi pulse.
- Active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 from the provided sequence variables and exported variable values.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, the resonant rectangular-pulse population transfer is
  P_1(Delta = 0) = sin^2(pi f_R t).
- With t = 52 ns:
  P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup m_S = 0 to m_S = +1 contrast scale is about 22%, so an on-resonance pulse should reduce fluorescence by
  0.22 * 0.996 = 0.219, about a 21.9% dip relative to the m_S = 0 readout.
- With the observed readout-1 mean of 52.721 counts, the expected on-resonance readout-2 level is
  52.721 * (1 - 0.219) = 41.168 counts.
- Detuned rectangular-pulse calculation using
  P_1(Delta) = (Omega^2/(Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),
  with Omega = 2*pi*10 MHz, gives expected fractional dips of about 20.4% at 2.5 MHz detuning,
  16.5% at 5 MHz, 6.0% at 10 MHz, 1.1% at 20 MHz, and 0.7% at 50 MHz.
- Therefore, if the scan crosses a resonance, at least one 5 MHz-spaced point should show a large darkening,
  typically readout 2 far below readout 1.

Observed data:
- Scan range is 3.825 to 3.925 GHz in 5 MHz steps, 21 points.
- Mean readout 1 = 52.721 and mean readout 2 = 52.728.
- The paired difference readout2 - readout1 has mean +0.007 counts and standard deviation 1.393 counts.
- The minimum readout2/readout1 ratio is 0.929, much shallower than the expected resonant ratio near 0.781.
- Even the deepest observed paired decrease is 3.94 counts at 3.920 GHz, while the model predicts about 11.55 counts for a resonant pi pulse at the mean baseline.
- At every point, observed readout 2 is at least 8.23 counts above the modeled on-resonance value for that point's readout-1 baseline.
- The per-average traces mainly show an offset between the two stored averages, consistent with tracking or cadence effects rather than independent repeatable spectral structure.

Decision:
The active sequence should produce a large pODMR dip if a resonance is present, but the measured readout after the pulse remains essentially equal to the m_S = 0 reference throughout the scan. I classify this case as resonance_absent.
