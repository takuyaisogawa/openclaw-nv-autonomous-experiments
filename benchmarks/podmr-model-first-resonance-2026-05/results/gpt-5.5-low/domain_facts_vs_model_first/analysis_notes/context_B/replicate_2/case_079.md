Case: podmr_065_2026-05-17-071421

Sequence identification:
- Active sequence from the saved export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS = +1 reference block is skipped.
- Readout roles: readout 1 is the initial bright mS = 0 reference after optical polarization; readout 2 is the measurement after the modulated Rabi microwave pulse.
- Active pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Expected signal model:
- Given Rabi frequency approximately 10 MHz at mod_depth = 1, the pulse area is f_Rabi * tau = 10 MHz * 52 ns = 0.52 cycles.
- On resonance, the two-level transition probability is sin^2(pi * 0.52) = 0.996.
- With a setup contrast scale of about 22% between mS = 0 and mS = +1, an on-resonance pi-like pulse should reduce the post-pulse readout by approximately 0.996 * 22% = 21.9% relative to the bright reference.
- Using the detuned rectangular-pulse model
  P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau),
  the expected contrast fractions are about 21.9% at 0 MHz detuning, 16.5% at 5 MHz, 6.0% at 10 MHz, and 1.1% at 20 MHz. Thus a resonance within the scanned range should appear as a clear local dark feature in readout 2 relative to readout 1 over one to several frequency points.

Observed data:
- Combined readout 1 mean is 47.48 counts and combined readout 2 mean is 47.21 counts.
- The mean readout difference readout1 - readout2 is only 0.27 counts, about 0.6% of the bright level, not the roughly 10-count darkening expected for a near-pi pulse on resonance.
- Both readouts show a broad upward trend with frequency rather than a localized ODMR-like dip in the post-pulse readout.
- After linear detrending, the largest negative residual in readout 2 is about -1.70 counts, far smaller than the expected approximately 10-count contrast and not corroborated by a matching reference-normalized resonance feature.
- Stored averages are not a strong repeatability test here because they can reflect tracking cadence, but they also do not provide evidence for a large reproducible resonance-scale darkening.

Decision:
The active pulse should produce nearly full contrast if an addressed pODMR resonance is present in this scan window. The observed post-pulse signal lacks the expected localized dark response and is dominated by drift/noise at a much smaller scale, so I decide resonance_absent.
