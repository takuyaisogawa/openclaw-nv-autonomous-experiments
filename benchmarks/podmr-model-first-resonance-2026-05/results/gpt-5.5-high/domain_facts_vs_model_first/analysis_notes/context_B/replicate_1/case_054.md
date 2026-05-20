Case podmr_040_2026-05-16-222642

Sequence interpretation

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.

Important sequence values:
- sample_rate = 250 MHz, so length_rabi_pulse = 52 ns is exactly 13 samples after rounding.
- mod_depth = 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The active readouts are therefore:
  - readout 1: detection after adj_polarize, the true mS = 0 bright reference.
  - readout 2: detection after the Rabi-modulated microwave pulse, the pODMR signal readout.

Physical model calculation

For the stated setup, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse with detuning delta, I used the two-level transition probability

P1(delta) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * sqrt(fR^2 + delta^2) * tau)

with fR = 10 MHz and tau = 52 ns. The expected normalized optical contrast is approximately 0.22 * P1(delta), because the mS = 0 to mS = +1 contrast scale is about 22%.

At resonance, P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996, so the expected signal drop is 0.22 * 0.996 = 0.219, or about 21.9%. Even if the resonance lies halfway between two 5 MHz-spaced scan points, at delta = 2.5 MHz the model gives P1 = 0.929 and expected contrast = 20.4%. At delta = 5 MHz the expected contrast is still 16.5%.

Data comparison

I normalized the raw signal as contrast = 1 - readout2 / readout1. Across the 21 scan points:
- mean contrast = 1.08%
- maximum observed positive contrast = 7.63% at 3.885 GHz
- minimum observed contrast = -4.22% at 3.910 GHz
- contrast standard deviation = 2.76%

The largest observed drop is less than half of the minimum on-grid resonant response expected from the physical model, and far below the approximately 20% drop expected for a near-pi pulse anywhere inside a 5 MHz grid interval. An unconstrained fit of the expected Rabi lineshape plus constant baseline to the normalized data prefers a negative amplitude, which is not the physical sign for an ODMR dip in the post-microwave signal readout. A forced positive 22% contrast model only improves by moving the resonance outside the scanned range.

Decision

The scan does not contain the quantitatively expected near-pi-pulse pODMR contrast feature. I classify this case as resonance_absent.
