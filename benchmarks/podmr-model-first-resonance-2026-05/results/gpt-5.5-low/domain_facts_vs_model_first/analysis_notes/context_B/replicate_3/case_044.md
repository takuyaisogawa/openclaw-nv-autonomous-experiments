Case podmr_030_2026-05-16-194429

Sequence identification and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The saved run variables show length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us.
- Because full_expt = 0, the intermediate "1 level reference" block is skipped even though do_adiabatic_inversion is true. The active readouts are therefore:
  - readout 1: after adj_polarize and detection, the bright m_S = 0 reference.
  - readout 2: after the modulated Rabi pulse and detection, the pODMR probe readout.

Physical model calculation:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the resonant rectangular-pulse transfer probability for a 52 ns pulse is
  P = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a true on-resonance pODMR response should change the probe readout by approximately
  0.22 * 0.996 = 0.219, or 21.9% of the bright level.
- The raw baseline is about 53 counts, so the expected on-resonance readout1-readout2 separation is about 0.219 * 53 = 11.6 counts if the scanned frequency crosses the addressed transition.
- More generally for a detuned rectangular pulse, P(delta) = (Omega^2/(Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)), with Omega = 10 MHz in cycle-frequency units. This line shape would still produce a prominent multi-count feature over the 5 MHz scan grid near resonance.

Observed data check:
- Combined readout1-readout2 differences across the 21 scan points have mean 0.080 counts and sample standard deviation 1.263 counts.
- The largest absolute difference is 2.769 counts at 3.895 GHz, corresponding to only about 5.4% fractional separation, and it is not part of a clear resonance-shaped feature.
- Neighboring points and the two stored averages do not show a consistent bright-reference versus probe-readout dip of the expected approximately 11.6-count scale. The stored averages mainly show offset/tracking changes rather than an independent repeatability test.

Decision:
- The active pulse is strong enough that a resonance should be large and obvious in readout 2 relative to readout 1. The observed deviations are much smaller than the modeled signal and lack a coherent pODMR line shape, so I decide resonance_absent.
