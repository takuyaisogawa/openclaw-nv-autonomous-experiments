<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_072

Sequence/readout identification

The provided sequence XML is Rabimodulated.xml. The active settings are:
- sample_rate = 250 MHz
- varied parameter = mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- length_rabi_pulse = 52 ns, which is already an integer 13 samples at 250 MHz
- mod_depth = 1
- full_expt = 0

Because full_expt is zero, the "Acquire 1 level reference" block is skipped. The active measurement is:
1. adj_polarize, then detection: this is the true m_s = 0 reference/readout 1.
2. wait.
3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth): the microwave test pulse.
4. detection: this is the signal readout after the Rabi pulse/readout 2.

Physical model calculation

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1. With a 52 ns pulse, the on-resonance spin transfer probability for a rectangular Rabi pulse is

P(+1) = sin^2(pi * f_Rabi * t)
      = sin^2(pi * 10e6 * 52e-9)
      = sin^2(1.6336)
      = 0.996.

Using the stated contrast scale of about 22%, the expected fluorescence change at resonance is therefore approximately

fractional drop = 0.22 * 0.996 = 0.219,

or about a 21.9% lower signal readout relative to the m_s = 0 reference. The measured readout 1 mean is 45.68 counts, so the expected resonant dip in readout 2 relative to readout 1 is about

45.68 * 0.219 = 10.01 counts.

Including detuning for a rectangular pulse, I used

P(Delta) = (f_Rabi^2 / (f_Rabi^2 + Delta^2)) *
           sin^2(pi * t * sqrt(f_Rabi^2 + Delta^2)).

This predicts a broad, several-point dip of order 10 counts when the scan crosses resonance, because the pulse is close to a pi pulse and the 5 MHz scan spacing is smaller than the approximate 1/t spectral width.

Data comparison

The combined raw readouts are:
- readout 1 mean = 45.681, standard deviation over scan = 0.962 counts
- readout 2 mean = 45.584, standard deviation over scan = 1.400 counts
- readout2 - readout1 mean = -0.097 counts
- readout2 - readout1 standard deviation = 1.834 counts
- most negative readout2 - readout1 value = -3.231 counts
- most negative fractional value = -6.88%

The largest observed negative excursions are only about 3.2 counts, roughly one third of the expected 10-count resonant response, and they are not part of a coherent Rabi-pulse detuning feature. A least-squares fit of the detuned Rabi model with free center, baseline, and amplitude gives a best-fit amplitude of only about 2.93 counts, far below the physically expected about 10.0 counts. Forcing the expected 10-count amplitude gives residuals dominated by a dip shape that is absent from the data.

The per-average traces mainly show baseline/tracking changes between stored averages and do not provide a strong independent repeatability check. They do not rescue a resonance interpretation because the active readout difference lacks the expected contrast-scale response.

Decision

Given the active pulse is effectively a pi pulse at mod_depth = 1, a true pODMR resonance in this scan should produce a large readout-2 dip relative to readout 1. The measured differential signal is near zero with only small, incoherent excursions. I therefore decide that a pODMR resonance is absent.
