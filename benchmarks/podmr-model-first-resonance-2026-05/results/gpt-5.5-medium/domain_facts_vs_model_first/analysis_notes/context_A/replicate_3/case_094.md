<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML has full_expt = 0, so the enabled acquisition consists of:
- readout 1: after adj_polarize, before the microwave pulse, serving as the true mS = 0 / bright reference.
- readout 2: after rabi_pulse_mod_wait_time and detection, serving as the microwave-affected signal readout.

The mS = +1 reference branch is skipped because full_expt is zero, despite do_adiabatic_inversion being set true. The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Given the stated setup, Rabi frequency is about 10 MHz at mod_depth = 1, so a 52 ns pulse is approximately a pi pulse on resonance. If a pODMR resonance were present, readout 2 should show a clear fluorescence reduction relative to readout 1 near resonance, with scale related to the roughly 22% mS = 0 to mS = +1 contrast.

The combined readouts do not show such a feature. The readout2/readout1 ratio ranges only about 0.965 to 1.030 and has no convincing, localized, repeatable dip. The deepest apparent low point is small compared with the expected contrast and the per-average overlays show large average-to-average offsets consistent with tracking cadence rather than a robust resonance feature. Therefore I classify this case as resonance absent.
