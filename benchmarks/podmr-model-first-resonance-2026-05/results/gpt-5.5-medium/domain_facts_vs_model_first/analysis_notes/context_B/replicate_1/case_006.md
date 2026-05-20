Case: podmr_010_2026-05-11-155154

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The instruction block first runs adj_polarize and detection. This is explicitly commented as "Acquiring true 0 level reference", so readout 1 is the m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The active signal operation is then one rabi_pulse_mod_wait_time call followed by detection, so readout 2 is the post-microwave signal readout.
- The relevant active microwave pulse is length_rabi_pulse = 52 ns.
- The provided XML and exported Variable_values list mod_depth = 1. The embedded saved sequence text also contains an old/default float expression with 0.3, but the active exported variable value and provided sequence XML give mod_depth = 1.

Physical model calculation:
- Given setup Rabi frequency f_R ~= 10 MHz at mod_depth = 1, the resonant transition probability for a square pulse is
  P = sin^2(pi * f_R * tau).
- With tau = 52 ns and f_R = 10 MHz:
  pi * f_R * tau = pi * 0.52 = 1.6336 rad
  P = sin^2(1.6336) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fluorescence deficit in readout 2 relative to readout 1 is
  0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout 1 level is 39.83 raw units, so the expected on-resonance count drop is
  39.83 * 0.219 = 8.73 raw units.

Square-pulse detuning model:
- I used P(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau), with Omega = 2*pi*10 MHz and Delta = 2*pi*detuning.
- For a resonance centered on a sampled frequency, this model predicts a broad feature at this pulse length: near 21.9% deficit at line center and about 16.5% deficit at +/-5 MHz detuning.

Observed data:
- Mean readout 1 = 39.826.
- Mean readout 2 = 39.261.
- Mean readout 2 - readout 1 = -0.565 raw units, only about 1.4% of the reference.
- The largest single-point deficit is about 9.2%, still less than half of the expected 21.9% resonant deficit for mod_depth = 1.
- The largest single-point deficit occurs without the required neighboring-point support: the expected +/-5 MHz deficits would be large, but the adjacent observed deficits are not consistently negative or resonance-shaped.
- The two stored averages show different baselines and trends, consistent with tracking cadence effects rather than independent repeatability of a resonance.

Decision:
- For the active Rabimodulated.xml pulse sequence with readout 1 as the m_S = 0 reference, readout 2 as the post-pulse signal, mod_depth = 1, and tau = 52 ns, a real pODMR resonance should produce a large, structured readout-2 deficit relative to readout 1.
- The observed data do not show the expected magnitude or detuning-dependent line shape.
- Prediction: resonance_absent.
