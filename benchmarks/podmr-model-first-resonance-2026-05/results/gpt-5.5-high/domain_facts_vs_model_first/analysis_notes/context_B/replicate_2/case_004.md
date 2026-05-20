Case: podmr_007_2026-05-11-064944

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles
- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instruction block polarizes first, then calls detection before the microwave pulse. This first detection is the bright m_S = 0 reference, corresponding to readout 1.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active measurement pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This post-pulse detection is readout 2.
- length_rabi_pulse = 52 ns after sample-rate rounding because 52 ns is exactly 13 samples at 250 MS/s.
- mod_depth = 1 in the provided sequence XML.

Explicit signal model
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency scale: f_R = 10 MHz at mod_depth = 1.
- For a square pulse, the driven population transfer probability versus detuning delta is
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  using f_R and delta in cycles/s.
- At zero detuning with t = 52 ns:
  P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52 pi) = 0.996.
- The expected fractional fluorescence drop in readout 2 relative to readout 1 is therefore
  C * P(0) = 0.22 * 0.996 = 0.219, or about 21.9%.
- The observed readout scale is about 31.7 counts, so an on-resonance point should drop by about
  31.7 * 0.219 = 7.0 counts.
- Because the scan step is 5 MHz, any resonance inside the scan range should be sampled within at most 2.5 MHz. At delta = 2.5 MHz, the same model gives P = 0.929, or an expected drop of about 6.5 counts.
- Even at delta = 5 MHz, the expected drop remains about 5.2 counts.

Data comparison
- Combined readout 1 mean and standard deviation: 31.72 +/- 0.95 counts.
- Combined readout 2 mean and standard deviation: 31.55 +/- 1.21 counts.
- The paired difference readout2 - readout1 has mean -0.18 counts and standard deviation 1.70 counts.
- The largest paired darkening is -3.81 counts at 3.855 GHz; the next notable darkening is -3.00 counts at 3.895 GHz.
- These excursions are far smaller than the 6.5 to 7.0 count drop expected from the active near-pi pulse if a pODMR resonance were being sampled.
- The readout 2 trace alone also does not show a corresponding large resonance-scale dip: its minima near those points are only about 1.4 to 1.6 counts below the readout 2 mean.
- The per-average overlays show those two negative excursions in both stored averages, but stored averages can reflect tracking cadence and are not a strong independent repeatability test. Quantitatively, their amplitudes still fall well short of the model expectation for mod_depth = 1 and 52 ns.

Decision
The active pulse should create a large near-pi pODMR dip if a resonance is present in the scanned range, but the observed readout changes are noise-scale and substantially below the expected signal. I therefore classify this case as resonance_absent.
