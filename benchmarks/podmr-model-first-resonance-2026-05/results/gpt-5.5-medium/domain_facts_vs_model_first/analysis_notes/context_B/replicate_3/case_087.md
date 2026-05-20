Case podmr_073_2026-05-17-090948.

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- The sequence is Rabimodulated.xml / Rabimodulated.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout 1 is the first detection after adj_polarize, therefore the pumped m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time, therefore the pODMR signal after the microwave pulse.
- The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- From the provided sequence XML, length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative signal model:
- Given domain fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_R = 10 MHz for this case.
- For a rectangular driven two-level pulse, transition probability versus detuning is
  P(f) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),
  where Delta = f - f0 in cycles/s and t = 52 ns.
- On resonance, P0 = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With a contrast scale of about 22 percent between m_S = 0 and m_S = +1, a resonant pi pulse should reduce the post-pulse readout by about 0.22 * 0.996 = 21.9 percent relative to the pumped reference.
- The mean readout-1 level is 50.17 counts, so the expected resonant dip is about 50.17 * 0.219 = 10.99 counts. A true resonance near the center of the scan should therefore make readout 2 roughly 39 counts while readout 1 remains near 50 counts.

Measured comparison:
- Mean readout 1 = 50.17 counts.
- Mean readout 2 = 50.04 counts.
- Mean readout2 - readout1 = -0.12 counts, with point-to-point standard deviation of 1.09 counts.
- At 3.875 GHz, the nominal center frequency from the embedded scan sequence, readout1 = 49.94 and readout2 = 51.48, so readout2 - readout1 = +1.54 counts, opposite the expected resonant dip.
- The largest negative readout2 - readout1 excursions are -2.52 counts at 3.855 GHz and -2.37 counts at 3.910 GHz, much smaller than the approximately -11 count dip expected for mod_depth = 1 and not forming the modeled resonance response.
- A least-squares comparison to the expected dip shape at 3.875 GHz gives the wrong sign: the data prefer a small peak rather than a dip.

Decision:
The physically expected pODMR signal for this pulse is large compared with the measured fluctuations, and the observed readout-2 signal does not show the required resonant decrease relative to the m_S = 0 reference. A pODMR resonance is absent.
