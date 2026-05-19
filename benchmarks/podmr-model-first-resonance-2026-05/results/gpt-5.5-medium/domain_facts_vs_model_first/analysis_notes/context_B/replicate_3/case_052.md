<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_052

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion = 1.
- Readout 1 role: fluorescence after adj_polarize and detection, i.e. true m_S = 0 reference.
- Readout 2 role: fluorescence after the active rabi_pulse_mod_wait_time pulse and detection, i.e. pODMR signal.
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at sample_rate = 250 MHz to 52 ns.

Expected signal model:
For a rectangular microwave pulse, the transition probability versus detuning is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

using frequencies in cycles/s. The setup gives f_R about 10 MHz at mod_depth = 1, and t = 52 ns. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected normalized fluorescence loss at resonance is

C * P(0) = 0.22 * 0.996 = 0.219

Thus a real pODMR resonance driven by this near-pi pulse should produce roughly a 22% dip in readout 2 relative to readout 1 at the resonant frequency, corresponding to about 10 raw-count units for a 46-count reference. The finite-pulse model predicts a strong central feature across the 5 MHz sampled grid if the resonance lies in the scan range.

Data reduction:
The combined readout ratios readout2/readout1 have mean 0.9930 and standard deviation 0.0251. The largest positive normalized loss, 1 - readout2/readout1, is only 0.0599 at 3.845 GHz; several points have negative apparent loss where readout 2 is brighter than readout 1. At 3.875 GHz, the loss is only 0.0051. No point approaches the expected 0.219 on-resonance loss.

A fixed physical model using f_R = 10 MHz, t = 52 ns, and contrast = 0.22 was scanned over possible resonance centers. Allowing only a constant baseline offset, the best resonance-shaped model gives only a small SSE improvement over a flat-contrast null model and places its best center outside the measured span near 3.804 GHz, driven by minor low-frequency fluctuations rather than a central pODMR dip. A resonance inside the measured scan would require a much larger, localized reduction in readout 2 than is observed.

Stored averages show broad offsets between the two average blocks, consistent with tracking or cadence drift, and are not treated as an independent repeatability test. The combined data and the explicit pulse-response calculation do not support a pODMR resonance in this scan.

Decision: resonance_absent.
