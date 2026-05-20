Case: podmr_010_2026-05-11-155154

Input basis

- Used only the local files in this workspace: inputs/sequence.xml and inputs/raw_export.json.
- The active sequence is Rabimodulated.xml / Rabimodulated-style pODMR. The instructions perform:
  1. adj_polarize
  2. detection
  3. wait
  4. optional "1 level reference" block only if full_expt is nonzero
  5. rabi_pulse_mod_wait_time
  6. detection
- full_expt is 0, so the optional 1-level reference block is inactive.
- Therefore readout 1 is the pre-microwave bright mS = 0 reference, and readout 2 is the post-Rabi-pulse signal readout.
- Active mod_depth is 1.
- Active Rabi pulse duration is 52 ns.

Quantitative physical model

Given setup facts:

- Contrast between mS = 0 and mS = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Rabi frequency scales linearly with mod_depth, so f_R = 10 MHz for this scan.
- Pulse duration: t = 52 ns.

For resonant driving of a two-level transition, the transfer probability after a square pulse is:

P_transfer = sin^2(pi * f_R * t)

Substituting:

pi * f_R * t = pi * 10e6 * 52e-9 = 1.6336 rad
P_transfer = sin^2(1.6336) = 0.9961

The expected fluorescence reduction in the post-pulse readout at resonance is:

expected fractional drop = C * P_transfer = 0.22 * 0.9961 = 0.2191

The measured mean of readout 1 is 39.826 counts, so an on-resonance point should be reduced by:

expected drop = 39.826 * 0.2191 = 8.73 counts

That gives an expected resonant post-pulse signal near:

39.826 - 8.73 = 31.10 counts

Data check

- Combined readout 1 mean: 39.826 counts.
- Combined readout 2 mean: 39.261 counts.
- Mean readout2 - readout1: -0.565 counts.
- Minimum combined readout 2: 35.923 counts at 3.830 GHz.
- In the central scan region around 3.85 to 3.90 GHz, readout 2 ranges from 38.25 to 40.79 counts.
- The largest observed readout2-readout1 deficit is -3.87 counts, much smaller than the modeled 8.73-count resonant drop and not a clean localized pODMR dip.

Decision

The active sequence should produce a large post-pulse fluorescence dip if a pODMR resonance is present, because the 52 ns pulse at mod_depth 1 is essentially a pi pulse under the stated 10 MHz Rabi calibration. The observed readout 2 trace stays close to the reference and lacks the expected approximately 22% localized reduction. Stored per-average traces appear dominated by drift/tracking cadence and do not provide independent support for a resonance.

Prediction: resonance_absent
