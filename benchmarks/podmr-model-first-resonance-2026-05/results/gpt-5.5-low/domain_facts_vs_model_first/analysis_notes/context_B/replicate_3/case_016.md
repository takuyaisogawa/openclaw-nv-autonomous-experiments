Case: podmr_001_2026-05-16-000631

Sequence inspection:
- Active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive even though it appears in the XML.
- Readout 1 is the direct bright reference after adj_polarize and detection, representing the m_S = 0 level.
- Readout 2 is the detection after a single rabi_pulse_mod_wait_time pulse.
- Active pulse parameters: length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Physical model calculation:
- Given setup contrast scale between m_S = 0 and m_S = +1 is about 22%.
- Given Rabi frequency at mod_depth = 1 is about 10 MHz and scales linearly with mod_depth.
- For this case mod_depth = 1, so f_Rabi = 10 MHz.
- For a resonant Rabi pulse of duration t = 52 ns, the driven population transfer is modeled as P = sin^2(pi * f_Rabi * t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected on-resonance fluorescence reduction is contrast * P = 0.22 * 0.996 = 0.219, or about 21.9%.

Data calculation:
- At 3.880 GHz, readout 1 = 37.135 and readout 2 = 28.981.
- Normalized contrast 1 - readout2/readout1 = 1 - 28.981/37.135 = 0.220, or about 22.0%.
- Using edge points of readout 2 as an off-resonant baseline gives median baseline 37.452 and a dip depth of (37.452 - 28.981)/37.452 = 0.226, or about 22.6%.
- The dip is centered around 3.875 to 3.880 GHz and appears in the active readout after the Rabi pulse, while readout 1 remains comparatively flat aside from normal tracking-scale variation.

Decision:
The measured dip magnitude and location match the expected 52 ns, mod_depth 1 resonant Rabi-pulse signal, so a pODMR resonance is present.
