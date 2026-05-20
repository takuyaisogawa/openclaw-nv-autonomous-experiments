Sequence/readout identification:

The provided sequence is Rabimodulated.xml. Its active instructions first polarize the NV and immediately detect, giving readout 1 as the true m_S = 0 reference. The optional m_S = +1 reference block is guarded by full_expt, and full_expt = 0, so that block is inactive. The active signal branch is then a single rabi_pulse_mod_wait_time pulse followed by detection, giving readout 2 as the post-pulse signal. The active pulse parameters from the provided XML are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and the rounded pulse duration remains 52 ns.

Physical model calculation:

Using the stated setup scale, mod_depth = 1 gives a Rabi frequency of about 10 MHz. For a square pulse, the driven population transfer versus detuning is

P(detuning) = f_R^2 / (f_R^2 + detuning^2) * sin^2(pi * t * sqrt(f_R^2 + detuning^2)),

using cycle-frequency units. With f_R = 10 MHz and t = 52 ns, the on-resonance transfer is sin^2(pi * 10e6 * 52e-9) = 0.996. With the setup contrast scale of 22%, an on-resonance pODMR response should therefore make readout 2 lower than the m_S = 0 reference by about 0.22 * 0.996 = 0.219, or about 11 counts for a 50-count reference. The same model gives expected fractional drops of about 0.165 at 5 MHz detuning and 0.060 at 10 MHz detuning, so a resonance in this 5 MHz step scan should appear as a clear localized dip across at least one to a few points.

Data comparison:

The observed fractional signal y = 1 - readout2/readout1 across the scan is:

0.0225, 0.0565, -0.0216, 0.0102, 0.0313, 0.0177, 0.0262, -0.0198, 0.0545, 0.0056, 0.0165, 0.0131, 0.0142, 0.0243, 0.0007, 0.0038, -0.0150, 0.0104, 0.0272, 0.0271, 0.0437.

The mean is 0.0166 and the largest observed value is 0.0565, far below the 0.219 expected for an on-resonance pi-pulse response. For example, if the resonance were at 3830 MHz, the model predicts readout 2 near 38.77 counts at that point, but the observed readout 2 is 46.85 counts. If the resonance were at 3865 MHz, the model predicts readout 2 near 39.70 counts, but the observed value is 48.08 counts.

I also fit y with a linear baseline null model and with the explicit Rabi line shape. The linear baseline null has RMSE 0.0205. A fixed physical-amplitude resonance model with the 0.22 contrast and center constrained inside the scanned range has best RMSE 0.0410, about 4.0 times the null RSS, so the expected physical resonance shape is inconsistent with the data. A free-amplitude fit constrained to positive contrast finds a best peak drop of only about 0.038, roughly 17% of the expected 0.219 full response, and this small feature is within the raw fluctuation scale rather than a physically sized pODMR dip.

Decision:

No pODMR resonance is present in this scan.
