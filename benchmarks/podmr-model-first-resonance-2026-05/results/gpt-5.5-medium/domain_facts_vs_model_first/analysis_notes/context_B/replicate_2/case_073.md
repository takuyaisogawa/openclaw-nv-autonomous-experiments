<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_073

I used the provided sequence XML rather than labels or prior outputs. The active sequence is Rabimodulated.xml. With full_expt = 0, the sequence does not acquire the optional m_S = +1 reference. It first performs adj_polarize followed by detection, giving the true m_S = 0 optical reference readout. It then applies one rabi_pulse_mod_wait_time pulse and performs a second detection, giving the post-microwave-pulse readout. Thus readout 1 is the bright reference and readout 2 is the signal after the microwave pulse.

Relevant pulse parameters from the provided sequence XML:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- mod_depth = 1.
- mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps in the raw export.

Quantitative expected-signal model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the resonant transfer probability is

P = sin^2(pi * f_R * t).

With f_R = 10 MHz and t = 52 ns,

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the given contrast scale of 22% between m_S = 0 and m_S = +1, an on-resonance pi-like pulse should reduce the post-pulse readout by

0.22 * 0.996 = 0.219,

or about 21.9% of the bright reference. At the observed reference level of about 42.7 counts, this is an expected dip of about 9.4 counts in readout 2 relative to readout 1 near resonance.

I also evaluated the detuned Rabi response

P(f) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz and Delta = 2*pi*(f - f0), scanning candidate resonance centers across the measured frequency span. Fitting the normalized contrast C = 1 - readout2/readout1 to C = a + b P(f) gives a best-fit contrast scale b = 0.042, far below the physical 0.22 contrast expected for this pulse. Forcing the physical 22% contrast produces a predicted normalized dip near 0.19 at the best center, which is much larger than the observed normalized contrast values.

Observed data comparison:
- mean readout 1 = 42.67 counts.
- mean readout 2 = 42.11 counts.
- readout2 - readout1 ranges from -2.87 to +1.52 counts.
- the largest apparent darkening is about 6.4% at 3.880 GHz, only about 2.9 counts, and there are comparable scattered positive/negative deviations elsewhere.

Because the provided sequence XML gives a nearly complete resonant transfer pulse at mod_depth = 1, a real pODMR resonance should be a large, coherent dip of roughly 9 counts. The measured readout difference is much smaller and not a convincing line shape. Stored averages are only two averages and can reflect tracking cadence, so I do not treat the per-average overlay as an independent repeatability confirmation.

Decision: resonance_absent.
