Case: podmr_071_2026-05-17-084118

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- The scan uses Rabimodulated.xml while varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence XML, full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The two active detections are therefore:
  - readout 1: true mS = 0 reference after adj_polarize and before the microwave test pulse.
  - readout 2: signal after the modulated Rabi microwave pulse.
- The relevant microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- sample_rate = 250 MHz, length_rabi_pulse = 52 ns, and rounding to sample ticks keeps it at 13 samples = 52 ns.
- mod_depth = 1 in the provided XML/current exported variable values.

Physical model calculation:

Given the stated setup, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant square pulse with duration t = 52 ns, the expected population transfer is

P = sin^2(pi * f_Rabi * t)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

With an mS = 0 to mS = +1 contrast scale of about 22%, an on-resonance point should reduce the post-pulse readout by

0.22 * 0.996 = 0.219, or about 21.9%.

For a typical reference level of 49.46 counts, this corresponds to an expected dip of about 10.84 counts, giving a resonant post-pulse level near 38.62 counts. Equivalently, the readout2/readout1 ratio should approach about 0.781 at resonance.

The scan step is 5 MHz. Even if the true resonance sits halfway between sampled points, using the detuned Rabi expression

P(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * sqrt(f_Rabi^2 + delta^2) * t)

at delta = 2.5 MHz gives P = 0.929 and an expected readout2/readout1 ratio of about 0.796. Thus a real resonance within the scanned range should produce a large, obvious dip at one or more points.

Data comparison:

- Mean readout 1: 49.459 counts.
- Mean readout 2: 49.448 counts.
- Mean readout2 - readout1: -0.011 counts.
- Standard deviation of pointwise readout2 - readout1: 1.469 counts.
- Most negative pointwise difference: -2.788 counts at 3.860 GHz.
- Minimum readout2/readout1 ratio: 0.946 at 3.860 GHz.

The largest observed normalized dip is only about 5.4%, far smaller than the expected roughly 20-22% dip for the active 52 ns, mod_depth = 1 pulse. It is also comparable to the point-to-point scatter and is not supported by the expected absolute count drop. The per-average traces mostly reflect slow level/tracking changes rather than independent repeatability evidence, consistent with the provided caution.

Decision: resonance_absent.
