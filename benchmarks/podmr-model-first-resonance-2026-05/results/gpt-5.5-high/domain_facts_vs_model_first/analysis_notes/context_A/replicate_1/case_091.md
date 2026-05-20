Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

Readout roles from the XML:
- readout 1 is the first detection immediately after optical polarization, so it is the bright m_S = 0 reference.
- readout 2 is the detection after the microwave rabi_pulse_mod_wait_time call, so it is the microwave-addressed signal readout.
- full_expt is 0, so the optional m_S = 1 reference block is skipped.

The provided sequence XML and variable values indicate mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If the scan crossed a pODMR resonance, the signal readout should show a clear drop relative to the bright reference, potentially on the order of the setup contrast scale (about 22%) for strong transfer.

The combined raw readouts do not show a clear frequency-localized dip in readout 2 relative to readout 1. The two traces cross repeatedly and differ by only a few percent, with fluctuations comparable to the point-to-point noise and the per-average drift. The per-average overlays mainly show a large average-to-average count offset, consistent with tracking cadence effects rather than independent repeatability of a resonance feature.

Decision: no convincing pODMR resonance is present in this scan.
