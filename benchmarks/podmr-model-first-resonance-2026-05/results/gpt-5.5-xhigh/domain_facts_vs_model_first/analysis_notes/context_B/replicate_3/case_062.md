Case: podmr_048_2026-05-17-002650

Sequence interpretation from inputs/sequence.xml and the exported variable values:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- Readout 1 is the true m_s = 0 reference after adj_polarize and detection.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) and detection.
- mod_depth = 1.
- length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Quantitative expected-signal model:
Use the driven two-level Rabi response for a rectangular pulse,

    P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

with f_R = 10 MHz * mod_depth = 10 MHz and tau = 52 ns. The readout contrast expected for a resonance is

    C(delta) = 0.22 * P1(delta)

where C = (readout_1 - readout_2) / readout_1.

Model values:
- delta = 0 MHz: P1 = 0.996, expected contrast = 0.219, about 11.1 raw readout units for the measured 50.5 count reference.
- delta = 5 MHz: P1 = 0.749, expected contrast = 0.165, about 8.3 raw units.
- delta = 10 MHz: P1 = 0.273, expected contrast = 0.060, about 3.0 raw units.
- delta = 15 MHz: P1 = 0.0117, expected contrast = 0.0026.

Measured normalized contrast, C = (readout_1 - readout_2) / readout_1:
- Mean C = 0.0134.
- Standard deviation across scan points = 0.0265.
- Maximum C = 0.0735 at 3.850 GHz, a 3.87-count drop.
- Minimum C = -0.0352 at 3.920 GHz, where readout 2 is higher than readout 1.

Line-shape comparison:
- A constant-baseline null model gives SSE = 0.01479 in normalized contrast units.
- Fitting C = baseline + A * P1(f - f0) with A unconstrained gives best A = -0.0387 at f0 = 3.883 GHz, which is a nonphysical inverted response.
- Constraining 0 <= A <= 0.22 gives best A = 0.0331 at f0 = 3.90175 GHz, far below the expected A = 0.22.
- Forcing the physical setup amplitude A = 0.22 gives no meaningful improvement over the null model and places the best center outside the scan window.

Decision:
With mod_depth = 1 and a 52 ns pulse, a real in-window pODMR resonance should produce a near-pi-pulse fluorescence drop of about 22% at or very near one scan point, with adjacent 5 MHz points still strongly affected. The measured data only show small, irregular percent-level differences and no physically shaped resonance feature. Stored averages are not treated as a strong independent repeatability test. Prediction: resonance_absent.
