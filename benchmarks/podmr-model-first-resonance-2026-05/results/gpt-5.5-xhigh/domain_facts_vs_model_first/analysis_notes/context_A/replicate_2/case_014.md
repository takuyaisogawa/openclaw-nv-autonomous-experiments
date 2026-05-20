Active sequence: the scan uses Rabimodulated.xml with mw_freq as the swept variable. The active instructions first acquire the true m_S = 0 reference after optical polarization, then skip the optional m_S = 1 reference block because full_expt = 0, then apply rabi_pulse_mod_wait_time and acquire the signal detection.

Readout roles: readout 1 is the polarized m_S = 0 reference. Readout 2 is the post-microwave-pulse signal readout. There is no active independent m_S = 1 reference in this run.

Pulse settings: mod_depth = 1 and length_rabi_pulse = 52 ns. Using the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse, so a true resonance should strongly reduce the post-pulse signal readout relative to the m_S = 0 reference, on the order of the known 22% contrast scale.

Data assessment: the combined readouts show a localized suppression of readout 2 near 3.875 GHz. At that point readout 1 is about 38.5 while readout 2 is about 28.83, a roughly 25% drop relative to the reference. Neighboring points around 3.870 to 3.880 GHz are also suppressed, while readout 1 remains near its normal baseline. The two stored averages have different baselines consistent with tracking cadence, but both retain a central post-pulse depression rather than a reference-channel artifact.

Decision: a pODMR resonance is present.
