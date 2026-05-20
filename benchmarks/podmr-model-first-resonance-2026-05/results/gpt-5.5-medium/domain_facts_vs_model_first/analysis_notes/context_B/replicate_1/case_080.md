Active sequence and readout roles

The active sequence is Rabimodulated.xml. With full_expt = 0, the conditional "Acquire 1 level reference" block is skipped. The executed readouts are therefore:

1. readout 1: detection immediately after adj_polarize, a true mS = 0 fluorescence reference.
2. readout 2: detection after one rabi_pulse_mod_wait_time pulse, the pODMR signal readout.

The provided sequence XML and exported Variable_values give length_rabi_pulse = 52 ns and mod_depth = 1. The saved raw export also contains an embedded sequence text with mod_depth = 0.3, but the standalone provided sequence XML and Variable_values agree on mod_depth = 1, so I use mod_depth = 1 as the active setting for the decision.

Expected signal model

For a resonant square Rabi pulse, use

P(ms=+1) = sin^2(pi * f_Rabi * t)

with f_Rabi = 10 MHz * mod_depth and t = 52 ns. For mod_depth = 1:

f_Rabi = 10 MHz
pi * f_Rabi * t = pi * 10e6 * 52e-9 = 1.6336 rad
P(ms=+1) = sin^2(1.6336) = 0.996

The setup contrast between mS = 0 and mS = +1 is about 22%, so the expected resonant fractional fluorescence drop is

0.22 * 0.996 = 0.219

At the observed reference level of about 45.9 counts, the expected resonant signal is a drop of about

45.9 * 0.219 = 10.1 counts

Data check

The combined readout means are:

readout 1 mean = 45.90 counts
readout 2 mean = 45.37 counts
mean readout2 - readout1 = -0.53 counts

The strongest pointwise normalized drop is at 3.890 GHz:

readout 1 = 47.60
readout 2 = 44.54
ratio = 0.936
drop = 3.06 counts = 6.4%

The broad low region from 3.880 to 3.910 GHz has mean normalized ratio 0.961, while the off-region mean is 1.003, giving a fractional depression of about 4.2% and a count depression of about 1.84 counts.

Decision

With mod_depth = 1 and a 52 ns pulse, a real resonance should produce an almost full Rabi transfer and therefore about a 22% fluorescence drop, roughly 10 counts at this signal level. The observed depressions are much smaller, comparable to drift/noise in the raw readouts, and do not meet the expected physical signal size. I therefore decide that a pODMR resonance is absent.
