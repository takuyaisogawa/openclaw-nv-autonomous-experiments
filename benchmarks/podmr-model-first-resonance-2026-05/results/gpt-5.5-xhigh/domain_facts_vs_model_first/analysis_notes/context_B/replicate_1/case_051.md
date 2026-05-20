Case: podmr_037_2026-05-16-213011

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The active instructions polarize the NV, then perform a detection before any microwave pulse. This first detection is the m_S = 0 / bright reference readout.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. There is no separate dark-state reference readout in this run.
- The sequence then applies one rabi_pulse_mod_wait_time pulse with length_rabi_pulse and mod_depth, followed by a second detection. This second detection is the pODMR signal readout after the microwave pulse.

Active pulse parameters from the provided XML:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- The pulse is rounded by sample_rate = 250 MHz. 52 ns * 250 MHz = 13 samples exactly, so the rounded duration remains 52 ns.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1: Omega_R = 10 MHz.
- With linear scaling and mod_depth = 1, Omega_R = 10 MHz for this pulse.
- For a rectangular pulse, the transition probability versus detuning is modeled as:
  P(delta) = (Omega_R^2 / (Omega_R^2 + delta^2)) * sin^2(pi * t * sqrt(Omega_R^2 + delta^2))
  where frequencies are in cycles/s.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.9961.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected resonant readout-2 fractional drop relative to the bright reference is:
  0.22 * 0.9961 = 0.2191, or about 21.9%.
- The mean reference readout is 47.63, so the expected resonant drop is about 10.44 raw-readout units.

Observed data comparison:
- Using readout 1 as the reference and readout 2 as the signal, the observed fractional contrast 1 - readout2/readout1 ranges from -6.19% to +4.37%.
- The largest observed signal drop is only 2.12 raw-readout units, or 4.37%, far below the expected 10.44 units / 21.9% for an on-resonance 52 ns, mod_depth 1 pulse.
- The mean observed contrast is -0.68%, meaning readout 2 is slightly higher than the reference on average rather than lower.
- A fixed-amplitude resonance model with the expected 22% contrast scale gives a worse residual error than a flat no-resonance model: best present-model SSE = 0.05523 versus absent-model SSE = 0.01570.
- Allowing the resonance amplitude to fit freely gives a best amplitude of -0.047, i.e. the opposite sign of the expected pODMR dip.

Decision:
The expected resonant feature for the active pulse should be a large, broad readout-2 dip relative to the first readout. The measured readout ratios do not show such a feature, and the quantitative model comparison favors no resonance. I therefore decide that a pODMR resonance is absent.
