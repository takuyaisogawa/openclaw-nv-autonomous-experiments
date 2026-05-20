Case: podmr_077_2026-05-17-100811

Inputs used:
- inputs/sequence.xml and the saved sequence embedded in inputs/raw_export.json.
- inputs/raw_export.json numeric readouts only; no labels or sibling context.

Sequence identification:
- Active sequence: Rabimodulated.xml.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- The sequence first polarizes and detects the bright m_S = 0 reference, then waits.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- The active microwave operation before the second detection is:
  PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)
- Therefore readout 1 is the optically polarized m_S = 0 reference. Readout 2 is the post-microwave signal readout after the scanned-frequency Rabi-modulated pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already exactly 13 samples.

Explicit physical model:
- Given setup Rabi frequency f_R approximately 10 MHz at mod_depth = 1, the resonant population transfer from the microwave pulse is modeled as
  P_transfer = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns:
  pi * f_R * t = pi * 0.52
  P_transfer = sin^2(pi * 0.52) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence change is
  0.22 * 0.996 = 0.219, or about 21.9%.
- Around the measured baseline of about 51 raw-count units, this corresponds to an expected on-resonance change of about
  51 * 0.219 = 11.2 raw-count units.

Observed signal calculation:
- Combined readout 1 mean: 50.936.
- Combined readout 2 mean: 50.769.
- Pointwise readout2/readout1 ratio mean: 0.99695.
- Ratio standard deviation across scan: 0.02345.
- Ratio range: 0.9578 to 1.0530.
- Pointwise readout2 - readout1 mean: -0.167 raw counts.
- Pointwise readout2 - readout1 standard deviation across scan: 1.192 raw counts.
- Difference range: -2.192 to +2.635 raw counts.

Decision:
- A resonant 52 ns pulse at mod_depth = 1 should be close to a pi pulse and should produce an approximately 22% fluorescence feature, about 11 raw counts on this baseline.
- The observed scan contains only small fluctuations of order 1 to 3 raw counts, with no localized dip or peak near the expected magnitude.
- Stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.
- The data are therefore inconsistent with a present pODMR resonance under the active pulse sequence.

Prediction: resonance_absent.
