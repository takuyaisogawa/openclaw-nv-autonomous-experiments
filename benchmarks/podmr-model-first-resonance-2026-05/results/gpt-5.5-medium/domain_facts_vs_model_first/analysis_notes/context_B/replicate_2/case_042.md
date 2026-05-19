<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_042

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence and readout roles

The active sequence is Rabimodulated.xml. In the provided XML, full_expt = 0, so the optional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true. The executed measurement has:

1. adj_polarize
2. detection
3. wait_for_awg
4. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth)
5. detection
6. wait_for_awg

Thus readout 1 is the polarized m_S = 0 reference/tracking readout. Readout 2 is the microwave-driven pODMR signal readout after the Rabi pulse.

The provided XML values are:

- length_rabi_pulse = 5.2e-08 s = 52 ns
- mod_depth = 1
- scan variable = mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns

Physical model calculation

Given the setup facts, the resonant Rabi frequency at mod_depth = 1 is about 10 MHz. For a square pulse, the transition probability versus detuning is

P(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * t * sqrt(f_R^2 + detuning^2))

with f_R in cycles/s and detuning in Hz. At resonance with t = 52 ns and f_R = 10 MHz:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

The m_S = 0 to m_S = +1 contrast scale is about 22%, so a true on-resonance point should have an expected fractional fluorescence decrease of

0.22 * 0.996 = 0.219, or about a 22% dip of readout 2 relative to the local m_S = 0 reference readout.

With raw counts around 52, this corresponds to roughly an 11 count drop at resonance, not a 1-3 count fluctuation.

Observed quantitative comparison

The combined readouts have means:

- readout 1 mean = 51.718, standard deviation across scan points = 1.100
- readout 2 mean = 51.570, standard deviation across scan points = 0.972

The readout2/readout1 ratio ranges from 0.9446 to 1.0504. The largest apparent dip is therefore about 5.5%, far below the expected about 22% resonant dip for the actual pulse. The most negative readout2-readout1 differences are:

- 3.875 GHz: readout1 = 52.308, readout2 = 49.885, ratio = 0.9537, difference = -2.423
- 3.880 GHz: readout1 = 53.654, readout2 = 51.654, ratio = 0.9627, difference = -2.000
- 3.885 GHz: readout1 = 53.769, readout2 = 50.788, ratio = 0.9446, difference = -2.981

These are only small depressions relative to the expected approximately 11 count resonant effect. The same data also contain a positive excursion at 3.890 GHz where readout2/readout1 = 1.0504, comparable in size and opposite in sign to the apparent dips. The two stored averages should not be treated as a strong independent repeatability test because stored averages often reflect tracking cadence.

Decision

For the active pulse sequence, the expected pODMR resonance is a large near-pi-pulse fluorescence dip. The observed readout 2 signal does not show the expected amplitude or a quantitatively convincing model-shaped resonance. I classify this case as resonance_absent.
