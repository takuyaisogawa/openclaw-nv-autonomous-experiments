Case: podmr_006_2026-05-11-020739

I used only the provided inputs in this workspace.

Sequence/readout interpretation:
- SequenceName is Rabimodulated.xml.
- Active variables from the provided sequence/raw export: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and detect a true m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. The active experiment then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection.
- Therefore readout 1 is the m_S = 0 reference readout, and readout 2 is the post-Rabi-pulse signal readout.

Quantitative physical model:
- The setup Rabi frequency is about 10 MHz at mod_depth = 1, and this case uses mod_depth = 1, so f_R = 10 MHz.
- For a square resonant Rabi pulse, transition probability is P = sin^2(pi * f_R * tau). With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, a resonant point should reduce the normalized signal by about 0.22 * 0.996 = 0.219, giving normalized PL near 0.781 of the off-resonant m_S = 0 level for ideal transfer.
- Including detuning, I used P(delta) = (f_R^2/(f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)) across the sweep. A fixed-contrast fit prefers a center near 3.8796 GHz. A free-amplitude fit also centers near 3.8796 GHz and gives an observed effective dip amplitude of about 12.5%, smaller than the ideal 22% but in the expected direction and frequency-localized.

Observed data:
- Combined readout 2 / readout 1 ratios have an off-resonance mean of 0.975 using points outside 3.870-3.890 GHz.
- The lowest combined normalized ratio is at 3.880 GHz: 0.846, a 13.3% drop from the off-resonance baseline. Neighboring points are also suppressed: 3.875 GHz is 0.911 and 3.885 GHz is 0.870.
- The two stored averages both show their minimum normalized ratio at 3.880 GHz, with drops of about 14.1% and 12.6% relative to their own off-resonance baselines. Since stored averages can reflect tracking cadence, I treat this only as support, not as an independent repeatability proof.
- The fixed 22% model predicts a deeper ideal minimum than observed, but the observed dip is centered where the Rabi model fits and has the expected sign, width scale, and amplitude order for a strong but nonideal pODMR response.

Decision: resonance_present.
