Case podmr_070_2026-05-17-082720

I used the provided sequence information before deciding. The active sequence is Rabimodulated.xml, varied over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction flow is: polarize, detect the true mS=0 reference readout, wait, skip the optional mS=1 reference because full_expt = 0, apply rabi_pulse_mod_wait_time, then detect the pulsed readout. Thus readout 1 is the mS=0 fluorescence reference and readout 2 is the readout after the microwave Rabi pulse. The saved active pulse parameters in raw_export are length_rabi_pulse = 52 ns and mod_depth = 0.3, with sample-rate rounding leaving the pulse at 52 ns.

Quantitative expected-signal model:

- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the expected on-resonance Rabi frequency here is 3 MHz.
- For a square pulse of duration tau = 52 ns, the resonant transfer probability is sin^2(pi * f_Rabi * tau) = sin^2(pi * 3e6 * 52e-9) = 0.222.
- With the stated 22% mS=0 to mS=+1 contrast scale, the expected fractional fluorescence reduction at resonance is 0.22 * 0.222 = 0.0487, about 4.9%.
- The mean reference readout is 50.71 counts, so the expected resonant reduction would be about 2.47 counts in the pulsed readout relative to the local reference/baseline.

Data comparison:

- Combined readout means: readout 1 = 50.71, readout 2 = 50.23.
- The readout 2 minimum is 47.33 counts at 3.915 GHz, but readout 1 is also low in the same high-frequency region and both traces show a broad downward drift with frequency/tracking.
- After subtracting a linear trend, readout 2 residual scatter is about 1.17 counts and the strongest negative residual is at the low-frequency edge, not at a clear interior resonance. For readout2 - readout1, the linear-trend residual scatter is about 1.15 counts and the most negative residual is also at the scan edge.
- The two readouts are positively correlated (about 0.72), indicating shared baseline/tracking variation. The stored two averages are consistent with this slow drift and do not provide a strong independent repeatability test.

Decision:

The physical model predicts a localized approximately 2.5-count pulsed-readout dip if the scan crosses an efficiently driven resonance. The observed structure is instead a common baseline change in both readouts, with no isolated, repeatable, local pulsed-readout depression of the expected size after accounting for the reference. I therefore classify this case as resonance absent.
