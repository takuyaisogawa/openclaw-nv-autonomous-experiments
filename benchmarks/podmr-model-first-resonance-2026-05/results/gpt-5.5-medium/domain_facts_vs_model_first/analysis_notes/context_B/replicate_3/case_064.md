Case: podmr_050_2026-05-17-005655

Sequence identification from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml / Rabimodulated pulse sequence.
- Scan variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference branch is inactive.
- Readout 1 role: after adj_polarize, before any active microwave pulse; this is the true m_S = 0 fluorescence reference.
- Readout 2 role: after the active rabi_pulse_mod_wait_time pulse; this is the pODMR signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding gives 13 samples = 52 ns.
- mod_depth = 1.

Quantitative physical model:
- Given setup contrast between m_S = 0 and m_S = +1: C = 22%.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- For a square resonant pulse, transferred population is P_1 = sin^2(pi f_R t).
- With t = 52 ns, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- Therefore a true resonance should produce an expected fractional fluorescence drop of C * P_1 = 0.22 * 0.9961 = 0.2191, about 21.9%.
- With a typical m_S = 0 readout near 53.29 counts, the expected absolute drop at resonance is about 11.68 counts.

Observed data calculation:
- Mean readout 1 = 53.2866.
- Mean readout 2 = 52.9295.
- Mean readout2 - readout1 = -0.3571 counts, only about -0.67% of readout 1.
- The strongest pointwise readout2/readout1 suppression is at 3.865 GHz: readout2 - readout1 = -3.4231 counts, or -6.16%.
- This strongest suppression is far smaller than the modeled expected -21.9% contrast for a resonant 52 ns pulse at mod_depth = 1.
- Readout 2 alone has mean 52.9295, standard deviation 0.9296, minimum 50.9038 at 3.910 GHz, and maximum 54.8462; this is small fluctuation relative to the expected approximately 11.7 count resonant drop.
- Per-average traces have different baselines, consistent with stored averages reflecting tracking cadence rather than strong repeatability evidence. They do not show a consistent 22% dip tied to a common resonance frequency.

Decision:
The active pulse is essentially a pi pulse under the given Rabi calibration, so a pODMR resonance in this scan should be large and obvious in the second readout relative to the first. The measured differential and normalized readouts show only small fluctuations and no quantitatively compatible resonance feature. I therefore classify this case as resonance_absent.
