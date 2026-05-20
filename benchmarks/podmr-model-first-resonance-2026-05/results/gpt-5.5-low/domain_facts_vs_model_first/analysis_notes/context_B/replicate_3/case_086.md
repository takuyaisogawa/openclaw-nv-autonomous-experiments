Case: podmr_072_2026-05-17-085551

Active sequence identification:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instruction path has full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped.
- Readout 1 role: after adj_polarize and detection, a direct polarized m_S = 0 reference.
- Readout 2 role: after a single rabi_pulse_mod_wait_time pulse and detection, the pODMR signal readout.
- Pulse parameters from the provided sequence XML: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. Rounding to the sample clock keeps 52 ns because 52 ns * 250 MHz = 13 samples.

Quantitative expected-signal model:
- Given setup contrast between m_S = 0 and m_S = +1 of about 22%.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so f_Rabi = 10 MHz here.
- For a square resonant pulse, the transferred m_S = +1 population is modeled as P1 = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected on-resonance fluorescence reduction relative to the m_S = 0 reference is therefore 0.22 * 0.996 = 0.219, about 21.9%.
- The mean readout 1 level is 50.168 counts, so the expected on-resonance readout 2 drop is about 10.99 counts if the sweep crosses a resonance and the pulse is resonant.

Observed data comparison:
- Mean readout 1 = 50.168 counts.
- Mean readout 2 = 49.541 counts.
- Signal difference readout2 - readout1 has mean -0.627 counts and standard deviation 1.203 counts across scan points.
- The largest observed drop is -2.442 counts at 3.925 GHz, corresponding to only about 4.8% of readout 1.
- No scan point shows a drop near the roughly 11-count, 21.9% signal predicted by the active pulse model.
- Stored averages are only two and can reflect tracking cadence, so they are not treated as an independent repeatability test; still, the combined data do not show the expected pODMR response.

Decision:
The active pulse sequence should produce a large negative readout2-versus-readout1 contrast on resonance. The observed readouts show only small fluctuations and no quantitatively compatible dip. I therefore decide that a pODMR resonance is absent.
