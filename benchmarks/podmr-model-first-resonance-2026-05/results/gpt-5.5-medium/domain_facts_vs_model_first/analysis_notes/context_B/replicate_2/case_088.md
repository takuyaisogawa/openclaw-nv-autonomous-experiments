<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_088

Sequence identification

The active scan is Rabimodulated.xml / Rabimodulated with mw_freq swept from
3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence has
length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, sample_rate =
250 MHz, and freqIQ = 50 MHz. Because full_expt is zero, the optional
m_S = +1 reference block is inactive. The two readouts in the data are
therefore:

- readout 1: the "true 0 level reference", acquired immediately after
  adj_polarize and before the swept microwave pulse.
- readout 2: the signal readout after the Rabi-modulated microwave pulse.

Expected physical signal

Use the two-level square-pulse Rabi response

P(+1 | detuning) = (f_R^2 / (f_R^2 + detuning^2))
                  * sin^2(pi * pulse_duration * sqrt(f_R^2 + detuning^2)).

The setup fact gives f_R = 10 MHz at mod_depth = 1. With pulse_duration =
52 ns,

P_on_resonance = sin^2(pi * 10e6 * 52e-9) = 0.996.

The optical contrast scale is about 22%, so a resonant point should have
signal/reference ratio

1 - 0.22 * 0.996 = 0.781,

or a drop of about 10.75 raw counts from the observed readout-1 mean of
49.08 counts. With the 5 MHz scan step, even if the resonance lies halfway
between sampled points, the nearest sampled detuning is only 2.5 MHz and
the same model still predicts a drop of roughly 20% of the reference. A
grid calculation for resonance frequencies inside the scan gives a largest
sampled predicted drop between 9.67 and 11.17 counts.

Observed data comparison

The combined readouts have:

- readout 1 mean 49.08, standard deviation 1.09
- readout 2 mean 48.78, standard deviation 1.47
- readout2 - readout1 mean -0.29, standard deviation 1.72
- minimum readout2/readout1 ratio 0.923
- largest observed pointwise drop readout1 - readout2 = 3.92 counts

The observed largest fractional drop, 7.7%, is far below the approximately
21.9% drop expected for a resonant 52 ns pulse at mod_depth = 1. A fixed
contrast Rabi model constrained to place the resonance inside the scanned
frequency range gives a much worse residual sum of squares than the
no-resonance comparison (225.3 versus 61.0 for readout2 approximately equal
to readout1). The best unconstrained fixed-contrast model moves the
resonance outside the scan range and only contributes a small off-resonant
tail, which is not evidence for an in-range pODMR line.

Decision

No pODMR resonance is present in this scan.
