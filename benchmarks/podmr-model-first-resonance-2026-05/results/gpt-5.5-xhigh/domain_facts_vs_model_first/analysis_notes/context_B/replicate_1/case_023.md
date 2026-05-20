Case: podmr_008_2026-05-16-014743

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence interpretation from inputs/sequence.xml:
- Sequence name in the export is Rabimodulated.xml; the varied property is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active variables after ignoring XML/MATLAB comments: sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, detuning = 0.
- The code rounds length_rabi_pulse to the sample grid. At 250 MHz, 52 ns is exactly 13 samples, so the active pulse duration remains 52 ns.
- Readout 1 role: after adj_polarize and before any active microwave pulse, so it is the bright m_s=0 reference/readout.
- The optional "Acquire 1 level reference" block is disabled because full_expt = 0, so it does not define an active readout here.
- Readout 2 role: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the pODMR signal readout after the microwave pulse.

Quantitative physical model:
- Given setup fact: f_Rabi approximately 10 MHz at mod_depth = 1 and linear in mod_depth.
- Therefore f_Rabi = 10 MHz for this sequence.
- For a rectangular resonant pulse, transfer probability to m_s=+1 is P = sin^2(pi * f_Rabi * t).
- With t = 52 ns, P_res = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Given contrast scale C = 0.22, expected fractional optical loss on resonance is C * P_res = 0.219, or about 22%.
- The off-resonance median of readout 2, excluding the deepest point +/- 20 MHz, is 41.29 counts. The expected resonant minimum is 41.29 * (1 - 0.219) = 32.24 counts.

Observed data comparison:
- The deepest readout-2 point is 31.31 counts at 3.875 GHz, with the next point 32.31 counts at 3.880 GHz.
- Relative to the off-resonance readout-2 median of 41.29 counts, the deepest point is a 24.2% drop, close to the 21.9% expected drop.
- The readout-1 value at the deepest readout-2 point is 42.46 counts, so the dip is not a common drop in both readouts.
- Per stored average, the readout-2 fractional drops at the same frequency are 22.0% and 25.7%. The stored averages are tracking-cadence limited rather than a strong repeatability test, but both averages show the expected-size dip.

Explicit lineshape simulation:
- I evaluated the rectangular-pulse detuned Rabi response
  P(delta) = f_Rabi^2 / (f_Rabi^2 + delta^2) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2))
  and modeled readout2 = baseline * (1 - 0.22 * P(delta)).
- Least-squares fit over resonance center and baseline gave f0 = 3.8774 GHz, baseline = 41.35, and predicted minimum = 32.85 counts.
- The physical lineshape model SSE was 29.3, compared with 199.6 for a constant no-resonance baseline, a 6.8x improvement.

Decision:
The observed readout-2 dip has the amplitude, frequency-localized shape, and readout-role specificity expected for pODMR under the extracted pulse settings. Resonance is present.
