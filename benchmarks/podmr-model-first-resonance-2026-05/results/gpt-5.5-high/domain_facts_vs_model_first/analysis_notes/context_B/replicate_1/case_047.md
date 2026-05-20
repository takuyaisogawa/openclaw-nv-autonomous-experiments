Case: podmr_033_2026-05-16-203113

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, previous outputs, sibling cases, or external context.

Active sequence identification:
- Sequence: Rabimodulated.xml.
- Scan variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is inactive.
- Readout 1 role: true m_S = 0 reference immediately after optical polarization and before the microwave pulse.
- Readout 2 role: post-pulse pODMR readout after rabi_pulse_mod_wait_time.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:
The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular resonant pulse, the transition probability versus detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

With f_R = 10 MHz and t = 52 ns:
- On resonance: P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- At 2.5 MHz detuning, the largest possible offset from a resonance to the nearest 5 MHz scan point: P = 0.929.
- At 5 MHz detuning: P = 0.749.

The current setup contrast between m_S = 0 and m_S = +1 is about 22 percent. The combined readout-1 mean is 53.899 counts, so the predicted post-pulse readout drop for a resonance sampled on the grid is about

53.899 * 0.22 * 0.996 = 11.81 counts

on resonance, and still about

53.899 * 0.22 * 0.929 = 11.02 counts

if the resonance is halfway between adjacent scan points. Thus a real resonance in the scanned range should appear as an approximately 11-count negative feature in readout2 - readout1 at one or more nearby scan points. Even at 5 MHz detuning the expected drop remains 8.88 counts.

Observed data:
- Mean readout 1: 53.899 counts.
- Mean readout 2: 54.309 counts.
- Mean readout2 - readout1: +0.409 counts.
- Sample standard deviation of readout2 - readout1 across scan points: 1.025 counts.
- Observed readout2 - readout1 values range from about -1.44 counts to +2.52 counts.

The observed post-pulse readout is not lower than the m_S = 0 reference by anything close to the modeled resonance signal. The largest negative excursion is only about 12 percent of the expected on-grid resonance drop, and the mean sign is positive rather than negative. Stored per-average traces show large offsets consistent with tracking cadence, so I did not treat them as strong independent repeatability evidence.

Decision: resonance_absent.
