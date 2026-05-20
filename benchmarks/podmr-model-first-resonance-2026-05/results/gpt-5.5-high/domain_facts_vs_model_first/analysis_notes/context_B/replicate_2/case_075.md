Case: podmr_061_2026-05-17-061719

Used only the provided files in this workspace.

Sequence interpretation:
- Active sequence: Rabimodulated.xml / Rabimodulated-style pODMR scan, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize, then detect: this is the bright m_S = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- The active microwave manipulation is rabi_pulse_mod_wait_time followed by detection: this is the pODMR signal readout, corresponding to readout 2.
- mod_depth = 1 from the provided sequence XML/variable values.
- length_rabi_pulse = 52 ns; at sample_rate = 250 MHz this is exactly 13 samples, so no effective rounding change.

Quantitative expected-signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- Pulse duration tau = 52 ns.
- For a rectangular resonant pulse, transition probability is
  P(delta) = f_R^2/(f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected normalized readout-2 drop at resonance is about 0.22 * 0.996 = 21.9%.
- Because the scan step is 5 MHz, if a resonance lies inside the scanned range the nearest grid point is at most 2.5 MHz detuned. The same model gives:
  - delta = 2.5 MHz: P = 0.929, expected dip = 20.4%.
  - delta = 5 MHz: P = 0.749, expected dip = 16.5%.
  - delta = 7.5 MHz: P = 0.508, expected dip = 11.2%.
  - delta = 10 MHz: P = 0.273, expected dip = 6.0%.

Data comparison:
- I compared readout 2 against readout 1 pointwise using (readout2 - readout1) / readout1.
- The largest observed drop is at 3.880 GHz: readout1 = 49.519, readout2 = 45.788, normalized contrast = -7.53%.
- Neighboring points are not consistent with the expected Rabi line shape: at 3.875 GHz the contrast is +1.27%, and at 3.885 GHz it is -0.27%. A true resonance near 3.880 GHz should produce a broad dip with roughly -16% contrast at +/-5 MHz.
- The point-to-point robust scatter of the combined normalized contrast is about 3.3% (MAD scaled by 1.4826). The stored two per-average traces give an estimated mean-point contrast scatter of about 3.25%, and stored averages are not a strong independent repeatability test here.
- A least-squares scan of the rectangular-pulse model with the physical 22% contrast fixed performed worse than a flat null model. Allowing the amplitude to float gave only about a 3.1% fitted contrast scale, far below the expected 22% physical scale.

Decision:
The isolated low readout-2 point is too small and too narrow relative to the expected 52 ns, mod_depth = 1 pODMR response. The data do not show a physically consistent pODMR resonance.
