Case: podmr_045_2026-05-16-234216

Sequence identification from inputs/sequence.xml:
- Sequence: Rabimodulated.xml / Rabimodulated pulse scan with mw_freq varied.
- Active readout roles: readout 1 is the bright m_S = 0 reference immediately after adj_polarize and detection. The full_expt branch is inactive because full_expt = 0, so no separate m_S = +1 reference is acquired. readout 2 is the pODMR signal after rabi_pulse_mod_wait_time and detection.
- Active pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- mod_depth: 1.
- length_rabi_pulse: 5.2e-08 s = 52 ns. At sample_rate = 250 MHz, the 4 ns grid leaves 52 ns unchanged.

Physical model calculation:
The setup contrast between m_S = 0 and m_S = +1 is about C = 0.22. The Rabi frequency is about f_R = 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so here f_R = 10 MHz. For a square pulse of duration tau = 52 ns, the transfer probability versus detuning delta is modeled as:

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

The expected fractional fluorescence dip is C * P(delta). On resonance:
P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, so the expected dip is 0.22 * 0.996 = 0.219, or about 21.9% of the bright reference. With the observed readout 1 mean of 48.85, that corresponds to about 10.7 raw readout units. Even if the resonance were halfway between 5 MHz scan steps, delta = 2.5 MHz gives P = 0.929 and an expected dip of about 10.0 raw units. At delta = 5 MHz, the expected dip is still about 8.1 raw units.

Observed data:
- readout 1 mean = 48.85.
- readout 2 mean = 48.77.
- mean readout2/readout1 ratio = 0.9986.
- standard deviation of readout2/readout1 across scan = 0.0215.
- mean readout2 - readout1 = -0.084 raw units.
- most negative readout2 - readout1 point = -1.83 raw units.

Thus the largest observed negative excursion is only about 17% of the expected on-resonance pi-pulse dip, and the average signal is essentially unity relative to the bright reference. A least-squares comparison of the measured readout2/readout1 trace with the 22% square-pulse Rabi lineshape gives no meaningful improvement over a flat model; the best model places the feature outside the scanned interval and only produces a shallow tail. Stored averages are not treated as strong independent repeatability evidence because they can reflect tracking cadence.

Decision: resonance_absent. The active pulse should have produced a large pODMR dip if a resonance were in the scanned range, but the observed signal is consistent with reference-level fluctuations and lacks the expected quantitative signature.
