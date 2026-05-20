Case podmr_044_2026-05-16-232730

Sequence inspection:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The exported variable values are the active values for this run: mod_depth = 1, length_rabi_pulse = 52 ns, sample_rate = 250 MHz, full_expt = 0.
- Because full_expt = 0, the optional m_S = +1 reference block is skipped.
- Readout roles:
  - readout 1 is the initial optical readout immediately after polarization, a true m_S = 0 reference.
  - readout 2 is the optical readout after the 52 ns microwave Rabi pulse.

Physical model calculation:
- Given f_Rabi approximately 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the effective Rabi frequency here is approximately 10 MHz.
- For a resonant square pulse of duration t = 52 ns, the population transfer is modeled as P = sin^2(pi f_Rabi t).
- P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant point should change the fluorescence by about 0.22 * 0.996 = 0.219, i.e. about 21.9% of the baseline.
- The measured baseline is about 48.62 counts, so the expected resonant feature size is about 10.65 counts.

Observed data check:
- Combined readout 1 mean = 48.56 counts, standard deviation = 1.15 counts.
- Combined readout 2 mean = 48.69 counts, standard deviation = 1.20 counts.
- The readout-2/readout-1 contrast has rms scatter about 2.22%, far below the approximately 21.9% feature expected for a resonant 52 ns pulse.
- The average trace varies from 46.875 to 50.779 counts, with a linear-detrended residual standard deviation about 0.76 counts.
- No point or local region shows the expected approximately 10.7 count fluorescence reduction in readout 2 relative to the m_S = 0 reference.
- A simple Gaussian-feature scan does not find a physically relevant dip; the best small feature is order 1.5 counts and is much smaller than the expected resonant contrast.

Decision:
The active pulse sequence would produce an easily visible pODMR contrast if a resonance were present in the scanned range. The measured readouts show only small drift/noise-scale fluctuations and no expected resonant fluorescence dip, so the resonance is absent.
