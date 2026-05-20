Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout roles:
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- readout 1 is the initial detection after optical polarization, therefore the m_S = 0 / bright reference for each sweep point.
- readout 2 is the detection after the modulated Rabi microwave pulse.

Pulse parameters from the provided sequence XML:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is approximately a pi pulse, so a resonant microwave frequency should strongly transfer population out of m_S = 0 and produce a large drop in readout 2 relative to readout 1.

Decision:
The second readout has a sharp, centered dip near 3.875 GHz: readout 2 falls to about 34.17 while readout 1 remains about 45.40. This is roughly a 25% reduction relative to the bright reference, matching the expected order of the stated 22% contrast for m_S = 0 to m_S = +1. The dip appears in both stored averages, although the averages are not treated as a strong independent repeatability test because they may reflect tracking cadence. Given the active pulse is near a pi pulse at mod_depth = 1 and the dip is large, localized, and readout-role consistent, a pODMR resonance is present.
