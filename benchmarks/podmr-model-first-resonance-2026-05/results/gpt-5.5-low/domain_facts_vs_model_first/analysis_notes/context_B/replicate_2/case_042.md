Case podmr_028_2026-05-16-185605

I used the provided sequence XML/raw export only. The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect the true mS=0 level reference, then skip the optional mS=+1 reference because full_expt = 0, then apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the mS=0 reference and readout 2 is the post-Rabi pulse signal.

Quantitative expected-signal model:

- Current setup contrast between mS=0 and mS=+1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse length: t = 52 ns.
- On-resonance population transfer for a square resonant Rabi pulse: P = sin^2(pi f_R t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional fluorescence change on resonance: C * P = 0.219.
- Mean readout 1 baseline from raw data: 51.718.
- Expected post-pulse resonance dip magnitude: 51.718 * 0.219 = 11.33 raw readout units.

Observed data comparison:

- Mean readout 2 - readout 1 = -0.148 raw readout units.
- Standard deviation of pointwise differences = 1.239 raw readout units.
- Most negative pointwise difference = -2.981 raw readout units.
- Most positive pointwise difference = 2.596 raw readout units.

The expected resonant response for this pulse would be a large post-pulse reduction of roughly 11.3 raw units, because the 52 ns pulse at mod_depth 1 is almost a pi pulse under the stated 10 MHz Rabi frequency. The measured readout difference is centered near zero and never approaches the expected amplitude. The stored two averages show tracking-scale variation and do not supply an independent repeatability test strong enough to override the missing expected contrast. I therefore decide that a pODMR resonance is absent.
