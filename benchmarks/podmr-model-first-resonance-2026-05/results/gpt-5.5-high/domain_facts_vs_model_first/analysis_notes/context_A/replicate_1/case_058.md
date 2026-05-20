Active sequence: Rabimodulated.xml / Rabimodulated, varying mw_freq over 3.825 to 3.925 GHz.

The provided XML has full_expt = 0, so the active acquisition is:
1. adj_polarize followed by detection: this is the true m_S = 0 reference readout.
2. a modulated Rabi pulse followed by detection: this is the microwave-exposed readout.

The m_S = +1 reference block is skipped because full_expt is zero, even though the do_adiabatic_inversion boolean is set. Thus readout 1 is the unpulsed bright reference and readout 2 is the test readout after the Rabi pulse.

Pulse settings before deciding:
- length_rabi_pulse = 52 ns
- mod_depth = 1
- setup Rabi frequency at mod_depth 1 is about 10 MHz, so this is approximately a pi pulse scale pulse.
- setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pi pulse should produce a large decrease of the post-pulse readout relative to the 0-reference.

Observed data:
- The two combined raw readouts are similar in scale, and the microwave-exposed readout is often comparable to or higher than the 0-reference.
- There is no frequency-localized dip of the post-pulse readout relative to the reference at the expected contrast scale.
- The apparent point-to-point changes are only a few raw-readout units and are comparable to drift/tracking differences between averages.
- The stored averages show broad offset changes rather than consistent independent reproduction of a resonance feature, and stored averages should not be treated as a strong repeatability test here.

Decision: resonance absent. With a 52 ns pulse at mod_depth 1, a real resonance should give a clear negative contrast in the second readout against the bright reference; that signature is not present.
