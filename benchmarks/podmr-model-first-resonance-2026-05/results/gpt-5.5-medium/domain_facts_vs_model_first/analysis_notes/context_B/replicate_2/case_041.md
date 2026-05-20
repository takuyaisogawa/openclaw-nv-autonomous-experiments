Case: podmr_027_2026-05-16-184117

I used the provided sequence XML and raw export only.

Active sequence and readout roles:
- SequenceName: Rabimodulated.xml.
- The active varied parameter is mw_freq, scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and immediately detect. This is readout 1, the true m_S = 0 level reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The active microwave operation is one rabi_pulse_mod_wait_time call before the final detection. This final detection is readout 2, the post-Rabi-pulse signal readout.
- mod_depth = 1 and length_rabi_pulse = 52 ns in the provided sequence/variable values.

Quantitative expected signal model:
- Given the domain fact, Rabi frequency at mod_depth = 1 is about 10 MHz.
- The resonant pulse area in Rabi cycles is f_R * t = 10e6 * 52e-9 = 0.52 cycles.
- For a two-level Rabi pulse, the population transferred from m_S = 0 to m_S = +1 on resonance is sin^2(pi * f_R * t).
- sin^2(pi * 0.52) = 0.996, so an on-resonance point should be very close to a pi pulse.
- With a setup contrast scale of about 22%, the expected relative fluorescence reduction in readout 2 versus readout 1 is 0.22 * 0.996 = 0.219, i.e. readout2/readout1 should be about 0.781 on resonance.
- The combined readout 1 mean is 53.794 counts, giving an expected on-resonance count drop of about 11.79 counts.

Observed data:
- Combined mean readout 1 = 53.794, mean readout 2 = 52.947.
- Mean paired difference readout2 - readout1 = -0.847 counts.
- Standard deviation of paired differences across scan points = 1.468 counts.
- The minimum combined readout2/readout1 ratio is 0.9368 at 3.835 GHz, only a 6.3% apparent drop and not near the 21.9% expected resonant drop.
- Stored averages are not treated as independent repeatability evidence because the prompt notes they often reflect tracking cadence. Still, the deepest average-level ratio is not a stable 22% resonance-scale feature.
- A simple matched sinc-squared pulse-spectrum dip fit to the combined readout ratio, scanning possible centers on the measured frequency grid, gives a best dip amplitude of about 0.037 in ratio units, versus the expected 0.219. This is about 17% of the expected resonant contrast.

Decision:
The active pulse should generate a large, nearly full-contrast pODMR dip if a resonance is present in the scanned range. The measured readout 2 signal shows only small fluctuations and no dip at the expected scale. I therefore decide that a pODMR resonance is absent.
