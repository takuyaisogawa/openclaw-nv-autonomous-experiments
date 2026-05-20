Case: podmr_013_2026-05-16-123121

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML has full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Active readout 1 is the true m_S = 0 reference after adj_polarize and detection.
- Active readout 2 is detection after rabi_pulse_mod_wait_time with length_rabi_pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, rounding keeps this at 13 samples = 52 ns.

Quantitative physical model:
- Given setup Rabi frequency approximately 10 MHz at mod_depth = 1.
- For a resonant pulse, transfer probability is modeled as P = sin^2(pi * f_Rabi * t), where f_Rabi is the population oscillation frequency.
- With f_Rabi = 10 MHz and t = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Current setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence drop in the post-pulse readout is:
  0.22 * 0.996 = 0.219, or about 21.9%.

Observed data calculation:
- Using readout 2 off-resonant points excluding the central dip indices 9-12 gives baseline 42.959.
- Minimum readout 2 is 34.077 at 3.880 GHz.
- Observed drop relative to the readout 2 off-resonant baseline is (42.959 - 34.077) / 42.959 = 20.7%.
- The expected resonant value from the model is 42.959 * (1 - 0.219) = 33.545, very close to the observed 34.077.
- The dip is localized across 3.870-3.885 GHz and is much larger than the off-resonant readout 2 scatter (population standard deviation about 1.16 counts).
- Stored averages both show a corresponding reduced post-Rabi readout near the same frequency region, but this is treated only as supportive because averages may reflect tracking cadence.

Decision:
The observed dip amplitude and frequency-localized shape match the expected near-pi-pulse pODMR response quantitatively. A pODMR resonance is present.
