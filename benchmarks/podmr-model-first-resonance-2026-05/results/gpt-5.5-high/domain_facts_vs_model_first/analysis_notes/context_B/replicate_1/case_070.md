Case: podmr_056_2026-05-17-050447

Sequence and readout roles:
- The active sequence is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML instructions first polarize and detect, giving readout 1 as the true mS=0 reference.
- full_expt = 0, so the conditional mS=1 reference block is inactive.
- The active pODMR measurement is then a rabi_pulse_mod_wait_time pulse followed by detection, giving readout 2 as the MW-pulsed signal readout.
- The relevant pulse parameters from the provided XML are mod_depth = 1 and length_rabi_pulse = 52 ns.

Quantitative expected signal model:
- Given the supplied calibration, the Rabi frequency is about 10 MHz at mod_depth = 1.
- For a square pulse, the resonant population transfer is P = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast scale is about 22%, so an on-resonance pODMR feature should reduce the signal readout by about 0.22 * 0.996 = 0.219, or 21.9%, relative to the mS=0 reference.
- At the observed raw baseline near 44 counts, that corresponds to an expected dip amplitude of about 9.6 raw-count units in readout 2 relative to readout 1.

Data comparison:
- The normalized signal/reference ratio readout2/readout1 has mean 1.004, standard deviation 0.032, and minimum 0.943.
- A resonant 52 ns, mod_depth 1 pulse should produce a ratio near 0.781 at resonance, far below the observed minimum.
- The raw readout2 - readout1 difference has mean +0.16 counts and minimum -2.60 counts, much smaller than the expected approximately -9.6 count resonant dip.
- The visible structure is dominated by slow drift/tracking-scale variation and readout-to-readout scatter. The stored averages are not treated as a strong independent repeatability test.

Decision:
The active MW-pulsed signal readout does not show the quantitatively expected pODMR contrast for the specified pulse, so I decide that a pODMR resonance is absent.
