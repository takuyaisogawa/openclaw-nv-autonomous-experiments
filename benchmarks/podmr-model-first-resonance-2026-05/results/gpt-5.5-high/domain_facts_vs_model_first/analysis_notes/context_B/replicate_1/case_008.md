Case: podmr_014_2026-05-12-081841

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first performs adj_polarize, then detection, so readout 1 is the polarized m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion being true.
- The active microwave operation before the second detection is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the post-Rabi-pulse signal.

Quantitative expected signal model:

For a rectangular driven two-level pulse, the transferred population is

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t).

Using the provided setup facts, f_R = 10 MHz * mod_depth = 10 MHz and t = 52 ns. On resonance,

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With 22% contrast between m_S = 0 and m_S = +1, the expected normalized post-pulse signal on resonance is

R_signal / R_reference = 1 - 0.22 * 0.996 = 0.781.

On this data's roughly 46-count baseline, that is an expected dip of about 10.1 counts in readout 2 relative to readout 1 at resonance. At detunings of 5 MHz and 10 MHz, the same model predicts normalized ratios of about 0.835 and 0.940 respectively, so a resonance within the scan should create a broad, easily visible trough over neighboring frequency points.

Observed data:

- Mean readout 1: 46.624.
- Mean readout 2: 46.315.
- Mean readout2-readout1: -0.309 counts.
- Standard deviation of readout2-readout1 over scan points: 1.331 counts.
- The minimum observed readout2/readout1 ratio is 0.937 at 3.865 GHz, equivalent to only a 6.3% drop.
- The per-point two-average ratio scatter has median SEM estimate about 0.027, and stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.

Model comparison:

Centering the expected mod_depth = 1 model at the deepest observed point, 3.865 GHz, predicts a ratio of 0.781 at the center and 0.835 at the adjacent +/-5 MHz points. The measured ratios at those three points are 1.000, 0.937, and 1.027 for 3.860, 3.865, and 3.870 GHz, which does not match the expected resonance shape or amplitude.

A least-squares search over possible resonance centers using the same Rabi-pulse lineshape but allowing the contrast amplitude to float gives a best effective contrast amplitude of about 0.038, far below the expected 0.22. The observed fluctuations include several isolated shallow dips and positive excursions, with no coherent post-pulse trough of the expected width and depth.

Decision:

No pODMR resonance is present. The active pulse should produce a large, quantitative drop in readout 2 relative to the m_S = 0 reference if resonant, but the data show only small, incoherent fluctuations comparable to scan scatter.
