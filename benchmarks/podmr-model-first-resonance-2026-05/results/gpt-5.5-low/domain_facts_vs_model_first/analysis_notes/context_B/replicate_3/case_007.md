Analysis note for podmr_011_2026-05-11-181506

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name in the export is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect. This is the true m_S = 0 optical reference, corresponding to readout 1.
- full_expt is 0, so the optional +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This post-Rabi detection is readout 2.
- The relevant standalone sequence XML values are length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation:
- Domain fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for this sequence.
- For a rectangular pulse, transferred population on resonance is P = sin^2(pi f_R t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Domain fact: the optical contrast scale between m_S = 0 and m_S = +1 is about 22%.
- Expected on-resonance fractional drop in the post-pulse readout relative to the m_S = 0 reference is 0.22 * 0.996 = 0.219, so the expected ratio readout2/readout1 is about 0.781.

Observed quantitative comparison:
- The deepest measured ratio readout2/readout1 occurs at 3.880 GHz: 16.980769 / 21.346154 = 0.7955, a 20.45% drop.
- This is close to the calculated 21.9% expected drop for an on-resonance nearly pi pulse.
- A simple detuned Rabi model P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi t sqrt(f_R^2 + df^2)), fit as ratio = offset - depth * P(df), gives best center about 3.877 GHz, fitted depth 0.199, and reduces SSE by about 79% relative to a constant-ratio model.
- The fitted depth is also close to the independent 22% setup contrast scale.

Decision:
The post-Rabi readout shows a frequency-localized drop with the correct magnitude for the specified pulse duration and modulation depth. Stored per-average traces mainly show drift/tracking cadence, but the combined readout ratio and explicit pulse model support a real pODMR resonance.
