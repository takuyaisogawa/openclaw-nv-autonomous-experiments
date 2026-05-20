Sequence XML and raw export review for podmr_043_2026-05-16-231159.

Active sequence:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first acquire a true m_S = 0 reference: polarize, detect, then wait.
- The m_S = 1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion = 1 is defined.
- The active microwave-dependent readout is acquired after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns.

Pulse expectation:
- With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is approximately a pi pulse.
- On resonance, this should transfer population from m_S = 0 toward m_S = +1 and produce a lowered fluorescence readout with contrast on the order of the setup scale, about 22%, relative to the m_S = 0 reference.

Observed raw readouts:
- The second readout compared with the first readout changes by only a few percent across the scan.
- Many of the larger deviations have the second readout higher than the reference, which is the opposite sign from the expected resonant pi-pulse fluorescence dip.
- The most dip-like point near 3.885 GHz is only about -2.4% in the combined readout, far below the expected contrast scale, and the stored averages do not provide a strong independent repeatability check because they can reflect tracking cadence.

Decision:
No convincing pODMR resonance is present in this scan. The data show small, irregular readout fluctuations rather than a resonance-scale, frequency-localized microwave-induced fluorescence decrease.
