Case podmr_078_2026-05-17-102220

Sequence identification:
The provided XML is Rabimodulated.xml. The active instructions first polarize the NV and perform a detection before any microwave pulse, then skip the optional "1 level reference" block because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and perform a second detection. Therefore readout 1 is the bright m_S = 0 reference, and readout 2 is the post-microwave-pulse signal. The active pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz.

Quantitative expected-signal model:
Using the supplied setup calibration, the resonant Rabi frequency at mod_depth = 1 is approximately 10 MHz. For a square pulse of duration t = 52 ns, the resonant m_S = +1 population after starting in m_S = 0 is

P_1(0) = sin^2(pi * f_Rabi * t)
       = sin^2(pi * 10e6 * 52e-9)
       = 0.996.

With the stated current setup contrast of about 22% between m_S = 0 and m_S = +1, a true resonance should reduce the post-pulse fluorescence by approximately

0.22 * 0.996 = 0.219, or 21.9% of the bright reference.

The mean measured m_S = 0 reference readout is 51.83 counts, so the expected on-resonance post-pulse readout is about

51.83 * (1 - 0.219) = 40.47 counts,

an expected drop of about 11.36 counts relative to readout 1. The finite-detuning Rabi model,

P_1(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2)),

also predicts a broad, obvious dip around any resonance within the 5 MHz-spaced scan, with the central ratio near 0.781 and neighboring points still strongly suppressed depending on alignment.

Observed data:
The combined readouts show readout 2 minus readout 1 has mean -0.07 counts and standard deviation 1.17 counts. The most negative post-pulse/reference ratio is 0.969 at 3.905 GHz, a 3.1% depression, corresponding to only about 1.6 counts. No measured point approaches the expected resonant signal near 40.5 counts, and there is no cluster with the large 20%-scale contrast required by the active 52 ns, mod_depth 1 near-pi pulse model. Stored averages are only two and can reflect tracking cadence, so they are not treated as a strong independent repeatability test.

Decision:
The physically expected pODMR resonance for this active sequence would be much larger than the observed fluctuations. The data do not show the expected resonant response, so I decide resonance_absent.
