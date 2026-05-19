<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_026

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- SequenceName / XML: Rabimodulated.xml.
- The instructions first polarize the NV and perform a detection before any microwave pulse. Because the comment says "Acquiring true 0 level reference", readout 1 is the mS = 0 fluorescence reference.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is skipped. There is no active mS = 1 reference readout in this acquisition.
- The active measurement pulse is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)`, followed by detection. Readout 2 is therefore the post-Rabi-pulse signal readout.
- From the provided sequence XML / exported variable values: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, scan variable = mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:
- Given setup Rabi frequency f_R approximately 10 MHz at mod_depth = 1, the resonant transition probability for a square pulse is
  P1(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * sqrt(Omega^2 + Delta^2) * tau),
  with Omega and Delta in cycles/s and tau = 52 ns.
- On resonance, P1(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = about 0.996.
- With the stated mS = 0 to mS = +1 contrast scale of about 22%, the expected on-resonance signal/reference fluorescence ratio is
  1 - 0.22 * 0.996 = about 0.781.
- For a reference readout around 41.40 counts near the feature, the expected resonant signal count is about 32.33 counts.

Observed quantitative comparison:
- At 3.880 GHz, readout 1 = 41.4038 and readout 2 = 33.0962, giving signal/reference ratio = 0.799 and a drop of 8.3077 counts.
- This is very close to the explicit model expectation of ratio about 0.781 / signal about 32.33 counts.
- Off the central 3.870-3.890 GHz region, the signal/reference ratio has mean about 0.977 and standard deviation about 0.0345. The 3.880 GHz ratio is lower than that by about 5.15 off-region standard deviations.
- The two stored averages both have their minimum readout 2 value at 3.880 GHz: average 1 ratio about 0.781, average 2 ratio about 0.818. These averages are treated only as tracking-cadence snapshots, but they are consistent with the combined dip.
- The dip is centered near 3.880 GHz and has neighboring suppressed points at 3.875 and 3.885 GHz, matching the expected several-MHz detuning response of a 52 ns near-pi pulse.

Decision:
The post-pulse readout shows a frequency-localized fluorescence reduction with the expected amplitude for a resonant near-pi Rabi pulse. A pODMR resonance is present.
