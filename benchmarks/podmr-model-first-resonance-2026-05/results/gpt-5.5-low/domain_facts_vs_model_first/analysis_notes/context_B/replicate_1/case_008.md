Case podmr_014_2026-05-12-081841

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name in the export: Rabimodulated.xml.
- The active instructions polarize the NV, acquire a true mS=0 readout, wait, apply one modulated Rabi microwave pulse, then acquire a second detection readout.
- full_expt = 0, so the optional mS=+1 reference block is skipped. Therefore readout 1 is the mS=0 reference and readout 2 is the post-pulse signal, not an independent +1 reference.
- The run variable values show length_rabi_pulse = 52 ns and mod_depth = 1. The supplied XML contains the same active instruction structure and the same 52 ns pulse duration.

Physical model calculation:
- Given setup contrast between mS=0 and mS=+1 is about C = 0.22.
- Given Rabi frequency at mod_depth = 1 is about f_R = 10 MHz and scales linearly with mod_depth.
- With mod_depth = 1 and t = 52 ns, the resonant population transfer for a square Rabi pulse is
  P1 = sin^2(pi * f_R * t)
     = sin^2(pi * 10e6 * 52e-9)
     = 0.996.
- Expected resonant fluorescence fraction relative to the mS=0 reference is
  1 - C * P1 = 1 - 0.22 * 0.996 = 0.781.
- The measured readout 1 mean is 46.624 raw counts, so the expected resonant readout 2 level is about
  46.624 * 0.781 = 36.407 counts, a drop of about 10.217 counts.

Observed data:
- There are 21 frequency points from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Combined readout 1 mean/std: 46.624 / 1.138 counts.
- Combined readout 2 mean/std: 46.315 / 1.078 counts.
- Difference readout2 - readout1 has mean -0.309 counts, std 1.331 counts, min -3.135 counts, max +2.481 counts.
- Ratio readout2/readout1 has mean 0.994, std 0.028, min 0.937, max 1.055.
- The deepest combined ratio point is at 3.865 GHz, with readout 1 = 49.788, readout 2 = 46.654, ratio = 0.937, only a 6.3 percent drop. That is far smaller than the expected 21.9 percent resonant drop.
- Stored averages are only two averages and may reflect tracking cadence. Their deepest ratio points are not consistent: average 1 is deepest at 3.865 GHz, while average 2 is deepest at 3.905 GHz.

Decision:
The expected resonant signal from the active pODMR sequence is a near-pi-pulse dip of roughly 22 percent, about 10 counts here. The observed readout2/readout1 variation is small, noisy, and not reproducible across the stored averages. I therefore decide that no pODMR resonance is present.
