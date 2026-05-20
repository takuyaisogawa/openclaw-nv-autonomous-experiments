Case: podmr_014_2026-05-12-081841

Input files used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName in the export is Rabimodulated.xml, matching the provided sequence XML.
- The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first runs adj_polarize and detection before any microwave pulse. This first detection is the true m_S = 0 reference readout.
- full_expt = 0, so the separate m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by a second detection. This second detection is the pODMR signal readout after the microwave pulse.
- Active mod_depth = 1.
- Active pulse duration length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, rounding keeps it at 52 ns because 52 ns * 250 MHz = 13 samples.

Quantitative expected-signal model:
- Given setup Rabi frequency f_R ~= 10 MHz at mod_depth = 1.
- For a square pulse, the spin-transfer probability versus detuning is modeled as
  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).
- On resonance with t = 52 ns and f_R = 10 MHz:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% contrast scale and a reference baseline near 46.62 raw units, the expected on-resonance signal decrease is
  0.22 * 46.62 * 0.996 = 10.22 raw units.
- The model still predicts a large feature on nearby scan points: about 9.53 raw units at 2.5 MHz detuning and 7.68 raw units at 5 MHz detuning. It falls to about 2.80 raw units at 10 MHz detuning.

Observed data:
- Combined readout 1 mean = 46.62 raw units; readout 1 range = 44.71 to 49.79.
- Combined readout 2 mean = 46.32 raw units; readout 2 range = 43.85 to 48.29.
- The most negative normalized signal relative to the reference is at 3.865 GHz: readout 1 = 49.79, readout 2 = 46.65, a drop of 3.13 raw units or 6.3%.
- The lowest absolute post-pulse readout is at 3.910 GHz: combined readout 2 = 43.85, but the two stored averages at that point are 41.58 and 46.12, so this is not a strong independent repeatability indication. Stored averages may mostly reflect tracking cadence.
- No point shows the roughly 10 raw-unit drop expected for a near-pi resonant pulse. The observed excursions are comparable to baseline fluctuations and do not form a clear pODMR resonance in the post-pulse readout.

Decision:
The expected pODMR resonance for this sequence should be a large fluorescence dip in the second readout relative to the first. The measured trace lacks a quantitatively compatible dip, so I decide resonance_absent.
