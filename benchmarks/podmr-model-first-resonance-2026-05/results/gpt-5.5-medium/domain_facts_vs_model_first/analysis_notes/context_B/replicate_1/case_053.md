Case podmr_039_2026-05-16-221215

Input sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets full_expt = 0, so the optional explicit m_S = +1 reference block is not executed.
- Readout 1 is the detection immediately after optical polarization, i.e. the bright m_S = 0 reference.
- Readout 2 is the detection after one modulated Rabi pulse, so it is the pODMR signal readout.
- The provided sequence XML uses mod_depth = 1 and length_rabi_pulse = 52 ns. At 250 MS/s this pulse length is already an integer 13 samples, so rounding does not change it.

Expected signal model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the on-resonance Rabi frequency for this sequence is about 10 MHz.
- For a resonant square Rabi pulse, the transferred population is P = sin^2(pi f_R t).
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected readout-2 fluorescence reduction at resonance is 0.22 * 0.996 = 0.219 of the bright reference.
- The observed readout-1 mean is 49.35 counts, so an on-resonance point should show an approximately 10.8 count drop in readout 2 relative to readout 1, modulo linewidth and detuning sampling.

Measured data check:
- Mean readout 1: 49.35 counts.
- Mean readout 2: 49.19 counts.
- Mean paired difference readout2 - readout1: -0.154 counts.
- Standard deviation of paired differences across the scan: 1.63 counts.
- Largest negative paired difference: -2.54 counts at 3.850 GHz, with readout2/readout1 = 0.951.
- The high-frequency end shows readout 2 below readout 1 by roughly 1.3 to 2.3 counts, but this is still far below the approximately 10.8 count drop expected for a real resonance under the pulse settings, and it is not a clean isolated resonance feature.
- The stored two averages differ substantially point by point, consistent with the warning that stored averages can reflect tracking cadence rather than independent repeatability.

Decision:
The expected pODMR signal from the active pulse sequence is large, about a 22% readout-2 dip or roughly 11 counts at the observed count level. The measured signal does not contain a dip of comparable magnitude or a convincing resonance-shaped feature. I therefore classify this case as resonance_absent.
