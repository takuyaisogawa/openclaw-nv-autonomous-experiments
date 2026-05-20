Case podmr_036_2026-05-16-211536

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json for the numeric raw readouts only

Active sequence and roles:
- Sequence: Rabimodulated.xml / Rabimodulated-style sequence.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- The executed readout order is:
  1. adj_polarize followed by detection: true m_S = 0 fluorescence reference.
  2. one rabi_pulse_mod_wait_time followed by detection: signal readout after the microwave pulse.
- Therefore readout 1 is the bright/polarized reference and readout 2 is the post-pulse signal.

Pulse parameters from the provided sequence XML:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- sample_rate = 250 MHz, so 52 ns rounds to 13 samples / 250 MHz = 52 ns.

Quantitative expected-signal model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a resonant square pulse, transition probability P = sin^2(pi * f_R * t), where f_R is the Rabi oscillation frequency in cycles/s.
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With m_S = 0 to m_S = +1 contrast scale about 22%, the expected fractional fluorescence drop at resonance is 0.22 * 0.996 = 0.219.
- The mean readout-1 level is 50.985, so the expected resonant drop is 50.985 * 0.219 = 11.17 raw-readout units. Expected resonant signal would be about 39.81 if a resonance receives this near-pi pulse.

Observed signal comparison:
- Mean readout 1 = 50.985.
- Mean readout 2 = 50.476.
- Mean paired difference readout2 - readout1 = -0.509 with standard deviation 1.360.
- The largest observed drop is -2.788 at 3.920 GHz, corresponding to a ratio of 0.946. The next endpoint drop is -2.192 at 3.925 GHz.
- No point approaches the expected about 11.17 unit drop or about 22% contrast. The observed fluctuations are only a few raw units and include positive excursions, consistent with noise/drift rather than a pODMR resonance.
- Stored averages show broad offsets and scatter, and by the provided domain note are not a strong independent repeatability test.

Decision:
- A resonant near-pi pulse at this mod_depth should produce a large post-pulse fluorescence decrease relative to the bright reference. The measured readout2/readout1 changes are far too small and not a coherent resonance feature.
- Prediction: resonance_absent.
