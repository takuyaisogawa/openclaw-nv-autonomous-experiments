Case podmr_058_2026-05-17-053345

Sequence and readout roles

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt is 0, so the conditional "Acquire 1 level reference" block is inactive. The executed readouts are therefore:

1. After adj_polarize: true m_S = 0 reference readout.
2. After rabi_pulse_mod_wait_time followed by detection: signal readout after the microwave pulse.

The provided XML has length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns, and mod_depth = 1. The embedded sequence text in raw_export.json also shows 52 ns but contains mod_depth = 0.3, while the exported Variable_values table lists mod_depth = 1. The standalone sequence.xml and Variable_values both support mod_depth = 1; I also checked the weaker mod_depth = 0.3 interpretation as a conservative bound.

Quantitative physical model

Use the Rabi transition probability

P_transfer = sin^2(pi * f_Rabi * tau)

with f_Rabi about 10 MHz * mod_depth and optical contrast C = 0.22 between m_S = 0 and m_S = +1. For a resonant microwave pulse, the expected fractional drop in the signal readout relative to the m_S = 0 reference is

drop_fraction = C * P_transfer.

For tau = 52 ns:

- If mod_depth = 1, f_Rabi = 10 MHz, P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996. Expected drop_fraction = 0.219, so signal/reference should be about 0.781. At a 45-count baseline this is about a 9.9-count dip.
- If mod_depth = 0.3, f_Rabi = 3 MHz, P_transfer = sin^2(pi * 3e6 * 52e-9) = 0.222. Expected drop_fraction = 0.0487, so signal/reference should be about 0.951. At a 45-count baseline this is about a 2.2-count dip.

Data check

The combined readout-1 mean is 45.681 and readout-2 mean is 45.584, for a mean signal/reference ratio of 0.9984. The point with the largest apparent drop is at 3.890 GHz, where readout 1 = 46.962 and readout 2 = 43.731, ratio = 0.9312, a 6.88% drop. Other apparent drops of similar size occur at isolated points, including 3.885, 3.910, and 3.925 GHz, without a coherent single resonance feature. The largest observed drop is far smaller than the 21.9% expected for the provided XML's mod_depth = 1 pi pulse, and it is not localized in a way that supports a pODMR resonance. Even under the weaker mod_depth = 0.3 interpretation, the few possible 5-7% drops are comparable to point scatter and are not a stable resonance signature.

Decision

No pODMR resonance is present in this scan. The active signal readout does not show the quantitative contrast expected from the sequence's resonant Rabi pulse model.
