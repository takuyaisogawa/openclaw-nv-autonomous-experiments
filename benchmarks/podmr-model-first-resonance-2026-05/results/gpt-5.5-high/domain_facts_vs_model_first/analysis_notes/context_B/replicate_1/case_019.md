Case: podmr_004_2026-05-16-005019

Sequence interpretation:
- The provided sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active microwave pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.
- mod_depth = 1 from the provided sequence XML and exported variable values.
- full_expt = 0, so the optional m_S=+1 reference block is inactive.
- Readout 1 is the optically pumped m_S=0 reference immediately after adj_polarize.
- Readout 2 is the signal after the modulated Rabi pulse.

Physical model calculation:
- Given setup contrast C = 0.22 and Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a rectangular microwave pulse, the transition probability versus detuning is
  P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau),
  with Omega = 2*pi*10 MHz and tau = 52 ns.
- On resonance, f_R * tau = 10e6 * 52e-9 = 0.52 cycles, giving
  P(0) = sin^2(pi * 0.52) = 0.996.
- Expected fluorescence ratio on resonance is therefore approximately
  1 - C*P(0) = 1 - 0.22*0.996 = 0.781.

Observed quantitative comparison:
- The combined readout-2/readout-1 ratio has an off-resonance outer-point mean of about 0.983.
- The minimum ratio is 31.8077 / 40.4231 = 0.7869 at 3.880 GHz.
- Relative to the off-resonance ratio, the observed dip depth is (0.983 - 0.7853) / 0.983 = 0.201, close to the expected 0.22 contrast for a near-pi pulse.
- A least-squares rectangular-pulse model with fixed C = 0.22, f_R = 10 MHz, and tau = 52 ns fits the ratio data with center frequency about 3.8776 GHz and scale about 0.991.
- Model predicted ratios at the two deepest sampled points are about 0.7898 at 3.875 GHz and 0.7875 at 3.880 GHz, matching the observed 0.7853 and 0.7869.

Decision:
The second readout has a frequency-localized dip of the correct sign, depth, and width for the active near-pi Rabi pulse, while the m_S=0 reference readout remains comparatively flat. This is a pODMR resonance.
