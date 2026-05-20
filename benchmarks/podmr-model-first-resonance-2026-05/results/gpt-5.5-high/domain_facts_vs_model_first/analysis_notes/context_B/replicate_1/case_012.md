Case podmr_030_2026-05-13-160024

I used the provided sequence and raw export values only. The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence performs:

1. adj_polarize for 1 us.
2. detection: this is readout 1, the true mS = 0 reference.
3. wait_for_awg for 2 us.
4. Because full_expt = 0, the optional mS = 1 reference block is skipped.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
6. detection: this is readout 2, the post-Rabi-pulse signal.

The pulse duration is rounded at sample_rate = 250 MHz. 52 ns is 13 samples, so it remains 52 ns.

Physical model calculation:

Given the setup facts, the on-resonance Rabi frequency at mod_depth = 1 is about 10 MHz. For a square pulse, the driven transition probability versus detuning is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz and tau = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

With an mS = 0 to mS = +1 contrast scale of about 22%, the expected readout-2/readout-1 ratio at resonance is

1 - 0.22 * 0.9961 = 0.7809.

Using the measured mean readout-1 level of 27.37 counts, the expected resonant drop in readout 2 is about 6.0 counts. Even if the resonance were halfway between sampled 5 MHz frequency points, the model gives P(2.5 MHz) = 0.929 and an expected ratio of 0.796. At one full scan step of detuning, P(5 MHz) = 0.749 and the expected ratio is still 0.835.

Measured combined readout comparison:

- Mean readout 1: 27.37
- Mean readout 2: 27.73
- Minimum readout-2/readout-1 ratio: 0.918 at 3.860 GHz
- Other low ratios are 0.925 at 3.885 GHz, 0.944 at 3.915 GHz, and 0.954 at 3.845 GHz.

None of the measured points approaches the expected 0.781 to 0.835 ratio for the relevant resonance model. A fixed positive-contrast resonance model using the 22% contrast and 10 MHz Rabi rate gives a best-center SSE of 123.64, worse than the no-resonance comparison r2 = r1 with SSE 52.11. If the contrast amplitude is allowed to float in the ratio model, the best fit gives a negative amplitude of about -0.052 rather than a positive ODMR dip.

The two stored averages show substantial tracking/scatter, so I did not treat the average overlays as an independent repeatability test. Still, the expected physical signal from the active 52 ns, mod_depth = 1 near-pi pulse is large enough that it should appear as a clear readout-2 depression relative to the readout-1 reference. It is not present in the measured combined readouts.

Decision: resonance_absent.
