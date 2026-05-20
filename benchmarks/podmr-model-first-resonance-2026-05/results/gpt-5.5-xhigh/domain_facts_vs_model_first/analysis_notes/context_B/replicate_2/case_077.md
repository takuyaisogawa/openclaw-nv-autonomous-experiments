Case: podmr_063_2026-05-17-064555

I used the provided sequence XML and the raw readout export only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is not executed.
- readout 1 is the detection immediately after adj_polarize, therefore it is the m_s = 0 fluorescence reference.
- readout 2 is the detection after rabi_pulse_mod_wait_time.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse is 13 samples = 52 ns.
- mod_depth = 1.
- The adiabatic inversion setting is not active for the measured two-readout sequence because the full_expt block is skipped.

Physical model calculation:
For a driven two-level transition, using Rabi frequency f_R = 10 MHz at mod_depth = 1, the transfer probability after a square pulse of duration t is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

where delta is the detuning in Hz and f_R is in cycles/s. With t = 52 ns:
- P(0 MHz) = 0.996, so the expected resonant contrast is 0.22 * 0.996 = 0.219.
- P(2.5 MHz) = 0.929, so even a resonance halfway between 5 MHz-spaced scan points should give contrast about 0.204.
- For a raw m_s = 0 readout near 52 counts, this corresponds to an expected readout-2 loss of about 10.6 to 11.4 raw counts at the nearest sampled point.

Observed quantitative comparison:
- Combined readout difference readout1 - readout2 has mean 0.42 counts, range -1.69 to +2.73 counts, and standard deviation 1.36 counts.
- Ratiometric contrast 1 - readout2/readout1 has mean 0.0078, range -0.0329 to +0.0504, and standard deviation 0.0261.
- The largest observed positive contrast is 5.0%, far below the approximately 20% to 22% expected from the active pulse if a resonance is in the scan.
- A linear-baseline-only fit to the contrast has RMS residual 0.0253. Fitting the Rabi lineshape with free amplitude gives best amplitude 0.052 near 3.8347 GHz, with peak contrast 0.0517, much smaller than the expected 0.22. A fit with the expected amplitude 0.22 inside the scan gives RMS residual 0.0419 and is worse than the baseline-only model.
- The two stored averages show similar small contrast ranges; they do not reveal a repeatable 20% class feature. They are treated cautiously because stored averages can reflect tracking cadence.

Decision:
The measured data show only small readout-to-readout fluctuations and shared slow drift. The active Rabi pulse should create a large localized dip in readout 2 relative to the polarized reference if a pODMR resonance is present in this sweep. That expected feature is absent, so the decision is resonance_absent.
