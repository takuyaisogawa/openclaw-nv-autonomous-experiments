Case podmr_073_2026-05-17-090948

Active sequence interpretation:

The provided sequence XML is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active variables are mod_depth = 1 and length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so the pulse length is exactly 13 samples after rounding. full_expt = 0, so the optional m_S = +1 reference block is inactive.

There are two active detections. The first detection occurs immediately after optical polarization and is the bright m_S = 0 reference. The second detection occurs after the 52 ns modulated Rabi pulse and is the pODMR signal readout. Therefore readout 1 is the m_S = 0 reference and readout 2 is the microwave-pulse signal. There is no active independent m_S = +1 readout in this sequence.

Quantitative physical model:

Using the provided setup facts, the Rabi frequency at mod_depth = 1 is about f_R = 10 MHz. For a rectangular pulse, the driven transition probability versus detuning is

P(delta_f) = f_R^2 / (f_R^2 + delta_f^2) * sin^2(pi * t * sqrt(f_R^2 + delta_f^2)).

On resonance with t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the setup contrast scale of 22%, the expected fractional fluorescence loss in the signal readout is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean reference readout is 50.17 counts, so an on-resonance point should be lower by about 10.99 counts. Because the scan spacing is 5 MHz and the Rabi frequency is 10 MHz, the model is also broad on this frequency grid: for any resonance center inside the scanned range, at least one sampled point should have a fractional loss of at least about 20.4%.

Measured data comparison:

The measured mean readout 1 is 50.17 and mean readout 2 is 50.04. The mean difference readout2 - readout1 is only -0.12 counts. The largest reference-normalized drop, (readout1 - readout2) / readout1, is 0.0496 at 3.855 GHz, about 5.0%, which is only about one quarter of the minimum sampled loss expected from the model for an in-range resonance.

The measured drops are also not a broad Rabi-broadened pODMR dip. A constrained fit of the model shape to readout2/readout1 gives a best dip amplitude of about 0.023 in ratio units, only about 10.6% of the expected 0.219 amplitude. Forcing the expected 22% contrast model gives a best sum of squared residuals about 8.3 times worse than a flat ratio baseline. The stored two averages show small, isolated drops with different strongest positions, consistent with tracking or readout scatter rather than a repeatable resonance feature.

Decision:

Given the active sequence and expected near-pi-pulse signal, a real pODMR resonance in this scan should produce a large, broad readout-2 loss relative to readout 1. The observed signal is near unity ratio with only small isolated fluctuations. I therefore classify this case as resonance_absent.
