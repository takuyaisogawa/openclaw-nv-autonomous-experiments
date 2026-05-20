Sequence inspection:

The active sequence is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The executed instructions first
polarize and detect, giving readout 1 as the true m_S = 0 reference. The
`full_expt` variable is 0, so the intermediate m_S = +1 reference branch is
skipped. The sequence then applies
`rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, ...)`
and detects again, so readout 2 is the post-microwave pODMR signal. The relevant
parameters are mod_depth = 1 and length_rabi_pulse = 52 ns.

Quantitative model:

Given the setup fact that the Rabi frequency is about 10 MHz at mod_depth = 1,
the resonant spin-transfer probability for a square pulse is

    P = sin^2(pi * f_R * t)

With f_R = 10 MHz and t = 52 ns:

    P = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant
point should reduce the post-pulse readout by about

    0.22 * 0.996 = 0.219

of the m_S = 0 reference. The mean readout 1 value is 48.56 counts, making the
expected on-resonance drop about 10.64 counts and the expected resonant readout
2 level about 37.92 counts.

Observed data:

The observed mean readout 2 value is 48.69 counts. Across the 21 scan points,
readout2 - readout1 ranges from -2.42 to +2.06 counts, with mean +0.13 counts
and standard deviation 1.09 counts. The normalized observed contrast
(readout1 - readout2) / readout1 ranges from -4.37% to +4.78%, far below the
expected resonant contrast of about 21.9%. The largest apparent dip is only
about 2.4 counts, roughly one quarter of the expected resonant drop and not a
coherent pODMR feature.

Decision:

A pODMR resonance is absent. With a near-pi pulse at full modulation depth, a
true resonance should produce a large negative feature in readout 2 relative to
the m_S = 0 reference, and the measured readouts remain nearly equal over the
scan.
