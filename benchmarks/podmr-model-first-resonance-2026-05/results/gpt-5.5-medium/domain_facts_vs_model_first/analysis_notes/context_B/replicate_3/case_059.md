<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_059

Active sequence and readout roles

The sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first run adj_polarize and detection, then wait. This first detection is the optically polarized m_S = 0 reference readout. The optional "Acquire 1 level reference" block is inactive because full_expt = 0, so no independent m_S = +1 reference is acquired. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by a second detection. Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-microwave-pulse signal.

The provided sequence XML gives:

- length_rabi_pulse = 5.2e-08 s = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1.
- mw_freq is the scanned variable.

Expected-signal calculation

Using the stated setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square resonant pulse, the driven population transfer is

P_exc = sin^2(pi * f_Rabi * t)

with f_Rabi = 10e6 Hz and t = 52e-9 s:

P_exc = sin^2(pi * 10e6 * 52e-9) = 0.996.

The m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected fractional fluorescence deficit at resonance is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout 1 level is 48.852 raw units, so a resonant 52 ns pulse should produce a readout-2 dip of about

48.852 * 0.219 = 10.705 raw units

relative to the readout-1 reference, allowing for linewidth/broadening to distribute this over nearby scan points but still producing a large local depression if the resonance lies in the scanned window.

Observed data check

The combined means are:

- mean readout 1 = 48.852
- mean readout 2 = 48.767
- mean(readout 2 - readout 1) = -0.084
- standard deviation of pointwise differences = 1.039

The largest observed readout-2 deficit relative to readout 1 is at 3.845 GHz:

- readout 1 = 50.058
- readout 2 = 48.231
- deficit = 1.827 raw units
- fractional deficit = 3.65%

This is only about 17% of the expected 10.7-count resonant deficit for the active pulse settings. Several scan points have readout 2 above readout 1, including the high-frequency end, and there is no localized dip with the expected sign and amplitude. The stored two averages have similar scatter-scale excursions, but the prompt notes that stored averages often reflect tracking cadence rather than an independent repeatability test, so I do not treat them as decisive evidence for a weak feature.

Decision

Given the active 52 ns, mod_depth = 1 pulse, the physical model predicts an approximately pi-pulse-scale pODMR dip of about 22% if a resonance is present in the scanned range. The observed normalized deficit never exceeds 3.65% and lacks a resonance-shaped localized depression. I decide that a pODMR resonance is absent.
