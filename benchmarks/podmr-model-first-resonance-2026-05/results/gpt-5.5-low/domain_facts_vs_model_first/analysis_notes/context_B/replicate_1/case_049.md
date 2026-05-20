Case: podmr_035_2026-05-16-210045

Sequence identification

The provided sequence is Rabimodulated.xml / Rabimodulated. The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active instructions are:

- adj_polarize, then detection: this is the first readout and is the true m_S = 0 optical reference.
- full_expt = 0, so the optional m_S = 1 reference block is inactive.
- rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then detection: this is the second readout and is the pODMR signal readout after the swept microwave pulse.

Quantitative expected-signal model

Given the domain facts, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Thus for this sequence:

Omega_R / 2pi = 10 MHz
t_pulse = 52 ns
theta = 2 pi * 10e6 * 52e-9 = 3.267 rad
P(m_S = +1 | on resonance) = sin^2(theta / 2) = 0.996

The current setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected fractional fluorescence dip at resonance is:

0.22 * 0.996 = 0.219, or about 21.9%.

The mean first-readout reference is 50.94 raw counts, so a resonant point should be lower than the reference by about:

50.94 * 0.219 = 11.16 raw counts.

Observed data comparison

The two combined raw readouts are close together across the sweep. The second-minus-first differences range from -2.81 to +1.06 raw counts, with no narrow dip anywhere near the expected -11.16 counts. The lowest signal/reference ratio is 0.943 at 3.830 GHz, a 5.7% reduction, and the linear-detrended ratio residual scale is about 0.0215. The larger structure in both readouts is a shared upward drift over scan frequency, consistent with tracking or brightness drift rather than an ODMR resonance.

The stored averages are only two averages and should not be treated as a strong repeatability test; they mainly reflect tracking cadence. Even so, neither the combined readouts nor the per-average overlay show a contrast feature comparable to the quantitative expectation for a 52 ns, mod_depth 1 resonant pulse.

Decision

A pODMR resonance is absent. If a resonance were in this scanned window, this sequence should produce an approximately 22% raw fluorescence drop in the second readout relative to the first, but the observed deviations are only a few percent and drift-like.
