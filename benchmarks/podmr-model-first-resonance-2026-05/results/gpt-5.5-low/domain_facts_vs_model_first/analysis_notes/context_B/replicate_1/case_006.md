pODMR decision note for podmr_010_2026-05-11-155154

Inputs used: inputs/sequence.xml and inputs/raw_export.json only. I did not use labels, sibling cases, previous outputs, or external context.

Sequence identification and readout roles

The active sequence is Rabimodulated.xml. The instruction block first performs optical polarization, then a detection call, then waits. Because full_expt = 0, the conditional "Acquire 1 level reference" block is skipped. The only microwave manipulation before the second acquired signal is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);
PSeq = detection(PSeq,sample_rate,delay_wrt_1mus,ch_on);

Therefore readout 1 is the m_S = 0 optical reference before the microwave pulse, and readout 2 is the post-microwave-pulse pODMR readout. A resonance should make readout 2 dimmer than readout 1 by the population transferred out of m_S = 0, scaled by optical contrast.

The provided sequence XML has length_rabi_pulse = 5.2e-08 s, mod_depth = 1, sample_rate = 250 MHz, and full_expt = 0. The raw export also embeds an older Sequence text that shows mod_depth = 0.3, but its Variable_values table and the provided sequence.xml list mod_depth = 1. Since the instruction is to use the provided sequence XML, I used mod_depth = 1 for the main expected-signal calculation. The 52 ns pulse is already on the 4 ns sample grid, so rounding does not change it.

Quantitative physical model

Given the stated setup calibration, Rabi frequency is approximately

f_R = 10 MHz * mod_depth.

For a resonant square Rabi pulse of duration t, the transferred population is

P_transfer = sin^2(pi * f_R * t).

With mod_depth = 1 and t = 52 ns:

f_R = 10 MHz
pi * f_R * t = pi * 10e6 * 52e-9 = 1.6336 rad
P_transfer = sin^2(1.6336) = 0.996

The optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected fractional readout-2 dip on resonance is

0.22 * 0.996 = 0.219, about 21.9%.

The measured readout-1 mean is 39.826 raw counts, giving an expected resonant dip of

39.826 * 0.219 = 8.73 raw counts.

As a sensitivity check only, if the stale embedded Sequence text value mod_depth = 0.3 were used instead, then f_R = 3 MHz, P_transfer = sin^2(pi * 3e6 * 52e-9) = 0.222, expected fractional dip = 4.87%, and expected raw-count dip = 1.94 counts.

Data comparison

Combined readout means:

mean(readout 1) = 39.826
mean(readout 2) = 39.261
mean(readout 2 - readout 1) = -0.565 counts
standard deviation of pointwise differences = 1.356 counts
deepest single point readout 2 - readout 1 = -3.865 counts at 3.875 GHz

Pointwise differences readout 2 - readout 1 across the scan are:

3.825 GHz: -1.558
3.830 GHz: -2.673
3.835 GHz: +0.635
3.840 GHz: -0.500
3.845 GHz: +1.327
3.850 GHz: -0.808
3.855 GHz: -1.615
3.860 GHz: +0.635
3.865 GHz: +0.577
3.870 GHz: -2.692
3.875 GHz: -3.865
3.880 GHz: +0.115
3.885 GHz: -1.365
3.890 GHz: -0.404
3.895 GHz: +0.404
3.900 GHz: +0.538
3.905 GHz: +0.635
3.910 GHz: -1.038
3.915 GHz: +0.250
3.920 GHz: +0.538
3.925 GHz: -1.000

For the provided XML's mod_depth = 1 model, the expected resonance signal is a roughly 8.7-count dip in readout 2 relative to readout 1. The observed deepest point is less than half that magnitude and is not accompanied by a robust resonance-shaped depression; the average offset is only -0.565 counts. Stored averages show strong tracking-like drift, so I did not treat the two averages as an independent repeatability test.

Decision

The expected pODMR resonance signal for the active sequence should be large compared with the observed readout-2/readout-1 differences. The data do not show the required post-pulse fluorescence drop, so I decide resonance_absent.
