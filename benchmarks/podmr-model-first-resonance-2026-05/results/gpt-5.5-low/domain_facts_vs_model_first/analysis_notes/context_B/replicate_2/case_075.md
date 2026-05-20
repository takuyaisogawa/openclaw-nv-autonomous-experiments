Case: podmr_061_2026-05-17-061719

Inputs used
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout roles from the active instructions:
  - readout 1: after adj_polarize and detection, the true mS = 0 fluorescence reference.
  - readout 2: after rabi_pulse_mod_wait_time and detection, the microwave-affected pODMR signal.
  - full_expt = 0, so the optional mS = 1 reference block is inactive.
- mod_depth = 1.
- length_rabi_pulse = 52 ns after sample-rate rounding.

Physical model calculation
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, the resonant square-pulse transfer probability is
  P = sin^2(pi * f_Rabi * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With setup mS = 0 to mS = +1 contrast of about 22%, a resonant pODMR feature should reduce the microwave-affected readout by approximately
  0.22 * 0.996 = 0.219, or 21.9% of the reference fluorescence.
- The mean readout-1 level is 49.615 counts, so the expected on-resonance drop is about
  49.615 * 0.219 = 10.87 counts.

Observed data check
- Mean readout 1: 49.615 counts.
- Mean readout 2: 49.086 counts.
- Mean readout2-readout1: -0.529 counts, standard deviation 1.723 counts.
- The largest negative ratio excursion is at 3.880 GHz with readout2/readout1 = 0.925, only a 7.5% apparent drop.
- The largest negative readout2-readout1 point is -3.788 counts at 3.830 GHz; the 3.880 GHz point is -3.731 counts. These are isolated excursions and are only about one third of the 10.87-count drop expected for a true on-resonant pi-pulse response.
- Neighboring three-point averages around candidate dips remain small, around -0.8 to -1.7 counts, not close to the expected -10.9 counts.
- The two stored averages differ substantially point by point, consistent with tracking/noise cadence rather than an independently repeatable resonance trace.

Decision
The active pulse should produce a large, obvious pODMR dip if a resonance is present. The measured scan shows only small, non-repeatable fluctuations well below the quantitative expected signal. I therefore classify this case as resonance_absent.
