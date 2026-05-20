Sequence/readout interpretation:

The provided sequence XML is Rabimodulated.xml. The active instructions first polarize the NV, then perform a detection readout before any microwave pulse. This makes readout 1 the m_S = 0 / bright reference. The "Acquire 1 level reference" block is inactive because full_expt = 0, so there is no separate dark-state reference acquisition. The active pODMR signal path then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection. Thus readout 2 is the microwave-pulse signal readout.

The provided sequence XML has length_rabi_pulse = 5.2e-08 s and mod_depth = 1. I noted that raw_export.json contains an embedded Sequence text with mod_depth = 0.3, while its Variable_values table and the standalone inputs/sequence.xml report mod_depth = 1. Per the instruction to use the provided sequence XML, I use mod_depth = 1 for the physical model.

Quantitative model:

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. On resonance, the transition probability after a square pulse is modeled as

P_transfer = sin^2(pi * f_Rabi * tau).

With f_Rabi = 10 MHz and tau = 52 ns:

pi * f_Rabi * tau = pi * 0.52,
P_transfer = sin^2(pi * 0.52) = 0.996.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected resonant fluorescence reduction in the signal readout relative to the bright reference is approximately

0.22 * 0.996 = 0.219, or 21.9%.

For comparison only, if the embedded-export mod_depth = 0.3 were used instead, f_Rabi would be 3 MHz and the same 52 ns pulse would give P_transfer = sin^2(pi * 0.156) = 0.222, implying only about 4.9% contrast. That is not the model selected from the provided sequence XML.

Data calculation:

Using readout2/readout1 as the normalized signal ratio across the mw_freq scan, the off-feature baseline ratio outside 3.865-3.89 GHz is about 0.974 with standard deviation about 0.047. The minimum ratio occurs at 3.880 GHz:

readout1 = 38.1154,
readout2 = 26.9615,
readout2/readout1 = 0.7074.

Relative to the off-feature baseline this is a drop of 0.2666 in normalized ratio, about 27.4%. Directly as 1 - readout2/readout1, the point contrast is 29.3%. The dip is centered around the expected mw_freq region and spans adjacent points near 3.870-3.885 GHz. In the per-average data, the lowest normalized ratios also occur at 3.875 GHz and 3.880 GHz, respectively, which is consistent with the same feature despite the warning that stored averages mostly reflect tracking cadence.

Decision:

The active sequence should produce a large pODMR dip on resonance, about 22% for the provided mod_depth = 1 and 52 ns pulse. The measured signal readout shows a localized dip of comparable or larger magnitude near 3.88 GHz when normalized to the bright reference. I therefore decide that a pODMR resonance is present.
