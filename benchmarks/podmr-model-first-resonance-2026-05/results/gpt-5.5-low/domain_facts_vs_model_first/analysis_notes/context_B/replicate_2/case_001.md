Case: podmr_004_2026-05-10-171142

Sequence/readout interpretation:
- The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the initial true m_S = 0 reference after adj_polarize and detection.
- Readout 2 is the signal readout after a single rabi_pulse_mod_wait_time pulse and detection.
- Active pulse parameters from the provided sequence XML: length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Quantitative expected-signal model:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the pulse area for a 52 ns pulse is 2*pi*(10e6)*(52e-9) = 1.04*pi radians.
- The two-level population transfer probability on resonance is sin^2(theta/2) = sin^2(pi*f_Rabi*t) = sin^2(pi*10e6*52e-9) = 0.996.
- With the setup contrast scale of about 22% between m_S = 0 and m_S = +1, an on-resonance response should make readout 2 approximately 1 - 0.22*0.996 = 0.781 of readout 1.
- The mean readout 1 level is 43.679, so the expected resonant readout 2 level is about 34.108, a drop of about 9.572 raw-readout units from readout 1.

Observed data check:
- Across the scan, readout 2 / readout 1 ranges from 0.943 to 1.092.
- The largest observed negative readout2-readout1 difference is -2.462 at 3.855 GHz, far smaller than the expected about -9.57 drop for a near-pi pulse resonance.
- Several points show readout 2 above readout 1, including +3.962 at 3.915 GHz, which is opposite the expected fluorescence decrease for transfer from m_S = 0 to m_S = +1.
- Stored averages are only two and can reflect tracking cadence; they do not provide strong independent repeatability evidence.

Decision:
The physically expected pODMR signature for this pulse and contrast is a large negative-going feature in readout 2 relative to the m_S = 0 reference. The measured trace shows no feature with the expected amplitude or sign consistency. I therefore decide resonance_absent.
