Sequence interpretation:

The active sequence is Rabimodulated with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV, then performs a detection before any microwave pulse; because full_expt is 0, the optional m_S = +1 reference block is skipped. The second active readout occurs after a single rabi_pulse_mod_wait_time call using length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection.

Readout roles:

Readout 1 is the initialized m_S = 0 bright reference. Readout 2 is the signal after the microwave Rabi pulse. There is no active independent dark-state reference in this run.

Pulse and expected response:

The stated setup gives about 10 MHz Rabi frequency at mod_depth = 1, so a 52 ns pulse is near a pi-scale pulse on resonance. Given the about 22% m_S = 0 to m_S = +1 contrast scale, a true resonance should produce a sizable and frequency-localized reduction of the post-pulse readout relative to the pre-pulse bright reference.

Data assessment:

The two combined raw readouts fluctuate at the few-count level across the scan, but readout 2 does not show a stable localized dip relative to readout 1. Around the likely central scan region, readout 2 is often comparable to or above readout 1 rather than showing the expected darkening. The per-average traces are also not a strong independent repeatability test here because stored averages can reflect tracking cadence, but they likewise do not establish a consistent resonance-shaped contrast feature.

Decision:

No convincing pODMR resonance is present in this scan.
