Case podmr_051_2026-05-17-011109

I used the provided sequence XML and raw export directly. The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML has full_expt = 0, so the optional m_S = +1 reference block is skipped. The two active detections are therefore:

1. readout 1: immediately after optical polarization, a true m_S = 0 fluorescence reference.
2. readout 2: after a Rabi-modulated microwave pulse, the pODMR signal readout.

The active pulse is:

- length_rabi_pulse = 52 ns, already aligned to the 250 MHz sample rate.
- mod_depth = 1.
- mw_freq is the swept variable.

Quantitative expected-signal model:

The supplied setup facts say the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a square resonant pulse, the transferred population is

P = sin^2(pi * f_Rabi * t).

With f_Rabi = 10 MHz and t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce the post-pulse readout by approximately

0.22 * 0.996 = 0.219, or about 21.9%.

Using the measured readout 1 mean of 48.33 counts, the expected resonant post-pulse readout is about

48.33 * (1 - 0.219) = 37.74 counts,

for an expected drop of about 10.6 counts relative to the polarized reference.

Observed data:

- readout 1 mean = 48.33 counts, standard deviation across scan points = 1.11 counts.
- readout 2 mean = 47.86 counts, standard deviation across scan points = 1.13 counts.
- readout2/readout1 mean = 0.991.
- minimum readout2/readout1 = 0.908 at 3.895 GHz.
- minimum raw difference readout2 - readout1 = -4.62 counts.

The largest observed suppression is far smaller than the approximately 10.6-count, 21.9% dip expected for an on-resonance 52 ns pulse at mod_depth = 1. A simple Gaussian-dip fit to the ratio found only a narrow single-point dip of about 6.7% depth, improving the constant model only modestly and not approaching the physical contrast predicted by the active pulse model. The stored per-average traces are only two averages and likely reflect tracking cadence, so I did not treat the apparent average-to-average baseline shifts as independent confirmation.

Decision: resonance_absent. The expected resonant signal should be large and obvious under the active XML pulse settings, but the observed readout is consistent with scan noise and tracking-scale fluctuations rather than a pODMR resonance.
