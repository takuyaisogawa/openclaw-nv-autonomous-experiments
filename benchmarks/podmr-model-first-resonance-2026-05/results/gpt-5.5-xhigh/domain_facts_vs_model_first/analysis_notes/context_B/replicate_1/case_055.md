I used the provided sequence XML to identify the active measurement. The active sequence is Rabimodulated.xml / Rabi-modulated pODMR with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true m_S = 0 reference. The optional m_S = 1 reference block is disabled because full_expt = 0. The second recorded readout is therefore the signal after a single rabi_pulse_mod_wait_time microwave pulse followed by detection. The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the pulse is already exactly 13 samples, so rounding leaves it at 52 ns.

Quantitative model:

Use the stated setup calibration f_R = 10 MHz at mod_depth = 1, with linear scaling, so f_R = 10 MHz here. For a square microwave pulse, the resonant transfer probability is

P(0) = sin^2(pi * f_R * tau)

with tau = 52 ns. Numerically,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996057.

The stated bright/dark contrast scale is 22%, so an on-resonance pulse should reduce the post-pulse readout relative to the m_S = 0 reference by

0.22 * 0.996057 = 0.219133,

or a readout-2/readout-1 ratio of 0.780867. The mean reference readout is 46.354 counts, so the expected resonant drop is about 10.16 counts.

I also evaluated the detuned square-pulse model

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

and compared readout-2/readout-1 ratios with and without a resonance in the scanned range.

Observed combined data:

readout 1 mean = 46.354, readout 2 mean = 46.142.
The normalized ratio readout2/readout1 has mean 0.9955, standard deviation 0.0303, and minimum 0.9437 at 3.895 GHz. The largest observed positive contrast is therefore only 1 - 0.9437 = 0.0563, a 5.6% drop, far below the expected 21.9% drop for the active pulse.

The stored per-average traces have large absolute offsets consistent with tracking cadence: average 1 is near 41 counts while average 2 is near 51 counts. Looking within each stored average, the maximum positive normalized drops are still only about 6.4% and 7.6%, not close to the expected 21.9%.

Model comparison in normalized-ratio space:

No-resonance baseline ratio = 1 gives SSE = 0.01966.
A fixed-contrast 22% resonance model with the resonance center constrained inside the scanned frequency range gives best SSE = 0.08531, worse than the no-resonance baseline. Centering the model at the strongest observed dip, 3.895 GHz, gives SSE = 0.09276. If the model amplitude is allowed to float, the best fitted contrast amplitude is only about 4.5%, which is inconsistent with the expected 21.9% from mod_depth = 1 and a 52 ns pulse.

Decision: the small observed readout fluctuations are not quantitatively compatible with the expected pODMR response for the active pulse sequence. I classify this case as resonance_absent.
