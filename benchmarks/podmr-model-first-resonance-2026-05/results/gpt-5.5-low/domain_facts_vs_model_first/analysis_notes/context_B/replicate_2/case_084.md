Case: podmr_070_2026-05-17-082720

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- SequenceName in the export is Rabimodulated.xml, and the provided sequence XML is a Rabi-modulated pulse sequence swept over mw_freq.
- The active microwave operation is:
  PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);
- The earlier "Acquire 1 level reference" branch is inactive because full_expt = 0, so it does not add a separate mS=+1 reference readout.
- Therefore readout 1 is the true mS=0 bright reference after optical polarization and before the active microwave pulse. Readout 2 is the signal readout after the active Rabi-modulated pulse.
- From the provided sequence XML, length_rabi_pulse = 5.2e-08 s, mod_depth = 1, sample_rate = 250 MHz. The pulse is exactly 13 samples, so the rounded duration remains 52 ns.

Physical model calculation:
- Given setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For mod_depth = 1, f_Rabi = 10 MHz.
- For a resonant rectangular Rabi pulse, transferred population is P = sin^2(pi * f_Rabi * tau), using f_Rabi in cycles/s.
- tau = 52 ns gives P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The mS=0 to mS=+1 contrast scale is about 22%, so a resonant point should reduce the post-pulse signal readout by approximately 0.22 * 0.996 = 21.9% of the bright readout.
- The observed bright reference mean is 50.71 counts, so the expected resonant signal drop is about 11.11 counts, with an expected readout2/readout1 ratio near 0.781 at resonance.

Measured readout comparison:
- Mean readout 1 = 50.71 counts; mean readout 2 = 50.23 counts.
- The pointwise signal difference readout2 - readout1 has mean -0.48 counts, standard deviation 1.19 counts, minimum -1.96 counts, and maximum +1.69 counts.
- The readout2/readout1 ratio has mean 0.991 and minimum 0.961.
- The largest observed depression is only about 3.9% of the bright level, far smaller than the approximately 21.9% drop expected for an on-resonance 52 ns pulse at mod_depth = 1.
- Both raw readouts show a similar slow downward trend at high scan values, indicating common-mode drift or tracking behavior rather than a selective pODMR dip in the post-pulse readout.
- Stored averages are only two and can reflect tracking cadence, so I did not treat the two average traces as a strong independent repeatability test.

Decision:
The expected resonant response from the active pulse is large, about an 11-count signal drop relative to the mS=0 reference. The measured readout-pair contrast is at most about 2 counts and is dominated by common-mode drift. Therefore this case is best classified as resonance absent.
