Active sequence and roles:

The provided sequence is Rabimodulated.xml with mw_freq swept. It first polarizes the NV and immediately performs a detection readout; this is the true m_S = 0 bright-state reference and corresponds to readout 1. The full_expt branch is inactive, so no separate m_S = +1 reference is acquired. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection; this post-microwave signal corresponds to readout 2.

Pulse settings:

The active rabi pulse duration is 5.2e-08 s, rounded at 250 MS/s to 52 ns. The active mod_depth is 1. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, the pulse is approximately a pi pulse, so on resonance it should be capable of producing close to the full m_S = 0 to m_S = +1 contrast scale, about 22%.

Data assessment:

The post-microwave readout has a pronounced local dip at the central scan points around 3.875 to 3.880 GHz: readout 2 falls to about 30.6 and 30.3 while the reference readout remains about 41.0 and 39.2. That is roughly a 23-25% drop relative to the simultaneous bright reference at the deepest points, matching the expected contrast scale for an approximately pi pulse. The neighboring points recover toward the high-30s, so this is a localized resonance-like feature rather than a broad tracking offset. The stored per-average traces are only two averages and may reflect tracking cadence, but both averages show the same central suppression in the post-pulse readout.

Decision:

A pODMR resonance is present.
