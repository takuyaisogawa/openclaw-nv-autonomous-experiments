Active sequence and readout roles:

The provided sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz. The active experiment has full_expt = 0, so the optional m_S = +1 reference branch is not executed. Each scan point first acquires a true m_S = 0 bright reference after optical polarization, then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then acquires the post-pulse readout.

Pulse interpretation:

Using the stated setup scale, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so the 52 ns pulse is close to a pi pulse on resonance. With an m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant transition should make the post-pulse readout substantially lower than the pre-pulse bright reference near resonance.

Data assessment:

The combined raw readouts are noisy and show only small, irregular differences between the pre-pulse reference and post-pulse readout, typically a few percent rather than anything near the expected pi-pulse contrast. The per-average traces mainly show strong opposite tracking drift between the two stored averages; that cadence-related drift largely explains the broad trends and does not provide an independent repeatability test. There is no localized, reproducible post-pulse dip against the pre-pulse reference that would support a pODMR resonance.

Decision: resonance_absent.
