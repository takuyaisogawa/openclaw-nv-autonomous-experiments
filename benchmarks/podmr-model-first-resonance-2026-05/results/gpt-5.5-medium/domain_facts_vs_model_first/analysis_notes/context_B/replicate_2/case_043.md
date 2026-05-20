Case: podmr_029_2026-05-16-193002

I used the provided sequence XML to identify the active experiment as `Rabimodulated.xml`, a scan of `mw_freq` from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse after initialization is:

`rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)`

with `length_rabi_pulse = 52 ns` and `mod_depth = 1`. The sequence has `full_expt = 0`, so the "Acquire 1 level reference" block is inactive. The two recorded detections are therefore:

- readout 1: true `m_S = 0` reference immediately after polarization
- readout 2: signal readout after the modulated Rabi pulse

Physical model calculation:

For a driven two-level transition, I used

`P_flip(f; f0) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * sqrt(f_R^2 + detuning^2) * t)`

where `f_R = 10 MHz * mod_depth`, `t = 52 ns`, and detuning is in Hz. The expected signal readout at resonance is

`S = R0 * (1 - C * P_flip)`

with setup contrast `C = 0.22` and measured baseline `R0 ~= 44.92 counts`.

For `mod_depth = 1`, `f_R = 10 MHz`. On resonance:

`P_flip = sin^2(pi * 10e6 * 52e-9) = 0.996`

so the expected resonant contrast is `0.22 * 0.996 = 0.219`, or a loss of about `9.84 counts` from the measured baseline. A pODMR resonance in this sequence should therefore show readout 2 falling to roughly `35.1 counts` relative to a `~44.9 count` reference.

Measured comparison:

The combined data have

- mean readout 1: `44.929`
- mean readout 2: `44.908`
- mean `(readout 2 - readout 1)`: `-0.021 counts`
- standard deviation of `(readout 2 - readout 1)`: `1.273 counts`
- most negative point in `(readout 2 - readout 1)`: `-2.558 counts`

Thus the largest observed signal loss is only about 26% of the expected resonant loss for the provided XML parameters, and the average signal is essentially unchanged from the reference.

I also compared the full scan to the detuned Rabi line shape. With the expected fixed contrast and `mod_depth = 1`, the best resonance-center fit gave `SSE = 182.88`, much worse than a flat/no-resonance model with `SSE = 32.39`. Letting the amplitude float gave a best-fit amplitude of `+2.33 counts`, opposite the expected negative pODMR dip (`-9.88 counts`). As a sensitivity check, even a lower `mod_depth = 0.3` would predict only a `2.19 count` dip, but the provided XML parameters and exported variable values specify `mod_depth = 1`; the fixed `mod_depth = 1` model is the relevant decision basis.

Decision: resonance_absent. The measured readout 2 trace does not contain the expected resonance-shaped negative contrast relative to readout 1.
