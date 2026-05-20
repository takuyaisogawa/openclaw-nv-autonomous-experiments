Case: podmr_051_2026-05-17-011109

Input inspection:
- The scan sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions polarize, detect a true mS=0 bright reference, wait, then apply one rabi_pulse_mod_wait_time pulse and detect the signal.
- full_expt = 0, so the optional mS=1 reference block is inactive.
- Therefore readout 1 is the bright mS=0 reference and readout 2 is the post-Rabi-pulse pODMR signal.
- The provided sequence values give length_rabi_pulse = 52 ns and mod_depth = 1.

Expected signal model:
- Current setup contrast between mS=0 and mS=+1 is about C = 0.22.
- Rabi frequency at mod_depth = 1 is about f_R = 10 MHz.
- For a resonant rectangular Rabi pulse, transferred population is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected fractional fluorescence loss on resonance is C * P = 0.219.
- The mean bright reference readout is 48.33 raw units, so the expected on-resonance drop is about 48.33 * 0.219 = 10.6 raw units. The expected signal readout on resonance would be about 37.7 raw units.
- Including detuning for a rectangular pulse, P(detuning) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi t sqrt(f_R^2 + delta^2)). At 5 MHz detuning this is still about 0.75 transfer, implying an expected drop of about 16.5% or roughly 8 raw units in adjacent scan bins if a resonance lies on a sampled point.

Observed data:
- Mean readout 1 = 48.33 and mean readout 2 = 47.86, an average difference of only -0.47 raw units.
- The largest negative readout2-readout1 difference is -4.62 raw units at 3.895 GHz, corresponding to a ratio of 0.908.
- Neighboring differences are -1.83 raw units at 3.890 GHz and -0.79 raw units at 3.900 GHz, not the broad response expected for a 52 ns pi pulse.
- The observed minimum is less than half of the expected on-resonance contrast and is localized to one point. Stored averages are only two and can reflect tracking cadence, so they do not provide a strong independent repeatability test.

Decision:
The quantitative pulse model predicts a large, broad fluorescence loss of order 8-11 raw units around resonance, but the measured readout overlay shows only a small and isolated dip relative to the mS=0 reference. I therefore decide that a pODMR resonance is absent.
