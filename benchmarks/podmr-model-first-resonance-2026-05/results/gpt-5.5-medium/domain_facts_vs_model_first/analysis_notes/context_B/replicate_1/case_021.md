<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_021

I used only the provided sequence XML and raw readout export. The active sequence is Rabimodulated.xml. The instructions first polarize the NV and perform a detection, then because full_expt = 0 the optional mS=1 reference block is skipped. The sequence then applies one rabi_pulse_mod_wait_time pulse and performs the second detection. Therefore readout 1 is the polarized mS=0 reference readout, and readout 2 is the signal after the microwave pulse. The active pulse settings are length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model:

- Setup contrast scale between mS=0 and mS=+1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: t = 52 ns.
- For a resonant square pulse, the transition probability is P = sin^2(pi f_R t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected resonant fluorescence drop relative to the mS=0 reference is C * P = 0.22 * 0.996 = 0.219, or about 21.9%.

Observed data:

- The deepest combined point is at 3.880 GHz, with readout 1 = 40.192 and readout 2 = 30.788.
- The readout-2/readout-1 ratio there is 0.766, corresponding to a 23.4% drop relative to the same-point mS=0 reference.
- Using off-central points as a crude baseline gives readout 2 baseline = 38.441 and a minimum drop of 7.653 counts, while the model expectation is 38.441 * 0.219 = 8.424 counts.
- A simple negative Lorentzian dip fit to readout 2 improves SSE from 124.4 for a constant model to 24.8, with center about 3.8782 GHz, half-width about 5.2 MHz, and fitted dip amplitude about 9.24 counts.
- Both stored averages show the central readout-2 dip near 3.875-3.880 GHz, but I treat this only as consistency because stored averages can reflect tracking cadence.

Decision:

The observed central pODMR dip has the expected sign, frequency-localized shape, and magnitude for a near-pi pulse under the active sequence. The expected 21.9% fluorescence loss and the observed 23.4% loss agree closely. I decide that a pODMR resonance is present.
