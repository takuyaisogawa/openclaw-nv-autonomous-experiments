Active sequence: Rabimodulated.xml / Rabimodulated.xml-style pODMR scan varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles from the provided sequence XML:
- The first detection occurs after optical polarization and before the microwave pulse, so readout 1 is the bright m_S = 0 reference.
- full_expt is 0, so the optional m_S = 1 reference block is skipped.
- The second active detection occurs after rabi_pulse_mod_wait_time, so readout 2 is the microwave-pulse signal readout.

Pulse parameters:
- mod_depth = 1 in inputs/sequence.xml and Variable_values.
- length_rabi_pulse = 52 ns.
- With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is approximately a pi pulse. If the microwave frequency were resonant, the post-pulse signal readout should show a sizeable contrast change on the order of the setup's 22% m_S = 0 to m_S = +1 scale.

Data assessment:
- The combined readouts fluctuate around roughly 48 to 52 counts, with no clean frequency-localized dip in the signal readout relative to the pre-pulse reference.
- The signal readout does not show a coherent ODMR-like contrast feature at the expected scale for a near-pi pulse; the largest excursions are comparable to scan noise and baseline wander.
- The two stored averages differ substantially and appear consistent with tracking cadence/noise rather than independent repeatable confirmation.

Decision: resonance_absent. There is no convincing pODMR resonance in this scan.
