Sequence review:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. The provided sequence XML sets length_rabi_pulse to 52 ns and mod_depth to 1. The full_expt variable is 0, so the optional m_S = +1 reference branch is skipped. The measurement therefore records the initial optical readout after polarization as the true m_S = 0 reference, then applies one modulated Rabi pulse and records the mw-driven readout.

Domain expectation:

At mod_depth = 1 the setup Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse on resonance. Given the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a real resonance should produce a fairly clear localized reduction of the mw-driven readout relative to the m_S = 0 reference, not just percent-level fluctuations.

Data assessment:

The two combined readouts track each other loosely but the difference between the driven readout and the reference alternates sign across the sweep. The largest fractional deviations are around a few percent, with no robust, localized dip of the expected sign and scale. Stored per-average traces are only two averages and likely reflect tracking cadence, so I do not treat their apparent variations as an independent repeatability test.

Decision:

I do not see evidence for a pODMR resonance in this scan.
