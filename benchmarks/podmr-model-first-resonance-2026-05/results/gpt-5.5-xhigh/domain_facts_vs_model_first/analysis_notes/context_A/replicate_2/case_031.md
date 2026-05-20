Sequence file: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Active instructions:
- The first detection after adj_polarize is the true m_s = 0 fluorescence reference.
- full_expt = 0, so the optional 1-level reference block is skipped.
- The second active detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the signal after the microwave pulse.

Pulse parameters from the provided XML/exported variable values:
- mod_depth = 1.
- length_rabi_pulse = 5.2e-8 s = 52 ns, rounded at 250 MHz sample rate to 13 samples, still 52 ns.
- With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, the Rabi period is about 100 ns, so a 52 ns pulse is approximately a pi pulse on resonance.

Data assessment:
The 0-reference readout stays near 47 counts with no matching narrow dip. The post-pulse readout has a clear, localized depression around 3.875-3.880 GHz: readout 2 falls to about 39.6 while readout 1 remains about 47.7-47.8, a ratio near 0.83 and contrast of roughly 17%. This is of the expected sign and size for a near-pi pODMR pulse given the stated 22% m_s = 0 to m_s = +1 contrast scale. The per-average traces should not be over-weighted as independent repeatability evidence, but they are consistent with the same localized feature.

Decision: resonance present.
