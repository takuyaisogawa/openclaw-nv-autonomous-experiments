Case: podmr_077_2026-05-17-100811

I used only the supplied sequence XML and raw export for this decision.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is not active.
- Readout 1 is the "true 0 level reference": adj_polarize followed by detection.
- Readout 2 is the detection after the active rabi_pulse_mod_wait_time block.
- mod_depth = 1 in the provided XML and exported variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounding statement keeps it at 13 samples = 52 ns.

Quantitative model:

The setup facts give a contrast scale C = 0.22 between m_S = 0 and m_S = +1, and a Rabi frequency f_R = 10 MHz at mod_depth = 1. For a square pulse of length T = 52 ns, I modeled the excited-state population versus detuning d as

P(d) = f_R^2 / (f_R^2 + d^2) * sin^2(pi * T * sqrt(f_R^2 + d^2)).

The expected normalized post-pulse readout is then approximately

R(d) = 1 - C * P(d).

At d = 0, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961, so a resonance should give R(0) = 1 - 0.22 * 0.9961 = 0.7809. With the observed reference mean of 50.94 raw counts, this corresponds to an expected on-resonance drop of about 11.16 raw counts. At one 5 MHz scan step away, the same model gives P = 0.7488 and R = 0.8353, still a large dip.

Observed data:
- Mean readout 1: 50.94
- Mean readout 2: 50.77
- Mean normalized readout2/readout1: 0.9970
- Minimum normalized readout2/readout1: 0.9578 at the first scan point
- Largest raw decrease readout2 - readout1: -2.19 counts

I also fit the normalized data to the same pulse response shape, y = baseline - A * P(d), scanning possible resonance centers. The best unconstrained amplitude was A = 0.0347, far below the expected physical contrast A = 0.22. The flat baseline sum of squared residuals was 0.01100, while the best pulse-shape fit was 0.00924, only a small improvement and with an amplitude about 16 percent of the expected resonant contrast. The stored per-average traces differ enough to reflect tracking or drift cadence, so I did not treat the two averages as a strong independent repeatability test.

Decision:

A real pODMR resonance under this active sequence should produce a deep, pulse-shaped reduction in the post-pulse readout, close to a 22 percent normalized contrast at resonance. The observed data show only small few-percent fluctuations and no compatible resonant dip. I therefore decide resonance_absent.
