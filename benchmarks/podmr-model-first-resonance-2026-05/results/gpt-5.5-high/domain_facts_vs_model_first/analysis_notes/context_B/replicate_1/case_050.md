Case: podmr_036_2026-05-16-211536

Sequence identification from inputs/sequence.xml:
- Active sequence file: Rabimodulated.xml.
- Scan variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Readout roles: readout 1 is the initial post-polarization detection, the true m_S = 0 reference. Because full_expt = 0, the optional m_S = +1 reference block is skipped. Readout 2 is the detection after the Rabi-modulated microwave pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Quantitative model:
- Given setup calibration: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For the active pulse, Omega_R = 10 MHz and t = 52 ns.
- Resonant population transfer probability for a square pulse:
  P = sin^2(pi * Omega_R * t)
    = sin^2(pi * 10e6 * 52e-9)
    = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant readout-2 fractional drop relative to the true-0 reference is:
  0.22 * 0.996 = 0.219, or about 21.9%.
- The readout-1 mean is 50.985 counts, so the expected resonant change is about:
  -0.219 * 50.985 = -11.17 counts.
- Including detuning for a two-level square pulse,
  P(Delta) = Omega_R^2 / (Omega_R^2 + Delta^2) * sin^2(pi * t * sqrt(Omega_R^2 + Delta^2)).
  Since the scan step is 5 MHz, a resonance anywhere between sampled scan points would be at most 2.5 MHz from a sampled point. At Delta = 2.5 MHz, this still gives P about 0.93, so the expected sampled dip would still be about 20% or about 10 counts.

Observed data calculation:
- Combined readout-1 mean: 50.985 counts.
- Combined readout-2 mean: 50.476 counts.
- Mean difference readout2 - readout1: -0.509 counts, about -1.0%.
- Standard deviation of pointwise differences: 1.360 counts.
- Most negative pointwise difference: -2.788 counts at 3.920 GHz, about -5.4%.
- Next endpoint at 3.925 GHz: -2.192 counts, about -4.2%.
- Some points have positive readout2 - readout1 differences, including +3.481 counts at 3.840 GHz.

Decision:
The observed differences are small, sign-changing, and at least a factor of about four below even the largest local dip expected from a resonant response under the active 52 ns, mod_depth = 1 pulse. A real pODMR resonance in this scan should produce an approximately 10 to 11 count readout-2 drop at one or more sampled frequencies. The data do not show that expected signal, so the resonance is absent.
