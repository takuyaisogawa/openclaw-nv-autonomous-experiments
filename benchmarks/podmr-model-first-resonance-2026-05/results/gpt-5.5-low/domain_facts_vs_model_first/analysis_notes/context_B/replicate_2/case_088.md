Case podmr_074_2026-05-17-092418

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels,
previous outputs, sibling cases, or external context.

Active sequence and readout roles:
- Sequence name from the export is Rabimodulated.xml, matching the provided
  Rabimodulated-style XML.
- The instructions first run adj_polarize followed by detection. This is the
  true m_S = 0 reference readout.
- full_expt is 0, so the optional m_S = 1 reference block is inactive.
- The active signal block then applies rabi_pulse_mod_wait_time with
  length_rabi_pulse and mod_depth, followed by detection. This is the pODMR
  microwave-pulse readout.
- In the provided XML, length_rabi_pulse is 5.2e-08 s (52 ns) and mod_depth is
  1. The raw export also contains an embedded sequence string with mod_depth
  0.3, so I checked that as a sensitivity case, but the decision below is made
  against the provided XML as requested.

Explicit model calculation:
- Setup contrast between m_S = 0 and m_S = +1 is about C = 0.22.
- Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with
  mod_depth.
- For a square resonant pulse, transition probability is
  P = sin^2(pi * f_Rabi * tau), where f_Rabi is in cycles/s.
- With mod_depth = 1: f_Rabi = 10 MHz, tau = 52 ns,
  P = sin^2(pi * 10e6 * 52e-9) = 0.996. The expected fractional fluorescence
  drop at resonance is C * P = 0.219, or about 10.75 raw-count units for a
  49.08-count reference.
- Sensitivity check using the embedded export sequence value mod_depth = 0.3:
  f_Rabi = 3 MHz, P = 0.222, expected fractional drop = 0.0487, or about
  2.39 raw-count units.

Data comparison:
- The combined reference readout mean is 49.08 and the signal readout mean is
  48.78.
- Signal minus reference has mean -0.29, standard deviation 1.72, minimum
  -3.92 at 3.900 GHz, and maximum +2.31 at 3.920 GHz.
- A true resonance under the provided XML should produce a near-pi-pulse dip
  around 10.8 counts, far larger than any observed point.
- Even under the lower mod_depth = 0.3 sensitivity check, the largest apparent
  dip is not robust across stored averages: at 3.900 GHz the two average-level
  differences are about -6.92 and -0.92 counts, respectively. The second stored
  average does not reproduce a clear resonance-scale dip.
- The readout-2 trace also rises above readout 1 at nearby high-frequency
  points, which is inconsistent with a stable pODMR resonance line shape.

Decision:
The quantitative expected signal from the active physical model is not present
in the measured readouts. The observed structure is small relative to the
mod_depth = 1 expected contrast and not repeatable enough to support a
resonance call in the lower-power sensitivity check. I therefore classify this
case as resonance_absent.
