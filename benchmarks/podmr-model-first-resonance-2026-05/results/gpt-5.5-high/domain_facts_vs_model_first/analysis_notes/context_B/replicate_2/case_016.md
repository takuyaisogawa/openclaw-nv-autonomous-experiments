Case podmr_001_2026-05-16-000631

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name in the export: Rabimodulated.xml.
- The instructions first polarize the NV and immediately run detection. This is readout 1, the bright m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive. The adiabatic inversion flag is therefore not used for the acquired readouts.
- The active signal block is a single rabi_pulse_mod_wait_time followed by detection. This is readout 2, the microwave-pulse signal readout.
- mod_depth = 1 in inputs/sequence.xml and in Variable_values.
- length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the rounded pulse duration remains 52 ns.

Quantitative model:
- Given setup Rabi frequency at mod_depth = 1: Omega = 10 MHz.
- Pulse duration: t = 52 ns.
- On-resonance transfer probability for a rectangular Rabi pulse:
  P(Delta=0) = sin^2(pi * Omega * t)
             = sin^2(pi * 10e6 * 52e-9)
             = sin^2(0.52*pi)
             = 0.996.
- Expected fluorescence model:
  F_signal(Delta) = F_bright * (1 - C * P(Delta)),
  where C = 0.22 and
  P(Delta) = Omega^2/(Omega^2 + Delta^2) * sin^2(pi * t * sqrt(Omega^2 + Delta^2)).
- The mean bright reference from readout 1 is 37.757 counts. The expected on-resonance signal is
  37.757 * (1 - 0.22 * 0.996) = 29.483 counts, an expected drop of 8.274 counts.

Observed data:
- Readout 2 has a minimum of 28.981 counts at 3.880 GHz.
- A selected off-resonance readout 2 baseline is 37.544 counts, giving an observed dip of 8.564 counts.
- The observed minimum ratio to the bright reference mean is 28.981 / 37.757 = 0.768, close to the expected resonant ratio 1 - 0.22 * 0.996 = 0.781.

Explicit line-shape comparison:
- I fit the rectangular-pulse model above with a free resonance center and a single scale factor multiplying the bright reference.
- Best center: 3.8774 GHz.
- Resonant-model SSE: 35.603.
- No-resonance model r2 = scale * r1 SSE: 157.309.
- The no-resonance SSE is 4.42 times larger than the resonant-model SSE.

Decision:
The active pulse is expected to create an approximately 22% dip if the scanned microwave frequency crosses the transition, and the observed readout 2 dip has the expected depth, location-localized shape, and line-shape improvement over a no-resonance model. A pODMR resonance is present.
