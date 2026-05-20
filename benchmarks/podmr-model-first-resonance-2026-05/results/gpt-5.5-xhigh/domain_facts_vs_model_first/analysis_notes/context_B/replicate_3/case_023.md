Case: podmr_008_2026-05-16-014743

Sequence and readout roles:
- The provided sequence XML is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The first active detection occurs immediately after adj_polarize(...), so readout 1 is the optically polarized m_S = 0 reference.
- The second active detection occurs after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), so readout 2 is the signal after the microwave pulse.
- mod_depth = 1 in the provided sequence XML and in raw_export Variable_values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the sequence rounds this to round(52 ns * 250 MHz) / 250 MHz = 13 / 250 MHz = 52 ns.

Physical model calculation:
- Use the two-level square-pulse excitation probability
  P_exc(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau),
  where delta is frequency detuning in Hz.
- Given f_R = 10 MHz at mod_depth = 1 and tau = 52 ns:
  P_exc(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale C = 0.22, the expected on-resonance PL reduction is
  C * P_exc(0) = 0.219, or about 21.9%.

Observed quantitative signal:
- Combined readout 2 reaches its minimum at 3.875 GHz: readout 2 = 31.3077, readout 1 = 42.4615.
- The normalized loss at that point is (42.4615 - 31.3077) / 42.4615 = 0.2627.
- Averaging readout 2 outside +/-15 MHz of the fitted resonance gives a baseline of 41.0372, while the +/-5 MHz near-resonance mean is 31.8077, a relative drop of 22.49%.
- Correcting by the corresponding readout 1 baseline/near values gives a relative normalized drop of 22.81%.
- The two stored averages both have their readout 2 minimum at 3.875 GHz; their point contrasts are about 23.2% and 29.3%. These averages are not treated as independent repeatability proof, but they do not contradict the combined signal.

Model fit:
- I fit readout2/readout1 to b * (1 - 0.22 * P_exc(freq - f0)).
- Best fit: f0 = 3.87736 GHz, b = 0.9982.
- Sum of squared residuals for a flat normalized response: 0.12461.
- Sum of squared residuals for the fixed-contrast pulse model: 0.02622.
- The pulse model improves the residual by a factor of 4.75 over flat.
- Allowing the contrast amplitude to float gives an effective contrast of 0.245 at the same f0, close to the stated 0.22 scale.

Decision:
The observed readout 2 dip is centered near the scanned transition frequency, has the width expected for a 52 ns approximately pi pulse, and has amplitude consistent with the 22% m_S = 0 to m_S = +1 contrast scale. Therefore a pODMR resonance is present.
