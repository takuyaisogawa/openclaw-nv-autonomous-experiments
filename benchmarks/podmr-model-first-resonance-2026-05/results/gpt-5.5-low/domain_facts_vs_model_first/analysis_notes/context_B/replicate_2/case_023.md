Case podmr_008_2026-05-16-014743

I used the sequence embedded in inputs/raw_export.json as the run record, cross-checking it against inputs/sequence.xml. The active sequence is Rabimodulated.xml with vary_prop mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active readouts are:

- first detection after adj_polarize: true m_S = 0 reference/readout 1
- second detection after rabi_pulse_mod_wait_time: microwave-pulse readout/readout 2

The optional m_S = 1 reference block is inactive because full_expt = 0, even though do_adiabatic_inversion is set true. Therefore readout 2 is the relevant pODMR signal channel, while readout 1 is a reference/background channel.

Run parameters from the export:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so 52 ns is already on the 4 ns sample grid
- mw_freq scan center region includes 3.875 GHz

Quantitative expected signal model:

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square resonant pulse of duration t = 52 ns, the resonant transition probability is

P = sin^2(pi * f_Rabi * t)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fractional fluorescence decrease in the post-pulse readout is

0.22 * 0.996 = 0.219, or 21.9%.

The measured combined readout 2 values show a pronounced dip:

- off-dip median baseline excluding the central dip region: 41.365
- local baseline from neighboring points at 3.865 and 3.890 GHz: (39.654 + 41.558) / 2 = 40.606
- minimum at 3.875 GHz: 31.308
- fractional drop versus off-dip median: (41.365 - 31.308) / 41.365 = 24.3%
- fractional drop versus local baseline: (40.606 - 31.308) / 40.606 = 22.9%

This observed dip depth agrees with the explicit expected signal scale for a near-pi 52 ns pulse at mod_depth = 1. The dip is also present in both stored averages near the same scan region, but the averages are not treated as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision: resonance_present.
