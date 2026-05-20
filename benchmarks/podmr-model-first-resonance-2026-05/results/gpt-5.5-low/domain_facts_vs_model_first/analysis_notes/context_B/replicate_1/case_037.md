Case: podmr_022_2026-05-16-172725

I used only the provided XML/exported sequence and raw readouts.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active experiment has full_expt = 0, so the optional 1-level reference block is not executed.
- The first detection after adj_polarize is the true m_S = 0 fluorescence reference.
- The second active detection follows rabi_pulse_mod_wait_time and is the pODMR/Rabi-modulated signal readout.
- Active pulse duration is length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.
- Active mod_depth is 1.

Expected signal model:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, the relevant Rabi frequency here is about 10 MHz.
- For a resonant square pulse, the population transferred to m_S = +1 is P = sin^2(pi*f_Rabi*t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi*10e6*52e-9) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fluorescence reduction is 0.22*0.996 = 0.219, or about 21.9% of the 0-reference readout.
- The mean reference readout is 46.76 counts, so the expected on-resonance drop is about 10.25 counts.

Measured comparison:
- I compared readout 2 to readout 1 point-by-point because readout 1 is the active 0-reference and readout 2 is the post-Rabi signal.
- The mean of readout2 - readout1 is 0.07 counts with standard deviation 1.48 counts.
- The largest negative excursion is -3.27 counts at 3.890 GHz, about -6.9% relative to the local reference, far smaller than the expected roughly -10.25 count / -21.9% resonance-scale signal.
- The difference trace alternates signs and does not show a clear resonance-shaped fluorescence dip of the expected magnitude.
- The per-average overlays show large slow drift between stored averages, consistent with tracking cadence rather than an independent repeatability check, so I do not treat those averages as confirming a weak feature.

Decision:
The active pulse should produce an almost full-contrast response if a pODMR resonance is within the scanned range. The observed readout difference lacks the expected magnitude and coherent dip structure, so I classify this case as resonance_absent.
