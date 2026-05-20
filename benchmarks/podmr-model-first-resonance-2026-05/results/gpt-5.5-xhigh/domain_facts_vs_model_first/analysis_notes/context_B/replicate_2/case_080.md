Case: podmr_066_2026-05-17-072831

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, sibling cases, or external context.

Active sequence and readout roles:

- SequenceName is Rabimodulated.xml; the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions acquire a true 0-level reference first:
  adj_polarize -> detection -> wait_for_awg.
- full_expt = 0, so the optional 1-level reference block is inactive.
- The active microwave-dependent measurement is then:
  rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) -> detection.
- Therefore readout 1 is the pre-microwave m_s = 0 reference/tracking readout, and readout 2 is the post-Rabi-pulse pODMR signal readout.
- The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, 52 ns is exactly 13 samples after rounding.

Quantitative expected-signal model:

Using the provided setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse with detuning Delta, the transition probability is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

with f_R = 10 MHz and t = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated m_s = 0 to m_s = +1 contrast scale is about 22%, so the expected resonant post-pulse readout drop relative to the 0 reference is

0.22 * 0.996 = 0.219, or about 21.9%.

Because the scan spacing is 5 MHz, a resonance inside the scanned interval should be within 2.5 MHz of at least one measured point. The same model gives expected drops of about 20.4% at 2.5 MHz detuning and about 16.5% at 5 MHz detuning. Thus a real resonance in this sweep should produce a large, broad dip in readout 2 relative to readout 1.

Observed comparison:

I used the normalized contrast-like quantity (readout1 - readout2) / readout1. Across the 21 combined points:

- Mean observed value: 1.10%.
- Maximum observed value: 6.42%.
- Minimum observed value: -5.44%.
- Population standard deviation: 3.41%.

The largest combined readout depressions are far below the expected 16%-22% resonant response. A least-squares fit of the physical Rabi lineshape plus a constant baseline, allowing the line amplitude to float, prefers an amplitude of about 6.5% centered near 3.8874 GHz. That is only about 30% of the expected 21.9% amplitude. Forcing the expected 22% amplitude gives a worse residual than a no-resonance constant-baseline model, indicating the expected resonant signature is not present.

The per-average overlays also do not provide a strong independent repeatability test here because stored averages can reflect tracking cadence. Their maxima are only about 8.6% and 7.9%, at different frequencies, still well below the expected near-pi-pulse pODMR response.

Decision: resonance_absent.
