Case podmr_082_2026-05-17-111957.

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, varying mw_freq over 3.825 to 3.925 GHz in 5 MHz steps.
- The instructions first polarize, then call detection before any microwave pulse. This makes readout 1 the true m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. do_adiabatic_inversion is set true but inactive because that block is skipped.
- The only active microwave manipulation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns.
- Therefore readout 2 is the post-Rabi-pulse signal readout.

Physical model calculation:
For a resonant two-level rectangular pulse, the transferred population is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

where f_R is the Rabi frequency in cycles/s and delta is frequency detuning in Hz. The supplied setup facts give f_R = 10 MHz * mod_depth = 10 MHz and contrast C = 0.22 between m_S = 0 and m_S = +1. The pulse duration is tau = 52 ns, so on resonance:

f_R * tau = 10e6 * 52e-9 = 0.52 cycles
P(0) = sin^2(pi * 0.52) = 0.996
expected normalized contrast drop = C * P(0) = 0.219

With about 50.4 counts in readout 1, the expected on-resonance readout-2 depression is about 11.0 counts. Even if the resonance were between scan samples, the nearest 2.5 MHz detuned points would still have P = 0.929 and about 10.2 counts of expected depression. At 5 MHz detuning the expected depression is still about 8.2 counts. A true resonance inside the scanned range should therefore be visually and quantitatively large in readout 2 relative to the same-frequency readout 1 reference.

Observed data calculation:
Using contrast_i = (readout1_i - readout2_i) / readout1_i, the largest positive observed drop is 6.60% at 3.850 GHz, equal to 3.46 counts. Other candidate positive drops are 4.85% at 3.905 GHz and 4.65% at 3.915 GHz. The data also contain negative excursions of similar scale, including -5.27% at 3.875 GHz and -5.03% at 3.865 GHz, where readout 2 is brighter than the reference.

A scan over possible resonance centers using the fixed physical amplitude C = 0.22 gave a best fixed-resonance residual sum of squares of 0.0495 on the normalized contrast data, worse than the no-resonance zero-contrast residual of 0.0189. Allowing the model amplitude to float finds a best amplitude of only 0.039, about 18% of the expected 0.22 contrast scale. The stored per-average traces do not establish strong independent repeatability; they mostly reflect tracking cadence, and the strongest combined dips are not consistently reproduced as a single resonance shape.

Decision:
The active pulse should be nearly a pi pulse at mod_depth = 1, so a pODMR resonance should produce an approximately 22% readout-2 drop near the resonant frequency. The observed structure is only a few percent, mixed with comparable positive and negative fluctuations, and is far below the expected physical signal. I therefore classify this case as resonance_absent.
