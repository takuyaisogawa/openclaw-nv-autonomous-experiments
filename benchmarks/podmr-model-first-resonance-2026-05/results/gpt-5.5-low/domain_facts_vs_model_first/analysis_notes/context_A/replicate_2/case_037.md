Case podmr_022_2026-05-16-172725.

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The pulse program first polarizes and detects the true mS = 0 fluorescence reference, then skips the optional mS = +1 reference because full_expt = 0, then applies a single rabi_pulse_mod_wait_time pulse and detects again. Thus readout 1 is the pre-microwave 0-level reference and readout 2 is the post-pulse signal. The actual variable values report mod_depth = 1 and length_rabi_pulse = 52 ns; with the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a resonant pi pulse duration.

If a pODMR resonance were present, the post-pulse readout should show a clear fluorescence reduction relative to the 0-level reference at the resonant microwave frequency, with a possible contrast scale up to roughly 22% between mS = 0 and mS = +1. The combined raw traces instead show readout 1 and readout 2 staying on the same scale with point-to-point differences of only a few counts and no localized, repeatable dip in the post-pulse readout. The per-average overlay is dominated by drift/tracking cadence rather than a stable resonance feature, and the two stored averages do not provide strong independent repeatability.

Decision: resonance absent.
