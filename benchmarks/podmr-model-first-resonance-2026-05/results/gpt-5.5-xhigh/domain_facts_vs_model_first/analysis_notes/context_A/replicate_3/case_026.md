Active sequence and readout roles

The sequence is the Rabimodulated pODMR scan while varying mw_freq from 3.825 GHz to 3.925 GHz. The active instruction path first polarizes the NV and detects immediately, which makes readout 1 the true m_S = 0 bright reference. The "Acquire 1 level reference" block is gated by full_expt, and full_expt is 0, so that block is inactive. After the reference readout, the active experiment applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detects again; therefore readout 2 is the post-microwave signal readout.

Sequence parameters relevant to the decision

The provided sequence uses mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With the 250 MHz sample rate, this pulse is exactly 13 samples, so it remains 52 ns after rounding. Given the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, the expected pi-pulse time is about 50 ns, so this pulse should strongly transfer population on resonance.

Observed response

Readout 1 stays near the bright reference level over the scan, around 42 counts, with only modest scan-to-scan structure. Readout 2 has a clear, localized dip centered near 3.88 GHz, reaching about 33.1 counts while the simultaneous readout 1 is about 41.4 counts. The deepest readout2/readout1 ratio is about 0.80, a roughly 20% reduction, which is close to the stated 22% contrast scale for m_S = 0 to m_S = +1. The per-average traces both show the same central readout 2 depression, but the stored averages are treated mainly as tracking cadence rather than a strong independent repeatability test.

Decision

The active sequence applies a near-pi microwave pulse before readout 2, and readout 2 shows a localized contrast-scale fluorescence decrease while readout 1 remains a bright reference. This is consistent with a pODMR resonance being present.
