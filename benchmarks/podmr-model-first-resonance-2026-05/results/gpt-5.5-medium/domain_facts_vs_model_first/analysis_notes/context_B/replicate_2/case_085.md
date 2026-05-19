<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_085

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence name: Rabimodulated.xml.
- The active microwave action is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- readout 1 is the initial bright-state / m_S = 0 reference after optical polarization and before the swept microwave pulse.
- readout 2 is the signal after the modulated Rabi pulse at the swept mw_freq.
- mod_depth = 1 from the provided sequence XML / variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MHz sample rate to 52 ns.

Quantitative physical expectation:
- Given f_Rabi ~= 10 MHz at mod_depth = 1 and linear scaling, f_Rabi = 10 MHz.
- For a resonant square pulse, transferred population P = sin^2(pi f_Rabi tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected fractional fluorescence change on resonance is -0.22 * 0.996 = -0.219.
- The observed mean readout level is about 49.46 counts, so an on-resonance point should show readout2 lower than readout1 by about 10.8 counts if the scanned transition is driven.
- Detuned Rabi formula used for sampled offsets:
  P(delta) = Omega^2/(Omega^2 + delta^2) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau), Omega = 2*pi*10 MHz.
  This gives expected fractional drops of about -20.4% at 2.5 MHz detuning, -16.5% at 5 MHz, -6.0% at 10 MHz, and -1.1% at 20 MHz.

Observed data check:
- Combined readout means: readout1 = 49.459, readout2 = 49.448.
- Mean readout2-readout1 difference = -0.011 counts, essentially zero.
- The largest negative fractional pair difference is about -5.4% at 3.860 GHz, far smaller than the expected near-resonant -16% to -22% response and not supported by a clear line shape.
- A fixed-width Rabi line fit to readout2 relative to readout1 does not recover a physical positive contrast; the best least-squares coefficient corresponds to the opposite sign, while a scale-only null fit is nearly as good.
- Stored per-average traces differ mainly by slow baseline/tracking changes, so they do not provide strong independent repeatability for a resonance decision.

Decision:
The expected resonant pODMR signal from the active 52 ns, mod_depth 1 pulse would be a large post-pulse fluorescence dip relative to the bright reference. The measured readout-pair data do not show that modeled response, so I decide resonance_absent.
