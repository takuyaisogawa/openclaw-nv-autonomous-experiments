Case: podmr_030_2026-05-13-160024

Inputs used: inputs/sequence.xml for the active pulse sequence and inputs/raw_export.json for the raw readouts. I did not use labels, sibling cases, previous outputs, or external context.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive even though do_adiabatic_inversion is true.
- readout 1 is the detection immediately after adj_polarize, so it is the true mS = 0 fluorescence reference.
- readout 2 is the detection after rabi_pulse_mod_wait_time, so it is the pODMR signal readout.
- mod_depth = 1 from the provided sequence XML and the active variable values.
- length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns.

Physical model calculation:
The setup contrast scale between mS = 0 and mS = +1 is C = 0.22. The Rabi frequency is f_R = 10 MHz * mod_depth = 10 MHz. For a rectangular pulse, the driven transition probability at detuning Delta is

P(Delta) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz and t = 52 ns. On resonance this gives

P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The expected resonant fluorescence contrast in readout 2 relative to readout 1 is therefore C * P(0) = 0.219, i.e. readout 2 should drop to about 0.781 of readout 1. With the observed mean readout 1 level of 27.37 counts, the expected resonant drop is about 6.00 counts. Because the scan step is 5 MHz and the Rabi frequency is 10 MHz, a resonance anywhere inside the swept interval should still produce a large nearby point; the model gives a near-resonant darkening of order 20 percent, not a sub-percent effect.

Observed normalized contrast:
I computed c_i = 1 - readout2_i/readout1_i. The mean contrast is -0.0146 and the standard deviation across the sweep is 0.0581. The largest positive contrast is only 0.0825, corresponding to a 2.26 count drop at 3.860 GHz. Several points have negative contrast, meaning the signal readout is brighter than the reference. There is no contiguous dip with the expected 0.219 contrast.

Model fit check:
- A flat no-resonance model c_i = constant gives SSE = 0.0674.
- A fixed physical resonance model with 22 percent contrast and center constrained inside the scan gives best SSE = 0.1227, worse than flat.
- Letting the resonance amplitude float while keeping the same pulse-response line shape gives best amplitude A = -0.040, i.e. a small brightening rather than the expected positive darkening.
- If the fixed 22 percent model is allowed to move outside the scan, its best fit shifts outside the measured window to avoid placing a strong dip in the data.

Decision:
The expected signal from the active 52 ns, mod_depth = 1 Rabi pulse is a roughly 22 percent darkening of readout 2 near resonance. The measured readout ratio shows only small, non-reproducible fluctuations and the quantitative pulse-response fit rejects a resonance inside the sweep. I therefore classify this case as resonance_absent.
