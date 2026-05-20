Case podmr_007_2026-05-11-064944.

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active sequence first polarizes and detects the bright m_S = 0 reference, then because full_expt = 0 it skips the separate m_S = +1 reference branch. It then applies one rabi_pulse_mod_wait_time pulse and detects again. Therefore readout 1 is the polarized bright reference and readout 2 is the microwave-pulse signal readout, not an independent dark reference.

The sequence values show length_rabi_pulse = 52 ns and mod_depth = 1. With the given setup estimate of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so a real resonance should produce a clear fluorescence reduction in readout 2 relative to readout 1, potentially on the order of the setup's m_S = 0 to m_S = +1 contrast scale.

The combined readouts do not show a stable, coherent pODMR dip. The normalized signal has isolated low points, especially near 3.855 GHz and 3.895 GHz, but the trace is jagged, neighboring points do not form a convincing line shape, and the per-average overlay suggests the variations are strongly affected by drift/tracking cadence rather than repeatable resonance structure. Since stored averages are not a strong independent repeatability test here, I do not treat the isolated low points as sufficient evidence.

Decision: resonance_absent.
