Case: podmr_065_2026-05-17-071421

Sequence interpretation:
- The provided sequence is Rabimodulated.xml.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive. The adiabatic inversion flag is therefore not used in the active sequence.
- Active detections are:
  1. After adj_polarize: this is the true mS=0 reference readout.
  2. After rabi_pulse_mod_wait_time: this is the post-microwave pODMR signal readout.
- The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- From inputs/sequence.xml, mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- The given setup has Rabi frequency about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. Thus f_Rabi = 10 MHz.
- For a rectangular resonant pulse, the transition probability is P(f0) = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, P_on_res = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22 percent mS=0 to mS=+1 contrast scale, the expected on-resonance readout drop is 0.22 * 0.996 = 0.219, or 21.9 percent of the reference level.
- The mean reference readout is 47.48 counts, so the expected on-resonance drop is about 10.4 counts.
- Including detuning, I used P(d) = f_Rabi^2/(f_Rabi^2 + d^2) * sin^2(pi * tau * sqrt(f_Rabi^2 + d^2)). On the 5 MHz scan grid this gives expected contrast of about 21.9 percent at line center, 16.5 percent at +/-5 MHz, and 6.0 percent at +/-10 MHz.

Observed data comparison:
- Combined readout1 is the reference and combined readout2 is the post-microwave signal.
- The normalized signal readout2/readout1 has mean 0.9945, standard deviation 0.0259, minimum 0.9523, and maximum 1.0434.
- The largest combined dip is only 4.8 percent, corresponding to 2.27 counts, far below the expected roughly 21.9 percent or 10.4-count resonance signature.
- The two stored averages have large baseline offsets, consistent with tracking cadence effects. Their ratio minima are 0.922 and 0.927, still much shallower than the expected approximately 0.778 on-resonance normalized signal, and they occur at different frequencies.
- A linear-baseline null fit to readout2/readout1 gives RMSE 0.0241. A fixed 22 percent physical resonance model does not find an in-scan dip; its best center is outside the scan at about 3.8035 GHz. Allowing the dip amplitude to float prefers a negative dip amplitude near 3.856 GHz, i.e. a bump rather than the expected pODMR dip.

Decision:
The active pulse should produce a large, broad dip if a pODMR resonance is present in the scanned range. The data show only small tracking-scale fluctuations and no quantitatively compatible pODMR resonance.
