Case: podmr_027_2026-05-16-184117

Sequence interpretation

The raw export identifies the sequence as Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence XML has full_expt = 0, so the "Acquire 1 level reference" branch is inactive. There are therefore two active detections:

- readout 1: detection immediately after adj_polarize, the bright m_S = 0 reference.
- readout 2: detection after rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, the pODMR signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The sequence rounds length_rabi_pulse by sample_rate. With sample_rate = 250 MHz and length_rabi_pulse = 52 ns, the rounded duration remains 52 ns. The sequence XML and exported variable values give mod_depth = 1.

Expected physical signal

Given the setup facts, the on-resonance Rabi frequency at mod_depth = 1 is about 10 MHz. Using the standard driven two-level model with detuning Delta in cycles/s,

P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

At resonance, f_R = 10 MHz and t = 52 ns, so f_R * t = 0.52 cycles and

P_1(0) = sin^2(pi * 0.52) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a true resonance should cause a readout-2 reduction relative to the bright readout-1 reference of

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout-1 level is 53.79 counts, so the expected on-resonance raw-count dip is about

53.79 * 0.219 = 11.79 counts.

Observed data comparison

Using the measured normalized contrast c = 1 - readout2/readout1:

- mean contrast: 0.0154, corresponding to only a 1.5% average reduction.
- maximum point contrast: 0.0632, corresponding to a 6.3% reduction, at 3.835 GHz.
- largest raw-count dip: 3.46 counts.
- adjacent-difference noise estimate in normalized contrast: about 0.0306.

A scan over possible resonance centers using the Rabi-model lineshape above and a floating baseline gives the best variable-amplitude fit at about 3.880 GHz with amplitude scale 0.172 relative to the expected physical contrast and R^2 = 0.162. Thus the best data-matched Rabi-like feature has a peak amplitude of only about 0.172 * 21.9% = 3.8%, far below the expected near-pi-pulse pODMR response. A fixed-amplitude physical model requires an approximately 22% dip and is visibly inconsistent with the observed readout-2 values, which never approach the expected roughly 42-count level near resonance.

The stored two averages show tracking-scale variation and do not provide a strong independent repeatability test. The combined data do not show the large, coherent, multi-point dip expected from the active 52 ns mod_depth 1 pulse.

Decision: resonance_absent.
