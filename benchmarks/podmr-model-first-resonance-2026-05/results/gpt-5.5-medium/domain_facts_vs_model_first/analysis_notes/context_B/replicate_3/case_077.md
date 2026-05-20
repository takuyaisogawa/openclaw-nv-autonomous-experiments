Case podmr_063_2026-05-17-064555

I used the provided sequence XML and raw export only.

Active pulse sequence and readout roles:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The first detection happens immediately after adj_polarize and is the true m_S=0 optical reference readout.
- full_expt is 0, so the optional m_S=1 reference block is inactive.
- The second detection happens after rabi_pulse_mod_wait_time and is the pODMR contrast-bearing readout.
- The active pulse has length_rabi_pulse = 52 ns.
- mod_depth = 1 in the provided sequence XML and in Variable_values.

Quantitative expected-signal model:

For a rectangular driven two-level pulse, using Rabi frequency Omega = 10 MHz at mod_depth = 1 and pulse duration t = 52 ns, the transition probability versus detuning delta is

P(delta) = Omega^2 / (Omega^2 + delta^2) * sin^2(pi * sqrt(Omega^2 + delta^2) * t),

where Omega and delta are in cycles per second. The fluorescence contrast scale between m_S=0 and m_S=+1 is about 22%, so the expected fractional readout drop is 0.22 * P(delta).

Model values:
- delta = 0 MHz: P = 0.996, expected drop = 21.9%.
- delta = 2.5 MHz, the worst-case halfway offset from a 5 MHz scan grid point: P = 0.929, expected drop = 20.4%.
- delta = 5 MHz: P = 0.749, expected drop = 16.5%.
- delta = 10 MHz: P = 0.273, expected drop = 6.0%.

With a typical first-readout level of 51.82 counts, an on-grid or halfway-between-grid resonance should lower the second readout by about 10.6 to 11.4 counts, to roughly 40 to 41 counts. That is a large signal relative to the observed point-to-point fluctuations.

Observed data:
- Mean readout 1 = 51.82 counts.
- Mean readout 2 = 51.40 counts.
- The readout2/readout1 ratios range from 0.950 to 1.033, with mean 0.992 and standard deviation 0.026.
- The largest observed readout2 depression relative to readout1 is 2.73 counts, or 5.0%, at 3.840 GHz.

Decision:

The expected pODMR resonance from the active 52 ns, mod_depth 1 pulse should be a near-pi-pulse-scale feature of about 20% fractional contrast over the scan grid if present. The observed data show only small fluctuations and slow baseline drift, with no second-readout dip approaching the expected magnitude. Stored averages are not treated as a strong independent repeatability test. I therefore decide that a pODMR resonance is absent.
