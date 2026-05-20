I used inputs/sequence.xml to identify the active measurement.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml / Rabimodulated pulse sequence.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is therefore the polarized m_S = 0 reference: adj_polarize -> detection.
- Readout 2 is the pODMR signal after the Rabi-modulated microwave pulse: rabi_pulse_mod_wait_time -> detection.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, 52 ns is exactly 13 samples, so rounding leaves it at 52 ns.

Quantitative physical model:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the active pulse has f_R = 10 MHz.
- For a square resonant pulse, transition probability is P = sin^2(pi f_R tau).
- With tau = 52 ns, P_res = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale C = 0.22 between m_S = 0 and m_S = +1, the expected signal/reference ratio on resonance is 1 - C * P_res = 0.7809, a 21.9 percent dip in readout 2 relative to readout 1.
- The scan step is 5 MHz. Even if the resonance center falls midway between two scan points, the nearest sampled detuning is 2.5 MHz. Using P(Delta) = f_R^2/(f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)), P(2.5 MHz) = 0.929, so any resonance inside the scan should produce at least a 20.4 percent sampled dip, ratio <= 0.7956.

Observed combined readouts:
- Frequencies span 3.825 to 3.925 GHz in 5 MHz steps.
- The combined readout-2/readout-1 ratios have mean 0.9834, minimum 0.9435, and maximum 1.0216.
- The largest observed drop below the reference is therefore only 5.65 percent, at 3.830 GHz, much smaller than the >=20.4 percent expected from the active pulse if a resonance were sampled.
- Around 3.880 GHz, a centered physical resonance would predict ratio 0.7809, but the observed ratio is 0.9869.

Model comparison:
- A linear baseline-only fit to the measured ratios gives SSE = 0.00881 and RMSE = 0.0205.
- Forcing the physical resonance model with fixed C = 0.22 and allowing the resonance center anywhere inside the scan gives best SSE = 0.03531 and RMSE = 0.0410, worse than baseline-only.
- Fitting the same resonance shape with free amplitude gives best amplitude +0.0379, i.e. a small positive feature rather than the required negative contrast dip.

Decision: resonance_absent. The active 52 ns, mod_depth 1 pulse should produce an approximately 20-22 percent sampled dip if a pODMR resonance were present in this scan, but the measured signal/reference ratios remain close to unity and do not match the expected resonance signature.
