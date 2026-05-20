Case: podmr_043_2026-05-16-231159

I treated inputs/sequence.xml as the authoritative pulse sequence file, as requested. The active sequence is Rabimodulated.xml. The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence roles:
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- readout 1 is the first detection immediately after adj_polarize; it is the polarized mS = 0 reference / tracking readout.
- readout 2 is the detection after a single rabi_pulse_mod_wait_time pulse; it is the pODMR signal readout.

Pulse parameters from sequence.xml:
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- sample_rate = 250 MHz, so the rounded pulse length remains 52 ns.

Physical model calculation:
For a rectangular microwave pulse, the driven population transfer is

P1(delta) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * t * sqrt(fR^2 + delta^2))

using cycle/s units, where fR is the on-resonance Rabi frequency. With the supplied setup fact fR = 10 MHz at mod_depth = 1 and t = 52 ns:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The supplied contrast scale is about 22%, so an on-resonance pODMR signal should reduce the post-MW fluorescence by about

0.22 * 0.996 = 0.219

or about 21.9% relative to the mS = 0 readout. At a baseline near 47 counts, that is an expected dip of about 10.3 counts in readout 2 relative to the off-resonant / reference level.

Observed data:
- mean readout 1 = 47.11, mean readout 2 = 47.55.
- readout2/readout1 mean = 1.009, standard deviation = 0.020, minimum = 0.976, maximum = 1.041.
- readout2 - readout1 ranges from -1.19 to +1.87 counts.

I also compared the measured ratio readout2/readout1 to the fixed-contrast rectangular-pulse model y = b * (1 - 0.22 * P1(delta)), scanning possible resonance centers. A true resonance inside the scan would require a ratio minimum near 0.78, but the observed minimum is 0.976. The best fixed-contrast fit avoids placing the resonance inside the measured span; the best free-amplitude fit gives a negative effective contrast, i.e. a peak rather than the expected dip. The per-average traces are not treated as independent confirmation because the stored averages mainly reflect tracking cadence.

Decision: resonance_absent. The pulse should have produced a large pODMR dip if the transition were in the scan window, and the measured signal does not contain that feature.
