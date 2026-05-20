Active sequence assessment:

The provided XML and exported active values identify the sequence as Rabimodulated.xml. The active pulse sequence first polarizes and detects the true m_S = 0 level, then because full_expt = 0 it skips the separate m_S = +1 reference block, then applies one rabi_pulse_mod_wait_time pulse followed by the second detection. Thus readout 1 is the pre-microwave m_S = 0 reference and readout 2 is the post-microwave readout used to look for a driven population change.

The active parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse on resonance, so a real resonance should drive a large contrast-scale reduction in the post-pulse readout relative to the m_S = 0 reference. The expected scale is on the order of the stated 22% setup contrast, not merely small percent-level scatter.

The raw readouts do not show that behavior. Readout 2 is close to readout 1 across the scan and sometimes higher, while both traces share a slow downward drift at high scan values. The largest readout differences are small compared with the expected contrast for a near-pi pulse, and the two stored averages mainly show similar noisy/drifting behavior rather than a repeatable resonance feature. Since stored averages can reflect tracking cadence, the per-average overlay is not strong independent evidence for a resonance.

Decision: no convincing pODMR resonance is present in this scan.
