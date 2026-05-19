<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_058

Sequence inspection

The provided sequence XML is Rabimodulated.xml. The active path is:

1. adj_polarize for 1 us
2. detection: this is the true m_S = 0 reference readout
3. wait_for_awg for 2 us
4. The "Acquire 1 level reference" block is skipped because full_expt = 0
5. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth
6. detection: this is the post-Rabi-pulse signal readout
7. wait_for_awg for 1 us

Thus readout 1 is the pre-pulse m_S = 0 reference, and readout 2 is the measurement after the microwave Rabi pulse. There is no independent m_S = +1 reference in this active sequence.

Relevant pulse parameters from the provided sequence XML:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so the 52 ns pulse is exactly 13 samples after rounding
- mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps

Quantitative expected signal model

Using the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant square pulse, the transferred population is modeled as:

P(+1) = sin^2(pi * f_Rabi * t)

With f_Rabi = 10 MHz and t = 52 ns:

P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional signal reduction in the post-pulse readout is:

0.22 * 0.996 = 0.219, or about 21.9%

The measured mean m_S = 0 reference readout is 48.56 counts. Therefore an on-resonance post-pulse readout should be approximately:

48.56 * (1 - 0.219) = 37.92 counts

Equivalently, the expected resonance dip is about 10.64 counts below the reference readout.

Observed data check

The combined raw readouts give:

- mean readout 1 = 48.56
- mean readout 2 = 48.69
- mean(readout 2 - readout 1) = +0.13 counts
- standard deviation of readout 2 - readout 1 across scan points = 1.09 counts
- most negative readout 2 - readout 1 value = -2.42 counts
- readout 2 / readout 1 ranges from 0.952 to 1.044

The largest observed suppression of the post-pulse readout is only about 2.4 counts, far smaller than the approximately 10.6-count dip expected from a resonant near-pi pulse at mod_depth = 1. The scan also does not show a localized deep dip in readout 2 relative to the reference readout. Stored per-average traces mainly show an offset between averages consistent with tracking cadence, not a reproducible resonance-depth feature.

Decision

Given the active readout roles and the quantitative expected near-pi-pulse contrast, the observed data are inconsistent with a pODMR resonance being present in this scan.
