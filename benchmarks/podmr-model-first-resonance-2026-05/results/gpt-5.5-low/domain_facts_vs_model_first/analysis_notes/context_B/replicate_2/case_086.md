Case podmr_072_2026-05-17-085551

Inputs used:
- inputs/sequence.xml and the embedded executed Sequence in inputs/raw_export.json.
- raw_export.json numeric readouts only; no labels or external cases used.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions polarize the NV, take a detection readout, wait, skip the optional 1-level reference because full_expt = 0, apply one rabi_pulse_mod_wait_time pulse of length_rabi_pulse, then take a second detection readout.
- Therefore readout 1 is the true m_S = 0 optical reference before the microwave pulse.
- readout 2 is the signal after the Rabi-modulated microwave pulse.
- No active adiabatic inversion is executed, even though do_adiabatic_inversion is true, because the whole 1-level reference block is gated by full_expt and full_expt = 0.

Sequence parameters:
- Sweep variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Pulse duration: length_rabi_pulse = 52 ns.
- The XML file on disk lists mod_depth = 1. The embedded saved Sequence string lists mod_depth = 0.3, while Variable_values lists mod_depth = 1. This is internally inconsistent, so I evaluated both. The executed-sequence text favors 0.3, but either value should be detectable if a resonance is present.

Physical model calculation:
- Setup contrast between m_S = 0 and m_S = +1 is about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For a rectangular resonant pulse, transferred population is P = sin^2(pi * f_R * t).
- At mod_depth = 0.3: f_R = 3 MHz, t = 52 ns, P = sin^2(pi * 3e6 * 52e-9) = 0.2216. Expected fractional PL contrast = 0.22 * 0.2216 = 0.0487, about 4.9%.
- At the observed mean readout level of 49.85 counts, this is an expected resonant readout1-readout2 change of about 2.43 counts.
- At mod_depth = 1: f_R = 10 MHz, P = sin^2(pi * 10e6 * 52e-9) = 0.9961. Expected fractional PL contrast = 0.219, about 21.9%, or about 10.9 counts at the observed mean readout.
- Off resonance I used the standard driven two-level response P(detuning) = (f_R^2/(f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * t) to compare the expected frequency-dependent signal shape to readout1-readout2.

Observed data:
- Mean readout 1 = 50.1685.
- Mean readout 2 = 49.5412.
- Mean difference readout1-readout2 = 0.6273 counts, about 1.26% of the mean signal.
- Standard deviation of pointwise differences = 1.2034 counts.
- Pointwise differences range from -1.1731 to +2.4423 counts and change sign repeatedly across the sweep.
- Per-average differences have similar means but large scatter: average 1 mean difference 0.6117 counts, std 1.9270; average 2 mean difference 0.6429 counts, std 2.3681. These stored averages likely also reflect tracking cadence, so I did not treat them as a strong repeatability test.

Model comparison:
- For mod_depth = 0.3, the expected on-resonance peak difference is about +2.43 counts. That size appears only as isolated noisy points, not as a consistent pODMR line shape. A least-squares fit of the two-level pulse response over resonance frequency gave the best unconstrained fit with negative amplitude, meaning the observed fluctuations are anti-correlated with the expected positive readout1-readout2 resonance response.
- For mod_depth = 1, the expected peak difference is about +10.9 counts, far larger than anything observed. The best unconstrained pulse-response fit again did not produce the physically expected positive-amplitude resonance.
- The data show a small global offset between readout 1 and readout 2, but not a localized resonance feature with the sign and amplitude expected from the active sequence.

Decision:
- pODMR resonance absent.
