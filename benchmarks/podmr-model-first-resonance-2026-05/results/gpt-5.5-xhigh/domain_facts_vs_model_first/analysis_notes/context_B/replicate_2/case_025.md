The active sequence is Rabimodulated.xml. The sequence first polarizes and detects the bright m_S = 0 reference, then skips the optional m_S = +1 reference because full_expt = 0, then applies one rabi_pulse_mod_wait_time pulse and detects again. Therefore readout 1 is the bright/reference readout and readout 2 is the driven pODMR readout.

Relevant XML parameters:
- sample_rate = 250 MHz, so length_rabi_pulse = round(52 ns * 250 MHz) / 250 MHz = 52 ns.
- mod_depth = 1.
- The setup Rabi rate is therefore about 10 MHz.
- The expected full contrast scale between m_S = 0 and m_S = +1 is about 22%.

Quantitative model:
For a square pulse with Rabi frequency f_R = 10 MHz and detuning delta in Hz, I used

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

with tau = 52 ns. The expected normalized driven/reference ratio is

R(delta) = baseline - C * P(delta)

with C approximately 0.22.

Model values for C = 0.22:
- delta = 0 MHz: P = 0.996, expected ratio = 0.781.
- delta = +/-5 MHz: P = 0.749, expected ratio = 0.835.
- delta = +/-10 MHz: P = 0.273, expected ratio = 0.940.
- delta = +/-15 MHz: P = 0.012, expected ratio = 0.997.

Observed normalized readout2/readout1 values near the feature:
- 3.865 GHz: 0.969
- 3.870 GHz: 0.824
- 3.875 GHz: 0.763
- 3.880 GHz: 0.843
- 3.885 GHz: 0.931
- 3.890 GHz: 1.025

The observed minimum at 3.875 GHz is a 23.7% reduction relative to the reference, which is very close to the expected 22% resonant contrast for a near-pi pulse. The width is also consistent with the pulse-limited Rabi response: the dip is strong at +/-5 MHz and mostly gone by about +/-15 MHz.

I also fit the normalized ratio to a Rabi response plus a linear baseline. The best fit gave center = 3.87525 GHz, contrast amplitude = 0.2159, and RMSE = 0.0253. Smooth no-resonance polynomial baselines had RMSE about 0.060 to 0.066, so the physical resonance model explains the data much better than a drift-only model. The two stored averages both show their strongest normalized dip at 3.875 GHz, but I treat that only as supporting context because stored averages can reflect tracking cadence.

Decision: resonance_present.
