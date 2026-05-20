Case: podmr_054_2026-05-17-043636

I used the provided sequence XML and the exported active variable values. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed instructions are:

1. Optical polarization with adj_polarize.
2. First detection immediately after polarization. This is the bright m_S = 0 reference readout.
3. The optional "Acquire 1 level reference" block is skipped because full_expt = 0, despite do_adiabatic_inversion = 1.
4. A rabi_pulse_mod_wait_time pulse is applied.
5. Second detection. This is the microwave-affected pODMR signal readout.

The active pulse duration is length_rabi_pulse = 52 ns. The provided XML and Variable_values give mod_depth = 1. The embedded raw-export sequence text contains an older/default-looking mod_depth = 0.3, but it conflicts with both the provided sequence XML and the active variable list, so I treated mod_depth = 1 as active.

Physical model calculation:

For a rectangular microwave pulse, I modeled the transition probability as

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

using cycle-frequency units. The expected normalized fluorescence signal is approximately

S(Delta) / S0 = 1 - C * P(Delta)

where C = 0.22 is the setup contrast between m_S = 0 and m_S = +1. With mod_depth = 1, Omega = 10 MHz and t = 52 ns. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

so the expected resonant signal is

S(0) / S0 = 1 - 0.22 * 0.996 = 0.781

That is an expected dip of about 21.9 percent in the second readout relative to the bright reference. At 5 MHz detuning the same model still predicts S/S0 about 0.835, and at 10 MHz detuning about 0.940, so a real resonance sampled on this grid should produce a large, structured depression spanning one or more nearby points unless the resonance is badly missed between grid points. Even if centered between two adjacent 5 MHz-spaced samples, both neighboring samples should still be far below baseline for mod_depth = 1.

Data calculation:

I normalized the pODMR signal readout by the bright reference readout point by point: readout2/readout1. The normalized ratios across the scan were:

3.825: 0.9685
3.830: 1.0366
3.835: 1.0468
3.840: 0.9468
3.845: 0.9927
3.850: 0.9561
3.855: 0.9721
3.860: 0.9894
3.865: 0.9871
3.870: 1.0018
3.875: 0.9855
3.880: 1.0559
3.885: 0.9756
3.890: 0.9969
3.895: 0.9670
3.900: 1.0093
3.905: 0.9834
3.910: 1.0065
3.915: 1.0032
3.920: 1.0042
3.925: 0.9991

The mean normalized ratio is 0.9945 with standard deviation 0.0276. The deepest point is 0.9468, a 5.3 percent reduction from the reference, far smaller than the 21.9 percent resonant dip expected for the active 52 ns, mod_depth 1 pulse. A linear baseline model for readout2/readout1 gives SSE = 0.01509. A fixed-contrast physical resonance model with the active mod_depth = 1 gives a best SSE = 0.05112, substantially worse than the no-resonance baseline, because it requires a much deeper and more structured dip than the data contain. A free-amplitude fit prefers a positive feature near 3.832 GHz rather than the negative fluorescence dip expected from transfer into the dimmer m_S = +1 state.

Conclusion:

The data do not show the expected pODMR resonance signature for the active sequence. The observed few-percent fluctuations are inconsistent with the expected near-pi-pulse, about 22 percent normalized fluorescence dip, so I classify this case as resonance absent.
