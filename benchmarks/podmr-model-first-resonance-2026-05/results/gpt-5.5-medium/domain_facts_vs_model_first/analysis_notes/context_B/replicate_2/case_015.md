Case: podmr_034_2026-05-15-235221

I used only the provided sequence XML and the raw export data in this isolated workspace.

Active sequence and readout roles:
- SequenceName is Rabimodulated.xml, with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first polarizes and detects before any microwave pulse. This is readout 1, the true m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is inactive and does not generate a readout.
- The active experimental microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is readout 2, the pulsed pODMR signal.
- mod_depth = 1 from the provided sequence variable values.
- length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this is already exactly 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, the active pulse has f_Rabi = 10 MHz.
- For a square resonant pulse, transition probability P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, P_res = sin^2(pi * 10e6 * 52e-9) = 0.996, i.e. essentially a pi pulse.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence reduction is about 0.22 * P_res = 21.9% of the off-resonant signal.
- The readout 2 off-resonant baseline, excluding the obvious three-point dip region at indices 9 to 11, is 35.13 counts. The expected resonant drop is therefore 0.22 * 0.996 * 35.13 = 7.70 counts, giving an expected minimum near 27.43 counts.

Explicit detuned square-pulse model:
- I used P(detuning) = (Omega^2/(Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau), with Omega = 2*pi*10 MHz, delta = 2*pi*(f - f0), tau = 52 ns, and f0 placed at the observed dip center.
- This predicts a broad few-point pODMR dip on the 5 MHz scan grid, with modeled values near the center approximately 33.02, 29.35, 27.43, 29.35, 33.02 counts across offsets -10, -5, 0, +5, +10 MHz.
- The observed readout 2 values around the feature are 33.38, 30.83, 26.81, 26.29, 33.06 counts from 3.865 to 3.885 GHz. The deepest point is 26.29 counts at 3.880 GHz, a drop of 8.85 counts from the off-resonant baseline.
- The square-pulse resonance model reduces readout 2 residual sum of squares relative to a flat baseline by about a factor of 3.3 (RSS model 58.5 versus RSS flat 194.8), despite noise and sparse 5 MHz sampling.
- Readout 1 does not show a corresponding fluorescence loss; it remains a reference-like trace with mean 36.01 counts and standard deviation 1.08 counts.

Decision:
The pulsed readout contains a dip of the expected amplitude and approximate width for the active 52 ns, mod_depth = 1 near-pi pODMR pulse, while the reference readout does not show the same behavior. The pODMR resonance is present.
