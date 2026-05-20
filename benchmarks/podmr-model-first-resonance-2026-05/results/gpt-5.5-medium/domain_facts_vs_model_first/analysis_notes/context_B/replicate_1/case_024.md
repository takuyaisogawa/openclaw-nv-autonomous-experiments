Case podmr_009_2026-05-16-113112

Inputs inspected:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml / Rabimodulated.xml-style pulse ODMR, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets a 52 ns rabi_pulse_mod_wait_time after the initial polarization/readout block.
- full_expt = 0, so the optional m_S = +1 reference block is not active.
- Readout 1 is the detection immediately after optical polarization, i.e. the m_S = 0 / bright reference.
- Readout 2 is the detection after the microwave Rabi pulse, i.e. the signal channel for pODMR.
- mod_depth = 1 from the provided XML and raw export variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to exactly 13 samples = 52 ns.

Quantitative physical expectation:
- Given f_Rabi ~= 10 MHz at mod_depth = 1 and approximately linear scaling, the active pulse has f_Rabi ~= 10 MHz.
- For a square pulse, the resonant transfer probability is P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, f_Rabi * tau = 0.52 cycles, so P_res = sin^2(pi * 0.52) = 0.996.
- With the setup contrast scale of about 22%, the expected resonant PL drop is 0.996 * 22% = 21.9% of the bright level.
- The readout 1 mean is 29.46 counts, so the expected resonant drop is about 6.45 counts and the resonant readout level should be near 23.0 counts if the pulse is on resonance and efficiently addresses the transition.

Explicit model calculation:
- I fitted readout 2 to y = baseline - A * P(delta), where
  P(delta) = f_Rabi^2 / (f_Rabi^2 + delta^2) * sin^2(pi * tau * sqrt(f_Rabi^2 + delta^2)).
- Sweeping the resonance center across the scan gave the best combined-readout fit at 3.8785 GHz.
- Best-fit baseline = 28.88 counts.
- Best-fit drop amplitude = 5.33 counts, or 18.5% of that baseline.
- Constant-null SSE = 61.99; Rabi-response SSE = 15.05; R^2 versus a constant model = 0.757.
- The measured minimum is 24.15 counts at 3.880 GHz, with neighboring low points 24.29 counts at 3.875 GHz and 25.00 counts at 3.885 GHz.
- The expected full-contrast resonant level using readout 1 mean is about 23.0 counts, while the observed minimum is 24.15 counts, consistent with a slightly reduced but physically plausible pODMR contrast.

Averages:
- Stored averages show strong opposite scan-direction/tracking drift, so I do not treat them as a strong independent repeatability test.
- Allowing each average a linear drift term plus the same Rabi-response shape still gives negative resonance-like coefficients for the post-pulse readout near the fitted center in one average, while the other average is dominated by endpoint/tracking drift.
- This is consistent with the domain note that stored averages often reflect tracking cadence.

Decision:
- The active post-pulse readout shows a localized dip at the frequency expected from a pODMR resonance.
- The magnitude and width are quantitatively compatible with the 52 ns, mod_depth = 1 Rabi pulse and the known 22% contrast scale.
- I therefore decide that a pODMR resonance is present.
