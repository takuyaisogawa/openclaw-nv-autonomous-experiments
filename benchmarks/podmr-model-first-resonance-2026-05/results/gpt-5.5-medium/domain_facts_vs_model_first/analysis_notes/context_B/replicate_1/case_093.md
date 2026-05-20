Case podmr_079_2026-05-17-103702 analysis note

I used the provided sequence information for this case before deciding. The active sequence is Rabimodulated.xml with full_expt = 0, so the executed readout roles are:

- readout 1: true m_S = 0 reference after optical polarization and detection.
- readout 2: signal readout after a Rabi-modulated microwave pulse and detection.
- the optional m_S = 1 reference block is inactive because full_expt = 0.

The sequence values recorded for the case are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps, and detuning = 0. The raw_export embedded sequence text still shows an older default mod_depth = 0.3, but the case Variable_values and inputs/sequence.xml both give mod_depth = 1, so I used mod_depth = 1.

Quantitative model:

For a rectangular pulse, I modeled the population transferred to m_S = +1 as

P1(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau),

with Omega = 10 MHz * mod_depth and tau = 52 ns. At mod_depth = 1, Omega = 10 MHz, so the on-resonance transfer is

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated contrast scale of 22% and the observed m_S = 0 reference level mean of 50.718 counts, the expected resonant signal drop is

50.718 * 0.22 * 0.996 = 11.11 counts.

Even if a resonance falls halfway between 5 MHz-spaced scan points, the nearest sampled point is only 2.5 MHz detuned. The same model gives max sampled P1 = 0.929, corresponding to an expected drop of about 10.37 counts. Thus a real resonance in this scan should create a large negative dip in readout2 - readout1, spanning one or more sampled points.

Observed data:

- readout 1 mean = 50.718 counts, standard deviation = 1.141 counts.
- readout 2 mean = 50.782 counts, standard deviation = 0.859 counts.
- readout2 - readout1 mean = +0.064 counts, standard deviation = 1.288 counts.
- deepest observed signal-reference dip = -2.096 counts at 3.870 GHz, only about -3.9% relative to readout 1.

I also fit the detuned Rabi response shape over possible resonance centers within the scanned band using y = c - A * P1(Delta). The best nonnegative dip amplitude inside the scan was about 1.0 count, far below the expected calibrated amplitude of about 11.1 counts. Stored averages are not treated as strong independent repeatability evidence; they are only used as a consistency check.

Decision: resonance_absent. The physically expected pODMR signal for this pulse and mod_depth is much larger than the observed fluctuations, and the scan does not show the required negative contrast feature in the signal readout relative to the m_S = 0 reference.
