Case podmr_082_2026-05-17-111957

Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The active instructions are:

1. Polarize the NV with adj_polarize.
2. Detect immediately after polarization. This is the true m_S = 0 reference readout.
3. The optional m_S = +1 reference block is skipped because full_expt = 0.
4. Apply one rabi_pulse_mod_wait_time pulse using length_rabi_pulse and mod_depth.
5. Detect again. This is the pODMR signal readout after the microwave pulse.

Thus readout 1 is the polarized reference and readout 2 is the signal after the microwave pulse. The relevant active pulse has length_rabi_pulse = 52 ns and mod_depth = 1 in the provided XML/variable values.

Physical model calculation

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so the active pulse has Omega_R = 10 MHz. For a square pulse, the transition probability versus microwave detuning is

P(f) = (Omega_R^2 / (Omega_R^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega_R^2 + Delta^2)).

On resonance, with t = 52 ns and Omega_R = 10 MHz,

P0 = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The expected resonant fluorescence drop in readout 2 relative to the m_S = 0 reference is therefore approximately

0.22 * 0.996 = 0.219 of the reference level.

The measured readout 1 mean is 50.38 counts, so the expected on-resonance drop is about

50.38 * 0.219 = 11.0 counts.

Data comparison

The combined data have:

- readout 1 mean = 50.38 counts, standard deviation across scan points = 0.99 counts
- readout 2 mean = 50.03 counts, standard deviation across scan points = 1.45 counts
- readout 2 minus readout 1 mean = -0.35 counts, standard deviation = 1.49 counts
- most negative readout 2 minus readout 1 point = -3.46 counts

The largest observed negative excursion is only about 31% of the expected 11-count resonant drop. It is also not a clean resonance-shaped feature in the signal readout: fitting the square-pulse response with the physical 11.1-count amplitude gives only a small reduction in residual RMS compared with a flat readout-difference baseline, and the best fixed-amplitude solution places the resonance outside the scan edge with only weak response in the measured window. Allowing the amplitude to float does not recover a physical dip; the best fit prefers the opposite sign because of positive excursions near 3.865-3.875 GHz.

The stored two averages should not be treated as a strong independent repeatability test because they can reflect tracking cadence, but they are consistent with point-to-point scatter at the count level rather than an 11-count resonant contrast feature.

Decision

Given the active pulse duration and mod_depth, a true pODMR resonance in the scanned range should be large and broad enough to stand out clearly in readout 2 relative to the polarized reference. The observed variations are much smaller than the expected physical signal and do not match a resonant dip. I therefore decide that a pODMR resonance is absent.
