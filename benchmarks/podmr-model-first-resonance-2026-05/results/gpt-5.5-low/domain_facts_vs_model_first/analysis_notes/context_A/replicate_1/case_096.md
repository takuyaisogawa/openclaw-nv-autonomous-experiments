Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- The first detection immediately follows adj_polarize and is the true m_s = 0 fluorescence reference.
- full_expt is 0, so the optional m_s = +1 reference block is not active.
- The second detection follows rabi_pulse_mod_wait_time and is the microwave-pulse signal readout.

Pulse settings:
- mod_depth is recorded as 1 in the provided sequence/variable values.
- length_rabi_pulse is 52 ns.
- With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, the pulse is about 0.52 Rabi cycles, close to a pi pulse. On resonance, this should produce a large transfer from m_s = 0 toward m_s = +1 and therefore a sizeable fluorescence drop, on the order of the stated 22% contrast scale if well driven.

Data assessment:
- The raw readouts are clustered around 50 counts with point-to-point scatter of a few counts.
- The post-pulse signal readout does not show a clear localized dip relative to the 0-reference readout at a plausible resonance frequency.
- Some points in the higher-frequency part of the scan have lower signal than reference, but the feature is broad/noisy, comparable to the per-average scatter, and not a strong repeatability check because only two stored averages are present and these may reflect tracking cadence.
- Given the expected contrast for a near-pi pulse at mod_depth = 1, the observed variations are too weak and inconsistent to call a pODMR resonance.

Decision: resonance_absent.
