Case: podmr_051_2026-05-17-011109

Sequence and readout roles

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence has sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, and length_last_wait = 1 us.

Because full_expt is zero, the optional 1-level reference block is skipped. The two acquired readouts are therefore:

1. Readout 1: polarized m_S = 0 reference, acquired immediately after adj_polarize and before the swept microwave pulse.
2. Readout 2: signal readout after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative expectation

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1. The rounded pulse length is exactly 13 samples at 250 MHz, so t = 52 ns. For a square resonant pulse, the expected transfer probability is:

P = sin^2(pi * f_R * t)
  = sin^2(pi * 10e6 * 52e-9)
  = 0.996.

Using the stated 22% m_S = 0 to m_S = +1 readout contrast scale, the expected on-resonance fractional drop in readout 2 relative to readout 1 is:

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout 1 level is 48.33 raw units, so a resonant pi pulse should lower readout 2 by about:

48.33 * 0.219 = 10.59 raw units,

giving an expected on-resonance readout 2 level near 37.74 raw units if the resonance is sampled. With 5 MHz scan spacing, any resonance within the scan range is at most 2.5 MHz from a sampled point. The same square-pulse model gives transfer probability 0.929 at 2.5 MHz detuning, corresponding to an expected fractional drop of 20.4%, still about 9.9 raw units. Even at 5 MHz detuning the expected drop is 16.5%, about 8 raw units.

Data comparison

The combined readout means are:

readout 1 mean = 48.33
readout 2 mean = 47.86
mean fractional contrast (readout1 - readout2) / readout1 = 0.009

The largest apparent dip is at 3.895 GHz:

readout 1 = 50.00
readout 2 = 45.38
fractional drop = 9.2%
raw drop = 4.62

This is less than half of the minimum expected sampled resonant response for the identified 52 ns, mod_depth = 1 pulse. Away from that point, the contrast fluctuates around zero with a standard deviation of about 2.6% after excluding the largest dip, and the largest remaining contrast is only about 4.4%.

The two stored averages both show a local low point at 3.895 GHz, but stored averages here are tracking-cadence chunks rather than a strong independent repeatability test. Their combined dip amplitude remains far below the physical expectation for a near-pi pulse at mod_depth = 1.

Decision

Under the relevant pulse model, a true pODMR resonance in this scan should produce a large readout 2 decrease of roughly 20% to 22% relative to the m_S = 0 reference at at least one sampled frequency. The observed maximum decrease is only 9.2% and the fitted pulse-response amplitude is about 0.056 versus an expected 0.22. I therefore classify this case as resonance_absent.
