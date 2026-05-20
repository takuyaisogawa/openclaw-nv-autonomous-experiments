Case: podmr_079_2026-05-17-103702

Sequence/readout identification:

- The provided sequence XML is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active readout sequence first runs adj_polarize followed by detection: this is readout 1, the true m_S = 0 bright reference.
- The optional m_S = +1 reference block is skipped because full_expt = 0.
- The active signal operation is then rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection: this is readout 2, the pulsed pODMR signal.
- sample_rate = 250 MHz, so the 52 ns pulse is 13 samples and remains 52 ns after rounding.

Quantitative expected-signal model:

Using the given setup facts, the Rabi frequency at mod_depth = 1 is f_R = 10 MHz. For a square pulse of duration t = 52 ns, the two-level excitation probability versus detuning df is

P_exc(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * t * sqrt(f_R^2 + df^2)).

The optical readout contrast scale between m_S = 0 and m_S = +1 is about C = 0.22, so the expected pulsed/reference ratio for a resonance is

readout2/readout1 = 1 - C * P_exc(df).

Model values:

- df = 0 MHz: P_exc = 0.996, expected contrast = 21.9%, expected drop = 11.1 counts for mean readout1 = 50.72.
- df = 2.5 MHz: P_exc = 0.929, expected contrast = 20.4%, expected drop = 10.4 counts.
- df = 5 MHz: P_exc = 0.749, expected contrast = 16.5%, expected drop = 8.4 counts.
- df = 10 MHz: P_exc = 0.273, expected contrast = 6.0%, expected drop = 3.0 counts.

Because the scan spacing is 5 MHz, any resonance inside the scanned interval should place at least one sampled point within 2.5 MHz of resonance and should therefore produce about a 20% pulsed-readout drop relative to the bright reference.

Observed data:

- mean readout1 = 50.718 counts.
- mean readout2 = 50.782 counts.
- mean readout2 - readout1 = +0.064 counts.
- The minimum observed readout2/readout1 ratio is 0.9607, i.e. the largest observed positive contrast is only 3.93%.
- The largest negative readout2 - readout1 excursion is about -2.10 counts, far smaller than the 10 to 11 count drop expected for a sampled resonance.
- Stored averages differ at a level consistent with tracking/cadence variation, so I did not treat the two averages as a strong independent repeatability test.

Decision:

The active 52 ns modulated pulse at mod_depth = 1 should act as a near-pi pulse on resonance and produce a large localized pulsed-readout dip. The measured pulsed readout stays close to the bright reference and never approaches the expected 22% contrast-scale drop. I decide that a pODMR resonance is absent in this scan.
