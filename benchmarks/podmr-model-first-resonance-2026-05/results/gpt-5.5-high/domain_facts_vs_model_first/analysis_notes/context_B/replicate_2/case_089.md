Case podmr_075_2026-05-17-093901

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabimodulated sequence, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions contain two active detection windows because full_expt = 0. Readout 1 is the true m_S = 0 reference after optical polarization and before the MW pulse. Readout 2 is the probe readout after the Rabi-modulated MW pulse. The optional m_S = +1 reference block is skipped.
- The active probe pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Setup Rabi frequency is about 10 MHz at mod_depth = 1, so the active pulse has f_R = 10 MHz.
- For a square MW pulse, the transition probability versus detuning is
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).
- At resonance with tau = 52 ns, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, a real on-resonance pODMR response should reduce the probe readout by about 0.22 * 0.996 = 0.219, or 21.9%, relative to the reference. At the observed fluorescence level near 50.5 counts, that is an expected drop of about 11.1 raw-count units.

Data comparison:
- The measured readout means are readout 1 = 50.523 and readout 2 = 50.390, so the average probe-minus-reference difference is only -0.133 counts.
- The measured probe/reference ratio has mean 0.9975, standard deviation 0.0236, and minimum 0.9509. Even the deepest point is only a 4.9% relative drop, far smaller than the expected approximately 21.9% resonant drop.
- A linear-baseline fit to the probe/reference ratio has residual standard deviation about 0.0238. Forcing the expected 22% square-pulse pODMR dip at any resonance center inside the scanned frequency range gives a best RSS of 0.0498, compared with 0.0108 for the baseline-only model, at least 4.6 times worse.
- The two stored averages do not provide a strong independent repeatability test here, and their differential minima occur at different scan positions, consistent with tracking/noise rather than a stable resonance.

Decision:
The active 52 ns, mod_depth = 1 pulse should produce a large near-pi-pulse pODMR dip if a resonance lies in the scanned range. The observed readout differences are small, inconsistent in position, and quantitatively incompatible with the expected signal scale. I therefore classify this case as resonance_absent.
