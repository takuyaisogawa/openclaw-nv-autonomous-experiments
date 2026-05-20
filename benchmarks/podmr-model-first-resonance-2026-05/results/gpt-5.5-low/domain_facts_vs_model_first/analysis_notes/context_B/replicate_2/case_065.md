Active sequence and readout roles

The active pulse sequence is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant active variables are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, delay_wrt_1mus = 0.2 us, and pumping_time = 1 us.

Because full_expt = 0, the optional ms = +1 reference block is skipped. The two readouts are therefore:

1. readout 1: after optical polarization, a true ms = 0 bright reference.
2. readout 2: after the modulated Rabi microwave pulse, the pODMR signal readout.

Quantitative physical model

The supplied setup facts give a Rabi frequency of approximately 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For a resonant rectangular Rabi pulse with duration t = 52 ns, the transferred population is

P = sin^2(pi * f_Rabi * t / 2)
  = sin^2(pi * 10e6 * 52e-9 / 2)
  = 0.531.

With a setup contrast between ms = 0 and ms = +1 of about 22%, the expected fractional fluorescence reduction at resonance is approximately

0.22 * 0.531 = 0.117, or 11.7%.

At the observed count level near 48 counts, this corresponds to an expected on-resonance drop of about 5.6 counts for the post-pulse readout relative to the bright reference, allowing for imperfect experimental details.

Observed data check

The combined readout means are:

- readout 1 mean = 48.33 counts, standard deviation across scan points = 1.11 counts.
- readout 2 mean = 47.86 counts, standard deviation across scan points = 1.13 counts.
- readout 2 minus readout 1 has mean = -0.47 counts and standard deviation = 1.56 counts.

The strongest candidate feature is at 3.895 GHz:

- readout 1 = 50.00 counts.
- readout 2 = 45.38 counts.
- signal/reference ratio = 0.908, a 9.2% reduction.
- absolute drop = 4.62 counts.

This is close to the quantitative model expectation of an approximately 11.7% reduction, or about 5.6 counts. The adjacent scan points do not show the same drop, so the feature is frequency localized. The stored averages should not be treated as a strong independent repeatability test, but both averages show a reduced signal/reference ratio at the same scan point: about 0.900 and 0.915.

Decision

The active sequence implements a resonant Rabi-pulse pODMR measurement, and the observed localized reduction in the post-pulse signal readout has the expected sign and a magnitude close to the model prediction. I therefore decide that a pODMR resonance is present.
