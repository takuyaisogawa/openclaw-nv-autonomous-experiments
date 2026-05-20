Active sequence and readout roles

The active sequence in the export is Rabimodulated.xml, scanned by mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The exported sequence parameters are the
ones used for the decision: length_rabi_pulse = 52 ns, mod_depth = 1,
full_expt = 0, sample_rate = 250 MHz, delay_wrt_1mus = 0.2 us, and
pumping_time = 1 us.

Because full_expt = 0, the conditional "Acquire 1 level reference" block is not
executed. Each point contains a true mS = 0 reference readout after optical
polarization, followed by the readout after the modulated Rabi pulse. The two
stored readout traces therefore correspond to reference and driven pODMR
readout, not independent resonance channels.

Quantitative expected signal model

For this setup, f_Rabi is about 10 MHz at mod_depth = 1. For a square pulse of
duration T = 52 ns, the resonant two-level transition probability is

P = sin^2(pi * f_Rabi * T)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

With the stated contrast scale of 22% between mS = 0 and mS = +1, a resonant
pulse should reduce fluorescence by about 0.22 * 0.996 = 0.219 of the reference
level. On the observed 53.29 count reference baseline, this is an expected dip
of about 11.7 counts in the driven readout near resonance.

I also evaluated the square-pulse detuning model

P(f) = (Omega^2 / (Omega^2 + Delta^2)) *
       sin^2(0.5 * sqrt(Omega^2 + Delta^2) * T),

with Omega = 2*pi*10 MHz and Delta = 2*pi*(f - f0), fitting baseline, linear
drift, resonance center, and amplitude to the driven readout. The no-resonance
linear baseline RSS is 17.23. The best resonance-shaped fit RSS is 11.60, but
its fitted dip amplitude is -2.30 counts in the convention y = baseline - A*P,
meaning the preferred feature has the opposite sign from a pODMR fluorescence
dip. This is also far smaller than the expected +11.7 count dip.

Observed data check

The combined reference readout mean is 53.29 counts and the driven readout mean
is 52.93 counts. The pointwise driven-minus-reference differences range from
-3.42 to +1.75 counts, with mean -0.36 counts and sample standard deviation
1.31 counts. The largest negative excursion occurs at 3.865 GHz, but it is only
about 3.4 counts, isolated, and not consistent with the broad, high-contrast
square-pulse response expected from a 52 ns near-pi pulse at mod_depth = 1.
Stored averages show tracking offsets and are not treated as a strong
independent repeatability test.

Decision

Given the active pulse sequence and the expected approximately 11.7 count
resonant fluorescence suppression, the observed traces do not contain a
physically consistent pODMR resonance. The appropriate prediction is resonance
absent.
