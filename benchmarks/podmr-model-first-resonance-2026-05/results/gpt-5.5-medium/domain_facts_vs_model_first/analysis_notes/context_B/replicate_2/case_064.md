<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_064

Sequence identification:
- The active sequence is Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave manipulation is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)` followed by detection.
- `full_expt = 0`, so the optional mS=1 reference block is disabled.
- Readout 1 is the initial bright-state / mS=0 reference acquired immediately after optical polarization.
- Readout 2 is the post-Rabi-pulse pODMR signal readout.
- From the provided sequence XML, `length_rabi_pulse = 52 ns` and `mod_depth = 1`.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1, the resonant population transfer for a square pulse is
  P_transfer = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns:
  pi * f_Rabi * tau = pi * 10e6 * 52e-9 = 1.6336 rad,
  P_transfer = sin^2(1.6336) = 0.996.
- With setup contrast 22%, the expected resonant fluorescence reduction is
  0.22 * 0.996 = 0.219, or about 21.9%.
- On the observed baseline near 53 counts, that predicts an on-resonance drop of about
  53 * 0.219 = 11.6 counts in the post-pulse signal.
- Even if the embedded exported sequence text's lower mod_depth value of 0.3 were used as a sensitivity check, the model gives f_Rabi = 3 MHz, P_transfer = 0.222, expected fractional drop = 4.87%, or about 2.6 counts.

Observed data:
- Combined readout 1 mean = 53.29 counts, standard deviation = 0.90 counts.
- Combined readout 2 mean = 52.93 counts, standard deviation = 0.93 counts.
- The readout2/readout1 ratio mean is 0.994 with standard deviation 0.024.
- The smallest readout2 value is 50.90 counts at 3.910 GHz, only about 2.03 counts below the readout2 mean. This is far smaller than the 11.6-count expected dip for the provided mod_depth = 1 sequence, and it is only a single-point excursion comparable to the noise/tracking scatter.
- Near the nominal center of the scan, readout 2 is not depressed: 3.870, 3.875, and 3.880 GHz are 53.06, 53.35, and 53.38 counts.
- The lowest normalized ratio at 3.865 GHz is mainly caused by an unusually high readout 1 value, not by a strong low post-pulse signal.

Decision:
The expected pODMR signal from the active pulse model should be large for the provided 52 ns, mod_depth 1 pulse. The measured data show only small, isolated fluctuations and no coherent resonance-shaped fluorescence loss. I therefore decide resonance_absent.
