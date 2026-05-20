Case: podmr_011_2026-05-16-120107

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR with mw_freq swept from 3.825 GHz to 3.925 GHz.
- The active microwave pulse is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)` followed by detection.
- `full_expt = 0`, so the optional "Acquire 1 level reference" block is inactive.
- Readout roles: readout 1 is the first detection after optical polarization and is therefore the true m_S = 0 reference. Readout 2 is the detection after the swept microwave Rabi pulse and is the resonance-sensitive signal readout.
- Pulse duration: length_rabi_pulse = 52 ns, already aligned to the 250 MHz sample rate because 52 ns equals 13 samples.
- mod_depth: the provided XML variable value is mod_depth = 1.

Quantitative model calculation:
- Setup contrast scale between m_S = 0 and m_S = +1: about 22%.
- Rabi frequency at mod_depth = 1: about 10 MHz.
- For a resonant rectangular Rabi pulse, using cyclic Rabi frequency f_R, the transferred population is P = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected fractional fluorescence drop at resonance is therefore 0.22 * 0.996 = 0.219, about 21.9%.
- Using the measured off-resonance/raw baseline near 42.7 counts, the expected resonant dip amplitude is about 42.7 * 0.219 = 9.36 counts.

Data comparison:
- Readout 1, the m_S = 0 reference, stays relatively flat: mean 42.20 counts, population standard deviation 0.82 counts, minimum 40.77 counts.
- Readout 2 has a clear dip centered near 3.880 GHz: edge/off-resonance mean about 41.40 counts, minimum 33.10 counts, dip amplitude 8.31 counts.
- The observed signal-readout dip is 8.31 / 9.36 = 0.89 of the expected full-contrast resonant-pulse dip, well within a plausible range for a real pODMR feature under this simple model.
- The per-average overlay shows the dip in both stored averages, but I treat that only as supporting evidence because stored averages can reflect tracking cadence.

Decision:
The physically expected resonant response for the active 52 ns, mod_depth 1 Rabi pulse is a large dip only in the post-pulse signal readout, and the data show just such a dip near 3.880 GHz with the correct order of magnitude. A pODMR resonance is present.
