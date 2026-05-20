Case podmr_078_2026-05-17-102220

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- SequenceName is Rabimodulated.xml.
- The XML instructions first polarize and detect, giving the true m_S = 0 reference readout.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped; there is no active m_S = +1 reference readout in this data.
- The active measurement readout is after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- The two stored readouts are therefore: readout 1 = m_S = 0 reference, readout 2 = pulsed MW readout.

Pulse parameters:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- Frequency scan: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Expected signal model:
- Given setup Rabi frequency about 10 MHz at mod_depth = 1, use f_R = 10 MHz.
- For a square resonant Rabi pulse, transition probability P = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- The m_S = 0 to m_S = +1 contrast scale is about 22%.
- Mean reference readout is 51.831 counts, so the expected resonant fluorescence drop is:
  51.831 * 0.22 * 0.996 = 11.36 counts.
- Thus a real resonance in the scanned band should appear as readout2 - readout1 near -11 counts at or near the resonance, with a width on the order of the 10 MHz Rabi frequency.

Observed data:
- Combined readout2 - readout1 values range only from -1.60 to +2.04 counts.
- The mean difference is -0.071 counts with standard deviation 1.17 counts across scan points.
- The most negative combined point is -1.60 counts at 3.905 GHz, far smaller than the expected about -11.36 count resonant drop.
- Per-average scatter of the readout difference is about 2.97 counts, so the expected on-resonance drop is about 3.8 times this per-average scatter and should be visually and numerically obvious.

Explicit lineshape check:
- I modeled the pulsed ODMR response as d(f) = offset - A * P(f - f0), where
  P(detuning) = (Omega^2 / (Omega^2 + detuning^2)) * sin^2(pi * sqrt(Omega^2 + detuning^2) * t),
  using Omega = 10 MHz and t = 52 ns.
- With the physically expected amplitude A = mean_reference * 0.22 = 11.40 counts, the best center frequency still predicts a minimum difference near -9.54 counts and gives a much worse residual than the flat/no-resonance model.
- Letting A float gives a best-fit A of about -2.30 counts, i.e. the opposite sign from a resonance dip, and not a physical pODMR resonance.

Decision:
The expected resonant pODMR signal for this pulse would be a large fluorescence loss of roughly 11 counts. The observed pulsed-minus-reference signal is small, noisy, and does not match the expected sign or amplitude of the Rabi-driven resonance model. Therefore, no pODMR resonance is present.
