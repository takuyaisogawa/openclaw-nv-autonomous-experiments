Case: podmr_035_2026-05-16-210045

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png for visual cross-check only

Active pulse sequence and readout roles:
- Sequence: Rabimodulated.xml / Rabimodulated pulse ODMR scan, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S=+1 reference block is inactive.
- Readout 1 is the true m_S=0 reference acquired immediately after optical polarization and detection.
- Readout 2 is the signal readout acquired after a single rabi_pulse_mod_wait_time pulse, followed by detection.
- length_rabi_pulse is 52 ns in the active XML, rounded at 250 MS/s to 52 ns.
- mod_depth is 1 in inputs/sequence.xml. The raw export also contains a serialized sequence string showing mod_depth = 0.3, but the explicit provided sequence XML and variable values list mod_depth = 1; I use the provided active XML setting.

Quantitative expected-signal model:
- Given setup Rabi frequency f_R approximately 10 MHz at mod_depth = 1.
- For a rectangular resonant pulse, transition probability P = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S=0 and m_S=+1 is about 22%, so the expected resonant fractional PL drop in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, or about 11 counts on a 50-count baseline.
- Even if the serialized mod_depth = 0.3 were used instead, f_R would be about 3 MHz, P = 0.222, and the expected resonant fractional PL drop would be about 4.9%, or about 2.4 counts on a 50-count baseline.

Measured comparison:
- Combined readout 1 mean: 50.936.
- Combined readout 2 mean: 50.084.
- Mean ratio readout2/readout1: 0.9834, i.e. only 1.66% lower on average.
- Maximum observed fractional drop readout2/readout1 is 5.65%, occurring at the low-frequency edge around 3.830 GHz, not as a coherent isolated ODMR resonance.
- The largest absolute deficit of readout 2 relative to readout 1 is 2.81 counts, far below the 10.96-count expectation for mod_depth = 1. The per-average traces vary substantially and stored averages are only two tracking-cadence averages, so they are not strong independent repeatability evidence.
- Across the scan the traces show a common upward drift and scattered readout-ratio fluctuations; no feature has the amplitude, line shape, or consistency expected from the active physical model.

Decision:
The expected resonant signal for the active XML pulse is large, but the measured readouts do not show that scale of contrast. I decide that a pODMR resonance is absent.
