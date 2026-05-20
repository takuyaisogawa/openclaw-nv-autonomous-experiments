Active sequence and roles:

- The active scan is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first polarizes the NV and detects immediately; this is the true m_S = 0 bright reference readout.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 2 is the post-microwave readout.

Pulse interpretation:

- With the stated setup calibration, Rabi frequency is about 10 MHz at mod_depth = 1.
- A 52 ns pulse is close to a pi pulse at that drive strength.
- If a pODMR resonance were present in the swept range, readout 2 should show a clear fluorescence loss relative to the readout 1 bright reference, on the order of the setup contrast scale near 22%, at the resonant frequency.

Data assessment:

- The combined readouts are both near 46 to 50 counts and cross each other repeatedly.
- The readout 2 minus readout 1 difference changes sign across the sweep rather than forming a localized, repeatable dip in the post-pulse readout.
- The largest excursions are only a few counts and are comparable to point-to-point noise and average-to-average drift.
- Stored averages should not be treated as a strong independent repeatability test here, and the per-average traces show broad drift/cadence structure rather than a stable resonance-shaped ODMR feature.

Decision:

No convincing pODMR resonance is present. Given the active near-pi pulse and expected contrast, a true resonance should be much more apparent as a post-pulse fluorescence decrease relative to the bright reference.
