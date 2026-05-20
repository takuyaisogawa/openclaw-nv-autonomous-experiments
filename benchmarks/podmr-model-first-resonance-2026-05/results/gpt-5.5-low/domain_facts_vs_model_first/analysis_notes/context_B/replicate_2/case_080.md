Case podmr_066_2026-05-17-072831

I used the supplied sequence information before deciding. The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. Because full_expt = 0, the optional "1 level reference" block is inactive. The active readouts are therefore:

- readout 1: detection immediately after optical polarization, the true m_S = 0 reference.
- readout 2: detection after a single rabi_pulse_mod_wait_time pulse.

The active Rabi pulse has length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse duration is still 52 ns. The provided sequence XML/variable values give mod_depth = 1.

Quantitative expected-signal model:

For the setup, the Rabi frequency is approximately 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant square pulse, the transferred population is

P_1 = sin^2(pi * f_R * t).

Using f_R = 10 MHz and t = 52 ns:

P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%. The measured mean readout 1 level is 45.90 raw counts, so a resonant pulse should make readout 2 lower than readout 1 by roughly

45.90 * 0.22 * 0.996 = 10.06 raw counts.

Measured comparison:

The combined readout difference readout2 - readout1 has mean -0.53 counts and standard deviation 1.62 counts across the frequency sweep. The largest negative difference is -3.06 counts at 3.890 GHz. That is far smaller than the approximately -10.06 count resonant signal expected for the active pulse, and the measured trace does not show a localized ODMR-scale contrast feature. The per-average traces appear offset by tracking/background cadence, so I do not treat the stored averages as independent repeatability evidence.

Decision: resonance_absent.
