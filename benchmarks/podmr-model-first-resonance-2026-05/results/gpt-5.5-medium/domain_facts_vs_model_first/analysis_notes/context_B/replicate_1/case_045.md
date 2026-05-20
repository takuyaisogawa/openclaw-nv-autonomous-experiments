Case podmr_031_2026-05-16-195907

Sequence interpretation:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR scan with mw_freq varied from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Relevant active branch: full_expt = 0, so the optional m_S = +1 reference block is skipped.
- Readout 1 role: after adj_polarize, before the microwave pulse; this is the m_S = 0 fluorescence reference.
- Readout 2 role: after a modulated Rabi microwave pulse; this is the pODMR signal readout.
- Pulse parameters used for the decision: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. Rounding to sample clock leaves 52 ns because 52 ns * 250 MHz = 13 samples.

Physical model calculation:
Given the supplied setup facts, f_Rabi ~= 10 MHz at mod_depth = 1. For a square pulse of duration t = 52 ns, the transition probability versus detuning df is

P(df) = f_Rabi^2 / (f_Rabi^2 + df^2) * sin^2(pi * t * sqrt(f_Rabi^2 + df^2)).

On resonance, pi * f_Rabi * t = pi * 10e6 * 52e-9 = 1.6336 rad, so P(0) = sin^2(1.6336) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected fractional fluorescence loss in readout 2 relative to the readout 1 reference is about 0.22 * 0.996 = 21.9%.

The scan step is 5 MHz. If a resonance lies anywhere inside the scanned range, the nearest sampled frequency is within 2.5 MHz. At df = 2.5 MHz, the same model gives P = 0.929 and expected loss = 20.4%. Even at df = 5 MHz the expected loss is 16.5%. With the observed reference level near 52.7 counts, a sampled resonance should therefore pull the signal readout to roughly 41.9 counts at worst for nearest-grid sampling, or about 44.0 counts at 5 MHz detuning.

Observed data:
- Mean readout 1 = 52.721 counts.
- Mean readout 2 = 52.728 counts.
- The largest readout-2 loss relative to readout 1 is at 3.920 GHz: readout 1 = 55.538, readout 2 = 51.596, fractional loss = 7.10%.
- Other negative excursions are smaller: 4.02% at 3.845 GHz and 3.42% at 3.885 GHz.
- The per-average overlays are strongly shifted in absolute level, consistent with stored averages being dominated by tracking cadence rather than an independent repeatability check.

Decision:
The active 52 ns, mod_depth = 1 pulse is effectively a pi pulse on resonance, so the expected pODMR contrast on the sampled grid is around 20% if a resonance is present. The observed signal never approaches that scale; the strongest apparent dip is only about 7% and is not a convincing match to the expected Rabi response. I therefore classify this case as resonance_absent.
