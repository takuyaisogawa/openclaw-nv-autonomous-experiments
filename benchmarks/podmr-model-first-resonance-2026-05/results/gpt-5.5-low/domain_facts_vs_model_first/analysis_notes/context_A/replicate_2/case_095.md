Sequence/readout analysis for podmr_081_2026-05-17-110558

The active sequence is Rabimodulated.xml while scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed logic first polarizes and detects a true m_S = 0 reference, waits, skips the optional m_S = +1 reference because full_expt = 0, then applies a rabi_pulse_mod_wait_time pulse and performs the signal detection. Thus the two stored readouts should be interpreted as the pre-pulse m_S = 0 reference and the post-pulse microwave/Rabi signal, not as a full 0/1 reference pair.

The provided sequence values show length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale, this corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. If a pODMR resonance were present and well driven, the post-pulse signal should show a localized contrast feature approaching the setup's roughly 22 percent m_S = 0 to m_S = +1 contrast scale, relative to the reference.

The combined readouts do not show a convincing localized resonance. Both channels have a broad downward drift across the scan, with point-to-point variations of only a few counts and no stable, narrow, frequency-localized dip or peak in the post-pulse readout relative to the reference. The per-average traces separate mainly by an offset consistent with tracking or cadence effects, and the averages should not be treated as strong independent repeatability evidence. The apparent changes are much smaller and less structured than expected for a resonant pi-pulse response at this contrast scale.

Decision: resonance_absent.
