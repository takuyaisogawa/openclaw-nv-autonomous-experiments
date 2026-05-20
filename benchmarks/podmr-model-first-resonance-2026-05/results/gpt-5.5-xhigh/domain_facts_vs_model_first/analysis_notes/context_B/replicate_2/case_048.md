Case podmr_034_2026-05-16-204545

Sequence and readout interpretation

The provided sequence is Rabimodulated.xml with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first run adj_polarize followed by detection; this is the true m_S = 0 fluorescence reference and corresponds to readout 1. The separate m_S = +1 reference block is inactive because full_expt = 0. The sequence then applies rabi_pulse_mod_wait_time followed by detection; this is the microwave-pulsed pODMR signal and corresponds to readout 2.

The active microwave pulse has length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence/variable values.

Quantitative expected signal model

Using the stated setup calibration, the Rabi frequency is f_R = 10 MHz at mod_depth = 1. For a square pulse, the driven population transfer versus detuning is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

where tau = 52 ns and delta is in Hz. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected on-resonance fractional fluorescence deficit in the pulsed signal relative to the m_S = 0 reference is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean reference readout is 50.016 raw-count units, so the expected resonant drop is about 50.016 * 0.219 = 10.96 raw-count units, putting the signal readout near 39.1 raw-count units at resonance. Since 1/tau is about 19 MHz and the scan step is 5 MHz, such a resonance should affect multiple neighboring scan points.

Measured comparison

Observed readout statistics:

- readout 1 mean = 50.016, standard deviation across scan = 0.942
- readout 2 mean = 49.366, standard deviation across scan = 1.187
- readout2/readout1 mean = 0.9872
- largest observed fractional deficit, 1 - readout2/readout1 = 0.0522, about 5.2%
- largest observed absolute deficit = 2.65 raw-count units

The largest observed deficit is roughly one quarter of the physically expected resonant deficit for this pulse, and no scan point approaches the expected approximately 11-count drop. A least-squares square-pulse line-shape scan over possible resonance centers gives a best fitted deficit amplitude of about 0.031 plus a small offset, not the expected 0.22. The raw per-average traces also vary enough that the small apparent deficits are compatible with cadence/drift/noise rather than a repeatable pODMR line.

Decision

The quantitative model predicts a large, multi-point fluorescence dip for a resonance under the active pulse conditions, but the measured differential signal only shows small few-percent fluctuations. I therefore classify this case as resonance absent.
