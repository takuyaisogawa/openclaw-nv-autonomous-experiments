Case: podmr_043_2026-05-16-231159

Sequence interpretation:

- Sequence file: Rabimodulated.xml.
- Scan variable: mw_freq, 3.825e9 to 3.925e9 Hz in 5e6 Hz steps.
- Active branch: full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout roles:
  - readout 1 is the detection immediately after adj_polarize, i.e. the bright m_S = 0 reference.
  - readout 2 is the detection after the microwave rabi_pulse_mod_wait_time pulse, i.e. the pODMR signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- sample_rate = 250 MHz; length_rabi_pulse = 52 ns. The rounding line round(length_rabi_pulse*sample_rate)/sample_rate leaves it at 52 ns because 52 ns is 13 samples.
- mod_depth = 1.
- switch_delay = 100 ns.

Physical signal model:

Use the two-level driven transition model for the post-pulse population:

P1(delta) = [Omega^2 / (Omega^2 + Delta^2)] * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau)

where Omega = 2*pi*f_Rabi, Delta = 2*pi*delta, tau = 52 ns. The setup facts give f_Rabi = 10 MHz at mod_depth = 1. Therefore:

- rotation angle on resonance = 2*pi*(10e6)*(52e-9) = 3.267 rad = 1.04*pi.
- on-resonance transfer P1(0) = sin^2(3.267/2) = 0.996.
- contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected fractional drop in readout 2 at resonance is 0.22 * 0.996 = 0.219.

With the observed bright-reference scale readout1 mean = 47.11 counts, the expected on-resonance signal is a deficit of about:

47.11 * 0.219 = 10.32 counts

relative to readout 1. Equivalently, a resonant point should have readout2/readout1 near 0.781, with a broad sinc/Rabi detuning response over several scan points around the resonance.

Observed data comparison:

- readout1 mean = 47.11 counts.
- readout2 mean = 47.55 counts.
- readout2 - readout1 mean = +0.44 counts.
- readout2 - readout1 standard deviation across scan points = 0.92 counts.
- most negative observed readout2 - readout1 point = -1.19 counts.
- readout2/readout1 minimum = 0.9757.

Thus the largest observed deficit is only about 1.2 counts, while the expected near-pi resonance deficit is about 10.3 counts. The post-pulse readout is mostly equal to or higher than the bright reference, not lower by the expected 22% contrast.

I also evaluated the explicit model over possible resonance centers within the scanned frequency range. For any center landing on the measured range, the fixed-contrast model requires an approximately 10-count dip at or near the center. The best fixed-contrast resonance placement still fits much worse than a no-resonance model with a constant readout offset:

- best fixed 22% resonance SSE: 195.34
- no-resonance same-reference SSE: 21.95
- no-resonance with mean readout offset SSE: 17.87

Allowing the contrast amplitude to float while keeping the Rabi line shape gives a best constrained amplitude of only 0.023, about one tenth of the expected 0.22 setup contrast, and this small fitted feature is comparable to tracking/readout fluctuations. Stored averages should not be treated as a strong repeatability test here because they can reflect tracking cadence.

Decision:

The physically expected pODMR signal for this active 52 ns, mod_depth 1 pulse would be a large negative signal in readout 2 relative to readout 1. That signature is absent in the measured scan, so I classify this case as resonance_absent.
