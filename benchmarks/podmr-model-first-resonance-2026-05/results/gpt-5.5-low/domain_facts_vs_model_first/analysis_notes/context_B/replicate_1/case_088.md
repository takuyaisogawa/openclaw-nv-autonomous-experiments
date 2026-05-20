Case podmr_074_2026-05-17-092418

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the detection immediately after optical polarization, i.e. the bright m_S = 0 reference for each point.
- Readout 2 is the detection after the Rabi-modulated microwave pulse.
- mod_depth = 1 in the provided sequence XML and exported variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given Rabi frequency approximately 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the on-resonance Rabi frequency is f_R = 10 MHz.
- For a resonant square pulse, the transferred population is P = sin^2(pi * f_R * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected relative fluorescence drop for readout 2 on resonance is 0.22 * 0.996 = 0.219.
- The observed readout 1 mean is 49.08 raw counts, so a resonant point should have readout 2 lower by about 49.08 * 0.219 = 10.75 counts, giving an expected readout 2 near 38.32 counts.

Observed data summary:
- readout 1 mean = 49.08, standard deviation across scan points = 1.09, range = 47.08 to 50.98.
- readout 2 mean = 48.78, standard deviation across scan points = 1.47, range = 46.60 to 51.38.
- readout2 - readout1 mean = -0.29 counts, standard deviation = 1.72 counts.
- The deepest readout2 - readout1 point is -3.92 counts at 3.900 GHz, far smaller than the approximately -10.75 count resonant response expected from the provided XML pulse parameters.
- The two stored averages differ substantially in baseline and point structure, consistent with the warning that stored averages can reflect tracking cadence rather than an independent repeatability test.

Decision:
The pulse sequence should produce a large negative readout2-vs-readout1 feature if the scan crosses the addressed resonance. The measured readout difference lacks the expected amplitude and does not show a quantitatively compatible pODMR dip. I therefore classify this case as resonance_absent.
