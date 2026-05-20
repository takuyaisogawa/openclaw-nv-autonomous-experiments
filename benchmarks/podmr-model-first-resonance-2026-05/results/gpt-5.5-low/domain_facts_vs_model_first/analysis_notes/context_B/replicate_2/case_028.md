Case podmr_013_2026-05-16-123121.

Sequence identification:
- The provided XML active sequence is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped.
- Active readout roles:
  - readout 1: polarized m_S = 0 reference acquired immediately after adj_polarize and before the microwave pulse.
  - readout 2: signal readout after one rabi_pulse_mod_wait_time pulse.
- Active pulse parameters from the provided XML:
  - length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
  - mod_depth = 1.
  - switch_delay = 100 ns.

Quantitative expected signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- With approximately linear scaling, f_R = 10 MHz for this pulse.
- For a resonant rectangular pulse, transferred population is P = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence loss is 0.22 * 0.996 = 0.219, about 21.9%.

Observed signal calculation from raw_export.json:
- readout 2 minimum is 34.08 at 3.880 GHz, with the adjacent low point 34.67 at 3.875 GHz.
- Excluding the four lowest readout-2 points to estimate the off-resonant baseline gives readout-2 baseline 42.96.
- The minimum readout-2 dip is (42.96 - 34.08) / 42.96 = 0.207, about 20.7%.
- The readout-2/readout-1 ratio reaches 0.7809 at 3.875 GHz and 0.7914 at 3.880 GHz, corresponding to about 20.9% to 21.9% raw contrast relative to readout 1 at those points.
- Readout 1 does not show a matching narrow dip at the same frequencies; the large feature is specific to the post-pulse readout.
- The stored averages both show the same broad central readout-2 depression, but I treat that only as a consistency check because stored averages may reflect tracking cadence.

Decision:
The observed dip amplitude and location-dependent behavior match the expected near-pi-pulse pODMR resonance signal. A resonance is present.
