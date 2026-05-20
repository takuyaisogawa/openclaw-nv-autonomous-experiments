Case: podmr_067_2026-05-17-074342

Sequence inspection

The sequence file is Rabimodulated.xml. The varied parameter is mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions perform:

1. adj_polarize for 1 us, then detection. This is the true m_S = 0 reference
   readout, corresponding to readout 1.
2. The optional m_S = +1 reference block is skipped because full_expt = 0.
   The do_adiabatic_inversion flag is therefore not active in this run.
3. A modulated microwave Rabi pulse is applied, then detection. This is the
   pODMR signal readout, corresponding to readout 2.

The microwave pulse parameters used for the active pODMR pulse are:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so the rounded pulse is still 52 ns

Quantitative model

Given the setup facts, the Rabi frequency at mod_depth = 1 is approximately
10 MHz. For a resonant square Rabi pulse of duration T = 52 ns, the transition
probability is

P = sin^2(pi * f_Rabi * T)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

With a 22% contrast between m_S = 0 and m_S = +1, a resonance should therefore
produce a readout-2/reference ratio of approximately

1 - 0.22 * 0.996 = 0.781.

In raw units, using the measured readout-1 mean of 48.92, the expected resonant
drop is about 0.219 * 48.92 = 10.7 raw readout units. The square-pulse model
has a half-maximum detuning width of about 7.6 MHz, so with a 5 MHz frequency
step, any resonance inside the scanned range should place at least one sampled
point close enough to show a large drop.

Data comparison

The measured combined readouts have:

- mean readout 1 = 48.920
- mean readout 2 = 48.757
- mean readout-2/readout-1 ratio = 0.99698
- minimum readout-2/readout-1 ratio = 0.95234 at 3.885 GHz
- mean readout-2 minus readout-1 = -0.163 raw units
- standard deviation of the pointwise differences = 1.568 raw units

The largest observed ratio drop is only about 4.8%, and the largest raw
negative pointwise difference is 2.35 units. Both are far below the roughly
21.9% or 10.7 raw-unit resonant response expected from the active 52 ns,
mod_depth = 1 pulse. A least-squares square-pulse fit to the ratio data gives
only about a 4.5% fitted contrast amplitude, which is also much smaller than
the expected 22% scale.

Decision

The active pulse should be near a pi pulse on resonance, so a real pODMR
resonance in the scan would be expected to produce a large readout-2 decrease
relative to the m_S = 0 reference. The observed readout-2 values remain near
the reference level and the small dips are consistent with scan-to-scan
fluctuation rather than the expected physical response. I therefore decide
that a pODMR resonance is absent.
