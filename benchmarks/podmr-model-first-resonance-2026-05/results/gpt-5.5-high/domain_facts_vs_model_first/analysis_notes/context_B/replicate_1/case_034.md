Case: podmr_019_2026-05-16-164247

Sequence and readout roles

Using the provided sequence XML, the active sequence is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV center and performs a detection immediately afterward; this is the true m_S = 0 reference readout. The block that would acquire a separate m_S = +1 reference is inactive because full_expt = 0. The only microwave manipulation before the second active detection is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

Thus readout 1 is the polarized reference and readout 2 is the post-microwave signal readout. The active pulse parameters from the XML are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s = 52 ns. With sample_rate = 250 MHz, the rounded duration is still 52 ns.

Expected signal model

Given the setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, I used the driven two-level transition probability

P_transfer(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * pulse_duration * sqrt(f_R^2 + detuning^2))

with f_R = 10 MHz and pulse_duration = 52 ns. On resonance,

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With a contrast scale of 22% between m_S = 0 and m_S = +1, the expected on-resonance fractional PL drop in the second readout relative to the first readout is approximately

0.22 * 0.996 = 0.219, or 21.9%.

The scan step is 5 MHz. If the resonance sits halfway between adjacent scan points, the nearest sampled detuning is 2.5 MHz. The same model gives P_transfer(2.5 MHz) = 0.929 and an expected drop of 20.4%. Even at 5 MHz detuning, the expected drop is 16.5%. Therefore a real resonance inside this scan range should create a broad, localized depression in readout 2 relative to readout 1 on the order of 16-22% at nearby sampled points.

Data comparison

From the combined raw data, the readout-2/readout-1 relative drop has:

- mean drop: 1.70%
- standard deviation across scan points: 2.76%
- largest observed drop: 7.07%
- largest observed increase of readout 2 over readout 1: 5.21%

The largest observed drop is much smaller than the expected 16-22% sampled resonance signature. It is also comparable to the scatter and does not form a clear pODMR dip with the expected finite-pulse line shape. A constant-ratio no-resonance model had lower residual error than a forced 22%-contrast resonance model. Allowing the resonance amplitude to float gave a best-fit contrast amplitude of only about 4.0%, roughly 18% of the expected physical contrast, which is not consistent with the stated mod_depth = 1, 52 ns near-pi pulse model.

The stored per-average traces show cadence-level changes and do not provide a strong independent repeatability test. They do not rescue the expected large, localized resonance signature.

Decision

The active pulse should have produced a large pODMR dip if a resonance were present in the scanned range. The measured readout ratios show only small, non-localized fluctuations relative to that expectation. I therefore classify this case as resonance_absent.
