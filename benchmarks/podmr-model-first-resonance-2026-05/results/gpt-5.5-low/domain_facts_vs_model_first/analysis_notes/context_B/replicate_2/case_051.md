Case: podmr_037_2026-05-16-213011

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png only as a visual check of the same raw readouts

Sequence identification:
- Active sequence file: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S=+1 reference block is inactive.
- Readout 1 role: true m_S=0 fluorescence reference after optical polarization, before the microwave test pulse.
- Readout 2 role: fluorescence after the modulated Rabi pulse.
- mod_depth = 1 from the provided sequence XML variable values.
- length_rabi_pulse = 5.2e-08 s = 52 ns. At the 250 MHz sample rate this is exactly 13 samples, so rounding does not change it.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Rabi frequency scales linearly with mod_depth, so f_R = 10 MHz for this sequence.
- For a resonant square pulse, the population transferred from m_S=0 to m_S=+1 is
  P = sin^2(pi * f_R * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale between m_S=0 and m_S=+1 is about 22%, so the expected resonant fluorescence change in readout 2 relative to readout 1 is approximately
  0.22 * 0.996 = 0.219, or a 21.9% drop.
- With the observed readout level near 47.6 counts, that corresponds to an expected on-resonance drop of about 10.4 counts in readout 2 relative to readout 1.

Observed quantitative comparison:
- Mean readout 1 = 47.629.
- Mean readout 2 = 47.929.
- Mean readout2/readout1 ratio = 1.0068, so readout 2 is slightly higher on average, not lower.
- Minimum readout2/readout1 ratio = 0.9563 at 3.825 GHz, equivalent to only a 4.4% drop.
- Minimum readout2 - readout1 = -2.115 counts, far smaller than the approximately -10.4 count drop expected for a resonant 52 ns pulse at mod_depth = 1.
- Around the upper end of the scan, including 3.920 to 3.925 GHz, readout 2 remains above readout 1 rather than showing the expected dip.
- The two stored averages differ substantially in baseline shape, consistent with the note that stored averages can reflect tracking cadence rather than independent repeatability.

Decision:
The expected pODMR resonance signature for this sequence is a large negative excursion of readout 2 relative to readout 1, approximately 22% on resonance. The measured data show only small fluctuations, with no frequency point or coherent line shape near the expected contrast scale. I therefore decide that a pODMR resonance is absent.
