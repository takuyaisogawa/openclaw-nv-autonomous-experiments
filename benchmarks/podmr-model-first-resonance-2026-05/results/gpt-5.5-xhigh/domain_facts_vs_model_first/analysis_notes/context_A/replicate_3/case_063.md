Active sequence and settings:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional separate m_S = +1 reference branch is inactive.
- Readout 1 is the detection immediately after optical polarization, serving as the m_S = 0 reference.
- Readout 2 is the detection after the Rabi-modulated microwave pulse, serving as the signal readout.
- mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With the provided setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse.

Decision reasoning:
For a near-pi pulse at full modulation depth, an on-resonance spin flip should produce a large signal reduction approaching the setup contrast scale of about 22% between m_S = 0 and m_S = +1. The combined signal/reference ratios never show such a feature: the largest negative contrast in readout 2 relative to readout 1 is only about 5% near 3.85 GHz. The per-average traces have larger offsets and occasional dips, but their minima are not consistent across averages and the stored averages are expected to reflect tracking cadence rather than strong independent repeatability. The raw readouts also show comparable drift and fluctuations in both readout roles rather than a clean, reproducible ODMR-shaped reduction in the pulse readout.

Conclusion: resonance_absent.
