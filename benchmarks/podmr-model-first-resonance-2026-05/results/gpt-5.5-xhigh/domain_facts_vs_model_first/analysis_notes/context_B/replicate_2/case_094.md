Case: podmr_080_2026-05-17-105113

Input basis used:
- Used inputs/sequence.xml for the active sequence parameters, as requested.
- Sequence name in the export is Rabimodulated.xml and the scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active sequence with full_expt = 0:
  1. adj_polarize
  2. detection: readout 1, the bright m_S = 0 reference
  3. wait_for_awg
  4. rabi_pulse_mod_wait_time with length_rabi_pulse
  5. detection: readout 2, the post-microwave pODMR signal
- The conditional "Acquire 1 level reference" block is inactive because full_expt = 0.
- From the provided XML: mod_depth = 1, length_rabi_pulse = 5.2e-08 s, sample_rate = 250 MHz. Rounding length_rabi_pulse to the sample grid leaves 52 ns exactly.

Physical model calculation:
- Given setup facts: contrast C = 0.22 between m_S = 0 and m_S = +1; Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a square pulse, the driven population transfer versus detuning df is:

  P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2))

  using f_R and df in cycles/s.
- At resonance, t = 52 ns and f_R = 10 MHz, so:

  P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996

- Expected resonant fractional fluorescence dip in readout 2 relative to readout 1:

  C * P(0) = 0.22 * 0.996 = 0.219

- The measured readout 1 mean is 51.671 counts, so the expected resonant count dip is:

  51.671 * 0.219 = 11.323 counts

  giving an expected on-resonance readout 2 near 40.35 counts.
- Because the scan step is 5 MHz, a resonance between points should still be visible. The same model gives:
  - df = 2.5 MHz: P = 0.929, expected dip = 20.4% = 10.56 counts
  - df = 5.0 MHz: P = 0.749, expected dip = 16.5% = 8.51 counts
  - df = 10.0 MHz: P = 0.273, expected dip = 6.0% = 3.10 counts

Measured data check:
- Combined readout 1: mean = 51.671, sd across scan = 0.777, min = 50.404, max = 53.154.
- Combined readout 2: mean = 51.700, sd across scan = 0.888, min = 50.173, max = 53.481.
- Difference readout2 - readout1: mean = +0.028 counts, sd = 0.884 counts, min = -1.808 counts, max = +1.519 counts.
- Normalized contrast estimate 1 - readout2/readout1: mean = -0.0007, sd = 0.0171, max positive dip = 0.0346 at 3.895 GHz.

Model comparison:
- The maximum observed normalized dip, 3.46%, is about 6.3 times smaller than the expected on-resonance 21.9% dip and far smaller than the expected 16.5-20.4% dip for a resonance within one scan step.
- The largest observed count deficit, 1.81 counts, is also far below the 8.5-11.3 count deficit expected from the sequence-derived model.
- A least-squares scan of the expected Rabi response shape over possible resonance centers prefers a negative amplitude in the normalized contrast, i.e. the opposite sign from a pODMR fluorescence dip. Forcing the physical 22% amplitude makes the residual much worse than an offset-only null model.
- The two stored averages differ mainly by a baseline offset consistent with tracking cadence; they do not provide a strong independent repeatability test for a resonance.

Decision:
The active sequence should produce a large post-pulse fluorescence dip if a resonance is present, but the measured readout 2 trace stays essentially at the readout 1 reference level with only percent-scale fluctuations. I therefore classify this case as resonance_absent.
