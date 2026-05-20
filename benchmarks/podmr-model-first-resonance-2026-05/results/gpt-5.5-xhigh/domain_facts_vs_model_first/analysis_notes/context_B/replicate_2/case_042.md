Case: podmr_028_2026-05-16-185605

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence/readout interpretation

- SequenceName in the export is Rabimodulated.xml.
- The provided sequence XML sets full_expt = 0, so the optional "Acquire 1 level reference" block is disabled.
- The active detections are therefore:
  - readout 1: after adj_polarize, before the microwave pulse; this is the true mS = 0 reference.
  - readout 2: after rabi_pulse_mod_wait_time; this is the pODMR signal readout.
- The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- From the provided sequence XML and exported variable table: length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model

Using the supplied domain facts, the resonant Rabi frequency is approximately

  f_R = 10 MHz * mod_depth = 10 MHz.

For a square Rabi pulse scanned in microwave frequency, I modeled the transferred mS = +1 population as

  P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)),

where Delta is the microwave detuning in Hz and t = 52 ns. On resonance:

  P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With a 22% mS = 0 to mS = +1 fluorescence contrast scale, the expected resonant fractional drop in the post-pulse readout relative to the mS = 0 reference is

  0.22 * 0.996 = 0.219, or about 21.9%.

The measured mean readout 1 level is 51.718 raw units, so the expected resonant drop is about

  51.718 * 0.219 = 11.33 raw units.

Observed data check

The observed contrast estimator for the active signal is

  C_obs = (readout1 - readout2) / readout1.

Across the 21 frequency points:

- mean C_obs = 0.0026
- standard deviation of C_obs = 0.0236
- maximum positive C_obs = 0.0554 at 3.885 GHz, corresponding to a 2.98 raw-unit drop
- minimum C_obs = -0.0504 at 3.890 GHz, where the post-pulse readout is brighter than the reference

The per-average stored traces are not an independent repeatability test because they can reflect tracking cadence, but they show similar scale: the pooled per-average contrast standard deviation is about 0.035.

I also fit the square-pulse model above over possible resonance centers in the scanned range. Fitting C_obs = b + A*P(Delta) gave:

- best center about 3.87895 GHz
- fitted amplitude A = 0.055
- baseline b = -0.0073
- RMS residual = 0.0170

The physically expected amplitude is approximately 0.219, about four times larger than the best fitted positive feature. Holding A fixed at 0.219 would require a modeled contrast peak around 0.179 after baseline offset at the best center, while the observed point near the modeled maximum is only about 0.037. In raw units, the expected pi-pulse resonance would place the post-pulse readout roughly 11 counts below the reference; the largest observed drop is only about 3 counts and is followed immediately by an opposite-sign excursion.

Decision

Given the active readout roles and the quantitative square-pulse Rabi model, a true pODMR resonance should produce a large, Rabi-broadened fluorescence dip in readout 2 relative to readout 1. The measured contrasts are near zero with only small tracking/noise-scale excursions and no physically sized resonance feature. I therefore decide that a pODMR resonance is absent.
