Case: podmr_065_2026-05-17-071421

Sequence interpretation

The provided XML is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions are:

1. adj_polarize for 1 us.
2. detection: this is readout 1, the bright mS=0 reference.
3. wait_for_awg for 2 us.
4. The full_expt branch is skipped because full_expt = 0, so no active
   mS=1 reference is acquired.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and
   mod_depth = 1.
6. detection: this is readout 2, the post-microwave signal readout.

The do_adiabatic_inversion flag is not active in this run because it is
inside the skipped full_expt branch. The active pulse relevant to pODMR is
therefore a 52 ns square/modulated Rabi pulse at mod_depth = 1.

Physical model calculation

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is
approximately f_R = 10 MHz. For a square resonant pulse, the transition
probability as a function of detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) *
           sin^2(pi * t * sqrt(f_R^2 + delta^2)).

With t = 52 ns and f_R = 10 MHz:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The current setup contrast between mS=0 and mS=+1 is about 22%, so an
on-resonance signal readout should drop by

0.22 * P(0) = 0.219, or about 21.9% of the bright readout.

The observed mean bright reference is 47.48 counts, so the expected
on-resonance dip is about

47.48 * 0.219 = 10.40 counts.

Equivalently, the signal/reference ratio at resonance should be about

1 - 0.219 = 0.781.

At the 5 MHz scan spacing, the same model still predicts a large nearby
response: P(5 MHz) = 0.749, corresponding to a 16.5% dip. At 10 MHz
detuning the predicted dip is still about 6.0%.

Data check

The measured combined readouts have:

- readout 1 mean = 47.48 counts, standard deviation = 1.26 counts.
- readout 2 mean = 47.21 counts, standard deviation = 1.50 counts.
- signal/reference ratio mean = 0.9945.
- signal/reference ratio minimum = 0.9523.
- signal-reference difference ranges from -2.27 to +2.00 counts.

The deepest observed signal/reference reduction is only 4.8%, about
2.27 counts. That is far smaller than the expected 21.9%, 10.4-count
resonant response for the active mod_depth = 1, 52 ns pulse. A linear
tracking-drift model for the signal/reference ratio gives residual
scatter of about 0.025, while forcing the expected 22% square-pulse
resonance shape increases the residual scatter rather than explaining
the data. A free-amplitude resonance-shaped fit does not recover a
positive dip amplitude near the expected contrast scale.

Decision

Given the active sequence and quantitative expected signal, the data do
not show the required pODMR fluorescence drop. The small few-percent
excursions are consistent with drift/noise at the observed scale and are
well below the physically expected response for this pulse.

Prediction: resonance_absent.
