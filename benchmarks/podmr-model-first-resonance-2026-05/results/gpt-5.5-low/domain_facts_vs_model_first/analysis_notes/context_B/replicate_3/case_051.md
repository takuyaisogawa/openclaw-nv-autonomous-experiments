Case: podmr_037_2026-05-16-213011

Sequence identification

The sequence XML is Rabimodulated.xml. The active instructions first acquire a true 0 level optical reference with adj_polarize followed by detection. The optional +1 reference block is disabled because full_expt = 0. The active experiment then applies one rabi_pulse_mod_wait_time pulse with length_rabi_pulse = 5.2e-08 s, mod_depth = 1, and switch_delay = 1e-07 s, followed by detection. Therefore readout 1 is the 0-state reference and readout 2 is the post-microwave signal readout.

Relevant scan/data

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, with 21 points, 2 stored averages, and 100000 repetitions. Stored averages are treated mainly as tracking cadence rather than as an independent repeatability test.

Physical model calculation

For a square resonant microwave pulse, the transition probability is

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * tau * sqrt(Omega^2 + Delta^2))

where Omega and Delta are in cycles/s. The setup facts give Omega approximately 10 MHz at mod_depth = 1. The active pulse duration is tau = 52 ns, so on resonance:

Omega * tau = 10e6 * 52e-9 = 0.52
P(0) = sin^2(pi * 0.52) = 0.996

With the setup contrast scale of about 22% between m_S = 0 and m_S = +1, a near-resonant pulse should reduce the signal readout by about

0.22 * 0.996 = 0.219

of the 0-state fluorescence. At the observed raw baseline near 48 counts, this corresponds to an expected signal-reference dip of about

48 * 0.219 = 10.5 raw-count units.

The same model gives a broad but recognizable response across the 5 MHz sampled scan. For example, at 5 MHz detuning:

sqrt(10^2 + 5^2) MHz = 11.18 MHz
P(5 MHz) = (100/125) * sin^2(pi * 52e-9 * 11.18e6) = about 0.75
expected dip = 0.22 * 0.75 * 48 = about 7.9 counts.

At 10 MHz detuning:

P(10 MHz) = (100/200) * sin^2(pi * 52e-9 * 14.14e6) = about 0.27
expected dip = 0.22 * 0.27 * 48 = about 2.9 counts.

Thus if a transition lies within this 100 MHz scan, the signal readout should show a clear negative contrast relative to the 0 reference, with the center point near -10.5 counts and adjacent points still substantially negative depending on detuning.

Observed quantitative comparison

Using combined ExperimentData, readout2 - readout1 ranges from -2.12 to +2.81 counts. The sign is mixed rather than consistently negative around any candidate resonance. There is no point with the approximately -10 count dip expected for an on-resonance 52 ns, mod_depth 1 pulse, and there is no local cluster matching the expected square-pulse lineshape. The largest negative difference is at the scan edge, 3.825 GHz, and is only about -4.4% of the reference, far below the approximately -22% expected contrast.

Decision

The active sequence and quantitative signal model predict a strong pODMR dip if the resonance is in the scanned range. The measured readout pair does not show that dip or a compatible lineshape. I therefore decide that a pODMR resonance is absent in this case.
