Case podmr_047_2026-05-17-001223

Files used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The exported scan identifies SequenceName = Rabimodulated.xml and vary_prop = mw_freq. The sequence instructions first polarize and detect:

  adj_polarize(...)
  detection(...)

This is labeled in the XML as acquiring the true 0 level reference, so readout 1 is the m_S = 0 reference readout. The optional 1-level reference block is guarded by full_expt:

  if abs(full_expt)>1e-12
      rabi_pulse_mod_wait_time(..., 52e-9, mod_depth, ...)
      detection(...)
  end

The exported variable full_expt is 0, so that block is inactive and no separate m_S = +1 reference is acquired. The active signal block is:

  rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)
  detection(...)

Thus readout 2 is the post-Rabi-pulse signal readout.

Relevant pulse parameters from the exported variable values:

  length_rabi_pulse = 5.2e-08 s = 52 ns
  mod_depth = 1
  sample_rate = 250 MHz, so 52 ns rounds to 13 samples exactly
  mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps

Explicit physical model calculation

Given the provided setup facts, the on-resonance Rabi frequency at mod_depth = 1 is about 10 MHz and scales linearly with mod_depth. Therefore this pulse has:

  f_R = 10 MHz
  t = 52 ns
  f_R * t = 0.52 cycles

Using the standard rectangular-pulse two-level transition probability,

  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) *
             sin^2(pi * t * sqrt(f_R^2 + Delta^2))

At resonance, Delta = 0:

  P(0) = sin^2(pi * 10e6 * 52e-9)
       = sin^2(0.52*pi)
       ~= 0.996

The current setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a real on-resonance pODMR response for this pulse should reduce the post-pulse readout by approximately:

  contrast * P(0) ~= 0.22 * 0.996 ~= 0.219

That is a roughly 21.9% fluorescence drop relative to the m_S = 0 reference. The readout-1 mean is 50.383 raw units, so the expected on-resonance dip size is:

  50.383 * 0.219 ~= 11.0 raw units

Expected signal shape: because the pulse is a nearly pi pulse at full modulation depth, a resonance inside the swept range should appear as a substantial localized readout-2 depression relative to readout 1, with the deepest point near 0.78 in the readout2/readout1 ratio, up to ordinary noise and baseline drift.

Observed data calculation

Combined readout means:

  mean(readout 1) = 50.383
  mean(readout 2) = 50.062
  mean(readout2 - readout1) = -0.321 raw units
  mean(readout2/readout1) = 0.994

Across all 21 frequency points:

  min(readout2/readout1) = 0.947
  max(readout2/readout1) = 1.051
  min(readout2 - readout1) = -2.731 raw units
  max(readout2 - readout1) = 2.538 raw units

The deepest observed relative drop is therefore only about 5.3%, or 2.73 raw units. This is much smaller than the approximately 21.9%, 11 raw unit dip expected from the active pulse if it were resonant. The largest negative points are also not a clean isolated resonance response: the ratio is low near 3.830 GHz and again across 3.905-3.920 GHz, then high at 3.925 GHz, which is more consistent with noise, drift, or readout mismatch than with the rectangular-pulse Rabi line shape.

Stored averages are not treated as strong independent repeatability evidence, per the provided domain fact, but they do show substantial per-average baseline/tracking variation. That reinforces using the combined readout-2/readout-1 signal scale and the explicit expected contrast calculation as the deciding evidence.

Decision

No pODMR resonance is present. The active 52 ns, mod_depth 1 pulse should produce a near-full-contrast on-resonance response of about 22%, but the observed frequency-dependent signal is only a few percent and does not match the expected resonance scale or shape.
