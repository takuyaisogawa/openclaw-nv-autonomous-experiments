Case: podmr_014_2026-05-12-081841

Sequence and readout roles

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed XML has full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped. The two readouts in ExperimentData therefore correspond to:

- readout 1: true mS = 0 optical reference immediately after adj_polarize and detection
- readout 2: signal after the modulated Rabi microwave pulse and detection

The active pulse parameters are length_rabi_pulse = 52 ns and mod_depth = 1. The sample rate rounds this to 52 ns exactly at 250 MS/s.

Explicit expected-signal model

Use the stated setup model: Rabi frequency f_R = 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For a square resonant pulse, the transferred population is

P_transfer = sin^2(pi * f_R * tau)

with tau = 52 ns and f_R = 10 MHz:

pi * f_R * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P_transfer = sin^2(1.6336) = 0.9961

The stated contrast scale between mS = 0 and mS = +1 is about 22%. Taking the observed mean readout-1 level as the local mS = 0 reference, mean(readout 1) = 46.624 counts. A resonant pulse should therefore reduce readout 2 by approximately

expected_drop = 46.624 * 0.22 * 0.9961 = 10.217 counts

so the expected resonant readout-2 value near resonance would be roughly 36.4 counts, or a readout-2/readout-1 ratio near 0.781.

Observed data check

Observed combined means:

- mean(readout 1) = 46.624
- mean(readout 2) = 46.315
- mean(readout 2 - readout 1) = -0.309 counts
- standard deviation of pointwise differences = 1.331 counts

The largest negative pointwise difference is -3.135 counts at 3.865 GHz, corresponding to a ratio of 0.937. Other negative excursions are similar in size or smaller and are not a 10-count depletion. The measured deviations are on the scale of readout scatter and tracking variation, not the expected nearly full-contrast Rabi response. Stored averages should not be treated as a strong repeatability test here because they often reflect tracking cadence.

Decision

Given the active sequence, the pulse should produce an easily visible roughly 22% dip in the post-pulse readout if a pODMR resonance is within the scanned range. The observed signal shows no such depletion, only small fluctuations of a few counts. I decide that a pODMR resonance is absent.
