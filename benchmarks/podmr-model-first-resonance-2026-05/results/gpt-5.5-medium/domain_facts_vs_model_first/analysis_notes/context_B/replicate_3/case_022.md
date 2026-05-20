Sequence and roles

The active sequence is Rabimodulated.xml. The saved scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant variable values are
length_rabi_pulse = 52 ns and mod_depth = 1. The XML sets full_expt = 0, so
the optional m_S = +1 reference block is skipped.

The executed readouts are therefore:

1. Readout 1: after adj_polarize and detection, a bright m_S = 0 reference.
2. Readout 2: after a 52 ns rabi_pulse_mod_wait_time pulse at mod_depth = 1,
   followed by detection. This is the pODMR signal readout, not an independent
   dark-state reference.

Physical model calculation

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is about
10 MHz. For a rectangular pulse, the driven transition probability versus
detuning is

P(f) = (Omega^2 / (Omega^2 + Delta^2)) *
       sin^2(pi * sqrt(Omega^2 + Delta^2) * tau)

with Omega = 10 MHz, tau = 52 ns, and Delta = f - f0, all in cycles per
second. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The bright-reference mean readout is 35.99 counts. With a 22% contrast scale,
the expected maximum fluorescence drop for nearly full transfer is

0.22 * 35.99 * 0.996 = 7.89 counts.

Data comparison

The observed readout-2 minimum is 28.21 counts at 3.880 GHz. Relative to the
readout-1 mean, the drop is

35.99 - 28.21 = 7.77 counts, or 21.6%.

This matches the expected 22% contrast-scale dip for a resonant near-pi pulse.
Fitting the readout-2 trace to the rectangular-pulse line shape with free
baseline, amplitude, and center gives a best center near 3.87775 GHz, a fitted
drop of 7.57 counts, and a much lower SSE than a constant model (32.6 versus
127.1). Stored per-average traces show the same central depression, but I do
not treat the two averages as a strong repeatability test because stored
averages can reflect tracking cadence.

Decision

A pODMR resonance is present. The active readout roles, pulse duration, and
mod_depth predict a large dip, and the observed dip has the expected magnitude
and line-shape scale.
