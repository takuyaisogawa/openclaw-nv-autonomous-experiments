Case: podmr_057_2026-05-17-051839

I used the sequence XML embedded in the raw export as the active scan sequence, because it contains the saved parameter values for this measurement. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed readouts are:

- readout 1: true m_S = 0 bright reference after adj_polarize and detection.
- readout 2: detection after a modulated Rabi microwave pulse.

The m_S = +1 reference block is inactive because full_expt = 0, so no independent dark reference is acquired. do_adiabatic_inversion is set but not used in the active branch. The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this pulse is already sample aligned.

Physical model calculation:

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. The resonant transition probability for a square pulse is

P_transfer = sin^2(pi * f_Rabi * t)

Using f_Rabi = 10 MHz and t = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the given m_S = 0 to m_S = +1 contrast scale of about 22%, a true resonance should reduce the post-pulse readout by about

0.22 * 0.996 = 0.219, or 21.9% of the bright level.

The bright reference level is about 45.46 raw counts, so the expected on-resonance dip is about 9.96 raw-count units. Therefore a resonant point should be near 35.5 counts in readout 2 if the pulse is on resonance and the contrast applies normally.

Observed data:

- mean readout 1 = 45.46
- mean readout 2 = 45.42
- mean readout2/readout1 = 0.999
- minimum readout 2 = 43.83 at 3.910 GHz
- drop of minimum readout 2 below its mean = 1.59 counts
- high-frequency scatter estimate for readout 2 = about 1.03 counts

The deepest observed readout-2 point is only about 1.5 sigma below the mean and about 6 times smaller than the expected resonant dip. Reference-normalized values also do not show a physically sized dip. The lowest ratio occurs at the sweep endpoint, not as a clear resonance feature, and stored averages do not provide a strong independent repeatability test here because they may mostly reflect tracking cadence.

Decision: resonance_absent. A resonance driven by a 52 ns, mod_depth 1 pulse should be a large approximately 22% dip, but the measured scan shows only small tracking/noise-scale fluctuations with no quantitatively compatible pODMR feature.
