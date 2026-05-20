Case: podmr_008_2026-05-11-131831

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is the true ms=0 reference: adj_polarize followed immediately by detection before the Rabi pulse.
- Readout 2 is the signal readout after rabi_pulse_mod_wait_time followed by detection.
- The active Rabi pulse uses length_rabi_pulse = 52 ns. At sample_rate = 250 MS/s this is 13 samples, so rounding leaves it at 52 ns.
- The XML value for mod_depth is 1.

Quantitative physical model:
The setup contrast between ms=0 and ms=+1 is about 22%. The Rabi rate is about 10 MHz at mod_depth = 1. For a square pulse, the population transfer versus detuning is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

with f_R = 10 MHz and tau = 52 ns. On resonance,
P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

The expected normalized fluorescence drop on resonance is therefore
0.22 * 0.9961 = 0.219, or about 21.9%.

The expected line is also several scan points wide at the 5 MHz spacing:
- detuning 0 MHz: expected contrast 21.9%
- detuning 5 MHz: expected contrast 16.5%
- detuning 10 MHz: expected contrast 6.0%
- detuning 15 MHz: expected contrast 0.3%

Measured normalized contrast:
I used c = (readout1 - readout2) / readout1, since readout1 is the in-sequence ms=0 reference and the stored averages show tracking-scale drift rather than independent repeatability.

Across the 21 scan points:
- mean c = 1.22%
- standard deviation of c = 5.53%
- maximum c = 11.85% at 3.840 GHz
- minimum c = -6.15%

I fit the normalized contrast to a linear baseline plus the expected Rabi line shape:

c(f) = b0 + b1 * f + A * P(f - f0)

The best fit over f0 in the scan range gave:
- f0 = 3.83955 GHz
- A = 0.0707 +/- 0.0497
- baseline-only residual RMS = 5.38%

This fitted amplitude is far below the expected A ~= 0.22 for a real resonance in this sequence and is only about 1.4 sigma from zero. Forcing the expected A = 0.22 made the residual sum of squares 34% worse than the no-resonance linear baseline. The largest measured contrast point also lacks the required neighboring 5 MHz points near 16% contrast.

Decision:
The active pulse should produce a large, broad, approximately 22% normalized dip if a pODMR resonance is present. The data show only small noisy readout-ratio fluctuations, no line shape matching the expected Rabi response, and no quantitatively supported resonance amplitude. I therefore classify this case as resonance_absent.
