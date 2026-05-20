Case: podmr_040_2026-05-16-222642

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification and readout roles:
- SequenceName in the export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence.xml has length_rabi_pulse = 5.2e-08 s, mod_depth = 1, sample_rate = 250 MHz, freqIQ = 50 MHz, and full_expt = 0.
- Because full_expt = 0, the "Acquire 1 level reference" block is skipped.
- The active measurement per scan point is therefore:
  1. adj_polarize followed by detection: true m_S = 0 reference readout.
  2. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth) followed by detection: MW-driven pODMR signal readout.

Quantitative physical model:
- The setup contrast between m_S = 0 and m_S = +1 is about C = 0.22.
- The Rabi frequency is about 10 MHz at mod_depth = 1, and the XML uses mod_depth = 1.
- For a square driven pulse of duration t = 52 ns, the transition probability versus detuning Delta is
  P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t),
  using f_R and Delta in cycles/s.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Therefore the expected normalized signal readout on resonance is 1 - C*P(0) = 0.781, a 21.9% drop from the m_S = 0 reference.
- With 5 MHz scan spacing, even if the true resonance fell halfway between two sampled points, the nearest sampled detuning would be 2.5 MHz, giving P = 0.929 and an expected drop of 20.4%. At a typical reference readout of 47 counts, this is a 9.6 to 10.3 count dip.

Observed data:
- Combined reference readout mean: 47.19 counts.
- Combined signal readout mean: 46.66 counts.
- The normalized drop (reference - signal) / reference has mean 1.08%, standard deviation 2.83%, and maximum 7.63%.
- The largest apparent dip is at 3.885 GHz: reference 48.37, signal 44.67, drop 3.69 counts or 7.63%.
- The two stored averages both show a low point near 3.885 GHz, but their maximum normalized drops are about 9.25% and 6.21%. These stored averages mainly reflect tracking cadence and are not a strong independent repeatability test.

Model-data comparison:
- A real in-range pODMR resonance under the provided XML parameters should produce a broad, sampled dip near 20-22% at one or more nearby frequency points.
- The observed maximum drop is only about one third of the expected minimum sampled resonant drop, and neighboring points do not follow the calculated Rabi-detuned line shape.
- Fitting a fixed-amplitude 22% resonance shape prefers placing the resonance outside the scan range rather than inside it, because an in-range resonance would overpredict the dip.

Decision:
The expected signal from the active sequence is much larger than the measured deviations. The data do not support a pODMR resonance in the scanned range.
