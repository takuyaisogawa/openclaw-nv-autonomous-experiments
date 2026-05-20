Case: podmr_001_2026-05-16-000631

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, scanned variable mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first run adj_polarize followed by detection, giving the true m_S = 0 reference readout.
- full_expt = 0, so the optional separate m_S = +1 reference block is skipped.
- The active signal operation is then rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. This second detection is the pODMR signal readout.
- do_adiabatic_inversion is set true but is only inside commented or skipped logic and is not active.

Quantitative model:
- Given setup Rabi frequency at mod_depth = 1 is about 10 MHz.
- With a 52 ns pulse, the resonant rotation angle is theta = 2*pi*(10 MHz)*(52 ns) = 3.267 rad = 1.04*pi.
- The expected transferred population on resonance is sin^2(theta/2) = 0.996.
- The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected pODMR fluorescence drop is 0.22*0.996 = 0.219, about 21.9% of the off-resonance signal.
- Using the observed readout-2 off-dip baseline excluding indices 9-12 gives 37.407 raw counts, so the expected resonant drop is 37.407*0.219 = 8.20 raw counts, with an expected minimum near 29.21 raw counts.

Observed data:
- Readout 2 has a clear dip centered near 3.875-3.880 GHz: values at indices 9-12 are 32.23, 30.00, 28.98, and 31.92.
- The minimum is 28.98 at 3.880 GHz, a drop of 8.43 counts or 22.5% from the off-dip baseline.
- This observed drop is 1.03 times the model expectation from a near-pi pulse and the known contrast scale.
- Readout 1, the 0-reference, does not show a comparable central resonance-scale dip; its same-window mean is 36.79 versus an off-window baseline of 37.99.
- The stored averages are consistent in the central readout-2 dip but are not treated as a strong independent repeatability test because averages can reflect tracking cadence.

Decision:
The active sequence should produce a near-full contrast pODMR dip when the scanned microwave frequency is resonant, and the signal readout shows a quantitatively matching dip with the correct readout role. A pODMR resonance is present.
