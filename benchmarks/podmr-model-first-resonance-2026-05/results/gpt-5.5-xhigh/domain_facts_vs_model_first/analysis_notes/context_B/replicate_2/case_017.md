Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction path first runs adj_polarize followed by detection. This first detection is the laser-polarized m_S = 0 fluorescence reference, so readout 1 is the bright reference.
- full_expt is 0, so the optional "Acquire 1 level reference" block is skipped. There is no separate m_S = +1 reference readout in this run.
- The active signal block is rabi_pulse_mod_wait_time followed by detection, so readout 2 is the fluorescence after the microwave pulse.
- The provided XML and exported active variable values give mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. With sample_rate = 250 MHz, the pulse is rounded to 13 samples, still 52 ns.

Expected signal model:

For a square pulse driving a two-level m_S = 0 to m_S = +1 transition, I used

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)),

where f_R is the on-resonance Rabi frequency in cycles/s, Delta is detuning in Hz, and tau is the pulse duration. The supplied setup scale gives f_R = 10 MHz at mod_depth = 1. With tau = 52 ns:

- On resonance: P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, the expected normalized readout 2/readout 1 ratio at resonance is 1 - 0.22 * 0.996 = 0.781.
- The same model gives expected ratios of about 0.835 at +/-5 MHz detuning and 0.940 at +/-10 MHz detuning, so the expected pODMR feature is a narrow dip spanning a few scan points.

Observed comparison:

- The combined readout 2/readout 1 ratios are 0.885 at 3.870 GHz, 0.763 at 3.875 GHz, 0.707 at 3.880 GHz, and 0.901 at 3.885 GHz.
- The minimum is at 3.880 GHz: readout 1 = 38.115 and readout 2 = 26.962, giving a normalized contrast of 29.3%.
- Excluding 3.870-3.885 GHz, the mean readout 2 level is 36.544 counts. The 3.880 GHz point is lower by 9.583 counts, or 26.2% of that off-resonance level.
- The expected full-pulse dip from the physical model is about 22% of the bright reference, or 8.385 counts at the 3.880 GHz reference level, predicting readout 2 near 29.73 counts. The observed minimum is somewhat deeper but on the same scale and has the predicted localized shape.
- A simple normalized-ratio model comparison also supports the resonance interpretation: a linear no-resonance baseline has RMSE 0.083, while the fixed 22% square-pulse model gives best center 3.8775 GHz with RMSE 0.045. Allowing the contrast amplitude to float gives best amplitude 0.251 and RMSE 0.0446, close to the supplied 22% contrast scale.
- The two stored averages both show the depressed signal around 3.875-3.880 GHz, but I treat this only as supporting information because stored averages can reflect tracking cadence rather than independent repeatability.

Decision: resonance_present. The active 52 ns, mod_depth 1 pulse should nearly invert on resonance, and readout 2 shows a narrow dip of the expected size and width relative to the m_S = 0 reference.
