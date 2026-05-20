Sequence and readout interpretation

The saved scan identifies the active sequence as Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant sequence values are length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, and delay_wrt_1mus = 0.2 us. Because full_expt is zero, the conditional "Acquire 1 level reference" block is skipped. The acquired readouts are therefore:

1. readout 1: true mS = 0 reference immediately after optical polarization.
2. readout 2: signal after a modulated Rabi pulse followed by detection.

Physical signal model

For the stated setup, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Thus this run has f_R = 10 MHz. For a resonant square pulse, the transferred population is modeled as

P(+1) = sin^2(pi * f_R * tau)

with tau = 52 ns. This gives

P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated mS = 0 to mS = +1 contrast scale is about 22%, so the expected resonant fractional fluorescence drop in readout 2 relative to readout 1 is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout 1 level is 47.48 counts, so the expected on-resonance drop is about

47.48 * 0.219 = 10.4 counts.

Data comparison

The measured combined readout means are readout 1 = 47.48 and readout 2 = 47.21, a mean difference of only -0.27 counts. The pointwise readout2/readout1 ratio has mean 0.994, minimum 0.952, and maximum 1.043. The largest observed depletion is therefore only about 4.8%, much smaller than the approximately 21.9% depletion predicted for a resonant 52 ns pulse at mod_depth = 1.

At any frequency point, a true resonant response would place readout 2 near readout1 * (1 - 0.219), roughly 37 counts for a 47 count reference. No scan point approaches that level; the minimum ratio occurs at 3.830 GHz, where readout 1 = 47.56 and readout 2 = 45.29. The per-average traces mainly show a large common vertical offset between stored averages, consistent with tracking cadence rather than an independent repeatability test.

Decision

The expected resonant contrast from the active pulse sequence is large compared with the observed fluctuations, and the measured post-pulse readout remains close to the reference across the sweep. I therefore decide that a pODMR resonance is absent in this scan.
