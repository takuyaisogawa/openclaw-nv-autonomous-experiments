Sequence interpretation:

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz. The XML instructions acquire a true m_S = 0 bright reference first using adj_polarize followed by detection, then, because full_expt = 0, skip the explicit m_S = +1 reference block and run one rabi_pulse_mod_wait_time before the second detection. Thus readout 1 is the bright reference and readout 2 is the microwave-pulsed signal readout.

The provided sequence XML uses length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, the pulse is about half a Rabi period, so on resonance it should behave near a pi pulse. Given the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a real resonance should produce a pronounced localized reduction of the pulsed readout relative to the bright reference, much larger and more coherent than ordinary point scatter.

Data assessment:

The combined readouts fluctuate around the high-40s with readout 2 sometimes below readout 1 and sometimes above it. There is no consistent, localized dip in the pulsed readout relative to the reference across the scanned microwave frequencies. The per-average traces show substantial tracking/noise-like offsets and do not provide strong independent repeatability. The largest deviations are only a few counts and change sign, whereas a near-pi pulse on a real resonance should give a clearer contrast-scale feature.

Decision:

No reliable pODMR resonance is present in this scan.
