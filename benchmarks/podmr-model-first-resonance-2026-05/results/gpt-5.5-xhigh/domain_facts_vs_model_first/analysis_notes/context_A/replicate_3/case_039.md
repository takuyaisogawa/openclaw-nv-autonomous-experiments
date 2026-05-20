Case podmr_024_2026-05-16-175646.

The provided sequence XML is Rabimodulated.xml. The active instruction path first polarizes the NV, performs a detection immediately after polarization, waits, then applies one Rabi-modulated microwave pulse and performs a second detection. The `full_expt` branch is disabled (`full_expt = 0`), so the optional m_S = +1 reference acquisition is skipped.

Readout roles:
- readout 1 is the post-polarization reference, nominally the m_S = 0 fluorescence level.
- readout 2 is the signal after the microwave Rabi pulse.

Pulse settings used for the decision:
- `length_rabi_pulse = 52 ns`.
- `mod_depth = 1` in the provided sequence XML and exported variable values.
- With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. A true resonance should therefore produce a large reduction in readout 2 relative to the m_S = 0 reference, on the order of the setup contrast scale rather than a few-percent fluctuation.

Observed raw data:
- readout 2 does not show a consistent dip relative to readout 1 across the 3.825 to 3.925 GHz scan.
- The lowest combined readout-2/readout-1 ratio is about 0.969 near 3.895 GHz, far smaller than the expected roughly 22% contrast-scale change for an on-resonant near-pi pulse.
- Several points have readout 2 above readout 1, and the per-average traces show offset changes consistent with tracking cadence rather than a stable resonance feature.

Decision: resonance absent.
