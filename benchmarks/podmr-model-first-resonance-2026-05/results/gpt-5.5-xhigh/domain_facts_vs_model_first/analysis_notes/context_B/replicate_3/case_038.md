case_id: podmr_023_2026-05-16-174219
timestamp: 2026-05-16-174219

Sequence/readout identification:
- The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets full_expt = 0, so the optional "1 level reference" branch is skipped.
- The two recorded readouts are therefore:
  - readout 1: true m_s = 0 bright reference after adj_polarize and detection, before the microwave pulse.
  - readout 2: signal detection after a rabi_pulse_mod_wait_time microwave pulse.
- Stored pulse settings: mod_depth = 1, length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded duration remains 52 ns.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and approximately linear scaling, the active pulse has f_R = 10 MHz.
- For a rectangular resonant pulse, the transfer probability is
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).
- At zero detuning with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the setup contrast scale C = 0.22, the expected normalized post-pulse signal on resonance is
  readout2/readout1 = 1 - C * P(0) = 0.781.
- Since the scan step is 5 MHz, a resonance inside the scan would be within at most 2.5 MHz of a sampled point. At delta = 2.5 MHz, the model gives P = 0.929 and readout2/readout1 = 0.796. Thus a real in-scan resonance should produce an approximately 20-22 percent dip in readout 2 relative to readout 1 at at least one sampled frequency.

Data comparison:
- The measured readout2/readout1 ratios range from 0.949 to 1.068, with mean 1.003 and standard deviation 0.031.
- The largest observed positive readout1-readout2 difference is 2.48 counts, while the expected on-resonance drop from the mean reference level is about 47.55 * 0.219 = 10.42 counts.
- A free dip fit using the same Rabi line shape finds only about a 5.3 percent fractional dip, far below the 21.9 percent expected physical contrast. A fixed-contrast model is not supported by the observed ratios.
- The stored per-average traces show substantial baseline/tracking changes, so they are not treated as strong independent repeatability evidence.

Decision:
The expected pODMR resonance for this pulse should be a large, sampled dip in the post-pulse signal relative to the 0-state reference. The measured data do not contain such a dip, so I classify this case as resonance_absent.
