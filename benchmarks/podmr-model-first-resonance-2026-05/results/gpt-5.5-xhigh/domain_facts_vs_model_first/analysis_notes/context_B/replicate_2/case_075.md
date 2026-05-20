Case: podmr_061_2026-05-17-061719

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:

- The active sequence is Rabimodulated.xml.
- The scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, mod_depth = 1, freqIQ = 50 MHz, mw_ampl = -5 dBm, ampIQ = 5 dBm.
- The pulse duration is rounded by the sequence to round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns.
- The active instructions first polarize and detect a true m_s = 0 bright reference. Since full_expt = 0, the optional m_s = 1 reference branch is skipped. The sequence then applies one modulated Rabi pulse and detects the post-microwave signal.
- Therefore readout 1 is the bright m_s = 0 reference, and readout 2 is the post-Rabi-pulse pODMR signal.

Quantitative physical model:

For a rectangular pulse with cyclic on-resonance Rabi frequency f_R = 10 MHz at mod_depth = 1 and pulse duration t = 52 ns, the transition probability as a function of detuning Delta is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The measured bright reference level is about 49.62 counts. With a stated m_s = 0 to m_s = +1 contrast scale of 22%, a resonant pi-like pulse should reduce the signal readout by approximately

0.22 * 49.62 * 0.996 = 10.87 counts,

or about 21.9% relative to the reference. The expected sampled detuning response is also broad enough that adjacent 5 MHz samples around a true resonance should show large drops: at +/-5 MHz the model gives P = 0.749, an expected drop of 8.17 counts; at +/-10 MHz it gives P = 0.273, an expected drop of 2.98 counts.

Data comparison:

The measured combined readout differences signal - reference have mean -0.529 counts and standard deviation 1.723 counts. The largest signal deficit is -3.788 counts at 3.830 GHz, with another isolated -3.731 counts at 3.880 GHz. These are only about 7.4% to 7.5% of the local reference, far below the expected 21.9% on-resonance contrast for the active pulse.

The strongest deficits are isolated rather than accompanied by the expected neighboring structure from the 52 ns Rabi lineshape. For example, a resonance centered at 3.880 GHz should have produced a roughly 10.87-count drop at 3.880 GHz and roughly 8.17-count drops at 3.875 and 3.885 GHz. Instead, the observed contrast values at 3.875, 3.880, and 3.885 GHz are -1.27%, +7.53%, and +0.27%, respectively.

I also fit the measured contrast y = (reference - signal) / reference to the same Rabi lineshape. A constant-contrast model has RSS 0.02396. An unconstrained best fit inside the scanned window prefers a negative resonance amplitude, which is unphysical for an ODMR dip. A nonnegative-amplitude fit gives only A = 0.0308, far below the expected A = 0.22. Forcing A = 0.22 anywhere inside the scan gives much worse residuals, with the best fixed-amplitude RSS 0.08196.

The two stored averages do not provide strong independent repeatability evidence here, and the prompt notes that stored averages often reflect tracking cadence. Their per-average difference traces are inconsistent at the candidate dip positions rather than showing a stable expected resonance profile.

Decision:

Given the active 52 ns, mod_depth = 1 pulse, a real pODMR resonance should produce a large, structured reference-to-signal drop near the resonance. The observed signal deficits are small, isolated, and not matched to the quantitative Rabi response. I therefore classify this case as resonance absent.
