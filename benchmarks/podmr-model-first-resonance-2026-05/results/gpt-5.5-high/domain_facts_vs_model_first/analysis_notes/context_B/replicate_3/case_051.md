Case: podmr_037_2026-05-16-213011

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated-style pulsed ODMR scan, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz, so length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- mod_depth = 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 role: detection immediately after adj_polarize, the true m_S = 0 reference.
- Readout 2 role: detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), the pODMR signal readout.

Quantitative physical model:
For a two-level driven transition, using the given setup Rabi frequency f_R = 10 MHz at mod_depth = 1 and a square pulse tau = 52 ns, the transition probability versus detuning delta is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

With f_R = 10 MHz and tau = 52 ns:
- At resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- At 2.5 MHz detuning, P = 0.929.
- At 5 MHz detuning, P = 0.749.
- At 7.5 MHz detuning, P = 0.508.
- At 10 MHz detuning, P = 0.273.

The expected optical readout contrast scale is about 22% between m_S = 0 and m_S = +1. The mean reference readout is 47.629 counts, so a resonant pi-like pulse should reduce the post-pulse readout by about

47.629 * 0.22 * 0.996 = 10.44 counts

relative to the m_S = 0 reference. Even a resonance halfway between scan samples should still give a roughly 7.85 count drop at the nearest 5 MHz-sampled point. This is far above the observed scatter.

Observed paired readouts:
- Mean readout1 reference = 47.629.
- Mean readout2 signal = 47.929.
- Mean signal-reference difference = +0.299 counts.
- Standard deviation of signal-reference difference = 1.323 counts.
- Minimum signal-reference difference = -2.115 counts.
- Maximum signal-reference difference = +2.808 counts.
- Signal/reference ratios range from 0.956 to 1.062.

The data do not contain the expected negative post-pulse contrast feature. The largest observed negative difference is only -2.115 counts, about one fifth of the expected on-resonance drop and smaller than the expected nearest-sample drop for a resonance falling between scan points. A fit of the Rabi lineshape to signal-reference differences gives the best unconstrained amplitude with the opposite sign from the physical expectation, while the fixed physical amplitude model is strongly inconsistent with the data.

Decision: resonance_absent.
