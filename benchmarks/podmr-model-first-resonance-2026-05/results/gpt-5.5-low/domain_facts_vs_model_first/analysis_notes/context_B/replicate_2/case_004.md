Case podmr_007_2026-05-11-064944

Sequence identification:
- Active sequence: Rabimodulated.xml / Rabimodulated sequence varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Runtime XML values from raw_export: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us.
- Readout roles: readout 1 is the true m_S = 0 reference acquired immediately after polarization. Because full_expt = 0, the optional m_S = 1 reference block is skipped. Readout 2 is the detection after the modulated Rabi pulse.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and approximately linear scaling, Omega_R = 10 MHz here.
- Pulse duration tau = 52 ns, so Omega_R * tau = 0.52 cycles.
- For resonant square-pulse transfer, P_1 = sin^2(pi * Omega_R * tau) = sin^2(pi * 0.52) = 0.996, essentially a pi pulse.
- With setup contrast about 22%, an on-resonance post-pulse readout should be lower than the m_S = 0 reference by 0.22 * 0.996 = 0.219 of the reference level.
- The mean readout 1 level is 31.72 counts, so the expected resonant drop is about 6.95 counts and the expected resonant readout 2 minimum is about 24.77 counts.
- Off resonance, the transfer probability follows P_1(df) = (Omega_R^2 / (Omega_R^2 + df^2)) * sin^2(pi * sqrt(Omega_R^2 + df^2) * tau), with frequencies in cycles/s. This gives a localized large dip when the sweep passes the transition.

Observed data check:
- Mean readout 1 = 31.72 counts; mean readout 2 = 31.55 counts.
- Mean readout 2/readout 1 ratio = 0.996, i.e. only about 0.4% low, not about 22% low.
- Mean readout 2 - readout 1 = -0.18 counts, far smaller than the approximately -6.95 count resonant expectation.
- The largest apparent low ratio is at 3.855 GHz, where readout 2/readout 1 = 0.887, but this isolated point is still only about an 11.3% drop and is not accompanied by the expected pulse-response line shape.
- A simple scan over resonance center using the explicit square-pulse detuning response and fitting readout 2 = intercept + slope * P_1(center) gives the best residual at the sweep edge with positive slope about +1.94 counts per transferred population. A real pODMR dip should have slope about -6.98 counts for the stated contrast.
- The constant model RSS for readout 2 is about 29.19; the best pulse-response fit RSS is about 24.05 but with the wrong sign and much smaller amplitude than the physical expectation.

Decision:
The sequence would have produced a large, localized post-pulse fluorescence dip if a pODMR resonance were present in this sweep. The measured readouts remain near the m_S = 0 reference with only noisy point-to-point fluctuations and no physically consistent negative pulse-response feature. Therefore the pODMR resonance is absent.
