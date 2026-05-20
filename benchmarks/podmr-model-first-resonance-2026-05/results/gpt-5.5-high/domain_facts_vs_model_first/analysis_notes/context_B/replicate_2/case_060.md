Case: podmr_046_2026-05-16-235726

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- Varying parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and immediately call detection. This is readout 1, the true mS = 0 reference.
- full_expt = 0, so the optional mS = +1 reference block is inactive.
- The instructions then apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection. This is readout 2, the pODMR signal after the microwave pulse.
- Pulse duration: length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz.
- mod_depth: 1 from the active variable values/provided XML.

Quantitative physical model:
For a square microwave pulse on a two-level transition, the mS = +1 population after a pulse is

P1(delta) = (fR^2 / (fR^2 + delta^2)) * sin^2(pi * sqrt(fR^2 + delta^2) * tau),

using frequencies in cycles/s. The supplied setup calibration gives fR = 10 MHz * mod_depth = 10 MHz. With tau = 52 ns,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between mS = 0 and mS = +1 is about 22%, so an on-resonance point should reduce readout 2 relative to readout 1 by approximately 0.22 * 0.996 = 21.9%. With the measured mean readout 1 of 52.16 counts, the expected resonant readout 2 would be about 40.73 counts, a drop of about 11.43 counts.

Observed data comparison:
- Mean readout 1: 52.16 counts.
- Mean readout 2: 51.12 counts.
- Mean readout1 - readout2: 1.03 counts.
- Deepest observed readout2/readout1 ratio: 0.914 at 3.860 GHz.
- Expected on-resonance ratio from the model: about 0.781.
- Largest observed drop: 4.60 counts, far below the expected 11.43 count resonant drop.

I also compared the measured readout2/readout1 ratios to the square-pulse lineshape over possible resonance centers in the scanned range. A flat-ratio model has SSE = 0.01799. The fixed 22% contrast square-pulse model, allowing the baseline ratio and resonance center to vary, has best SSE = 0.06267, worse than flat by a factor of 3.48. An unconstrained lineshape fit does not recover a positive ODMR dip; its best dip coefficient is negative, corresponding to a weak peak rather than the expected depletion.

Decision: the expected pODMR resonance should be a large, near-pi-pulse depletion in readout 2 relative to the mS = 0 reference. The measured data show only small tracking-scale fluctuations and no compatible 22% square-pulse resonance feature. Therefore I decide resonance_absent.
