<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_040

Sequence inspection

The provided sequence XML is Rabimodulated.xml. In the active instruction path, the sequence first polarizes and detects a true m_S = 0 reference, waits, skips the m_S = +1 reference because full_expt = 0, then applies:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on);

and performs the second detection. Therefore readout 1 is the m_S = 0 reference and readout 2 is the readout after the Rabi-modulated microwave pulse.

The relevant values from inputs/sequence.xml are:

- active sequence: Rabimodulated.xml
- scanned parameter: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- length_rabi_pulse: 52 ns
- mod_depth: 1
- full_expt: 0, so the optional m_S = +1 reference block is inactive

Quantitative physical model

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1, and the supplied XML has mod_depth = 1. I modeled the driven two-level transition probability for a square pulse as:

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

with f_R = 10 MHz and tau = 52 ns. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

Using the setup contrast scale of 22%, an on-resonance point should therefore change the post-pulse readout relative to the m_S = 0 reference by about:

0.22 * 0.996 = 0.219, or 21.9% of the raw readout.

The mean raw readout scale is about 49.6 counts, so the expected on-resonance dip is approximately:

49.6 * 0.219 = 10.9 counts.

Data comparison

The combined measured readout means are:

- readout 1 mean: 49.611
- readout 2 mean: 49.583
- mean(readout2 - readout1): -0.027 counts
- standard deviation of readout2 - readout1 across scan points: 1.471 counts
- minimum readout2 - readout1: -3.096 counts
- maximum readout2 - readout1: 3.173 counts

I also fit the detuned Rabi model shape over possible resonance centers on the scan grid using readout2 - readout1 = baseline - A * P(delta). The best grid-centered fit gave A = 2.06 counts, far below the expected approximately 10.9-count resonant amplitude. The stored per-average traces differ from each other by slow offsets and do not provide a strong repeatability test, consistent with the note that stored averages can reflect tracking cadence.

Decision

A true pODMR resonance for this sequence should produce a large, broad, resonance-shaped suppression in readout 2 relative to the m_S = 0 reference. The observed data show only small point-to-point fluctuations and no feature close to the expected amplitude. I therefore decide that a pODMR resonance is absent.
