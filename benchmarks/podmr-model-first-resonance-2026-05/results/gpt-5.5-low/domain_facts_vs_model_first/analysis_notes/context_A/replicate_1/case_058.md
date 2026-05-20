Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- First detection occurs immediately after adj_polarize and is the true m_S = 0 / bright reference.
- full_expt = 0, so the optional m_S = 1 reference block is not active.
- Second detection occurs after rabi_pulse_mod_wait_time and is the signal readout after the microwave pulse.

Pulse settings used for the decision:
- length_rabi_pulse = 52 ns.
- mod_depth = 1 from the provided sequence/variable values.
- With the stated setup calibration, the expected Rabi frequency is about 10 MHz at mod_depth = 1, so a 52 ns pulse is approximately a pi pulse when on resonance.
- If an ODMR resonance were present, the second readout should show a clear localized reduction relative to the first readout, on the order of the setup contrast scale.

Observed data:
- The two combined raw readouts track closely across the scan, with point-to-point fluctuations and slow drift but no robust localized dip in the post-pulse readout relative to the m_S = 0 reference.
- The per-average traces show large average-to-average offsets consistent with tracking cadence; they do not provide strong independent repeatability evidence for a resonance.
- The post-pulse readout is sometimes higher than the reference and does not show the expected ~22% contrast-scale suppression near any frequency.

Decision: resonance_absent. The data do not show a credible pODMR resonance under an active near-pi-pulse condition.
