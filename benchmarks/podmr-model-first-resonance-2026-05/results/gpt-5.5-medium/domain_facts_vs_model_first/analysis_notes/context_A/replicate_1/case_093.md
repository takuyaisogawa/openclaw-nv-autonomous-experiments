Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the "Acquire 1 level reference" block is skipped. The two active detections are:

1. Readout 1: after adj_polarize, a true m_S = 0 bright reference.
2. Readout 2: after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), the microwave-affected pODMR signal.

The active pulse parameters from sequence.xml are mod_depth = 1 and length_rabi_pulse = 5.2e-08 s = 52 ns. With the given setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so on resonance the second readout should show a large negative contrast relative to the m_S = 0 reference, approaching the setup contrast scale of about 22% if the transition is well driven.

The observed combined readouts do not show such a feature. Readout 2 is nearly equal to readout 1 on average, with mean difference about +0.13%, and pointwise signal/reference deviations only range from about -3.9% to +4.8%. The negative deviations are isolated and alternate with positive deviations; the per-average traces also show large tracking-like offsets between the two stored averages rather than reproducible resonance structure. Since stored averages may reflect tracking cadence, those overlays are not strong independent evidence for repeatability.

Decision: no credible pODMR resonance is present in this scan.
