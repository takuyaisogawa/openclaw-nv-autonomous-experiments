Case: podmr_078_2026-05-17-102220

Sequence interpretation:

- The provided XML is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active variables from the provided XML: length_rabi_pulse = 5.2e-08 s, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0.
- The Rabi pulse duration is rounded by round(length_rabi_pulse * sample_rate) / sample_rate. With 52 ns and 250 MHz sampling this is exactly 13 samples, so the active duration remains 52 ns.
- Because full_expt = 0, the optional m_S = +1 reference block is skipped.
- The two active detections are therefore:
  1. readout 1: polarized m_S = 0 reference after adj_polarize and detection.
  2. readout 2: signal after the Rabi-modulated microwave pulse and detection.

Physical model calculation:

The setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Here mod_depth = 1, so f_R = 10 MHz. For a resonant square pulse, the transferred population is

P_1 = sin^2(pi * f_R * t).

Using t = 52 ns:

pi * f_R * t = pi * 10e6 * 52e-9 = 1.6336 rad
P_1 = sin^2(1.6336) = 0.996.

Thus an on-resonance point should be almost a pi-pulse transfer from m_S = 0 toward m_S = +1. With the stated contrast scale of about 22%, and an observed m_S = 0 readout level near mean(readout 1) = 51.83 counts, the expected resonant drop in readout 2 relative to the m_S = 0 reference is approximately

51.83 * 0.22 * 0.996 = 11.36 counts.

So a resonance in this sweep should produce readout 2 near 40.5 counts at or near resonance, allowing for the finite-width Rabi lineshape.

Observed data:

- readout 1 mean = 51.83 counts, population standard deviation across scan points = 1.06 counts.
- readout 2 mean = 51.76 counts, population standard deviation across scan points = 1.18 counts.
- readout 2 - readout 1 has mean = -0.071 counts, standard deviation = 1.15 counts.
- The most negative observed readout 2 - readout 1 point is -1.60 counts at 3.905 GHz.

This largest observed deficit is only about 14% of the expected resonant drop, and the trace does not show a localized 22%-scale pODMR dip. Stored averages are only two and can reflect tracking cadence, so I do not treat the per-average overlay as a strong independent repeatability test. The primary combined readout comparison is inconsistent with the expected near-pi-pulse pODMR signal.

Decision: resonance_absent.
