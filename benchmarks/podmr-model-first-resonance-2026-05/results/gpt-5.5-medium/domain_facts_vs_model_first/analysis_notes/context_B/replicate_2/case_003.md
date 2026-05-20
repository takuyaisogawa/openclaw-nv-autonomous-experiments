Case podmr_006_2026-05-11-020739

I used inputs/sequence.xml as the sequence source. The active sequence is Rabimodulated.xml. With full_expt = 0, the enabled detections are:

1. A polarized true m_S = 0 reference readout after adj_polarize.
2. A signal readout after rabi_pulse_mod_wait_time.

The m_S = +1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion is true. Thus readout 1 is the m_S = 0 reference role and readout 2 is the pulsed pODMR signal role. The active pulse has length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative expected signal model:

The setup Rabi frequency is approximately 10 MHz at mod_depth = 1. The on-resonance transfer probability for a square Rabi pulse is

P(+1) = sin^2(pi * f_Rabi * t)

Using f_Rabi = 10 MHz and t = 52 ns:

P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance optical signal ratio for the pulsed readout relative to the m_S = 0 reference is

S_signal / S_ref = 1 - 0.22 * 0.996 = 0.781

Equivalently, for a reference level near 47 counts, the ideal resonance-center dip is about 10.3 counts. Including finite detuning with the square-pulse model

P(+1, detuning) = (f_Rabi^2 / (f_Rabi^2 + detuning^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + detuning^2))

gives expected signal ratios near a resonance centered at 3.880 GHz of about 0.835 at +/-5 MHz, 0.940 at +/-10 MHz, and approximately 1 far away, with oscillatory weak off-resonant structure.

Observed data:

The scan runs from 3.825 GHz to 3.925 GHz in 5 MHz steps. The combined readout ratios signal/reference have the strongest dip at 3.880 GHz:

- 3.875 GHz: 40.462 / 44.423 = 0.911
- 3.880 GHz: 40.538 / 47.923 = 0.846
- 3.885 GHz: 41.885 / 48.154 = 0.870

The mean normalized signal in the 3.875-3.885 GHz window is 0.876, while the off-window mean excluding those three points is 0.975. In counts, the same window has mean reference-minus-signal difference 5.87 counts, compared with 1.22 counts off-window. Stored averages are only two and can reflect tracking cadence, so I treat the per-average overlay as a sanity check rather than a strong independent repeatability test.

Decision:

The active pulse is approximately a pi pulse at the stated mod_depth, so a real resonance should appear as a localized dip in readout 2 relative to the m_S = 0 reference. The measured localized depression around 3.880 GHz has the correct sign, frequency-localized shape, and order of magnitude, although it is shallower than the ideal line-center 22% contrast. I therefore decide that a pODMR resonance is present.
