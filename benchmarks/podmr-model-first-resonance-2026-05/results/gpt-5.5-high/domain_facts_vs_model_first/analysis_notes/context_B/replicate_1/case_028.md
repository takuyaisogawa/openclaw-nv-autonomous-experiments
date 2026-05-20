Case: podmr_013_2026-05-16-123121

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR frequency scan.
- Vary parameter: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The executed readout order is therefore:
  1. adj_polarize followed by detection: true m_S = 0 fluorescence reference.
  2. rabi_pulse_mod_wait_time followed by detection: signal after the MW pulse.
- mod_depth = 1 from the provided sequence XML.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, this is exactly 13 samples, so rounding leaves it at 52 ns.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: Omega_R = 10 MHz.
- Rectangular-pulse transition probability versus detuning delta:
  P(delta) = (Omega_R^2 / (Omega_R^2 + delta^2)) * sin^2(pi * sqrt(Omega_R^2 + delta^2) * tau),
  with frequencies in cycles/s and tau = 52 ns.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- Expected resonant fluorescence drop in the post-pulse readout is C * P(0) = 0.2191, about a 22 percent dip relative to the m_S = 0 level.

Data/model comparison:
- The combined readout 2 trace has a deep dip at 3.875 to 3.880 GHz: 34.67 and 34.08 counts, while nearby/off-resonant values are mostly around 42 to 45 counts.
- The readout2/readout1 ratio drops to 0.7809 at 3.875 GHz and 0.7914 at 3.880 GHz.
- Fitting the ratio to a linear baseline minus the rectangular-pulse model above gave:
  - best center frequency: 3.87775 GHz
  - fitted contrast amplitude: 0.2153
  - fitted resonant ratio minimum: about 0.7723
  - null linear-baseline SSE: 0.09097
  - Rabi-model SSE: 0.01474
  - improvement factor over null: 6.17
- Holding the contrast fixed at 0.22 gave nearly the same center and SSE: center 3.87775 GHz, SSE 0.01478.
- The two stored averages both show the central ratio suppression:
  - average 1: ratio 0.7931 at 3.875 GHz and 0.7969 at 3.880 GHz
  - average 2: ratio 0.7657 at 3.875 GHz and 0.7847 at 3.880 GHz
  These averages are not treated as an independent repeatability test, but they are consistent with the combined dip.

Decision:
The observed signal amplitude, line center, and line shape are quantitatively consistent with the expected pODMR response of the active 52 ns modulated Rabi pulse. A pODMR resonance is present.
