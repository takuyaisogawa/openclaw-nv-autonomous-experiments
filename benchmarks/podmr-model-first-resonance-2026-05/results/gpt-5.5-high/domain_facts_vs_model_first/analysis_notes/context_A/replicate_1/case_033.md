Active sequence and roles:

The active sequence is Rabimodulated.xml. The instructions first polarize and detect, then because full_expt = 0 they skip the separate m_S = +1 reference block, then apply a modulated rabi pulse and detect again. Therefore readout 1 is the true m_S = 0 / bright reference, while readout 2 is the post-microwave signal readout.

Pulse settings:

The provided sequence XML and exported Variable_values give length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, and mod_depth = 1. At the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is approximately a pi-pulse duration, so an on-resonance microwave transition should produce a large drop in the signal readout, up to the order of the stated 22% contrast scale. The embedded sequence text inside raw_export contains an older/default-looking mod_depth = 0.3 line, but the active exported variable values and provided XML indicate mod_depth = 1.

Data assessment:

Readout 1 stays comparatively flat in the upper 40s across the scan, consistent with a stable bright reference rather than a broad optical or tracking artifact. Readout 2 shows a clear localized dip centered near 3.875-3.880 GHz, falling from a typical baseline around 47-49 counts down to about 39 counts. That is roughly a 17-20% decrease relative to the surrounding signal, close to the expected scale for an m_S = 0 to m_S = +1 contrast measurement with a near-pi pulse. The two stored averages both show the same central depression in readout 2, but I do not overweight that because stored averages may mainly reflect tracking cadence.

Decision:

A pODMR resonance is present.
