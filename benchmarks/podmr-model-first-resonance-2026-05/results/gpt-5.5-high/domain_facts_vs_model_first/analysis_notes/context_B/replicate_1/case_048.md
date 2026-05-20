Case: podmr_034_2026-05-16-204545

Inputs used: inputs/sequence.xml and inputs/raw_export.json.

Active pulse sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The instructions first polarize the NV and immediately detect; this is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the conditional m_S = +1 reference block is inactive.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and detects again; this is readout 2, the pODMR signal after the microwave pulse.
- Active pulse duration: length_rabi_pulse = 52 ns after sample-rate rounding.
- Active modulation depth: mod_depth = 1.

Expected physical signal calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the active pulse has f_R = 10 MHz.
- For a resonant square Rabi pulse, transition probability P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so a resonance should reduce the post-pulse signal by contrast * P = 0.22 * 0.996 = 0.219 of the bright reference.
- Therefore the expected resonant signal/reference ratio is 1 - 0.219 = 0.781.
- The mean readout 1 level is 50.016 counts, so the expected resonant dip is about 50.016 * 0.219 = 10.96 counts.

Observed quantitative comparison:
- Mean readout 1 = 50.016 counts.
- Mean readout 2 = 49.366 counts.
- Mean paired difference readout2 - readout1 = -0.649 counts.
- Largest observed paired deficit readout1 - readout2 = 2.654 counts.
- Smallest observed paired signal/reference ratio = 0.948.
- Stored averages differ from each other at roughly 2 counts mean absolute split difference per readout, so the observed sub-3-count paired deficits are comparable to average-to-average scatter.

Line-shape check:
- I also compared the readout2/readout1 ratios to a square-pulse Rabi excitation model across possible resonance centers in the scanned 3.825 to 3.925 GHz range:
  P(f) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t).
- With the physical 22% contrast fixed, the best model fit is worse than a simple no-resonance baseline+slope fit in ratio space.
- Letting the dip amplitude float gives only about 4.1% contrast, far below the expected about 21.9% active-pulse contrast.

Decision:
The active sequence should have produced an approximately 11-count resonant dip if a pODMR resonance were in the scanned range. The observed readout separation and any line-like structure are much smaller than the expected physical signal and are comparable to stored-average scatter, so I decide that a pODMR resonance is absent.
