Case podmr_063_2026-05-17-064555

Sequence and readout roles:
- The provided sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active experimental block first polarizes the NV and detects the true m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The second active detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so readout 1 is the m_S = 0 reference and readout 2 is the post-Rabi-pulse signal.
- length_rabi_pulse = 52 ns and mod_depth = 1 in the provided XML/variable values.

Explicit expected-signal calculation:
- Domain model: Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth.
- For a square resonant pulse, the transfer probability is P1 = sin^2(pi * f_R * t).
- With f_R = 10 MHz and t = 52 ns, P1 = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup m_S = 0 to m_S = +1 contrast scale is about 22%, so an on-resonance pulse should produce a fractional fluorescence drop of 0.22 * 0.996 = 0.219, about 21.9%.
- The measured readout 1 mean is 51.82 raw units, so the expected on-resonance readout 2 level is approximately 51.82 * (1 - 0.219) = 40.47, a drop of about 11.36 raw units relative to the reference.

Observed data comparison:
- readout 1 mean/sd: 51.82 / 1.49.
- readout 2 mean/sd: 51.40 / 1.53.
- The measured readout2-readout1 difference has mean -0.42, sd 1.36, minimum -2.73, and maximum +1.69 raw units.
- The measured normalized drop 1 - readout2/readout1 has mean 0.0078, sd 0.0261, and maximum 0.0504.
- Thus the largest observed pulse-specific drop is about 5.0%, far below the approximately 21.9% expected from a resonant 52 ns pulse at mod_depth = 1.
- A square-pulse detuning model fitted to normalized drop versus frequency does not recover a credible in-scan resonance: the apparent best improvement is small and the observed shared downward trend in both readouts is more consistent with drift/tracking than with a pulse-induced resonance.

Decision:
The quantitative model predicts a much larger and readout-specific dip than is present. The scan does not show a pODMR resonance.
