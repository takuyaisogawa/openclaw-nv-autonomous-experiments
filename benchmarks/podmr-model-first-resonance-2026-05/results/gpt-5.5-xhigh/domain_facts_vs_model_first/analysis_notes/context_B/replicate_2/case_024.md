Active sequence and readout roles

The provided XML is Rabimodulated.xml. With full_expt = 0, the optional m_S = +1 reference branch is inactive. The active sequence is:

1. adj_polarize
2. detection: true m_S = 0 reference readout
3. wait_for_awg
4. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth)
5. detection: post-Rabi-pulse signal readout
6. wait_for_awg

Thus readout 1 is the bright m_S = 0 reference, and readout 2 is the signal after the microwave pulse. The standalone sequence XML and exported Variable_values give mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so 52 ns is exactly 13 samples and is unchanged by the rounding instruction. I used those active values for the model. The exported serialized Sequence text contains an older default-looking mod_depth = 0.3, but the provided XML and exported actual Variable_values both indicate mod_depth = 1.

Physical model calculation

For a resonant pODMR/Rabi-pulse scan, the expected population transferred from m_S = 0 to m_S = +1 after a rectangular pulse is

P1(f) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

where delta = f - f0 in cycles/s, tau = 52 ns, and the setup gives f_R = 10 MHz * mod_depth = 10 MHz. With the stated bright/dark contrast C = 0.22, the expected normalized signal readout is

readout2 / readout1 = 1 - C * P1(f).

On resonance, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected normalized PL ratio is 1 - 0.22 * 0.996 = 0.781. For a readout-1 level near 30 counts, the expected resonant readout-2 level is about 23.4 to 24 counts, a drop of about 6.6 counts from the bright reference.

Quantitative comparison to data

Using the combined readouts, the observed normalized ratio readout2/readout1 has its minimum at 3.875 GHz:

- readout1 = 31.423
- readout2 = 24.288
- ratio = 0.773
- deficit = 22.7%

This agrees closely with the 22% contrast near-pi-pulse expectation. A grid fit of the fixed-contrast two-level model over resonance frequency gives best f0 = 3.8787 GHz, with SSE = 0.0312 against the normalized ratios. A no-resonance constant-ratio null gives SSE = 0.1187, about 3.8 times worse. Allowing a fitted multiplicative baseline and contrast-like amplitude gives the same best f0 = 3.8787 GHz, fitted baseline 0.9919, fitted amplitude -0.2336, and implied contrast 23.6%, again close to the stated 22%.

The stored two averages show strong opposite tracking-like drift, so I do not treat them as independent repeatability proof. The combined readout ratio, however, has the expected magnitude, frequency-localized line shape, and fitted center for a microwave resonance with this 52 ns, mod_depth = 1 pulse.

Decision

A pODMR resonance is present.
