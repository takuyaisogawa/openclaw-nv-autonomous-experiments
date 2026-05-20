Case: podmr_075_2026-05-17-093901

Active sequence identification:
- Sequence: Rabimodulated.xml.
- Swept parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the intermediate "Acquire 1 level reference" block is inactive.
- Readout 1 role: after adj_polarize, before any Rabi pulse, therefore the m_S = 0 fluorescence reference.
- Readout 2 role: after the active rabi_pulse_mod_wait_time call, therefore the pODMR signal readout.
- mod_depth = 1 from the provided sequence XML/variable values.
- Active pulse duration: length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already an integer 13 samples, so rounding does not change it.

Quantitative physical model:
Use a rectangular driven two-level Rabi model for the population transferred out of m_S = 0:

P(+1) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau)

where Omega / (2*pi) = 10 MHz * mod_depth = 10 MHz and tau = 52 ns. On resonance:

P_on = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.

With the stated setup contrast scale of 22% between m_S = 0 and m_S = +1, an on-resonance pODMR signal should be approximately:

signal/reference = 1 - 0.22 * P_on = 0.781.

This corresponds to a roughly 21.9% dip of readout 2 relative to readout 1. For reference, the same model gives expected signal/reference ratios of about 0.835 at 5 MHz detuning, 0.940 at 10 MHz detuning, and 0.989 at 20 MHz detuning.

Data check:
- Mean readout 1 = 50.523 counts.
- Mean readout 2 = 50.390 counts.
- Mean readout2 - readout1 = -0.133 counts.
- Measured readout2/readout1 ratios range from 0.951 to 1.048.
- The lowest measured ratio is 0.951 at 3.830 GHz, a 4.9% relative dip, far smaller than the expected 21.9% on-resonance dip.
- After a linear trend removal from the ratio data, the largest negative residual is about -0.043, also far below the expected resonant signature.
- The per-average overlays show comparable scatter and drift, and the two stored averages are more consistent with tracking cadence than with an independent repeatability test.

Decision:
The active sequence should produce a large post-pulse fluorescence decrease if the scanned range contains a pODMR resonance. The observed readout2/reference ratios show only small fluctuations and slow drift, with no feature approaching the expected modeled contrast. Therefore I classify this scan as resonance_absent.
