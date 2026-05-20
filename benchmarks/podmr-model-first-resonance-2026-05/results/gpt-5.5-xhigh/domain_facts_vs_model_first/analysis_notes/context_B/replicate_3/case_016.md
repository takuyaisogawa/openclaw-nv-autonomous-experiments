Inputs inspected: inputs/sequence.xml and inputs/raw_export.json.

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the XML, full_expt = 0, so the optional "Acquire 1 level reference" block is skipped even though do_adiabatic_inversion is true. The active readouts are therefore:

1. readout 1: detection immediately after adj_polarize, the "true 0 level reference".
2. readout 2: detection after rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.

The relevant pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so the rounded pulse is exactly 13 samples = 52 ns.

Quantitative expected signal model:

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. I used the rectangular-pulse two-level transition probability

P(f) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

with f_R = 10 MHz, t = 52 ns, and delta = f - f0. On resonance this gives

P_res = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, a fully resonant pulse should lower the second readout by about

0.22 * 0.996 * 38 counts = 8.33 counts,

or about 21.9% of the same-point m_S = 0 reference.

Observed readout differences, using readout1 - readout2, show the largest dip at the expected scale:

- 3.875 GHz: 38.2115 - 30.0000 = 8.2115 counts, normalized drop 21.49%.
- 3.880 GHz: 37.1346 - 28.9808 = 8.1538 counts, normalized drop 21.96%.

I fit readout2 with the physical model

readout2 = readout1 + b - 0.22 * readout1 * P(f; f0).

The best center was f0 = 3.87735 GHz with b = -0.146 counts and SSE = 35.73. A no-resonance offset-only model readout2 = readout1 + b had SSE = 158.05, so the physical resonance model reduced the residual sum of squares by 77.4%. If the contrast coefficient is also fit, the best value is 0.231, close to the expected 0.22.

The two stored averages both show the same scale of drop near 3.875-3.880 GHz, but I treat that only as a consistency check because stored averages can mainly reflect tracking cadence.

Decision: the data contain a pODMR resonance.
