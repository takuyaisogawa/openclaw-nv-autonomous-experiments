Case podmr_013_2026-05-16-123121

The provided sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz. The active instructions first polarize and detect a true m_S = 0 reference, then because full_expt = 0 they skip the optional m_S = +1 reference block. The final active block applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detects. Therefore readout 1 is the 0-level/reference readout and readout 2 is the microwave-pulsed signal readout.

For this setup, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the swept microwave frequency hits the NV transition, the pulsed signal should show a strong PL drop relative to the 0 reference, up to the stated contrast scale of about 22%.

The combined raw readouts show readout 1 staying roughly flat near 43-46 counts while readout 2 has a pronounced, localized dip around 3.875-3.880 GHz, falling from a local baseline near 42-44 counts to about 34 counts. That is roughly a 20-22% drop, matching the expected contrast for a near-pi pulse. The per-average overlay shows the same dip structure in both stored averages, although the averages may also reflect tracking cadence and should not be over-weighted as independent repeatability evidence.

Decision: a pODMR resonance is present.
