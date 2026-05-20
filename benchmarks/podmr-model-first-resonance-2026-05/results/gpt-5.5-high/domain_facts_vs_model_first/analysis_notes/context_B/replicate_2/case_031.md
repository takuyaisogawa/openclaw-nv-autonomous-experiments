Case: podmr_016_2026-05-16-131456

Sequence identification:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is disabled.
- Readout 1 role: polarized m_S = 0 reference after adj_polarize and before the microwave pulse.
- Readout 2 role: signal readout after the Rabi-modulated microwave pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.

Quantitative model:
The relevant signal is readout 2, not the reference readout. With the supplied setup facts, the Rabi frequency at mod_depth = 1 is approximately 10 MHz. For a square pulse of duration T = 52 ns, I used the driven two-level transition probability

P(f; f0) = (f_R^2 / (f_R^2 + detuning^2)) * sin^2(pi * T * sqrt(f_R^2 + detuning^2)),

where f_R = 10 MHz and detuning = f - f0 in Hz. On resonance this gives P = sin^2(pi * 10e6 * 52e-9) = 0.996, so the pulse is essentially a pi pulse. Given a contrast scale of 22%, a baseline near 46.7 counts would allow an ideal resonant depletion of about 10.3 counts in the signal readout.

Observed data:
- Readout 2 has a clear trough at 3.875-3.880 GHz: 39.65 and 39.62 counts.
- The off-resonance readout 2 mean excluding the trough neighborhood is about 46.71 counts with standard deviation about 0.75 counts.
- The observed minimum depletion is about 7.10 counts, or 15.2% of the off-resonance level.
- Readout 1 remains near 47 counts and does not show the same trough, consistent with it being a reference/tracking readout rather than the microwave-sensitive signal.

Model fit:
I fit readout 2 to a linear baseline plus the square-pulse depletion model above, allowing the resonance center and depletion amplitude to vary. The best fit found:
- resonance center f0 = 3.87745 GHz,
- fitted baseline near 47.01 counts,
- fitted depletion amplitude = 8.49 counts,
- SSE = 13.98.

A linear no-resonance baseline fit gave SSE = 132.46. The resonance model therefore reduces the squared residual by about 118.48 while using a physically expected lineshape and pulse duration. The fitted amplitude is somewhat below the ideal 22% contrast expectation but is of the right order and substantially larger than the off-resonance scatter. Stored per-average traces both show the same trough qualitatively, but I do not treat the two stored averages as a strong independent repeatability test because stored averages can reflect tracking cadence.

Decision:
The active post-pulse readout contains a quantitatively large, physically consistent pODMR depletion centered near 3.877 GHz. A pODMR resonance is present.
