# reimage1804_c02 strong-pi pODMR plan (20260514_1915)

Candidate `reimage1804_c02` passed standalone TrackCenter with final_counts_kcps=39.690 at [117.4211443249154, 117.27496844942901, 115.55260043233898] um. This follows rejection of `reimage1804_c01` by terminal strong-pi pODMR (healthy counts, no clear usable resonance).

Planned screen: `pulsed_odmr_rabimodulated_v1` / `Rabimodulated.xml`, mw_freq 3.825..3.925 GHz, 31 points, 4 averages x 50000 repetitions, mod_depth=1, length_rabi_pulse=52 ns, mw_ampl=-5, ampIQ=5, freqIQ=50 MHz. Averages are even.

Model calculation: with 52 ns strong-pi pulse, rectangular sinc FWHM is about 15.37 MHz. The 100 MHz scan at 31 points gives 3.333 MHz spacing, about 4.6 points across the expected width. Expected resonant signal dip is about 22% versus a binomial shot-noise floor near 0.224% for 200000 total shots, so an aligned in-window resonance should be visible in terminal raw/readout-aware review.

XML/manifest review: manifest is staging `pulsed_odmr_rabimodulated_v1` pointing to `Rabimodulated.xml`; with `full_expt=0`, the first detection is mS=0 reference and the final detection after `length_rabi_pulse` is signal. The mS=+1 reference block is disabled. Judge signal presence from raw signal and fitted-reference-normalized views; do not promote point-wise-normalization-only features.

Safety gates before enqueue: experiment intent verification, queue idle re-check, advisory/pre-enqueue JSON ok with no blockers, and project lifecycle still active.
