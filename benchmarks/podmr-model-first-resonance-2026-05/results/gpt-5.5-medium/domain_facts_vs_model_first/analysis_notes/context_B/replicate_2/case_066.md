Case podmr_052_2026-05-17-015447.

I used the provided sequence XML and the exported sequence values before deciding. The active sequence is Rabimodulated.xml. The instructions first polarize and detect a true m_S = 0 reference, then skip the optional m_S = 1 reference block because full_expt = 0, then apply one rectangular rabi_pulse_mod_wait_time pulse followed by the signal detection. Thus readout 1 is the unpulsed m_S = 0 reference and readout 2 is the microwave-pulsed pODMR signal readout.

Relevant active pulse parameters:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 in the provided XML and Variable_values.
- The optional adiabatic inversion settings are not active for the measured signal path.

Physical model calculation:

For a rectangular resonant pulse with Rabi frequency f_R, the transition probability is

P(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * t * sqrt(f_R^2 + df^2)).

Using the given setup calibration f_R = 10 MHz at mod_depth = 1 and t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonance centered in the scan should produce an approximately 0.22 * 0.996 = 0.219, or 21.9%, loss in the pulsed readout relative to the reference at line center.

Data check:

The combined raw readout 2 / readout 1 ratios over 3.825 to 3.925 GHz range from about 1.10 to 0.90. The largest apparent deficit is at the final point, 3.925 GHz:

readout1 = 28.9615, readout2 = 26.0769, ratio = 0.9004, apparent deficit = 9.96%.

Other apparent deficits are smaller and irregular, with many positive excursions. The adjacent-difference noise estimate for the normalized trace is about 0.044 in ratio units, so the endpoint deficit is only a modest edge feature rather than a resolved line shape.

I also fit the explicit rectangular-pulse response against the normalized ratio with a linear baseline. A fixed 22% contrast resonance centered inside the measured range worsened the fit, including centers at 3.875, 3.900, and 3.925 GHz. The best fixed-contrast model placed the resonance center outside the scanned interval, around 3.934 GHz, where the model contributes only an in-window wing with maximum expected contrast about 8.0%; that reduced the sum of squared residuals only slightly relative to a linear baseline. Allowing amplitude to float gave a similar outside-scan center near 3.934 GHz, which is not a resolved in-range resonance.

The per-average traces show large tracking-cadence drift, so I did not treat stored averages as an independent repeatability test.

Decision: resonance_absent. The active pulse should give a near-full 22% pODMR dip if the resonance is sampled, but the data show only a weak endpoint/possible outside-scan wing and no resolved resonance within the scanned range.
