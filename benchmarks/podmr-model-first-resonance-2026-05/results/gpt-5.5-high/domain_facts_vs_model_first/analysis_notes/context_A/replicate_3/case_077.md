Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the provided sequence:
- readout 1 is the "true 0 level reference": optical polarization followed immediately by detection, before any microwave manipulation.
- readout 2 is the signal readout after a rabi_pulse_mod_wait_time pulse and then detection.
- full_expt is 0, so the optional mS=1 reference block is skipped.

Pulse settings used for the decision:
- mod_depth = 1 from the provided sequence XML and the exported active variable values.
- length_rabi_pulse = 52 ns.
- With the given setup scale, mod_depth 1 gives about 10 MHz Rabi frequency, so 52 ns is about 0.52 Rabi cycles, close to a pi pulse. A resonance should therefore produce a strong and coherent drop of readout 2 relative to the mS=0 reference readout, with an available contrast scale on the order of 22%.

Data assessment:
The two readouts both drift downward at the high-frequency end, indicating common-mode tracking or brightness drift rather than a clean ODMR contrast feature. The pointwise readout2/readout1 contrast alternates sign across the scan: examples include negative excursions near 3.840, 3.860, 3.875, 3.900, and 3.915 GHz, but also positive excursions near 3.850, 3.870, 3.880, 3.895, 3.905, and 3.910 GHz. The apparent dips are only a few percent and are not organized into a repeatable resonance-shaped feature. The per-average traces show similar scatter and should not be treated as a strong independent repeatability test because the stored averages can reflect tracking cadence.

Decision: resonance_absent. The scan lacks a consistent MW-induced reduction in the post-pulse readout despite a pulse setting that should make a true resonance visible.
