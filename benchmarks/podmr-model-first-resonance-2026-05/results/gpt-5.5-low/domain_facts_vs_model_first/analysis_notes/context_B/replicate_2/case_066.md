Case: podmr_052_2026-05-17-015447

Sequence identification:
- The active sequence in the export is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- The executed readouts are therefore:
  1. readout 1: post-laser bright m_S = 0 reference before the microwave pulse.
  2. readout 2: signal after the modulated Rabi microwave pulse.
- length_rabi_pulse = 52 ns.
- mod_depth = 1.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a square resonant pulse, population transfer probability is
  P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With optical contrast scale C = 0.22 between m_S = 0 and m_S = +1, the expected resonant fractional signal drop in readout 2 relative to readout 1 is
  C * P = 0.219, or about 21.9%.
- Around a true resonance, the finite pulse model would produce a localized dip in readout2/readout1 over a bandwidth of order 1/t, about 19 MHz, with the central point approaching this contrast scale if the resonance is sampled.

Data comparison:
- Mean readout 1 = 27.413.
- Mean readout 2 = 26.974.
- Mean fractional drop 1 - readout2/readout1 = 0.015.
- Largest measured fractional drop is 0.100 at 3.925 GHz, at the edge of the scan.
- Several scan points have negative drop, including -0.101 at 3.840 GHz.
- The observed readout2/readout1 variations are irregular and comparable to baseline drift/tracking effects seen in the stored averages.
- No point or local group approaches the expected 21.9% resonant drop, and the strongest apparent drop is an edge point rather than a localized resonance feature with the expected finite-pulse shape.

Decision:
The active pulse should create a large, localized post-pulse fluorescence dip if a pODMR resonance is present in the scan range. The measured normalized signal lacks that amplitude and line shape, so I decide resonance_absent.
