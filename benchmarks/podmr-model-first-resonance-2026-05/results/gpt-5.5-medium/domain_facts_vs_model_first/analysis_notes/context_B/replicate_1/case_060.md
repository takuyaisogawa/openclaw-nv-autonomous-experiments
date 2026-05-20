Case: podmr_046_2026-05-16-235726

Sequence identification and readout roles:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed instruction flow first performs polarization and detection, then waits, then applies one Rabi-modulated microwave pulse, then detects again.
- full_expt = 0, so the optional m_S = +1 reference block is not executed.
- Readout 1 is therefore the true m_S = 0 reference after optical polarization.
- Readout 2 is the signal readout after the microwave pulse.
- Active exported variables give length_rabi_pulse = 52 ns and mod_depth = 1. The embedded sequence text contains an older literal mod_depth = 0.3, but the exported Variable_values table is the active run state, and the standalone sequence XML also lists mod_depth = 1.

Physical model calculation:

Use a driven two-level response for a square microwave pulse:

P_transfer(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2))

where Omega is the on-resonance Rabi frequency in cycles/s, delta is detuning in cycles/s, and t is the pulse duration. The setup facts give Omega about 10 MHz at mod_depth = 1. With t = 52 ns:

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a resonance driven by this pulse should produce an on-resonance PL drop of approximately:

0.22 * 0.996 = 0.219, or about 21.9%.

At the measured readout scale, readout 1 has mean 52.16 counts, so the expected resonant readout-2 suppression would be about:

52.16 * 0.219 = 11.43 counts.

Even if the stale embedded literal mod_depth = 0.3 were used instead of the active value, Omega would be about 3 MHz and the on-resonance transfer for a 52 ns pulse would be sin^2(pi * 3e6 * 52e-9) = 0.222, giving an expected PL drop of about 4.9%, or 2.54 counts. This is much smaller than the active mod_depth = 1 expectation, but still should appear as a coherent dip in readout 2 relative to readout 1 at the resonance frequency.

Data check:

- Combined readout 1 mean = 52.16, standard deviation = 1.40 counts.
- Combined readout 2 mean = 51.12, standard deviation = 1.08 counts.
- Mean readout1-readout2 difference = 1.03 counts, far below the 11.43 count active-pulse expectation.
- Normalized contrast-like quantity 1 - readout2/readout1 has mean 0.019, standard deviation 0.030, and maximum 0.086.
- The largest normalized drop is at 3.860 GHz, but it is only 8.6%, isolated, and not accompanied by the expected driven two-level spectral shape.
- Several frequencies have negative contrast-like values where readout 2 exceeds readout 1, inconsistent with a stable ODMR dip.
- Stored averages show large baseline movement and likely tracking cadence effects, so they should not be treated as strong independent repeatability confirmation.

Decision:

The active physical model predicts a near-pi pulse on resonance and therefore a large, coherent readout-2 dip relative to readout 1. The observed readout-role-normalized data show only small, irregular fluctuations and no lineshape consistent with the expected pODMR response. I therefore decide that a pODMR resonance is absent.
