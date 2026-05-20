Active sequence: Rabimodulated.xml, varying mw_freq over 3.825 to 3.925 GHz in 5 MHz steps.

From the provided XML, full_expt is 0, so the optional "1 level reference" branch is skipped. The two active readouts are therefore:
- readout 1: true m_S = 0 reference after optical polarization and detection.
- readout 2: detection after a microwave Rabi pulse.

The Rabi pulse duration is 52 ns and mod_depth is 1. With the given setup estimate of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. A real resonance should therefore make readout 2 show a clear, localized depletion relative to readout 1, on the order of the setup contrast scale rather than only a few percent.

The combined normalized difference (readout 2 - readout 1) / readout 1 only ranges from about +3.3% to -3.9%. Negative excursions occur at several separated scan points, while both raw readouts also share a broad downward drift later in the scan. The per-average traces are not a strong independent repeatability test because stored averages can reflect tracking cadence, and they do not turn the scattered few-percent dips into a convincing ODMR line shape.

Decision: resonance_absent.
