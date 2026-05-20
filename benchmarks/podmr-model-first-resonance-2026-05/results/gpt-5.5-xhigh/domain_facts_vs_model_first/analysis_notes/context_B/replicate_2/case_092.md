Case: podmr_078_2026-05-17-102220

Input files used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence: Rabimodulated.xml.
- The instructions first polarize and detect, then wait. Since full_expt = 0, the optional "Acquire 1 level reference" block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by detection.
- Readout 1 role: bright m_S = 0 reference after optical polarization, before the microwave Rabi pulse.
- Readout 2 role: signal after the modulated Rabi pulse.
- mod_depth: 1 from inputs/sequence.xml and the exported Variable_values.
- Pulse duration: length_rabi_pulse = 52 ns. The sample rate is 250 MHz, so the rounded duration is round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns.
- Scan: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points, 2 stored averages.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1 is about C = 0.22.
- Given Rabi frequency at mod_depth = 1 is about f_R = 10 MHz.
- For a square microwave pulse of duration t, the driven population transfer versus detuning df is
  P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2)).
- The expected driven/reference fluorescence ratio is then
  R2/R1 = 1 - C * P(df).
- At resonance, P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.9961, so the expected ratio is 1 - 0.22 * 0.9961 = 0.7809.
- With the measured mean readout 1 of 51.83 raw counts, an in-scan resonance should therefore lower readout 2 by about 51.83 * 0.22 * 0.9961 = 11.36 raw counts.
- Even if the resonance center fell halfway between 5 MHz-spaced scan points, df = 2.5 MHz gives P = 0.9292 and an expected ratio drop of 20.44%. At df = 5 MHz the expected ratio drop is still 16.47%.

Measured comparison:
- Mean readout 1 = 51.8306 raw counts.
- Mean readout 2 = 51.7601 raw counts.
- Mean readout2 - readout1 = -0.0705 raw counts.
- Across scan points, readout2 - readout1 ranges from -1.5962 to +2.0385 raw counts.
- The measured R2/R1 ratio has mean 0.9988, standard deviation 0.0228, minimum 0.9690, and maximum 1.0405.
- The largest observed relative drop is only 3.10% at 3.905 GHz, far smaller than the roughly 20-22% drop expected from the active 52 ns, mod_depth 1 pulse on resonance.

Model fit check:
- A constant R2/R1 model has SSE = 0.01040.
- Forcing the resonance center to lie inside the scanned frequency range gives best fixed-amplitude model SSE = 0.08823, much worse than the constant-ratio model, because the expected dip is much deeper than the data.
- Allowing a single overall scale factor still gives best in-scan resonance SSE = 0.06697, also much worse than constant.
- If the resonance center is allowed outside the scan, the best weak tail fit is above the scan near 3.94125 GHz and only creates a shallow edge effect; this is not evidence for an observed pODMR resonance in the scanned range.

Decision:
The active pulse should produce a large, readily visible pODMR dip if a resonance is present in the scan. The measured driven readout remains essentially equal to the bright reference, with only small fluctuations consistent with noise/tracking and no quantitatively compatible in-scan resonance. Prediction: resonance_absent.
