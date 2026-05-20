Case: podmr_035_2026-05-16-210045

Input files used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instruction path polarizes first, detects, waits, applies one rabi_pulse_mod_wait_time pulse, then detects again.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Therefore readout 1 is the true m_S = 0 reference after optical polarization, and readout 2 is the post-microwave pODMR signal readout.
- mod_depth = 1 from the provided sequence XML and exported Variable_values.
- length_rabi_pulse = 52 ns, rounded on the 250 MS/s sample clock to 52 ns.

Expected signal model:
The relevant model is a driven two-level square microwave pulse after optical initialization into m_S = 0. With Rabi frequency f_R = 10 MHz * mod_depth = 10 MHz and pulse duration T = 52 ns, the excitation probability at detuning delta is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * T * sqrt(f_R^2 + delta^2)).

On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected normalized fluorescence on resonance is approximately 1 - 0.22 * 0.996 = 0.781, i.e. about a 21.9% dip relative to the m_S = 0 reference. For readouts near 50 counts, that corresponds to an expected resonant signal near 39 counts instead of near 50 counts.

At 5 MHz detuning the same model predicts P = 0.749 and normalized fluorescence about 0.835. At 10 MHz detuning it predicts normalized fluorescence about 0.940. Thus a real resonance should appear as a broad, grid-resolved dip spanning multiple adjacent frequency points, not as a one-point small fluctuation.

Data comparison:
Using readout2/readout1 to remove the strong common drift, the normalized signal has mean 0.9834, standard deviation 0.0210, minimum 0.9435 at 3.830 GHz, and maximum 1.0216 at 3.835 GHz. The deepest observed normalized dip is only about 5.7%, far smaller than the expected 21.9% resonant dip. It is also immediately followed by the maximum point one 5 MHz step away, inconsistent with the broad pODMR line shape expected for the 52 ns, mod_depth = 1 pulse.

A least-squares comparison reinforces this. A linear baseline fit to readout2/readout1 gives RSS = 0.00881. Fitting the square-pulse resonance template with a free center and free dip amplitude finds no positive dip; the best coefficient is negative, meaning the template would improve the fit as a small bump rather than a dip. Forcing the expected 22% contrast resonance worsens the RSS to 0.03531 even with the center and linear baseline allowed to vary.

Stored averages are not treated as strong independent repeatability evidence, but they also do not show a common, broad, same-frequency resonant dip. Average 1 has its minimum ratio at 3.830 GHz, while average 2 has its minimum at 3.865 GHz.

Decision: resonance_absent. The active sequence should have produced a large, broad normalized dip if a pODMR resonance were present, and the measured readout2/reference ratios show only small drifting fluctuations without the expected line shape or amplitude.
