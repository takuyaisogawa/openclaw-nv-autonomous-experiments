Case podmr_028_2026-05-16-185605

I used only the provided sequence XML and raw export. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first performs adj_polarize followed by detection, waits, skips the optional +1 reference because full_expt = 0, then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) and performs a second detection. Therefore readout 1 is the mS = 0 reference before the microwave pulse, and readout 2 is the pulse-dependent pODMR signal readout.

Relevant active pulse parameters from the provided XML:
- length_rabi_pulse = 5.2e-08 s = 52 ns
- mod_depth = 1
- sample_rate = 250 MHz, so the 52 ns pulse is rounded to 13 samples and remains 52 ns
- full_expt = 0, so no independent mS = +1 reference is acquired in this scan

Explicit model calculation:

For a square microwave pulse in a two-level approximation, the transferred population is

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

using cyclic frequencies. The provided domain scale gives f_R = 10 MHz at mod_depth = 1. With t = 52 ns,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between mS = 0 and mS = +1 is about 22%, so the expected resonant signal readout is

signal/reference = 1 - 0.22 * P1(0) = 0.781.

The measured readout 1 mean is 51.718 raw-count units, so an on-resonance near-pi pulse should produce a drop of

51.718 * 0.22 * 0.996 = 11.33 raw-count units.

The expected response is also not a single-point artifact at this Rabi rate. At offsets from resonance:
- 0 MHz: P1 = 0.996, expected drop = 11.33 counts
- 5 MHz: P1 = 0.749, expected drop = 8.52 counts
- 10 MHz: P1 = 0.273, expected drop = 3.11 counts
- 15 MHz: P1 = 0.0117, expected drop = 0.13 counts

Observed raw data:
- readout 1 mean = 51.718, population standard deviation across scan points = 1.100
- readout 2 mean = 51.570, population standard deviation across scan points = 0.972
- readout2 - readout1 mean = -0.148 counts
- readout2 - readout1 range = -2.981 to +2.596 counts
- readout2/readout1 mean = 0.9974
- minimum readout2/readout1 = 0.9446 at 3.885 GHz

Thus the largest observed signal deficit is about 5.5%, and the mean deficit is about 0.3%, whereas the physical model predicts an approximately 22% dip on resonance and about 16.5% one scan step away from resonance. A brute-force fit of the square-pulse line shape with the center varied gives an effective contrast amplitude of about 0.055 rather than the expected 0.22, and the trace lacks the required broad, deep depletion in readout 2 relative to readout 1.

Stored averages are only two and can reflect tracking cadence, so I do not treat their disagreement as an independent repeatability test. The decisive point is the mismatch between the expected near-pi-pulse pODMR contrast and the observed near-zero readout difference. I therefore decide that no pODMR resonance is present in this scan.
