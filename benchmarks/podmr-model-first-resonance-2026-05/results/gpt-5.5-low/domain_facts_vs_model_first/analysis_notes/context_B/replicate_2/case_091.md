Case podmr_077_2026-05-17-100811

I used the provided sequence XML and the raw export only for the measured readout arrays.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive even though do_adiabatic_inversion is true.
- Readout 1 is the initial polarized m_S = 0 reference after adj_polarize and detection.
- Readout 2 is the detection after one rabi_pulse_mod_wait_time pulse.
- The active pulse has length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, the pulse rotation probability at exact resonance is
  P = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% contrast scale between m_S = 0 and m_S = +1, the expected resonant fractional readout change is
  -0.22 * P = -0.219.
- The measured readout-1 baseline mean is 50.936 counts, so the expected resonant post-pulse readout drop is
  50.936 * 0.219 = 11.16 counts, giving an expected readout 2 near 39.77 counts at resonance.

Observed data:
- Mean readout 1 = 50.936.
- Mean readout 2 = 50.769.
- Mean readout2 - readout1 = -0.167 counts, or -0.33%.
- Standard deviation of pointwise differences = 1.192 counts.
- Most negative pointwise difference is -2.192 counts at 3.825 GHz; the largest positive difference is +2.635 counts at 3.865 GHz.
- No scan point approaches the expected -11 count resonant response. The largest negative excursion is only about 20% of the modeled resonant signal and occurs at the scan edge rather than as a clear resonance feature.

Decision:
The expected resonant signal for this active pulse would be large relative to the observed fluctuations. The data show only small, sign-changing differences between the m_S = 0 reference and post-pulse readout, so a pODMR resonance is absent.
