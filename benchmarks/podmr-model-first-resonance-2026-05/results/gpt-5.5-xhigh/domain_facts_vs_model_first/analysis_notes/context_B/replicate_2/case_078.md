Case podmr_064_2026-05-17-065956

Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first runs adj_polarize and detection, so readout 1 is the bright m_S = 0 reference. full_expt is 0, so the optional one-level reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time followed by detection, so readout 2 is the pODMR signal after the microwave/Rabi pulse.

Relevant pulse parameters from the provided XML/exported variable values:
- length_rabi_pulse = 52 ns
- mod_depth = 1
- sample_rate = 250 MHz, so the 52 ns duration is rounded to 13 samples and remains 52 ns

Physical model calculation

Using the stated setup calibration, the on-resonance Rabi frequency is about 10 MHz at mod_depth = 1. I modeled the rectangular microwave pulse transition probability as

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz, t = 52 ns, and detuning delta in Hz. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

The stated bright-to-dark contrast scale is about 22%, so the expected fractional signal drop at resonance is

0.22 * 0.996 = 0.219, or about 21.9%.

The measured bright reference mean is 50.973 raw counts, so a resonant point should be lower by about

50.973 * 0.219 = 11.17 raw counts.

The same model gives expected signal drops at nearby detunings:
- 2.5 MHz detuning: P = 0.929, expected drop = 20.4%, about 10.42 counts
- 5.0 MHz detuning: P = 0.749, expected drop = 16.5%, about 8.40 counts
- 10.0 MHz detuning: P = 0.273, expected drop = 6.0%, about 3.06 counts

Because the scan step is 5 MHz, any resonance inside the scan range should place at least one sampled point within 2.5 MHz of resonance, giving an expected drop of roughly 10 counts, and adjacent points should also show a broad depression.

Observed data comparison

The combined readout means are:
- readout 1 mean = 50.973
- readout 2 mean = 50.921

The deepest observed readout 2 point is 49.269 at 3.900 GHz, only 1.635 counts below the readout 2 median. The most negative normalized signal, readout2/readout1 - 1, is -5.38% at 3.890 GHz. This is much smaller than the expected about -21.9% resonant response, and it is not a coherent rectangular-pulse line shape across neighboring scan points.

A grid fit of the normalized data to baseline minus A * P(delta) found the best unconstrained amplitude to be negative, corresponding to a peak-like feature at the scan edge rather than a dip. A fixed 22% amplitude resonance model had SSE = 0.03882, worse than a flat normalized baseline with SSE = 0.01431.

Decision

Given the active sequence, readout 2 should show a large microwave-induced fluorescence dip if a pODMR resonance is present. The expected dip is about 10 to 11 raw counts at the nearest sampled point, while the observed fluctuations are only a few counts and do not match the modeled line shape. I therefore decide that a pODMR resonance is absent.
