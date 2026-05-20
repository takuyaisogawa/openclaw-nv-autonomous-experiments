Case podmr_013_2026-05-16-123121

Inputs used:
- Active sequence: Rabimodulated.xml / Rabimodulated sequence.
- The sequence performs an optically polarized detection first, then (because full_expt = 0) skips the separate m_S=+1 reference block, then applies one modulated Rabi microwave pulse and detects again.
- Readout roles: readout 1 is the true m_S=0 optical reference after polarization; readout 2 is the signal after the microwave Rabi pulse.
- Pulse parameters from the measurement variables: length_rabi_pulse = 52 ns, mod_depth = 1, mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:
- Given setup contrast scale C = 22% between m_S=0 and m_S=+1.
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, so f_Rabi = 10 MHz here.
- For a resonant square Rabi pulse, transferred population is p = sin^2(pi * f_Rabi * t).
- With t = 52 ns, p = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected resonant fluorescence loss fraction = C * p = 0.22 * 0.996 = 0.219, or about 21.9%.
- Using the off-resonant readout-2 edge baseline of about 42.99 raw units, the expected resonant dip is about 9.42 raw units.

Observed data check:
- Readout 2 off-resonant edge baseline is about 42.99.
- Minimum readout 2 is 34.08 at 3.880 GHz, with 34.67 at 3.875 GHz.
- The observed drop is 8.92 raw units, or 20.7% of the baseline.
- A linear baseline fit excluding the central candidate region gives a minimum residual of -8.86 raw units and an off-feature residual scatter of about 1.18 raw units, roughly a 7.5 sigma localized dip.
- The dip appears in readout 2, not as a comparable collapse in readout 1, matching the expected role of the microwave-driven readout.
- Stored averages reproduce the same trough qualitatively, but I treat that only as a tracking-cadence consistency check rather than a strong independent repeatability test.

Decision:
The expected resonant signal from the pulse model is a nearly full pi-pulse contrast dip of about 22%, and the measured readout-2 feature is a localized 20-21% dip at the swept microwave frequency. This is quantitatively consistent with a pODMR resonance.
