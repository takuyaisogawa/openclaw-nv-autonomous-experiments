Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The active instructions polarize, detect, wait, then apply a Rabi-modulated microwave pulse and detect again. The optional "Acquire 1 level reference" block is inactive because full_expt = 0, so readout 1 is the polarized m_S = 0 reference and readout 2 is the post-microwave signal readout, not an independent m_S = +1 reference.

The provided sequence values give mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. A resonance should therefore make readout 2 lower than readout 1 by a large fraction of the available m_S = 0 to m_S = +1 contrast, whose scale is about 22%.

The combined readouts show readout 2/readout 1 near unity over much of the scan, but a localized minimum around 3.875-3.880 GHz. The deepest point is 3.880 GHz: readout 1 = 35.654 and readout 2 = 29.308, ratio = 0.822, or about 17.8% lower. The neighboring 3.875 GHz point is also low, ratio = 0.923. This is the right sign and magnitude for a resonance under this sequence. The per-average traces are dominated by tracking drift/cadence, but both averages still support reduced post-pulse readout near the dip rather than a single-average artifact.

Decision: resonance present.
