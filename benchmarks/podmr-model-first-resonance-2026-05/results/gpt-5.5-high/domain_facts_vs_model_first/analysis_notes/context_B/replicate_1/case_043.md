Case podmr_029_2026-05-16-193002

I used the provided sequence XML and raw export values to identify the active
experiment before deciding. The active sequence is Rabimodulated.xml with
mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first
polarizes the NV and detects the true m_S = 0 fluorescence reference. Because
full_expt = 0, the optional m_S = 1 reference branch is skipped. The second
stored readout is therefore the detection after the modulated Rabi microwave
pulse, i.e. the pODMR signal readout. The active pulse parameters are
mod_depth = 1 and length_rabi_pulse = 52 ns.

Quantitative expected-signal model:

The supplied calibration says the Rabi frequency is about 10 MHz at
mod_depth = 1 and scales linearly with mod_depth. For this sequence,
f_R = 10 MHz and tau = 52 ns. For a resonant two-level pulse starting in
m_S = 0, the transferred population is

P_1 = sin^2(pi * f_R * tau)
    = sin^2(pi * 10e6 * 52e-9)
    = 0.996.

With the stated 22% contrast scale between m_S = 0 and m_S = +1, a true
resonance should reduce the post-microwave readout by about
0.22 * 0.996 = 0.219, or 21.9% of the m_S = 0 reference. The measured
reference baseline is about 44.93 raw counts, so the expected on-resonance
drop is about 9.85 raw counts.

Observed data check:

The combined readout differences, readout2 - readout1, have mean -0.021
counts, standard deviation 1.27 counts, minimum -2.56 counts, and maximum
+3.23 counts. In fractional terms the largest negative point is about -5.6%,
far smaller than the expected -21.9% on-resonance signal. The trace also does
not show a clear line-shaped dip in the post-microwave readout relative to the
reference; most apparent structure is common-mode baseline variation between
readouts or average-to-average tracking variation.

Decision:

A pODMR resonance is absent in this scan. The expected resonant signal for the
active 52 ns, mod_depth 1 pulse is roughly a 10-count fluorescence drop, while
the observed signal-channel-minus-reference variations remain near zero and
never approach that scale.
