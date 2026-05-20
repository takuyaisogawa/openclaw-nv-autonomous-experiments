Case podmr_014_2026-05-12-081841

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first polarize and detect, then skip the "1 level reference" block because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and detect again.
- Therefore readout 1 is the true mS = 0 polarized reference, and readout 2 is the signal after the Rabi-modulated microwave pulse.
- The provided sequence parameters are length_rabi_pulse = 52 ns and mod_depth = 1. The pulse duration is already aligned to the 250 MHz sample clock: round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Quantitative expected signal model
- Given the stated calibration, the resonant Rabi frequency is f_R = 10 MHz * mod_depth = 10 MHz.
- For a rectangular resonant pulse, the driven population transfer is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The setup contrast between mS = 0 and mS = +1 is about 22%, so the expected resonant readout drop is 0.22 * 0.996 = 0.219, or about 21.9% of the mS = 0 reference.
- The measured readout 1 mean is 46.62 counts, so the expected on-resonance decrease in readout 2 relative to readout 1 is about 46.62 * 0.219 = 10.2 counts.
- Including detuning with P(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)), the expected drop is still localized and large near resonance: about 10.2 counts at delta = 0, about 1.28 counts at +/-25 MHz, and about 0.31 counts at +/-50 MHz.

Data comparison
- The combined readout 2 minus readout 1 differences range from -3.14 to +2.48 counts, and the mean difference is only -0.31 counts.
- The normalized depletion 1 - readout2/readout1 has mean 0.0062, maximum 0.0630, and is far below the expected 0.219 resonant depletion for the active mod_depth = 1 pulse.
- The deepest isolated combined point is at 3.865 GHz with a 3.14 count drop, about 6.3% normalized depletion, still only about 31% of the expected resonant effect. Neighboring points do not form the expected strong line shape, and the stored two averages show substantial tracking-scale variation rather than a stable, repeatable resonance feature.

Decision
- A real pODMR resonance under this pulse should create a large post-pulse fluorescence dip relative to the immediately preceding mS = 0 reference. The observed data show only small, inconsistent fluctuations and no quantitatively compatible resonant dip. I therefore decide resonance_absent.
