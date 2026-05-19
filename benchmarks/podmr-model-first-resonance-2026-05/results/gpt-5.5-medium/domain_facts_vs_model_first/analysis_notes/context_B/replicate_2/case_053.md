<!-- Model-generated analysis note. Not a ground-truth label. -->

pODMR decision note for case_053

Sequence identification

The provided sequence XML is Rabimodulated.xml. The active experiment polarizes the NV, takes a first detection readout, waits, applies one microwave Rabi pulse, then takes a second detection readout. The optional "Acquire 1 level reference" block is inactive because full_expt = 0, so there is no separate stored m_S = +1 reference in this run.

Readout roles:
- readout 1: true m_S = 0 fluorescence reference after optical polarization.
- readout 2: fluorescence after the swept microwave Rabi pulse.

Relevant pulse settings from inputs/sequence.xml:
- mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- length_rabi_pulse = 52 ns.
- mod_depth = 1.

Physical signal model

Use a square-pulse two-level Rabi model for the transition probability during the microwave pulse:

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2))

where Omega is the on-resonance Rabi frequency in cycles/s, Delta is detuning in cycles/s, and t is the pulse duration. The setup facts give Omega = 10 MHz at mod_depth = 1, and t = 52 ns. On resonance:

Omega * t = 10e6 * 52e-9 = 0.52 cycles
P(0) = sin^2(pi * 0.52) = 0.996

With a 22 percent contrast between m_S = 0 and m_S = +1, the expected resonant fluorescence drop in readout 2 relative to readout 1 is:

0.22 * P(0) = 21.9 percent.

The scan step is 5 MHz, so if a resonance is inside the scan range, the nearest sampled point is at most 2.5 MHz detuned. At Delta = 2.5 MHz:

P(2.5 MHz) = 0.929
expected fluorescence drop = 0.22 * 0.929 = 20.4 percent.

For a typical reference level near 49.35 counts, that is about a 10 count drop in readout 2. Even at 5 MHz detuning, the model gives P = 0.749 and an expected drop of about 16.5 percent, or about 8.1 counts.

Data check

Combined readout statistics from raw_export.json:
- readout 1 mean = 49.35 counts.
- readout 2 mean = 49.19 counts.
- readout 2 / readout 1 mean = 0.997.
- minimum readout 2 / readout 1 ratio = 0.951 at 3.850 GHz.
- largest negative readout2 - readout1 difference = -2.54 counts.

The largest observed second-readout suppression is only about 4.9 percent, far smaller than the roughly 20 percent sampled dip expected for this pulse if a resonance were present in the scanned range. There is also no coherent single-frequency dip with the expected square-pulse line shape; the readout differences fluctuate with comparable positive and negative excursions. Stored averages are not treated as an independent repeatability test because they can reflect tracking cadence.

Decision

Given the active sequence, the readout roles, mod_depth = 1, and the 52 ns pulse, a real pODMR resonance should produce a large second-readout fluorescence dip. The measured readouts do not show that quantitatively expected signal. I therefore decide that a pODMR resonance is absent.
