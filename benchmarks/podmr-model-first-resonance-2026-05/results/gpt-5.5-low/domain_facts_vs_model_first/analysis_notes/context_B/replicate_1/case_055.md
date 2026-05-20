Case: podmr_041_2026-05-16-224136

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence has full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true.
- The active readouts are therefore:
  - readout 1: after adj_polarize, before the Rabi pulse; this is the true mS = 0 fluorescence reference.
  - readout 2: after a single rabi_pulse_mod_wait_time pulse; this is the pODMR signal readout.
- Active pulse parameters from the sequence values are mod_depth = 1 and length_rabi_pulse = 52 ns. At 250 MS/s, 52 ns rounds to 13 samples, so the active duration remains 52 ns.

Quantitative expected-signal model:

Given the stated setup, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant square pulse of duration t = 52 ns, the population transfer probability is

P = sin^2(pi * f_R * t)

with f_R = 10 MHz. This gives

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current contrast scale between mS = 0 and mS = +1 is about 22%. The measured mS = 0 reference mean from readout 1 is 46.354 raw counts. A true resonance should therefore reduce the post-pulse readout by approximately

0.22 * 46.354 * 0.996 = 10.158 counts,

so the expected on-resonance readout 2 level is about

46.354 - 10.158 = 36.197 raw counts.

Data comparison:

- Combined readout 1 mean: 46.354 counts.
- Combined readout 2 mean: 46.142 counts.
- Minimum combined readout 2: 43.500 counts at 3.895 GHz.
- Largest observed drop relative to the readout 1 mean: 2.854 counts.
- Pointwise readout2 - readout1 has mean -0.212 counts and standard deviation 1.435 counts.

The largest observed drop is only about 28% of the expected resonant pi-pulse contrast. The combined trace does not contain any point near the modeled on-resonance level of about 36.2 counts. The stored averages also mainly show baseline offsets consistent with tracking cadence; they do not provide a strong independent repeatability check for a resonant feature.

Decision: resonance_absent. The active 52 ns, mod_depth 1 pulse should produce an almost full contrast pODMR dip if a resonance were present in this scan, but the observed signal remains near the mS = 0 reference with only small tracking/noise-scale deviations.
