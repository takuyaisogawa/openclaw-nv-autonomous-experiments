Case podmr_033_2026-05-15-233800

Active sequence/readout roles:
- Sequence: Rabimodulated.xml / Rabi-modulated pODMR while sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect the bright reference, then skip the 1-level reference because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and detect again.
- Readout 1 is therefore the m_S = 0 bright reference after optical polarization.
- Readout 2 is the signal after the microwave pulse and is the resonance-sensitive readout.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth: 1 from the provided XML/scan variable values.

Quantitative model:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1 and linear scaling, the resonant Rabi frequency is 10 MHz.
- For a rectangular resonant pulse of duration tau = 52 ns, the spin-transfer probability is
  P = sin^2(pi * f_R * tau) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence reduction is
  0.22 * 0.996 = 0.219, or 21.9% of the bright reference.
- Around the main dip, readout 1/readout 2 are:
  - 3.870 GHz: 39.40 -> 35.33, drop 10.3%.
  - 3.875 GHz: 38.50 -> 28.83, drop 25.1%.
  - 3.880 GHz: 37.87 -> 31.04, drop 18.0%.
  - 3.885 GHz: 38.31 -> 34.90, drop 8.9%.
- The central dip is therefore the expected size for a near-pi resonant pulse, while off-resonance points are mostly near the bright reference.
- A simple rectangular-pulse detuning model,
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),
  with contrast 0.22 gives a much lower residual error than a flat readout-2 model when centered near 3.877 GHz (SSE about 34.8 versus 146.9 for a flat model).

Decision:
The physically expected signal for this sequence is a strong dip in readout 2 near resonance, with readout 1 remaining a bright reference. The measured dip near 3.875-3.880 GHz has the right amplitude and width for the 52 ns, mod_depth = 1 pulse. A pODMR resonance is present.
