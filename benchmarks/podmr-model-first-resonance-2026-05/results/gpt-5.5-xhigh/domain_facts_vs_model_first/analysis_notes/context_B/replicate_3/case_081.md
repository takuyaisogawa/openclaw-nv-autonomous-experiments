Case: podmr_067_2026-05-17-074342

Input basis

I used inputs/sequence.xml and the numeric arrays in inputs/raw_export.json. I did not use any prior labels, sibling cases, or external context.

Active sequence and readout roles

The sequence is Rabimodulated. The active instruction order is:

1. Set microwave with mw_freq plus detuning, freqIQ = 50 MHz.
2. Polarize for pumping_time = 1 us.
3. Detect immediately after polarization. This is the true m_S = 0 reference readout.
4. Wait 2 us.
5. The "Acquire 1 level reference" block is skipped because full_expt = 0, even though do_adiabatic_inversion is set true.
6. Apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
7. Detect after that microwave pulse. This is the pODMR signal readout.

Therefore readout 1 is the m_S = 0 reference, and readout 2 is the signal after the swept microwave pulse. There is no active m_S = +1 reference in this run.

Pulse parameters from the provided XML

sample_rate = 250 MHz
length_rabi_pulse = 52 ns
rounded pulse duration = round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns
mod_depth = 1
full_expt = 0
sweep: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps

Physical model calculation

Given the domain facts, the on-resonance Rabi frequency is about

f_R = 10 MHz * mod_depth = 10 MHz.

For a square pulse, the transition probability versus cyclic detuning Delta is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

With t = 52 ns:

P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

Using the stated 22% contrast scale, a resonant point should reduce the signal readout by

0.22 * 0.996 = 0.219 of the m_S = 0 reference.

The observed m_S = 0 reference level is about 48.92 counts, so the expected resonant drop is

48.92 * 0.219 = 10.72 counts.

The scan step is 5 MHz. Even in the worst case where the resonance lies halfway between two sampled points, the nearest sampled detuning is 2.5 MHz:

P(2.5 MHz) = 0.929,
expected fractional drop = 0.22 * 0.929 = 0.204,
expected count drop at 48.92 counts = 9.99 counts.

At 5 MHz detuning the expected drop is still about 8.06 counts. Thus a resonance within the swept range should be a large, coherent dip in readout 2 relative to readout 1.

Observed data check

Mean readout 1 = 48.920 counts.
Mean readout 2 = 48.757 counts.
Mean readout2/readout1 = 0.99698.
Minimum readout2/readout1 = 0.95234 at 3.885 GHz.
Largest observed signal drop = 2.346 counts, or 4.77% of readout 1.

This largest observed drop is much smaller than the approximately 10 count, 20% to 22% sampled drop expected from the active near-pi pulse model. It is also surrounded by point-to-point fluctuations and a neighboring overshoot rather than a clean resonance-shaped depression. Stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.

Decision

The active physical model predicts a large pODMR dip if a resonance is inside the scan, but the measured signal readout stays close to the reference with only small incoherent fluctuations. I therefore decide that a pODMR resonance is absent.
