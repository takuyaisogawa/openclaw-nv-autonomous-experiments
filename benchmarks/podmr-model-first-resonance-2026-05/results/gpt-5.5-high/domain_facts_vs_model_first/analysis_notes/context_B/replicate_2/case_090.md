Case podmr_076_2026-05-17-095337.

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, scanned by mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and immediately detect; this is the true m_S = 0 fluorescence reference and corresponds to readout 1.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active spectroscopy readout is after one rabi_pulse_mod_wait_time call followed by detection; this corresponds to readout 2.
- Active pulse duration is length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz.
- Active mod_depth is 1.

Expected signal model:
The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse of duration tau = 52 ns, the transition probability versus detuning is

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * tau),

where Omega = 10 MHz and delta is the frequency detuning in cycles/s. On resonance, P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996. Therefore the expected readout-2 fluorescence on resonance is reduced by about 0.22 * 0.996 = 0.219, i.e. readout2/readout1 near 0.781. With a 5 MHz scan step, a resonance inside the scanned band would be sampled within at most 2.5 MHz of its center; at 2.5 MHz detuning the model still gives P1 = 0.929 and an expected normalized readout near 0.796. At 5 MHz detuning the expected normalized readout is about 0.835.

Observed data:
Using readout2/readout1, the mean normalized ratio is 0.9961 with sample standard deviation 0.0277. The minimum observed ratio is 0.9481 at 3.905 GHz, only about a 5.2% drop. Other low points, such as 3.825 GHz and 3.845 GHz, are similar isolated fluctuations rather than a broad resonance-shaped dip. The raw readout difference has standard deviation about 1.42 counts, and the largest negative differences are about -2.7 counts, while the physical model predicts a roughly 11-count fluorescence reduction for readout levels near 51 counts.

Model comparison:
A flat normalized baseline has SSE = 0.0153. A fixed-amplitude pODMR resonance constrained to lie inside the scanned band, with the above 52 ns/mod_depth 1 model and only a global baseline scale fitted, has best SSE = 0.0798, substantially worse because it must predict a deep minimum near 0.80 that is not present. A free-amplitude dip fit does not recover the expected contrast scale; the best fitted feature is not a physical positive dip of the expected amplitude.

Decision:
The active pulse should produce a large pODMR contrast if an addressed resonance is present in the scan, but the measured readout ratios contain only small scatter-level fluctuations. I therefore classify this case as resonance_absent.
