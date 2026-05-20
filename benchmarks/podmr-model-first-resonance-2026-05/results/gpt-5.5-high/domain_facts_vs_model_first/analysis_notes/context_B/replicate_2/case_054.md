Case: podmr_040_2026-05-16-222642

Sequence interpretation

The active sequence is Rabimodulated.xml. The scan variable is mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active readouts are:

1. readout 1: detection immediately after optical polarization, before any
   microwave pulse. This is the true m_S = 0 reference.
2. readout 2: detection after a single rabi_pulse_mod_wait_time call.

The full_expt branch is disabled because full_expt = 0, so the intermediate
"1 level reference" pulse/readout is not active. The active pulse is therefore
the final modulated Rabi pulse with length_rabi_pulse = 52 ns and mod_depth = 1.

Physical model calculation

Use the given setup facts: contrast between m_S = 0 and m_S = +1 is about 22%,
and the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular Rabi
pulse, the driven population transfer is

P(detuning) = (Omega^2 / (Omega^2 + delta^2)) *
              sin^2(0.5 * sqrt(Omega^2 + delta^2) * t)

with Omega = 2*pi*10 MHz, delta = 2*pi*detuning, and t = 52 ns.

At zero detuning this gives:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected resonant fluorescence drop is therefore:

0.22 * 0.996 = 0.219, or 21.9%.

The mean readout 1 level is 47.19 raw units, so a resonant scan point should
drop by about:

47.19 * 0.219 = 10.34 raw units.

The same model predicts a broad response on the 5 MHz grid:

- 0 MHz detuning: 21.9% drop, 10.34 raw units.
- 5 MHz detuning: 16.5% drop, 7.77 raw units.
- 10 MHz detuning: 6.0% drop, 2.83 raw units.
- 20 MHz detuning: 1.1% drop, 0.50 raw units.

Data comparison

The combined readout data have mean readout 1 = 47.19 and mean readout 2 =
46.66. The mean difference readout2 - readout1 is only -0.53 raw units. The
largest apparent fractional drop is at 3.885 GHz:

readout 1 = 48.37, readout 2 = 44.67, drop = 3.69 raw units = 7.6%.

This is far smaller than the expected 21.9% resonant drop for the active pulse.
It also does not show the expected adjacent-point structure: if the resonance
were centered on 3.885 GHz, the points at +/-5 MHz should still show about a
16.5% drop, but the observed drops at 3.880 GHz and 3.890 GHz are only about
2.3% and 2.5%. If the resonance were between grid points, two neighboring
points should show large dips rather than a single small one.

The stored per-average traces both show the 3.885 GHz point lower than nearby
points, but there are only two averages and the prompt states that stored
averages often reflect tracking cadence rather than an independent repeatability
test. The amplitude and lineshape are not consistent with the fixed physical
model for a 52 ns, mod_depth = 1 pulse.

Decision

No pODMR resonance is established in this dataset. The strongest apparent dip is
too small and too narrow compared with the expected Rabi-driven pODMR response.
