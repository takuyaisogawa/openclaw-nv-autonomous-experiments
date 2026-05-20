Case: podmr_017_2026-05-16-132945

Inputs used:
- inputs/sequence.xml for the pulse program.
- inputs/raw_export.json for the numeric readouts.

Active pulse sequence and readout roles:
- Sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The do_adiabatic_inversion flag is therefore not active in the executed path.
- Readout 1 is the detection immediately after adj_polarize, before the swept Rabi pulse. This is the true mS = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time, so it is the pODMR signal readout after the swept microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-8 s. With sample_rate = 250 MHz, round(length_rabi_pulse * sample_rate) = 13 samples, so the executed duration is 13 / 250 MHz = 52 ns.

Quantitative expected-signal model:
- Given the stated setup, the Rabi frequency is approximately fR = 10 MHz * mod_depth = 10 MHz.
- For a rectangular pulse, the expected transfer probability versus detuning is
  P1(detuning) = fR^2 / (fR^2 + detuning^2) * sin^2(pi * pulse_duration * sqrt(fR^2 + detuning^2)),
  where fR and detuning are in cycles per second.
- On resonance, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22 percent mS = 0 to mS = +1 contrast scale, the expected on-resonance readout2/readout1 ratio is 1 - 0.22 * 0.996 = 0.781, corresponding to an expected dip of about 9.9 counts for a 45-count reference.

Data comparison:
- Normalizing the post-pulse readout by the mS = 0 reference gives a minimum ratio of 34.173 / 45.404 = 0.75265 at 3.875 GHz, a drop of 11.23 counts or 24.7 percent relative to the reference.
- A fixed-contrast finite-pulse model y = B * (1 - 0.22 * P1(f - f0)) fits best at f0 = 3.87635 GHz with B = 0.99235, SSE = 0.01403, and RMSE = 0.02584.
- A flat normalized model has B = 0.95318, SSE = 0.09894, and RMSE = 0.06864, so the physical resonance model reduces SSE by about 7.1x.
- Allowing the contrast amplitude to float gives an effective contrast of 0.229, close to the expected 0.22.
- The two stored averages both show the central dip, but I do not treat those averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The observed dip depth and finite-pulse line shape are quantitatively consistent with the expected pODMR response for a near-pi pulse at mod_depth = 1. A pODMR resonance is present.
