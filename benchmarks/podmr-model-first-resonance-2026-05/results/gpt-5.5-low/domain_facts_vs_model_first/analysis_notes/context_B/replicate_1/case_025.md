Analysis note for podmr_010_2026-05-16-114624

Inputs used:
- Standalone sequence XML: inputs/sequence.xml
- Raw readout export: inputs/raw_export.json

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and acquire a detection window, then wait, then apply a modulated microwave Rabi pulse and acquire a second detection window.
- full_expt = 0, so the optional explicit m_S = +1 reference block is inactive.
- Readout 1 role: polarized m_S = 0 reference / bright reference acquired before the scanned Rabi pulse.
- Readout 2 role: signal readout after the scanned microwave Rabi pulse.
- From the standalone sequence XML, length_rabi_pulse = 52 ns and mod_depth = 1.

Important discrepancy:
- The embedded sequence text and variable table inside raw_export.json list mod_depth = 0.3 in one embedded sequence string, but Variable_values and the standalone inputs/sequence.xml list mod_depth = 1. The user explicitly requested use of the provided sequence XML, so the model calculation below uses mod_depth = 1.

Physical model calculation:
- Given setup facts, Rabi frequency at mod_depth = 1 is approximately 10 MHz and scales linearly with mod_depth.
- For a resonant square pulse, the transferred population can be modeled as P_1 = sin^2(pi * f_Rabi * tau), where f_Rabi is the population oscillation frequency.
- With f_Rabi = 10 MHz and tau = 52 ns:
  P_1 = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With an m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant pi-like pulse should reduce the post-pulse signal by about 0.996 * 22% = 21.9% relative to the bright reference.
- If instead mod_depth = 0.3 were used, the same calculation would give f_Rabi = 3 MHz, P_1 = sin^2(pi * 3e6 * 52e-9) = 0.221, and an expected dip of only about 4.9%. This is not the primary decision model because the provided XML says mod_depth = 1.

Observed quantitative readout comparison:
- Combined readout 1 is approximately 40 counts over the low-frequency off-resonance region.
- Combined readout 2 is also approximately 39-40 counts off resonance from 3.825 to 3.865 GHz, with readout-1 minus readout-2 differences mostly within a few percent.
- Around 3.870, 3.875, and 3.880 GHz, readout 2 drops to 33.21, 31.19, and 33.04 counts while readout 1 remains near 40.33, 40.90, and 39.19 counts.
- At 3.875 GHz, the observed contrast relative to readout 1 is (40.904 - 31.192) / 40.904 = 23.7%.
- This matches the expected approximately full-contrast dip for a resonant 52 ns pi-like pulse at mod_depth = 1.

Repeatability / average note:
- The two stored averages show baseline/tracking offsets, so I do not treat them as a strong independent repeatability test.
- However, the combined readout shape shows a localized dip in the signal readout at the physically expected amplitude and frequency region, while the pre-pulse reference does not show a comparable narrow dip.

Decision:
- A pODMR resonance is present.
