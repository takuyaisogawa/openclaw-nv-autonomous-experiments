Sequence and readout interpretation:
- The active sequence is Rabimodulated.xml varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is skipped. The two readouts are therefore the initial polarized/0-level reference detection followed by detection after the modulated Rabi pulse.
- mod_depth = 1 and length_rabi_pulse = 52 ns. With the given setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance, so a true pODMR resonance should produce a substantial reduction in the post-pulse readout relative to the 0-reference, on the order of the stated 22% contrast scale.

Data assessment:
- The combined raw readouts are both around 52-54 counts across the sweep and track each other closely; the post-pulse readout is not consistently suppressed at any frequency by a contrast-scale amount.
- There are isolated excursions, especially in readout 1 near 3.915-3.920 GHz, but they are not mirrored as a stable resonance-like dip in the post-pulse channel and appear comparable to tracking/average-dependent fluctuations.
- The two stored averages differ mainly by an offset/tracking cadence pattern, so they do not provide strong independent repeatability evidence for a resonance.

Decision: resonance_absent. The sequence should be sensitive under these pulse conditions, but the data lack a reproducible, contrast-scale pODMR feature in the active post-pulse readout relative to the 0-reference.
