Case: podmr_016_2026-05-12-120649

I used the provided sequence XML and raw export, not labels or prior outputs.

Active sequence and roles:
- SequenceName: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes, then performs a detection before any microwave pulse. This is the m_s = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional m_s = +1 reference block is skipped.
- The active pODMR measurement then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s and mod_depth = 1, followed by detection. This is the post-pulse signal, corresponding to readout 2.

Pulse scale:
- With mod_depth = 1, the setup Rabi frequency is about 10 MHz.
- A 52 ns pulse is approximately a pi-pulse at that Rabi frequency.
- If a resonance were present and well addressed by this pulse, the signal readout should show a fluorescence reduction on the order of the available m_s = 0 to m_s = +1 contrast, about 22%, relative to the reference.

Data assessment:
- The combined signal/reference ratios are mostly near 1.0, with the deepest signal dips only about 0.947 of the reference at 3.895 GHz and 3.915 GHz.
- Those small dips are far below the expected near-pi-pulse contrast scale and are not a coherent broad resonance feature.
- The raw readouts and per-average traces show strong common drift/tracking structure, and the stored averages should not be treated as independent repeatability evidence.

Decision: resonance_absent.
