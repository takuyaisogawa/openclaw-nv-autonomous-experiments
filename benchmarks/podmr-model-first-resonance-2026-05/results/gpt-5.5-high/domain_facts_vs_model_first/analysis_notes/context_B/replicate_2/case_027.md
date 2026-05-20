Case podmr_012_2026-05-16-121601.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML and exported Variable_values give length_rabi_pulse = 52 ns and mod_depth = 1. The raw export also contains an embedded sequence text with mod_depth = 0.3, but the file requested for sequence interpretation and the exported active variable table both indicate mod_depth = 1.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout 1 is the polarized m_S = 0 fluorescence reference acquired before the microwave pulse.
- Readout 2 is the fluorescence after the Rabi-modulated microwave pulse and is the pODMR signal readout.

Quantitative physical model:
For a square microwave pulse, the population transferred from m_S = 0 to m_S = +1 is

P1(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * sqrt(f_R^2 + df^2) * tau),

where f_R is the on-resonance Rabi frequency in cycles/s, df is the frequency detuning, and tau is the pulse duration. The expected normalized fluorescence is

F_signal / F_ref = 1 - C * P1(df),

with contrast scale C = 0.22.

Using f_R = 10 MHz at mod_depth = 1 and tau = 52 ns:
- On resonance, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected on-resonance fluorescence loss = 0.22 * 0.996 = 0.219, or about 21.9%.
- With the mean reference readout near 42.1 counts, this corresponds to an expected drop of about 9.2 raw-count units at exact resonance.

Observed normalized readout-2 loss relative to readout 1:
- Away from the central feature, the readout2/readout1 ratio averages 0.986 with standard deviation 0.025.
- Around 3.870, 3.875, 3.880, and 3.885 GHz, the normalized losses are 13.1%, 12.8%, 17.7%, and 13.3%.
- The largest drop is at 3.880 GHz: readout1 = 41.23, readout2 = 33.92, ratio = 0.823, loss = 17.7%, drop = 7.31 counts.

The square-pulse model centered at 3.880 GHz predicts its strongest loss at 3.880 GHz and substantial neighboring loss at +/- 5 MHz, with weaker loss by +/- 10 MHz. The measured second readout shows exactly this localized loss pattern while the first readout remains near its usual reference level. The observed maximum loss is somewhat smaller than the ideal 21.9% model prediction, but it is of the correct sign, size, and frequency-localized shape for a pODMR resonance under a near-pi pulse.

Decision: resonance_present.
