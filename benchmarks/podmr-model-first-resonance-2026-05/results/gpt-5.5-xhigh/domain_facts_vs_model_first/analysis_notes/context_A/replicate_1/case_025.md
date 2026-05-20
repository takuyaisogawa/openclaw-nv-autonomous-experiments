Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML executes an initial polarization and detection, giving a true m_S = 0 reference readout. The optional m_S = +1 reference block is guarded by full_expt, and full_expt is 0, so that block is inactive. The second active detection occurs after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

With the given setup facts, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. Therefore a real pODMR resonance should appear as a local reduction of the post-microwave readout relative to the immediately preceding m_S = 0 reference, potentially approaching the stated 22% contrast scale.

Data assessment:

The combined readout 1 reference drifts downward over the scan, so the absolute raw levels alone are not decisive. The readout 2 signal, however, shows a localized dip near 3.870-3.880 GHz. Around 3.875 GHz, readout 1 is about 40.9 while readout 2 is about 31.2, a suppression of about 24% relative to the reference. Adjacent points around 3.870 and 3.880 GHz also show elevated suppression, while points away from this region mostly have small differences or track the reference drift.

The stored averages have different baselines consistent with tracking cadence, but both averages show the same qualitative post-pulse readout suppression around the same frequency region. Given the active near-pi pulse and the localized contrast-scale dip in the microwave-conditioned readout, the data support a pODMR resonance being present.
