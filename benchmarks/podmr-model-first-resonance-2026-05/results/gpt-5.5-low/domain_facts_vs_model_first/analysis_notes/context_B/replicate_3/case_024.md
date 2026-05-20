Case: podmr_009_2026-05-16-113112

Sequence interpretation from inputs/sequence.xml:
- Active pulse sequence: Rabimodulated-style pODMR scan varying mw_freq.
- The sequence first performs optical polarization, then detection. This first detection is the bright m_S = 0 reference/readout role.
- full_expt = 0, so the conditional m_S = +1 reference block is not active.
- The active pODMR manipulation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second detection is the microwave-affected signal readout role.
- mod_depth = 1 in the provided XML.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, rounding leaves 52 ns exactly because 52 ns is 13 samples.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a square resonant pulse, transfer probability to m_S = +1 is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22 percent, so a resonant point should reduce fluorescence by about 0.22 * 0.996 = 21.9 percent of the bright readout.
- The median bright/readout-1 level is 29.73 counts, giving an expected resonant drop of 29.73 * 0.219 = 6.51 counts and an expected signal level near 23.22 counts.

Observed data comparison:
- Around 3.875-3.885 GHz, readout 2 drops to 24.29, 24.15, and 25.00 counts while readout 1 is 31.42, 30.04, and 30.75 counts.
- The corresponding readout-1 minus readout-2 differences are 7.14, 5.88, and 5.75 counts, close to the 6.51-count model expectation.
- Outside the central feature, readout-1 minus readout-2 averages only about 0.57 counts with standard deviation about 1.22 counts.
- The central feature is therefore both quantitatively consistent with the expected near-pi-pulse ODMR contrast and substantially larger than the off-feature readout mismatch.
- Stored averages show strong drift/tracking structure, so I treat them mainly as cadence/context rather than as an independent repeatability proof. The combined signal size and shape are nevertheless sufficient.

Decision: pODMR resonance present.
