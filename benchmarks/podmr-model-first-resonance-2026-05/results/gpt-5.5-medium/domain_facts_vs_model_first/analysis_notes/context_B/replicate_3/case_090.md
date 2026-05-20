Case podmr_076_2026-05-17-095337

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize the NV and acquire a detection window. This is readout 1, the m_S = 0 / bright reference for each scan point.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive despite the do_adiabatic_inversion flag being true.
- The only active microwave manipulation before the second detection is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on). The second detection is readout 2, the post-microwave pODMR readout.
- The pulse duration is length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.
- mod_depth is 1 from the provided XML / exported variable values.

Expected signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the on-resonance spin-flip probability for a rectangular pulse is
  P = sin^2(pi * f_R * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The current contrast scale between m_S = 0 and m_S = +1 is about 22%, so a resonant pulse should reduce the post-pulse readout by approximately 0.22 * 0.996 = 0.219, or 21.9% relative to the bright readout.
- The observed readout baseline is about 51 counts, so an on-resonance pODMR feature should be about 51 * 0.219 = 11.2 counts deep in readout 2 relative to readout 1, allowing for ordinary contrast imperfections.
- For detuning delta, I used the rectangular-pulse model
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).
  Across a 5 MHz scan grid this would still make a broad, several-point negative dip near resonance because f_R is 10 MHz.

Observed data:
- Combined readout 1 mean = 51.03 counts, standard deviation across scan points = 1.05 counts.
- Combined readout 2 mean = 50.82 counts, standard deviation across scan points = 1.30 counts.
- Pointwise readout2 - readout1 mean = -0.21 counts, standard deviation = 1.42 counts.
- The largest negative pointwise differences are about -2.7 counts at 3.825 GHz and -2.6 counts at 3.905 GHz, far smaller than the expected about -11 count resonant dip and not arranged as a broad Rabi-broadened pODMR feature.
- A least-squares fit of the expected pulse response shape to the normalized readout2/readout1 data gives a small positive amplitude rather than the expected negative contrast dip. Thus the observed structure is inconsistent with the physical pODMR signal expected from the active pulse.

Decision:
No pODMR resonance is present. The active pulse should produce an easily visible roughly 22% post-pulse fluorescence reduction if the swept microwave frequency hit the NV transition, but the measured variations are only noise-scale and have the wrong coherent shape.
