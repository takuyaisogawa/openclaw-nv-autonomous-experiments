Case podmr_074_2026-05-17-092418.

I used the provided sequence XML and raw export values only. The active sequence is Rabimodulated.xml. The instructions first polarize and detect, so readout 1 is the true m_S = 0 reference. The optional m_S = +1 reference block is guarded by full_expt > 0 and full_expt is 0, so that block is inactive. The active microwave operation is then a single rabi_pulse_mod_wait_time pulse followed by detection, so readout 2 is the post-Rabi-pulse pODMR signal. The relevant pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns, rounded consistently at the 250 MHz sample rate.

Quantitative model check:

Given the stated setup, f_R = 10 MHz at mod_depth = 1. For a rectangular resonant Rabi pulse, the transition probability is P = sin^2(pi f_R t). With t = 52 ns, f_R t = 0.52 and P = sin^2(1.6336) = 0.996. The pulse is therefore essentially a pi pulse on resonance. With a 22% m_S = 0 to m_S = +1 contrast scale, a resonance should make the signal readout about 0.781 times the m_S = 0 reference at line center. Around a 49 count reference level this is an expected drop of about 49 * 0.22 * 0.996 = 10.74 counts.

Using the detuned rectangular-pulse model P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi t sqrt(f_R^2 + delta^2)), the expected signal/reference ratios are about 0.781 at 0 MHz detuning, 0.835 at 5 MHz, 0.940 at 10 MHz, and nearly unity by 15 MHz except for small oscillatory side structure. Thus a real resonance should appear as a large, localized depression in readout 2 relative to readout 1 over one to several 5 MHz scan points.

Observed combined data:

readout 1 mean = 49.08 counts, readout 2 mean = 48.78 counts. The readout2 - readout1 differences have mean -0.29 counts, standard deviation 1.72 counts, minimum -3.92 counts, and maximum +2.31 counts. The signal/reference ratio has mean 0.994, standard deviation 0.0347, and minimum 0.923. The deepest observed ratio is far above the expected line-center ratio of 0.781, and even that deepest point is not followed by the expected fixed-contrast line shape; the next point jumps above the reference.

I also compared model fits on the observed signal/reference ratios. A constant-ratio model gives SSE = 0.0241. A fixed-contrast 22% resonance model scanned over possible center frequencies gives best SSE = 0.0734, worse than the constant model. Allowing the fitted contrast sign and amplitude to float gives a best effective contrast of about -5.7%, i.e. the best small feature is in the opposite direction from the expected pODMR dip.

Stored averages show offsets and drift consistent with tracking cadence effects, so I do not treat the two averages as independent confirmation. The active pulse should have produced a large dip if a resonance were in the scan window. The measured readout relationship is inconsistent with that expected signal.

Decision: resonance_absent.
