Case podmr_070_2026-05-17-082720.

I used the provided sequence XML as the deciding sequence. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 to 3.925 GHz. full_expt is 0, so the optional m_S = +1 reference block is inactive even though do_adiabatic_inversion is true. The two recorded readouts therefore are:

- readout 1: true m_S = 0 reference after optical polarization and detection
- readout 2: detection after the modulated Rabi microwave pulse

The pulse parameters in the provided XML are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth 1, so a 52 ns pulse is approximately a pi pulse on resonance. For a single NV with about 22% m_S = 0 to m_S = +1 contrast, an on-resonance response should produce a clear reduction of the post-pulse readout relative to the 0-level reference, not just a small count-level difference.

The combined data do not show such a feature. readout 2 minus readout 1 has mean about -0.48 counts and standard deviation about 1.16 counts, with the most negative point about -1.96 counts near 3.885 GHz. That is only about 4% of the raw readout level, far below the expected approximately 22% contrast for a near-pi pulse. The visible high-frequency decrease is shared by both readouts and is more consistent with drift or tracking cadence than a pODMR resonance. The two stored averages are sparse and should not be treated as a strong repeatability test.

Decision: resonance absent.
