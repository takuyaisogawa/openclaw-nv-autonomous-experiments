Case: podmr_030_2026-05-13-160024

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML sets full_expt = 0, so the optional "1 level reference" block is inactive.
- Readout 1 is the true m_S = 0 reference acquired immediately after optical polarization.
- Readout 2 is the measurement readout after the active rabi_pulse_mod_wait_time pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns after sample-rate rounding at 250 MS/s.

Physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, the expected on-resonance Rabi frequency here is 10 MHz.
- For a resonant square pulse, the transferred population is P = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected on-resonance readout-2 drop relative to the m_S = 0 reference is 0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout-1 level is 27.37 counts, so the expected resonant absolute drop is about 27.37 * 0.219 = 6.00 counts, giving an expected resonant readout near 21.37 counts.

Observed quantitative comparison:
- Mean readout 1 = 27.37 counts.
- Mean readout 2 = 27.73 counts.
- Mean readout2 - readout1 = +0.36 counts, not a negative contrast.
- The most negative readout2 - readout1 points are -2.26 counts at 3.860 GHz and -2.21 counts at 3.885 GHz.
- These are only about 8% relative dips, far below the approximately 22% model expectation for this pulse.
- The largest positive excursions are comparable or larger, e.g. +3.27 counts at 3.895 GHz.
- The two stored averages show broad drift/tracking behavior and should not be treated as strong independent repeatability evidence.

Decision:
The active pulse should create a large near-pi-pulse pODMR dip if a resonance lies in the swept band. The observed signal does not show a reproducible or correctly scaled readout-2 suppression relative to the m_S = 0 reference. Therefore I decide that a pODMR resonance is absent.
