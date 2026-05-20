Case: podmr_081_2026-05-17-110558

I used the saved sequence and variables embedded in inputs/raw_export.json as the active acquisition record. The active sequence is Rabimodulated.xml. The acquisition varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, with 21 points, 2 stored averages, and 100000 repetitions.

Active pulse/readout structure:
- The sequence first performs optical polarization, then detection. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional separate m_S = +1 reference block is skipped.
- The active microwave operation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. This is the post-pulse pODMR readout.
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-microwave-pulse readout.

Quantitative expected-signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, and linear scaling with mod_depth, the active f_R is 10 MHz.
- For a resonant square Rabi pulse of duration tau = 52 ns, the transferred population is P = sin^2(pi * f_R * tau).
- P = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.9961.
- With m_S = 0 to m_S = +1 contrast scale about 22%, the expected resonant fluorescence drop is 0.22 * 0.9961 = 0.2191, or about 21.9% of the reference.
- The mean m_S = 0 reference readout is 47.339 counts, so the expected drop at resonance is about 10.37 counts. A resonant point should therefore have post-pulse readout near 36.97 counts if the pulse drives the NV transition cleanly.

Observed data:
- Mean readout 1: 47.339
- Mean readout 2: 47.097
- Mean readout1 - readout2: 0.242 counts
- Standard deviation of pointwise readout1 - readout2 across the scan: 1.269 counts
- Minimum and maximum pointwise readout1 - readout2: -1.692 to 2.154 counts
- Mean readout2/readout1: 0.9952, with range 0.9548 to 1.0372.

The largest observed post-pulse reduction is only about 4.5%, and most points show no systematic reduction. This is far below the approximately 21.9% drop predicted by the active pulse model for a resonance. The scan also lacks a localized dip of the expected magnitude anywhere in the frequency range. Stored averages differ by an offset consistent with tracking cadence, so I did not treat average-to-average separation as independent resonance evidence.

Decision: resonance_absent.
