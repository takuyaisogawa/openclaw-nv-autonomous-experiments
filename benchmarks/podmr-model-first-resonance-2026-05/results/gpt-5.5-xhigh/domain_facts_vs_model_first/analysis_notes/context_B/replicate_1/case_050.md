Sequence and roles:

The provided XML is Rabimodulated.xml. With full_expt = 0, the gated "Acquire 1 level reference" block is inactive. Each scan point therefore has two detections:

1. readout 1: after adj_polarize and before the microwave pulse, so this is the polarized m_S = 0 reference.
2. readout 2: after rabi_pulse_mod_wait_time, so this is the pODMR signal readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative expected signal model:

For a square pulse driving a two-level transition, I used

P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz * mod_depth = 10 MHz and t = 52 ns. On resonance, f_R * t = 0.52 cycles, so

P_transfer(0) = sin^2(pi * 0.52) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should show a fractional dip in readout 2 relative to readout 1 of

0.22 * 0.996 = 0.219, or about 21.9%.

At the measured reference level mean(readout 1) = 50.99, this corresponds to an expected raw drop of about 11.17 readout units at resonance. A resonance in the scanned band should therefore be a large, localized dark feature in readout2/readout1 near 0.78, broadened by the 52 ns pulse and 10 MHz Rabi frequency.

Observed data comparison:

The measured readout2/readout1 ratios have mean 0.990, standard deviation 0.0267, minimum 0.946, and maximum 1.070. The largest raw drop is -2.79 units at 3.920 GHz, only about 5.4% of the local reference and much smaller than the expected roughly 11 unit / 21.9% resonant drop. Several nearby points do not form the expected resonance-shaped dip.

I also fit the measured ratios to the explicit Rabi model. A flat-ratio null model gave RMSE 0.0261. A fixed 22% contrast resonance model with the resonance center allowed anywhere in the scan gave worse RMSE 0.0519. Allowing the contrast amplitude to float gave a best dark feature of only about 4.3% contrast at the scan edge, still far below the physically expected 21.9% for this pulse.

The stored per-average traces show substantial baseline shifts consistent with tracking cadence; they are not a strong independent repeatability test. They also do not show a repeated 22% pODMR dip.

Decision: resonance_absent.
