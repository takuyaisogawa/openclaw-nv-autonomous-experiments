Case: podmr_032_2026-05-16-201700

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- SequenceName is Rabimodulated.xml. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the XML variables, sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, mod_depth = 1, and full_expt = 0.
- The 52 ns Rabi pulse is already on the 4 ns sample grid: 52 ns = 13 samples.
- do_adiabatic_inversion is true in Bool_values, but the relevant reference block is disabled by full_expt = 0 and the adiabatic-inversion call is commented out. It is not active in this sequence execution.
- The active detections are therefore:
  - readout 1: detection immediately after adj_polarize, before the scanned Rabi pulse; this is the bright m_S = 0 reference.
  - readout 2: detection after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on); this is the pODMR signal readout.
- There is no active m_S = +1 reference readout in this run.

Quantitative expected-signal model:

Use the stated setup values: contrast C = 0.22 between m_S = 0 and m_S = +1, and Rabi frequency f_R = 10 MHz at mod_depth = 1. For a rectangular pulse of duration T = 52 ns, the driven population transfer versus detuning Delta is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * T * sqrt(f_R^2 + Delta^2)).

On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. The expected fractional fluorescence drop in readout 2 relative to readout 1 is therefore C * P(0) = 0.219, so the expected r2/r1 ratio is about 0.781. With the observed mean readout 1 of 55.26 counts, this corresponds to an expected on-resonance drop of about 12.1 counts.

The scan spacing is 5 MHz. If a resonance is inside the scan range, the nearest sampled point should be within 2.5 MHz. The same model gives P(2.5 MHz) = 0.929, still implying an expected fractional drop of about 0.204. Even at 5 MHz detuning the expected drop remains about 0.165.

Observed paired data:

- Mean r2/r1 = 1.0004 with standard deviation 0.0275 across the 21 scan points.
- The deepest observed combined paired drop is at 3.830 GHz: r2/r1 = 0.9582, a 4.18% drop.
- Several points go in the opposite direction; the largest is at 3.875 GHz: r2/r1 = 1.0729, a 7.29% increase.
- The two stored averages shift in overall level, consistent with tracking cadence, and neither average shows the expected roughly 20% notch. Their maximum paired drops are about 5.6% and 6.6%.

Model comparison on the paired ratio r = readout2 / readout1:

- No-resonance model r = constant: best constant = 1.0004, SSE = 0.0151, RMSE = 0.0268.
- Fixed physical resonance model r = mu - 0.22 * P(f - f0), with only mu and f0 fitted: best f0 is at the scan edge, 3.925 GHz, SSE = 0.0629, RMSE = 0.0547. This is 4.16 times worse than the flat model.
- If the resonance amplitude is allowed to float despite the physical contrast constraint, the best fit amplitude is negative, about -0.063 near 3.875 GHz, meaning the feature is a brightening rather than the expected pODMR dip.

Decision: resonance_absent. The active 52 ns mod_depth 1 pulse should create a large paired fluorescence dip if a resonance is sampled, but the measured paired readouts remain near unity and are better explained by no resonance plus small drift/noise.
