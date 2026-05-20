Case podmr_047_2026-05-17-001223 analysis note

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName / active XML: Rabimodulated.xml.
- The executed instructions first call adj_polarize, then detection. This first detection is the true mS=0 reference readout.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is skipped. There is no active mS=+1 reference readout in this run.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This second detection is the microwave-pulse signal readout.

Pulse settings:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- The frequency scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Explicit expected-signal model:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Therefore f_Rabi = 10 MHz for this run.
- For a resonant rectangular Rabi pulse, the population transfer probability is P = sin^2(pi * f_Rabi * tau), with tau = 52 ns.
- pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 1.6336 rad.
- P = sin^2(1.6336) = 0.9961.
- With mS=0 to mS=+1 contrast scale about 22%, the expected resonant signal drop is 0.22 * 0.9961 = 0.2191, or about 21.9% of the mS=0 readout.
- The observed mS=0 reference readout mean is 50.38 counts, so an on-resonance signal readout would be expected near 50.38 * (1 - 0.2191) = 39.34 counts, a drop of about 11.04 counts.

Observed quantitative comparison:
- Mean reference readout = 50.38 counts.
- Mean signal readout = 50.06 counts.
- Mean signal-reference difference = -0.32 counts, with standard deviation 1.42 counts across scan points.
- The largest signal/reference normalized decrease is at 3.905 GHz, where signal/reference = 0.947, a 5.3% drop.
- The deepest absolute signal-reference difference is -2.73 counts, far smaller than the expected about -11.04 count resonant response.
- The signal readout minimum is 48.17 counts, not near the expected resonant level around 39.34 counts.
- Stored averages show sizable tracking-like offsets between averages and do not provide strong independent repeatability evidence.

Decision:
The active pulse should produce nearly full inversion on resonance and therefore an approximately 22% pODMR contrast feature. The measured signal readout remains close to the mS=0 reference and shows only small fluctuations, with no point approaching the expected resonant depletion. I therefore decide that a pODMR resonance is absent.
