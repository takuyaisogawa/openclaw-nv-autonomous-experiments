Case: podmr_053_2026-05-17-042031

Input used:
- The provided sequence file and exported variable values identify the active sequence as Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active readouts: because full_expt = 0, the optional mS=+1 reference block is skipped. The first detection is the polarized mS=0 reference. The second detection follows the Rabi-modulated microwave pulse and is the pODMR signal readout.
- Pulse parameters: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. do_adiabatic_inversion is defined true, but the active signal path uses rabi_pulse_mod_wait_time, not the commented/skipped adiabatic inversion block.
- Note: the embedded Sequence text in raw_export contains a default-looking mod_depth = 0.3 line, but the exported Variable_values and inputs/sequence.xml give mod_depth = 1. I used the active value mod_depth = 1.

Physical model calculation:
- Given the stated setup, Rabi frequency at mod_depth = 1 is about 10 MHz.
- For a rectangular pulse, use population transfer
  P1(delta) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * tau * sqrt(fR^2 + delta^2)),
  with fR in cycles/s, tau = 52 ns, and delta the microwave detuning.
- On resonance: P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% mS=0 to mS=+1 contrast, the expected on-resonance fluorescence reduction in the post-pulse readout is 0.22 * 0.996 = 0.219, about a 21.9% drop relative to the mS=0 reference. For a 45 count reference level this is about 9.9 counts.

Observed quantitative comparison:
- The measured readout2/readout1 relative differences range from +8.44% to -7.17%, with mean -0.35% and standard deviation 3.31%.
- The largest negative point is at 3.880 GHz: readout1 = 45.885, readout2 = 42.596, a -7.17% relative change, only about one third of the expected on-resonance contrast for the active mod_depth = 1 pulse.
- A fixed-contrast resonance line-shape fit using mod_depth = 1 is worse than a constant-ratio null model: null SSE = 0.02296, best resonance-model SSE = 0.07224.
- As a sensitivity check only, using mod_depth = 0.3 would give on-resonance transfer 0.222 and expected contrast 4.87%, but that is not the active value from the provided XML/exported values, and the improvement over the null is small.

Decision:
The active 52 ns, mod_depth = 1 pulse should produce a large near-pi-pulse pODMR dip if a resonance is in the scan. The observed readout differences are small, irregular, and not well described by the expected line shape, so I decide that a pODMR resonance is absent.
