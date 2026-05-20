Case podmr_034_2026-05-16-204545.

Sequence interpretation from inputs/sequence.xml and raw_export variable values:

- Active sequence: Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS = +1 reference branch is skipped.
- Readout 1 role: true mS = 0 bright reference after optical polarization, before the scanned microwave pulse.
- Readout 2 role: signal readout after the modulated Rabi microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s, so it remains 52 ns.

Quantitative model:

Use a resonant two-level Rabi model for the mS = 0 to mS = +1 transition:

P1(delta) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * sqrt(fR^2 + delta^2) * tau)

where fR = 10 MHz at mod_depth = 1, tau = 52 ns, and delta is detuning in Hz. The optical contrast scale between mS = 0 and mS = +1 is 0.22, so the expected fractional drop in the second readout relative to the first readout is 0.22 * P1(delta).

Computed expected response:

- At delta = 0 MHz: P1 = 0.996, expected fractional drop = 21.9%, about 10.96 counts for a 50.02-count reference.
- At delta = 2.5 MHz, the worst nearest-sample detuning for a 5 MHz scan step if a resonance lies inside the scan range: P1 = 0.929, expected fractional drop = 20.4%, about 10.22 counts.
- At delta = 5 MHz: P1 = 0.749, expected fractional drop = 16.5%, about 8.24 counts.

Observed combined readouts:

- Mean readout 1 = 50.016 counts.
- Mean readout 2 = 49.366 counts.
- Mean normalized contrast 1 - readout2/readout1 = 1.28%.
- Largest observed normalized contrast = 5.22%.
- Largest observed absolute drop readout1 - readout2 = 2.65 counts.
- Several scan points have readout 2 above readout 1, giving negative apparent contrast.

The expected pODMR signal from the active pulse sequence is therefore a roughly 10-count dip at or near resonance, not a 0-3 count fluctuation. The observed trace is far below the required 16-22% near-resonance contrast and does not show a coherent resonant dip in the post-pulse readout. The two stored averages are treated only as limited tracking-cadence samples, but they also do not provide a stable resonance-scale feature.

Decision: resonance absent.
