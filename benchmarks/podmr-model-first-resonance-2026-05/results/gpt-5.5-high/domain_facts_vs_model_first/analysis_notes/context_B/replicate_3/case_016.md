Case: podmr_001_2026-05-16-000631

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional m_S = +1 reference block is skipped.
- Active detections are therefore:
  1. readout 1: polarized m_S = 0 reference after adj_polarize, before the microwave pulse.
  2. readout 2: signal readout after rabi_pulse_mod_wait_time.
- mod_depth from the provided sequence XML / exported variable values is 1.
- Active pulse duration is length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding does not change it.

Quantitative expected-signal model:
- Setup contrast between m_S = 0 and m_S = +1 is about C = 0.22.
- Rabi frequency at mod_depth = 1 is about f_R = 10 MHz.
- For a resonant square pulse, the transferred population is P1 = sin^2(pi * f_R * t).
- With t = 52 ns, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected resonant readout ratio is readout2/readout1 = 1 - C * P1 = 0.7809, i.e. about a 21.9% PL drop from the m_S = 0 level.

Observed quantitative comparison:
- Off-resonant baseline ratio readout2/readout1, excluding 3.865-3.885 GHz, is 0.9832.
- The minimum ratio occurs at 3.880 GHz: readout1 = 37.1346, readout2 = 28.9808, ratio = 0.7804.
- The observed fractional dip relative to the off-resonant ratio is (0.9832 - 0.7804) / 0.9832 = 0.206, close to the expected approximately 0.219 contrast-scale dip for a near-pi pulse.
- readout 1 remains near its baseline while readout 2 shows the localized dip, matching the assigned roles of reference and post-pulse signal.

Decision:
The observed readout2 suppression is quantitatively consistent with the expected near-pi-pulse pODMR response for mod_depth = 1 and 52 ns pulse duration. A pODMR resonance is present.
