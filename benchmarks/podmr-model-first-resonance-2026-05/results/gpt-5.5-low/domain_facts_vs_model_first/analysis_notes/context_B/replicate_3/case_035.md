Case: podmr_020_2026-05-16-165809

Inputs used only from this isolated workspace:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png for visual cross-check only

Sequence identification and readout roles:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR while varying mw_freq.
- The sequence first runs adj_polarize followed by detection. This is the active mS = 0 / bright reference readout.
- The optional mS = +1 reference block is gated by if abs(full_expt)>1e-12. In the provided sequence full_expt = 0, so this block is inactive.
- The active pODMR signal readout is after rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...) followed by detection.
- Therefore ExperimentData readout 1 is the bright reference and readout 2 is the signal after the microwave pulse.

Pulse parameters from the provided sequence XML:
- sample_rate = 250 MHz, so the 52 ns Rabi pulse is exactly 13 samples after rounding.
- length_rabi_pulse = 52 ns.
- mod_depth = 1.
- Current setup Rabi frequency model: f_R = 10 MHz * mod_depth = 10 MHz.

Explicit expected-signal model:
- Use a two-level resonant Rabi model for the pODMR pulse.
- Transition probability on resonance: P = sin^2(pi * f_R * tau).
- With f_R = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated mS = 0 to mS = +1 contrast scale of 22%, the expected fractional fluorescence drop is 0.22 * 0.996 = 0.219, about 21.9%.
- The measured readout-1 mean is 45.19 raw-count units, so the expected on-resonance drop in readout 2 relative to readout 1 is 45.19 * 0.219 = 9.90 raw-count units.

Observed data summary:
- Readout 1 mean = 45.19, readout 2 mean = 44.54.
- The measured readout2 - readout1 range is -3.21 to +1.77 counts, with mean -0.65 counts.
- The largest negative readout2 - readout1 point occurs at the low-frequency edge, 3.825 GHz, not as a localized resonance feature.
- The normalized readout2/readout1 range is 0.929 to 1.040, and after removing a linear trend its peak-to-peak residual is about 0.084.
- The trace shows broad drift and crossing behavior between the two readouts, not a resonant dip of the expected magnitude.

Decision:
- A true resonance under the provided sequence parameters should create an approximately 10-count signal drop in the signal readout relative to the bright reference.
- No such localized, physically scaled pODMR response is present in the scan.
- Prediction: resonance_absent.
