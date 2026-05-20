The active sequence is Rabimodulated.xml. In the provided sequence XML, full_expt = 0, so the optional "Acquire 1 level reference" block is not active even though do_adiabatic_inversion is true. The two acquired readouts are therefore: readout 1 after polarization/detection as the true m_S = 0 reference, and readout 2 after the modulated Rabi microwave pulse followed by detection.

The active Rabi pulse uses length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns, with mod_depth = 1. For the stated setup, mod_depth = 1 gives about a 10 MHz Rabi frequency, so 52 ns is approximately a pi pulse on resonance. A real pODMR resonance should therefore produce a large suppression in readout 2 relative to the m_S = 0 reference, with a contrast scale comparable to the stated ~22% m_S = 0 to m_S = +1 contrast.

The combined readouts show readout 2 dropping sharply around 3.875-3.880 GHz, from a baseline near 38-40 down to about 31, while readout 1 remains near 40. At the deepest points, the readout-2 suppression relative to readout 1 is roughly 23-24%, matching the expected contrast scale for a near-pi pulse. The same dip is visible in both stored averages, although the averages should mainly be treated as tracking-cadence snapshots rather than a strong repeatability test.

Decision: a pODMR resonance is present.
