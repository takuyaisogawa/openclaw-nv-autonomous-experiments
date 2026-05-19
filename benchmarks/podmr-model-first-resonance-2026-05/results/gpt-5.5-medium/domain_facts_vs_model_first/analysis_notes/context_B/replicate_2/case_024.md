<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_024

Sequence/readout identification

The provided sequence XML is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

1. adj_polarize for 1 us, then detection: this is readout 1, the true m_S = 0 level reference.
2. The "Acquire 1 level reference" block is inactive because full_expt = 0, so no separate m_S = +1 reference is acquired.
3. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detection: this is readout 2, the pODMR signal after the microwave pulse.

Other relevant pulse parameters are sample_rate = 250 MHz, so 52 ns is exactly 13 samples after rounding; mw_freq is the swept variable; delay_wrt_1mus = 0.2 us; length_last_wait = 1 us. Although do_adiabatic_inversion is true, the active path does not call adiabatic_inversion because the full_expt reference block is skipped.

Expected signal model

Use the stated setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant rectangular pulse, the transition probability is

P_1(delta = 0) = sin^2(pi * f_R * t)

with f_R = 10 MHz and t = 52 ns:

pi * f_R * t = pi * 0.52 = 1.6336 rad
P_1(0) = sin^2(1.6336) = 0.9961

The stated optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so a resonant pulse should reduce the post-pulse readout to

S_res / S_0 = 1 - 0.22 * 0.9961 = 0.7809

The mean readout-1 level is 29.457 counts, giving an expected resonant drop of

29.457 * 0.22 * 0.9961 = 6.455 counts

Data comparison

The combined readouts show the largest readout1-readout2 drop at 3.875 GHz:

readout1 = 31.423
readout2 = 24.288
drop = 7.135 counts
ratio = 0.773

This observed ratio is very close to the predicted resonant ratio of 0.781, and the observed drop is close to the predicted 6.455 counts. Away from the central feature the edge mean drop is only about 0.460 counts, so the central depression is not explained by a constant offset between readout roles. Stored per-average traces are treated cautiously because they can reflect tracking cadence, but the combined trace still shows a frequency-localized dip with the correct sign and magnitude for the active pulse sequence.

Decision

A pODMR resonance is present. The feature near 3.875-3.885 GHz has the expected near-pi-pulse contrast for the identified 52 ns, mod_depth = 1 Rabi-modulated measurement.
