Case podmr_007_2026-05-11-064944

I used the provided sequence XML and raw export values without labels or outside cases.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The executed instructions first optically polarize the NV and acquire a detection before the microwave pulse. With full_expt = 0, the intermediate "1 level reference" block is skipped.
- Therefore readout 1 is the optically pumped m_S = 0 reference.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- Therefore readout 2 is the post-microwave-pulse pODMR signal.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 from the provided XML and exported active variable values.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Expected signal model:
- Given setup contrast between m_S = 0 and m_S = +1 of about 22%.
- Given Rabi frequency f_R about 10 MHz at mod_depth = 1, scaling linearly with mod_depth.
- For the active pulse, f_R = 10 MHz and pulse duration t = 52 ns.
- Resonant population transfer probability for a square Rabi pulse is P = sin^2(pi f_R t).
- P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.
- Expected fluorescence drop on resonance is contrast * P = 0.22 * 0.996 = 0.219, or about 21.9% of the m_S = 0 fluorescence.
- The observed readout 1 baseline mean is 31.72 raw-count units, so the expected resonant readout 2 value would be about 31.72 * (1 - 0.219) = 24.77, a drop of about 6.95 raw-count units relative to readout 1.

Observed data calculation:
- Mean readout 1 = 31.72.
- Mean readout 2 = 31.55.
- Mean(readout 2 - readout 1) = -0.18 counts.
- Standard deviation of pointwise differences = 1.70 counts; SEM over scan points = 0.37 counts.
- The largest single point drop is -3.81 counts at 3.855 GHz, still much smaller than the expected approximately -6.95 count resonance response and not reproduced as a clear resonance-shaped feature.
- Several frequencies have positive readout 2 - readout 1 differences, and the per-average traces show large tracking/average offsets, so stored averages are not a strong independent repeatability test here.

Decision:
The active pulse should produce an easily visible near-full-contrast pODMR dip if a resonance is present in this sweep. The measured post-pulse readout does not show the expected approximately 22% fluorescence suppression relative to the m_S = 0 reference. I therefore decide that a pODMR resonance is absent.
