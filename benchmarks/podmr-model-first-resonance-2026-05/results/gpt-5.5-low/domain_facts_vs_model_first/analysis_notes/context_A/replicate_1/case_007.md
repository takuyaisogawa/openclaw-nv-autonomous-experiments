Sequence review:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The instructions acquire a true 0-level reference by polarization followed by detection, then wait. The optional 1-level reference block is disabled because full_expt = 0, so the acquired second readout is the detection after the active Rabi-modulated microwave pulse, not an independent 1-level reference.

Relevant active settings from the provided XML are length_rabi_pulse = 52 ns and mod_depth = 1. With the given setup scale of about 10 MHz Rabi frequency at mod_depth = 1, the pulse duration is approximately a half period / pi pulse condition. Therefore, an on-resonance microwave drive should produce a large drop in the post-pulse readout relative to the bright reference, on the order of the stated 22 percent m_S = 0 to m_S = +1 contrast.

The combined raw readouts show readout 1 staying near roughly 20 to 22 counts across the scan, while readout 2 has a broad, deep minimum near 3.875 to 3.88 GHz, reaching about 17 counts compared with a reference near 21 to 22 counts. That drop is approximately the expected contrast scale for a near-pi pulse. The per-average traces show strong tracking-like baseline drift, so they are not a strong independent repeatability test, but the combined post-pulse suppression has the correct role, magnitude, and frequency-localized shape for a pODMR resonance.

Decision: resonance present.
