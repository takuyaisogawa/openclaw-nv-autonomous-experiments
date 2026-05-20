Case podmr_011_2026-05-16-120107

I used only the provided XML and raw readout export for this decision.

Sequence and readout roles:
- Active sequence: Rabimodulated microwave-frequency scan, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional +1 reference block is skipped.
- Readout 1 is the detection immediately after optical polarization, so it is the bright m_S = 0 reference.
- Readout 2 is the detection after one Rabi-modulated microwave pulse.
- The active pulse before readout 2 is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- The do_adiabatic_inversion flag is set, but the adiabatic inversion code is inside the skipped full_expt reference block and is commented in the executed path; it is not the active resonance-producing pulse here.

Quantitative model:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the on-resonance transition probability for a 52 ns square pulse is
  P = sin^2(pi * f_R * t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a setup contrast scale of 22%, the expected on-resonance fluorescence drop is 0.22 * 0.996 = 0.219, or about 21.9%.
- Using the off-resonance bright readout-1 baseline excluding the central 3.870-3.890 GHz region gives 42.315 counts. The predicted on-resonance minimum is 42.315 * (1 - 0.219) = 33.04 counts.
- The measured readout-2 minimum is 33.096 counts at 3.880 GHz. This is a 21.8% drop relative to the bright baseline and a 20.1% drop relative to the simultaneous readout-1 value at that point.
- A detuned Rabi model P(df) = f_R^2/(f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)), centered at 3.880 GHz, predicts a narrow dip with strongest suppression at the center and reduced suppression at +/-5 and +/-10 MHz. The observed readout-2 trace has exactly that central dip pattern: 37.54, 34.75, 33.10, 37.21, 39.77 counts from 3.870 to 3.890 GHz.
- Readout 1 remains comparatively flat and does not show the same narrow dip, which is the expected behavior for the pre-microwave bright reference.
- The two stored averages both have their readout-2 minimum at 3.880 GHz, but I treat those averages mainly as tracking-cadence snapshots rather than a strong independent repeatability test.

Decision:
The measured dip depth and location are quantitatively consistent with the expected near-pi-pulse ODMR response for mod_depth = 1 and inconsistent with ordinary readout drift alone. A pODMR resonance is present.
