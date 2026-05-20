Active sequence interpretation:

- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active branch has full_expt = 0, so the optional "Acquire 1 level reference" branch is skipped.
- Readout 1 is the "true 0 level reference": optical polarization followed immediately by detection.
- Readout 2 is the signal readout after the modulated Rabi pulse and detection.
- Active pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The 250 MHz sample rate gives a 4 ns clock and 52 ns is exactly 13 samples.

Quantitative expected signal model:

For a resonant square pulse, using the provided setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. The transition probability after pulse length t is

P0 = sin^2(pi * f_R * t).

With f_R = 10 MHz and t = 52 ns:

f_R * t = 0.52
P0 = sin^2(pi * 0.52) = 0.996.

The current m_S = 0 to m_S = +1 contrast scale is about 22%, so an on-resonance pODMR response should reduce the post-pulse readout relative to the m_S = 0 reference by

0.22 * 0.996 = 0.219, or about 21.9%.

At the observed readout-1 mean of 52.16 counts, this corresponds to an expected resonance drop of about 11.43 counts, giving a signal near 40.73 counts at line center.

Using the detuned Rabi model

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz, a real resonance within the scan should create a broad, structured dip in readout 2/readout 1 with a minimum ratio near 0.781 at line center.

Observed data comparison:

- Mean readout 1: 52.16 counts.
- Mean readout 2: 51.12 counts.
- Mean readout2/readout1 ratio: 0.981.
- Minimum readout2/readout1 ratio: 0.914, equivalent to only 8.6% contrast.
- The observed minimum drop is less than half of the expected 21.9% resonant drop.
- The low points are not a convincing detuned-Rabi line shape; an unconstrained fit to the resonance-shaped model gives the best amplitude with the wrong sign rather than a positive ODMR dip.
- Stored averages show fluctuations and drift-like changes, but they are not a strong independent repeatability test here and do not rescue the missing expected contrast-scale signal.

Decision:

Given the active pulse should be nearly a pi pulse at mod_depth = 1, the expected pODMR resonance signal is large. The measured normalized contrast never approaches the expected scale and does not show a coherent resonance-shaped dip. I therefore decide that a pODMR resonance is absent in this scan.
