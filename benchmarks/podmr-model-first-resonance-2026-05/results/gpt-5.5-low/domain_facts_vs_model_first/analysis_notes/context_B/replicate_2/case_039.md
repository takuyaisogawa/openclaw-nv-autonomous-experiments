Case: podmr_024_2026-05-16-175646

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabi-modulated pODMR scan varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Active readouts are therefore:
  - readout 1: true mS = 0 reference after optical polarization and detection.
  - readout 2: signal after the Rabi-modulated microwave pulse and detection.
- mod_depth = 1 from the provided sequence XML and exported variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s remains 52 ns.

Physical model calculation:
- Given Rabi frequency approximately 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a resonant square pulse, transfer probability from mS = 0 to mS = +1 is P = sin^2(pi * f_R * t).
- With t = 52 ns: P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Setup contrast scale between mS = 0 and mS = +1 is about 22%, so the expected fractional fluorescence drop at resonance is 0.22 * 0.996 = 0.219.
- Mean readout 1 is 53.855, so an on-resonance readout 2 should be about 53.855 * (1 - 0.219) = 42.054 counts, a drop of about 11.80 counts relative to readout 1.

Observed data comparison:
- Mean readout 1: 53.855.
- Mean readout 2: 54.175.
- Mean readout2 - readout1: +0.320 counts.
- Minimum readout 2: 52.154 counts at 3.925 GHz.
- Minimum readout2/readout1 ratio: 0.969 at 3.925 GHz.
- Most negative readout2 - readout1 value: -1.654 counts.

Decision:
The expected resonant depletion for this pulse is large, about 22% or 11.8 counts, but no scan point approaches that scale. The signal readout remains comparable to or higher than the mS = 0 reference across the scan, with only small point-to-point fluctuations. Stored averages are not treated as independent strong repeatability evidence. The quantitative model therefore supports resonance_absent.
