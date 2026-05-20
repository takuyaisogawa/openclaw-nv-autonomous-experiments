Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles from the XML instructions:
- readout 1 is the bright-state/true m_S = 0 reference acquired immediately after optical polarization.
- full_expt = 0, so the optional m_S = 1 reference block is not active.
- readout 2 is the signal after the microwave Rabi pulse and should drop below readout 1 at resonance.

Pulse settings used for the decision:
- mod_depth = 1 from the provided sequence values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 13 samples, still 52 ns.
- With the stated setup scale, this is near a pi pulse for a 10 MHz Rabi rate, so an on-resonance response should be a clear negative contrast approaching the 0 to +1 contrast scale, about 22%.

Data assessment:
The combined signal/reference contrast (readout1 - readout2) / readout1 has its largest positive excursion near 3.895-3.900 GHz, about 5.8% to 7.7%. That is much smaller than the expected response for a near-pi pulse at mod_depth = 1. The trace also has comparable few-percent fluctuations elsewhere and alternates sign across neighboring points, with no clean broad resonance-shaped depression of the post-pulse readout. The per-average overlay shows tracking-level drift and a weak local feature around the same region, but the stored averages are not a strong independent repeatability test.

Decision:
I do not count this as a pODMR resonance. There is a weak candidate dip near 3.9 GHz, but it is too small and irregular relative to the expected pi-pulse contrast scale.
