Case: podmr_003_2026-05-16-003531

Inputs used:
- Sequence file: inputs/sequence.xml.
- Raw export: inputs/raw_export.json.
- Raw readout plot: inputs/raw_readouts.png.

Active sequence and readout roles:
- The active saved scan is SequenceName = Rabimodulated.xml with vary_prop = mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first performs adj_polarize, then detection. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional explicit m_S = 1 reference block is inactive.
- The second detection follows a microwave rabi_pulse_mod_wait_time pulse and is therefore the signal readout for the pODMR microwave sweep.
- The relevant readout roles are readout 1 = bright m_S = 0 reference and readout 2 = after microwave pulse.
- The provided sequence variables and exported active Variable_values give length_rabi_pulse = 52 ns, sample_rate = 250 MHz, and mod_depth = 1. The pulse duration is already exactly 13 samples, so rounding keeps it at 52 ns.

Physical model calculation:
- Given the stated setup, Rabi frequency at mod_depth = 1 is approximately 10 MHz, scaling linearly with mod_depth.
- Therefore Omega_R = 10 MHz for this run.
- For a square microwave pulse with detuning Delta in Hz, the excited-state transfer probability is:
  P(Delta) = (Omega_R^2 / (Omega_R^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega_R^2 + Delta^2)).
- On resonance with t = 52 ns and Omega_R = 10 MHz:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fluorescence drop in the microwave readout is:
  0.22 * 0.996 = 0.219, or about 21.9%.

Data comparison:
- Combined readout 2 off-resonant median excluding the dip region is about 37.0 raw units.
- Minimum readout 2 is 28.06 raw units at 3.880 GHz.
- Observed fractional dip is (37.0 - 28.06) / 37.0 = 0.242, or about 24.2%.
- The off-resonant scatter estimate for readout 2 is about 1.59 raw units, so the dip depth is about 5.6 sigma relative to that scatter.
- The explicit Rabi-detuned model centered at 3.880 GHz and scaled only by the 22% contrast predicts raw readout 2 values near the dip of approximately:
  3.870 GHz: 34.78, 3.875 GHz: 30.90, 3.880 GHz: 28.89, 3.885 GHz: 30.90, 3.890 GHz: 34.78.
- The observed values over the same points are:
  3.870 GHz: 33.38, 3.875 GHz: 29.35, 3.880 GHz: 28.06, 3.885 GHz: 32.94, 3.890 GHz: 36.77.
- This is quantitatively consistent with a real pODMR resonance under the active pulse sequence. Stored averages are only two and can reflect tracking cadence, but the combined signal magnitude and frequency-localized shape match the expected physical response.

Decision:
- A pODMR resonance is present.
