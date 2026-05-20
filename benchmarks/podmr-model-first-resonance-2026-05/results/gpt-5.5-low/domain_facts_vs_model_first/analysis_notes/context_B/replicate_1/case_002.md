Case: podmr_005_2026-05-10-173726

Inputs used:
- Sequence name in raw export: Rabimodulated.xml.
- Sweep variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active sequence logic: adj_polarize -> detection -> wait; full_expt = 0 skips the optional mS=+1 reference block; then rabi_pulse_mod_wait_time -> detection.
- Readout roles: readout 1 is the polarized mS=0 reference before the microwave pulse; readout 2 is the signal after the modulated Rabi pulse.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s and unchanged.
- mod_depth: the provided sequence XML and exported Variable_values give mod_depth = 1. The embedded Sequence text contains an older/default-looking float(0.3), but the explicit exported variable value and the provided XML both indicate the run value is 1.

Quantitative physical model:
- Given setup Rabi frequency is approximately 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for the active pulse.
- For a resonant square pulse of duration t = 52 ns, the driven population transfer is P = sin^2(pi f_R t / 2).
- P = sin^2(pi * 10e6 * 52e-9 / 2) = 0.532.
- The stated mS=0 to mS=+1 contrast scale is about 22%, so the expected resonant fluorescence loss is 0.22 * 0.532 = 0.117, or about 11.7%.
- The mean readout-1 level is 42.29 counts, so the expected resonant dip in readout 2 is about 42.29 * 0.117 = 4.95 counts.

Observed data:
- Readout 2 has an off-resonance mean of about 41.69 counts when excluding the 3.865-3.885 GHz trough region.
- Readout 2 reaches a minimum of 34.73 counts at 3.880 GHz, with neighboring trough values 38.04, 35.65, 34.73, and 36.81 counts from 3.870-3.885 GHz.
- The five-point trough mean from 3.865-3.885 GHz is 36.92 counts, about 4.76 counts below the off-resonance readout-2 mean.
- This observed dip amplitude is close to the 4.95-count expected dip from the Rabi/contrast model.
- Readout 1 stays around 41-43 counts through the same region and does not show the same trough, so the feature is tied to the microwave-pulse readout rather than a common-mode tracking drop.
- The two stored averages are not a strong repeatability test because stored averages often reflect tracking cadence, but both the combined trace and the readout-role comparison support a real microwave-dependent depression.

Decision:
The expected signal from the active 52 ns, mod_depth 1 pulse is a roughly 5-count fluorescence dip on resonance, and the measured readout-2 trace shows a matching localized dip near 3.88 GHz while the mS=0 reference readout does not. I classify this case as resonance_present.
