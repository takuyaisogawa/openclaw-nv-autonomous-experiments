<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_085

Input sequence and active roles:
- Sequence: Rabimodulated.xml / Rabimodulated.
- Sweep variable: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- Active detections are therefore:
  - readout 1: detection immediately after adj_polarize, the bright mS = 0 reference.
  - readout 2: detection after a single rabi_pulse_mod_wait_time pulse, the pODMR signal channel.
- mod_depth = 1 from the provided sequence XML and exported variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate; this is already exactly 13 samples.

Physical model calculation:
For a square microwave pulse, using the supplied setup facts,
  f_R = 10 MHz * mod_depth = 10 MHz
  P_transfer(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau)
with tau = 52 ns. On resonance,
  P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
The contrast scale between mS = 0 and mS = +1 is about 22%, so the expected resonant fractional drop in readout 2 relative to readout 1 is
  0.22 * 0.996 = 0.219.
The observed readout 1 baseline is 49.459 counts, so an on-resonance point should be near
  49.459 * (1 - 0.219) = 38.621 counts,
or about 10.84 counts below the reference.

Observed data comparison:
- readout 1 mean/std/min/max: 49.459 / 1.744 / 44.769 / 51.558.
- readout 2 mean/std/min/max: 49.448 / 1.543 / 45.365 / 51.885.
- readout2 - readout1 mean/std/min/max: -0.011 / 1.469 / -2.788 / +2.712.
- readout2/readout1 mean/std/min/max: 1.0004 / 0.0296 / 0.9457 / 1.0572.
- The deepest observed post-pulse drop is only 2.79 counts at 3.860 GHz, about 5.4%, far smaller than the expected 10.84 count / 21.9% resonant drop.

Model fit check:
Using the fixed 22% contrast square-pulse model over possible resonance centers in the scanned band gives worse squared error than the no-resonance null model:
  null y2 = y1 SSE = 45.33
  best fixed-contrast resonance SSE = 229.17
Allowing the model amplitude to float gives a best amplitude of -0.0256, i.e. the wrong sign for pODMR contrast, with only a small SSE improvement from noise fitting:
  best free-amplitude SSE = 41.94

Decision:
The expected pODMR signature for this sequence is a broad, large reduction of the post-pulse readout relative to the mS = 0 reference. The measured signal stays essentially equal to the reference and does not show the expected drop. I classify this case as resonance_absent.
