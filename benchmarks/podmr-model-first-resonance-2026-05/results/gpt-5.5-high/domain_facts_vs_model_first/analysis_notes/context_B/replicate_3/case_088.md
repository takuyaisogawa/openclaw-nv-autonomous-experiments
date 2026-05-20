Case: podmr_074_2026-05-17-092418

Input sequence and readout roles

The provided XML is Rabimodulated.xml. The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active sequence first polarizes the NV, detects the bright m_S = 0 reference, waits 2 us, applies one modulated Rabi pulse, then detects the driven signal readout. The optional "Acquire 1 level reference" block is disabled because full_expt = 0, so the two stored readouts are:

- readout 1: bright m_S = 0 reference after optical polarization, no microwave pulse in that shot segment.
- readout 2: signal after the scanned microwave-frequency Rabi pulse.

The pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 52 ns. The pulse length is already an integer number of 250 MHz sample-clock ticks after rounding: 52 ns * 250 MHz = 13 samples.

Quantitative expected-signal model

Given the stated setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse, the population transferred from m_S = 0 to m_S = +1 is

P1(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * t * sqrt(f_R^2 + detuning^2)).

At line center, detuning = 0, f_R = 10 MHz, and t = 52 ns:

P1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

With the stated bright-to-dark contrast scale of about 22%, the expected signal readout at resonance is

signal/reference = 1 - 0.22 * 0.996 = 0.781.

For the observed mean readout-1 level of 49.08 counts, an on-resonance point should therefore be near 38.3 counts in readout 2, a drop of about 10.75 counts relative to the bright reference. This is the relevant physical expectation for this active sequence because the pulse is effectively a pi pulse at mod_depth = 1.

Observed data comparison

The combined readouts have:

- mean readout 1 = 49.08 counts, standard deviation across scan points = 1.09 counts.
- mean readout 2 = 48.78 counts, standard deviation across scan points = 1.47 counts.
- readout2/readout1 mean = 0.994, standard deviation = 0.0347.
- minimum readout2/readout1 = 0.923 at 3.900 GHz, where readout 1 = 50.98 and readout 2 = 47.06.

The deepest observed normalized dip is only 7.7%, much smaller than the 21.9% dip expected for a real on-resonance 52 ns pi pulse. In counts, the deepest observed readout-2/reference difference is -3.92 counts, whereas the expected resonant drop at this reference level is about -11.17 counts.

I also fit the fixed-depth physical lineshape above by scanning possible resonance centers across the measured frequency range and allowing only an overall multiplicative baseline scale. The best physical dip model occurs near 3.8973 GHz but has SSE = 0.0734 against the readout2/readout1 data. A flat constant-ratio null model has SSE = 0.0241, so the fixed-depth resonance model fits substantially worse than no resonance. The per-average traces show similar shallow, inconsistent ratio minima and should not be over-weighted because stored averages can reflect tracking cadence.

Decision

A pODMR resonance is absent. The active sequence should produce a large, near-pi-pulse ODMR dip if the scanned transition were resonant, and the measured signal readout remains near the bright reference with only small noisy fluctuations.
