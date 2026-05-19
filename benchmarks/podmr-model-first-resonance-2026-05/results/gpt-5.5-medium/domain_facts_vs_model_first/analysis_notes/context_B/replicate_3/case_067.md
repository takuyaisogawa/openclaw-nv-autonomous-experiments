<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_067

Sequence/readout interpretation

The provided sequence is Rabimodulated.xml. The active instruction path is:

1. adj_polarize, then detection: this is the true m_S = 0 / bright reference readout.
2. The "Acquire 1 level reference" block is skipped because full_expt = 0, so no independent m_S = +1 reference is acquired.
3. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detection: this is the microwave-driven signal readout.

The provided sequence.xml and exported Variable_values give length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding at 250 MHz leaves 52 ns unchanged because 52 ns is exactly 13 samples. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation

Using the stated setup calibration, the on-resonance Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the driven transition probability is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * tau),

with Omega and delta in cycles/s and tau = 52 ns. At zero detuning:

Omega * tau = 10e6 * 52e-9 = 0.52 cycles,
P(0) = sin^2(pi * 0.52) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant signal readout should be reduced by

0.22 * 0.996 = 0.219, or about 21.9%,

relative to the bright reference. For typical bright readout values near 45 counts, that corresponds to a signal readout near 35 counts at resonance. Even if the resonance fell halfway between 5 MHz grid points, the model gives P(2.5 MHz) = 0.929 and an expected reduction of about 20.4%; at a full 5 MHz offset it still gives about 16.5% reduction. The modeled line is broad enough that a real resonance in this scan should create a clear local multi-point suppression in readout 2 relative to readout 1.

Observed data comparison

The combined readout means are readout 1 = 45.197 and readout 2 = 45.018, so the average difference is only -0.179 counts. The pointwise readout2/readout1 ratio has mean 0.9965. The lowest ratio is 0.9283 at 3.880 GHz, a 7.2% suppression, and another low point appears at 3.890 GHz with ratio 0.9302. These are much smaller than the 16-22% suppression expected from the active 52 ns, mod_depth = 1 pulse. They also do not form the expected Rabi/ODMR line shape: the intermediate 3.885 GHz point returns to ratio 1.005, and nearby points fluctuate above and below the reference.

Fitting the fixed-contrast Rabi model to the readout2/readout1 ratios does not identify a physical resonance in the scanned band. The best fixed 22% contrast model over candidate center frequencies gives only a marginal improvement over a constant-ratio model and places the best center outside the scan, while the best in-band dip fit requires only about 4.9% effective contrast, far below the expected approximately 22% for this pulse. Because stored averages here may reflect tracking cadence rather than an independent repeatability test, I do not treat the two averages as strong confirmation of the small dips.

Decision

Given the active sequence and expected signal size, the observed few-percent, non-lineshape fluctuations are not consistent with a pODMR resonance. I classify this case as resonance_absent.
