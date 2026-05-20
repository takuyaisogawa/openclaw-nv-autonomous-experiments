Case: podmr_011_2026-05-16-120107

I used only the provided sequence XML, raw export, and raw readout plot. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz in 5 MHz steps. The instructions contain two active detections because full_expt = 0 disables the intermediate "Acquire 1 level reference" block. Therefore readout 1 is the true m_S = 0 fluorescence reference after laser polarization, and readout 2 is the signal after the modulated Rabi pulse. The active Rabi pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns.

Quantitative model calculation:

- Setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: t = 52 ns.
- Resonant population transfer model: P(+1) = sin^2(pi f_R t).
- P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected resonant fluorescence reduction relative to readout 1: C * P(+1) = 0.22 * 0.996 = 0.219, or about 21.9%.

Observed normalized contrast, using 1 - readout2/readout1, has its maximum at 3.880 GHz:

- readout 1 = 41.403846
- readout 2 = 33.096154
- observed fractional drop = 1 - 33.096154 / 41.403846 = 0.20065, or about 20.1%.

The observed dip amplitude is close to the 21.9% expected for a resonant near-pi pulse. Excluding the obvious dip region around indices 9-12, the off-resonance normalized contrast has mean 0.0228 and standard deviation 0.0334, making the 3.880 GHz point about 5.3 standard deviations above the off-resonance contrast scatter. The adjacent points form a coherent dip around 3.87-3.885 GHz rather than a single isolated outlier. Stored averages are only two and may mainly reflect tracking cadence, but both per-average overlays show the same central readout-2 depression.

Decision: a pODMR resonance is present.
