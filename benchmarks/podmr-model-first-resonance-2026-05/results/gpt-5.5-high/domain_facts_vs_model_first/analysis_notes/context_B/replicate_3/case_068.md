Case: podmr_054_2026-05-17-043636

Sequence read from inputs/sequence.xml / exported Rabimodulated.xml:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is disabled.
- Readout 1 role: detection immediately after adj_polarize, therefore the true m_S = 0 reference.
- Readout 2 role: detection after rabi_pulse_mod_wait_time, therefore the post-microwave signal readout.
- mod_depth = 1 from the provided sequence values.
- Microwave pulse duration length_rabi_pulse = 52 ns after sample-rate rounding.

Physical model calculation:
The setup contrast between m_S = 0 and m_S = +1 is about C = 0.22. The Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant square pulse of duration t = 52 ns, the expected transition probability is

P(0) = sin^2(pi * f_R * t)
     = sin^2(pi * 10e6 * 52e-9)
     = 0.996.

Thus a resonance should reduce readout 2 relative to readout 1 by C * P(0) = 0.219, about a 21.9% dip. With the observed readout-1 mean of 42.52 counts, the expected on-resonance drop is about 9.32 counts.

For finite detuning I used the standard driven two-level square-pulse model:

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

At detunings 0, 2.5, 5, and 10 MHz, the expected optical contrasts are approximately 21.9%, 20.4%, 16.5%, and 6.0%, respectively. Since the scan step is 5 MHz, a resonance inside the scanned interval should produce a large, broad, resolved deficit in readout 2 over at least one point and likely nearby points.

Observed data:
- Mean readout 1 = 42.52 counts.
- Mean readout 2 = 42.27 counts.
- Mean contrast (readout1 - readout2) / readout1 = 0.55%.
- Maximum observed positive contrast = 5.32%.
- Minimum observed contrast = -5.59%.
- Contrast standard deviation across scan points after removing the mean = 2.76%.

The observed maximum deficit is far smaller than the expected 21.9% resonant contrast and is comparable to the point-to-point scatter. A least-squares scan of the Rabi model with fixed 22% contrast is very poor when the resonance center is constrained inside the scanned interval (best SSE 0.088 without an offset, 0.066 with an offset, versus null SSE 0.015). The only fixed-contrast fit competitive with the null places the center outside the scan, where it predicts little in-range signal. Allowing the amplitude to float gives only about 4.1% contrast, far below the physically expected amplitude for this sequence and mod_depth.

Decision:
The active sequence would make a real pODMR resonance large and directly visible as readout 2 dropping below the m_S = 0 reference. The measured readout difference does not show that expected signal. I therefore classify this case as resonance_absent.
