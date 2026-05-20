Case podmr_069_2026-05-17-081236.

Sequence and readout roles:
- The active sequence is Rabimodulated.xml from the saved export.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first performs adj_polarize and detection, giving the true m_S=0 bright reference readout.
- full_expt = 0, so the optional m_S=1 reference block is skipped.
- The sequence then applies one rabi_pulse_mod_wait_time pulse and detects again, giving the microwave-pulse signal readout.
- Therefore readout 1 is the bright m_S=0 reference and readout 2 is the post-pulse signal channel.

Pulse parameters:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, already an integer 13 samples at the 250 MHz sample rate.
- Setup Rabi frequency is approximately 10 MHz at mod_depth = 1.

Explicit signal model:
- For a resonant square pulse, the transferred population is P(+1) = sin^2(theta/2), with theta = 2*pi*f_Rabi*t.
- f_Rabi = 10 MHz and t = 52 ns gives theta = 3.267 rad = 187.2 deg.
- P(+1) = sin^2(1.6336) = 0.996.
- With the stated m_S=0 to m_S=+1 contrast scale of 22%, a resonance should reduce the signal readout relative to the bright reference by about 0.22 * 0.996 = 21.9%.
- The mean bright reference is about 46.69 counts, so the expected resonant drop is about 10.23 counts, i.e. a signal/reference ratio near 0.781.

Observed data:
- Mean readout 1 = 46.686 counts; mean readout 2 = 46.582 counts.
- Mean readout2-readout1 = -0.104 counts with standard deviation 1.385 counts across scan points.
- The largest observed normalized drop is at 3.845 GHz: readout 1 = 48.231, readout 2 = 43.942, contrast = 8.89%, drop = 4.29 counts.
- No point approaches the modeled 21.9% contrast or about 10 count drop expected for a resonant 52 ns pulse at mod_depth = 1.
- Several points have readout 2 brighter than readout 1, and the deviations are comparable to tracking/noise structure rather than forming a strong pODMR resonance signature.
- Stored averages are not treated as an independent repeatability test because they may primarily reflect tracking cadence.

Decision:
The quantitative model predicts a large near-pi-pulse fluorescence drop if a pODMR resonance is present. The observed scan does not show a drop of the expected magnitude or a convincing resonance feature, so the decision is resonance_absent.
