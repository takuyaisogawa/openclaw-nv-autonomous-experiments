Case: podmr_010_2026-05-16-114624

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence uses length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, and do_adiabatic_inversion = 1.
- Because full_expt = 0, the conditional "Acquire 1 level reference" block is skipped. The two readouts are therefore:
  - readout 1: true mS = 0 optical reference after polarization, before the microwave pulse.
  - readout 2: signal readout after the active Rabi-modulated microwave pulse.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the relevant Rabi frequency is 10 MHz.
- For a resonant square pulse of duration t = 52 ns, the transferred population is:
  P = sin^2(pi * f_Rabi * t)
    = sin^2(pi * 10e6 * 52e-9)
    = 0.996.
- With the setup contrast scale between mS = 0 and mS = +1 of about 22%, the expected resonant fluorescence reduction in the pulsed readout is:
  0.996 * 22% = 21.9%.
- For a raw readout near 40 counts, this corresponds to an expected dip of about 8.8 counts.

Observed data check:
- Off the dip, readout 2 and readout 1 are nearly equal; over the first eight frequency points, mean(readout2/readout1) = 0.988.
- The pulsed readout has a localized minimum at 3.875 GHz:
  readout 1 = 40.904, readout 2 = 31.192.
- The same-point fractional reduction is:
  (40.904 - 31.192) / 40.904 = 23.7%.
- This is very close to the 21.9% expected from the resonant Rabi-pulse model.
- Stored averages show tracking-level offsets and should not be treated as strong independent repeatability evidence, but both averages contain the same central readout-2 suppression around the expected contrast scale.

Decision:
The measured pulsed readout contains a localized dip with the amplitude expected for the active resonant Rabi pulse. A pODMR resonance is present.
