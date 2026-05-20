Sequence and roles
==================

The provided sequence is Rabimodulated.xml. It sets a microwave frequency and uses a modulated Rabi pulse. The executed readout order is:

1. adj_polarize followed by detection: this is the true mS = 0 reference readout.
2. The mS = 1 reference block is skipped because full_expt = 0.
3. rabi_pulse_mod_wait_time followed by detection: this is the pODMR signal readout after the microwave pulse.

Relevant parameters from the saved export / XML:

- scan: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps
- active pulse: rabi_pulse_mod_wait_time
- length_rabi_pulse: 52 ns
- mod_depth: 1
- setup Rabi frequency at mod_depth 1: approximately 10 MHz
- setup mS = 0 to mS = +1 contrast scale: approximately 22%

Expected signal model
=====================

For a square resonant Rabi pulse, the transfer probability is

P = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10 MHz and tau = 52 ns:

pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 1.6336 rad
P = sin^2(1.6336) = 0.996

The expected fluorescence drop at resonance is therefore approximately

contrast * P = 0.22 * 0.996 = 0.219

or about a 21.9% drop of the signal readout relative to the mS = 0 reference. With the observed reference mean of 46.94 counts, the expected on-resonance raw-count drop is approximately

46.94 * 0.219 = 10.29 counts.

Observed data check
===================

The combined mS = 0 reference readout has mean 46.94 counts and standard deviation 1.45 counts. The combined signal readout has mean 46.13 counts and standard deviation 1.45 counts.

The pointwise signal/reference ratio has:

- mean: 0.983
- standard deviation: 0.028
- minimum: 0.929 at 3.895 GHz
- maximum: 1.052 at 3.925 GHz

Using the median signal/reference ratio, the largest observed normalized deficit is only about 0.051, equivalent to about 2.4 counts. This is much smaller than the approximately 10.3-count drop expected from the relevant physical model for an on-resonance 52 ns pulse at mod_depth 1.

Decision
========

The data do not show a resonance-sized pODMR contrast feature. The observed readout differences are small compared with the expected signal and are comparable to ordinary point-to-point variation and tracking changes. Since stored averages mainly reflect tracking cadence, the per-average overlay is not treated as a strong independent repeatability test. I decide that a pODMR resonance is absent.
