Case: podmr_008_2026-05-11-131831

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence identification:
- Sequence: Rabimodulated.xml.
- Varying scan parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Readout 1 role: after adj_polarize and before the scanned Rabi pulse, so it is the polarized m_S = 0 optical reference.
- Readout 2 role: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...), so it is the pODMR signal readout after the microwave pulse.
- Provided XML pulse settings: length_rabi_pulse = 52 ns, mod_depth = 1.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- With approximately linear scaling, the XML mod_depth = 1 gives f_R = 10 MHz.
- For a resonant rectangular pulse, the transferred population is P = sin^2(pi * f_R * tau).
- tau = 52 ns, so P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With m_S = 0 to m_S = +1 optical contrast scale about 22%, the expected on-resonance pODMR signal change is 0.22 * 0.996 = 0.219, i.e. about a 21.9% dip in readout 2 relative to the polarized reference.
- The mean readout 1 level is 20.08 raw-count units, so the expected resonant reduction is about 4.40 raw-count units, placing a resonant readout 2 near 15.68 counts if the scan crosses the addressed transition.

Observed quantitative comparison:
- Combined readout 1: mean 20.08, standard deviation 0.89, range 18.69 to 21.56.
- Combined readout 2: mean 19.79, standard deviation 0.59, range 18.60 to 21.19.
- The smallest readout 2 value is 18.60, only about 1.20 counts below the readout 2 mean and far above the approximately 15.68 count level expected for a resonant near-pi pulse.
- The normalized readout2/readout1 ratio has mean 0.988, standard deviation 0.055, and minimum 0.881 at 3.840 GHz. That isolated low ratio is driven by a high readout 1 and low readout 2 point, not a clear resonant feature in readout 2 of the expected amplitude.
- Per-average traces show large monotonic tracking drift between averages, so the stored averages are not a strong independent repeatability test here.

Decision:
The active sequence should produce a large pODMR dip if a resonance is present under the provided XML pulse settings. The observed signal lacks a dip of the expected magnitude or a convincing reproducible resonance-like feature. I therefore classify this case as resonance_absent.
