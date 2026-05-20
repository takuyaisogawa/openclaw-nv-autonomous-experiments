Case: podmr_002_2026-05-16-002114

Inputs used:
- sequence.xml and the embedded scan export both identify the active sequence as Rabimodulated.xml.
- Active scan variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Pulse parameters from the provided sequence XML / variable values: length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0.

Readout roles:
- The first detection occurs immediately after adj_polarize, before any Rabi pulse, so readout 1 is the optically polarized m_S = 0 reference / tracking readout.
- The m_S = +1 reference block is gated by if abs(full_expt)>1e-12, and full_expt = 0, so no independent +1 reference is acquired.
- The second detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so readout 2 is the pODMR signal readout.

Quantitative expected-signal model:
- Given setup fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- Here mod_depth = 1, so f_Rabi = 10 MHz.
- For a resonant square pulse, spin-flip probability P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant frequency should reduce the signal readout by about 0.22 * 0.996 = 21.9% relative to off-resonant signal.
- Using readout 2 off-resonance baseline about 36.8 raw units, expected resonant value is 36.8 * (1 - 0.219) = 28.7 raw units, an expected drop of about 8.1 raw units.

Observed data:
- Combined readout 2 has a clear dip centered near 3.875-3.880 GHz, with minimum 26.96 at 3.880 GHz.
- Excluding the dip window, readout 2 baseline is about 36.53, so the observed drop is about 9.56 raw units, or 26.2%.
- The two stored averages both show the same dip at the minimum index: drops about 9.0 and 10.1 raw units relative to their own off-window baselines. These averages are not treated as a strong independent repeatability test, only as consistency with the tracking cadence.
- Readout 1 at the readout 2 minimum is 38.12, about 0.64 above its own off-window/reference baseline, so the dip is not mirrored in the m_S = 0 reference readout.

Decision:
The expected resonant pODMR signal for the active pulse sequence is a large drop in the second readout of roughly 8 raw units. The observed second-readout dip is centered in the scan, has the correct magnitude, and is not present in the first reference readout. Therefore a pODMR resonance is present.
