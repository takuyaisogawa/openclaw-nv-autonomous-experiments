Case: podmr_081_2026-05-17-110558

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels or external/sibling context.

Active pulse sequence:

- Sequence name in the export: Rabimodulated.xml.
- The provided XML has sample_rate = 250 MHz, mw_freq swept from 3.825 GHz to 3.925 GHz, length_rabi_pulse = 52 ns, mod_depth = 1, and full_expt = 0.
- Because full_expt = 0, the optional "Acquire 1 level reference" block is inactive. The two acquired readouts are therefore:
  - readout 1: true m_S = 0 reference after adj_polarize and detection, with no Rabi pulse.
  - readout 2: post-pulse signal after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and detection.
- do_adiabatic_inversion is set true but no active adiabatic inversion pulse is executed because that code is inside the inactive full_expt block or commented out.

Expected physical signal calculation:

- Setup contrast scale between m_S = 0 and m_S = +1: about 22%.
- Given Rabi frequency scale: f_Rabi = 10 MHz at mod_depth = 1, approximately linear in mod_depth.
- Active mod_depth = 1, so f_Rabi = 10 MHz.
- Active pulse duration after sample-rate rounding: 52 ns. At 250 MHz, 52 ns is exactly 13 samples.
- Resonant Rabi population transfer model:
  P_1 = sin^2(pi * f_Rabi * t)
      = sin^2(pi * 10e6 * 52e-9)
      = sin^2(1.6336)
      = 0.996.
- Expected resonant readout depletion relative to the m_S = 0 reference:
  contrast * P_1 = 0.22 * 0.996 = 0.219, or about 21.9%.
- Therefore a real pODMR resonance within the swept frequency range should drive readout2/readout1 to about:
  1 - 0.219 = 0.781
  near resonance, aside from baseline drift/noise.

Observed readout comparison:

- Combined readout 1 spans about 45.31 to 49.17 raw units.
- Combined readout 2 spans about 44.87 to 50.00 raw units.
- The pointwise ratio readout2/readout1 has:
  - minimum = 0.9548
  - maximum = 1.0372
  - mean = 0.9952
  - standard deviation = 0.0275
- The largest observed depletion of readout2 relative to readout1 is only about 4.5%, far smaller than the expected 21.9% resonant depletion.
- The local minima in the ratio occur at several separated scan points rather than as one resonance-shaped feature. Both raw readouts also share a broad downward drift across the scan, consistent with tracking or count-rate drift rather than a microwave resonance.

Explicit model comparison:

- I evaluated the detuned Rabi response
  P(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * sqrt(f_Rabi^2 + delta^2) * t)
  and readout ratio model R = baseline * (1 - 0.22 * P(delta)).
- For any resonance center landing on a measured scan point, this model predicts a local ratio near 0.781 before the fitted baseline factor.
- A grid search over possible centers in the 3.825 to 3.925 GHz sweep cannot match the data without predicting a much deeper dip than observed. The best grid fit still requires a predicted minimum near 0.795 after baseline scaling, while the measured minimum is 0.955.

Decision:

The active pulse should produce a large, near-full-inversion pODMR contrast if resonance is present, but the measured readout ratio shows only small scatter and drift with no approximately 22% depletion. I decide that a pODMR resonance is absent in this scan.
