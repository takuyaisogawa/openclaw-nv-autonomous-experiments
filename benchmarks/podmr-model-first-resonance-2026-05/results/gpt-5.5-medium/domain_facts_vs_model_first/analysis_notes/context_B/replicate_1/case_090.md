<!-- Model-generated analysis note. Not a ground-truth label. -->

Sequence and readout identification

The provided sequence is Rabimodulated.xml. The active path polarizes the NV, immediately performs a detection readout, waits, then applies one rabi_pulse_mod_wait_time pulse and performs a second detection readout. The "Acquire 1 level reference" branch is inactive because full_expt = 0, so there is no separate m_S = +1 reference in the active sequence. Thus readout 1 is the m_S = 0 fluorescence reference after polarization, and readout 2 is the fluorescence after the scanned microwave Rabi pulse.

Relevant sequence values from inputs/sequence.xml and raw_export:
- varied parameter: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so 52 ns is already sample-grid aligned

Physical signal model

Using the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular resonant pulse of length t = 52 ns, the expected population transfer is

P_1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * t)

where Omega = 10 MHz and delta is the microwave detuning in cycles/s. On resonance:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance point should reduce readout 2 relative to the m_S = 0 reference by approximately 0.22 * 0.996 = 21.9%. The observed readout-1 mean is 51.03 counts, so the expected resonant fluorescence drop is about 11.18 counts. The response should also extend over nearby points because the pulse bandwidth is of order 1/t, about 19 MHz, while the frequency step is 5 MHz.

Data comparison

The combined readout values give readout2 - readout1:

mean = -0.21 counts, standard deviation = 1.42 counts, minimum = -2.73 counts, maximum = +2.13 counts.

The readout2/readout1 ratio has mean 0.996, standard deviation 0.0277, minimum 0.948, and maximum 1.041. The deepest apparent point is only about a 5.2% drop, far below the expected 21.9% drop for a near-pi pulse on resonance.

I also fit the explicit Rabi line-shape model across the scan. With the physically expected fixed amplitude, any resonance within the scanned range predicts an approximately 11-count dip, much larger than the data. Allowing the model amplitude to float gives the best center near 3.878 GHz, but the fitted dip amplitude is -1.31 counts, i.e. the wrong sign relative to a fluorescence decrease. Stored per-average traces show sizable tracking/cadence offsets and do not provide a strong independent repeatability check.

Decision

Given the active readout roles and the quantitative expected signal, a real pODMR resonance should be large and obvious in readout 2 relative to readout 1. The observed differences are small, noisy, and not consistent with the expected Rabi resonance signature. I decide resonance_absent.
