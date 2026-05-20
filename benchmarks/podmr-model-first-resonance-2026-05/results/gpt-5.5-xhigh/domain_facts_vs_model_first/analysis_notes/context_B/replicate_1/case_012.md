Case: podmr_030_2026-05-13-160024

Source restrictions: I used only the provided XML and raw export in this workspace.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the provided sequence XML, the instruction order is:
  1. adj_polarize, then detection.
  2. optional "1 level reference" block, but full_expt = 0 so this block is skipped.
  3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection.
- Therefore readout 1 is the polarized ms=0 reference. Readout 2 is the signal after the microwave Rabi pulse. There is no active ms=+1 reference readout in this sequence.
- The pulse used for the pODMR signal is length_rabi_pulse = 5.2e-08 s = 52 ns, mod_depth = 1. The sample rate is 250 MHz, so 52 ns corresponds to exactly 13 samples after rounding.

Quantitative expected-signal model:
- Given the supplied setup facts, the on-resonance Rabi frequency is about 10 MHz at mod_depth = 1.
- I modeled the pulse as a driven two-level square pulse with transition probability
  P(detuning) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * tau * sqrt(f_R^2 + detuning^2)),
  using f_R = 10 MHz and tau = 52 ns, with detuning in cycles/s.
- At zero detuning, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated optical contrast scale of 22%, the expected resonant fluorescence drop is 0.22 * 0.996 = 0.219, or 21.9% of the ms=0 reference.
- The mean readout-1 reference level is 27.37 raw units, so the expected resonant dip in readout 2 relative to readout 1 is about 5.997 raw units. A real resonance near a sampled point should therefore produce a large negative feature, with the neighboring points also affected by the finite pulse bandwidth.

Observed data comparison:
- Mean readout 1: 27.367.
- Mean readout 2: 27.729.
- Mean readout2/readout1 ratio: 1.0146.
- Standard deviation of readout2/readout1 over the scan: 0.0581.
- The most negative observed point is only -8.25% at 3.860 GHz, and it is isolated rather than the broad dip expected from the 52 ns near-pi pulse.
- Several points have positive readout2-readout1 excursions; the largest positive relative excursion is +12.34% at 3.895 GHz.

Model fit check:
- A flat normalized model has SSE = 0.0674 on the readout2/readout1 trace.
- Fitting the expected square-pulse lineshape with a free center frequency and nonnegative contrast amplitude gives best amplitude A = 0.0367, best center about 3.9128 GHz, and SSE = 0.0651. This is only a negligible improvement over flat and is far below the physically expected A about 0.22.
- Forcing the physically expected contrast amplitude A = 0.22 gives a worse fit, SSE = 0.1227.

Decision:
The active pulse should make a strong approximately 22% dip if it hits a pODMR resonance in this scan. The measured paired readout trace does not show that response, and the quantitative Rabi-lineshape fit finds only a small incoherent feature far below the expected signal. I decide resonance_absent.
