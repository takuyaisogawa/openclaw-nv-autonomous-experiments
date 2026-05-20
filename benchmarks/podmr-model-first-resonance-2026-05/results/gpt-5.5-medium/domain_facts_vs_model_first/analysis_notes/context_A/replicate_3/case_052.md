Sequence inspection:

The active sequence is Rabimodulated.xml with mw_freq as the scan variable over 3.825 to 3.925 GHz in 5 MHz steps. The active microwave operation is a rabi_pulse_mod_wait_time call before the final detection. full_expt is 0, so the optional 1-level reference block is skipped.

Readout roles:

The first readout follows adj_polarize and is the bright m_S = 0 reference. The second readout follows the modulated Rabi pulse and is the frequency-dependent signal readout. There is no independent m_S = +1 reference in this run because full_expt is disabled.

Pulse parameters from the provided sequence XML:

mod_depth = 1
length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns

Decision:

At mod_depth 1, the given setup has an approximate 10 MHz Rabi frequency, so a 52 ns pulse is near a pi pulse. If the microwave frequency crossed a real pODMR resonance, the post-pulse signal readout should show a substantial drop relative to the polarized reference, on the order of the stated 22% contrast scale for this setup.

The combined data do not show that. The average readout2-readout1 contrast is only about -0.7%, with pointwise relative deviations ranging roughly from -6.0% to +4.0%. The apparent dips near 3.845 to 3.850 GHz are small compared with the expected near-pi-pulse contrast and are not supported by a clean, consistent resonance feature across the scan or per-average overlays. The two stored averages mainly reflect drift/tracking behavior and do not provide strong repeatability evidence for a resonance.

Conclusion: no convincing pODMR resonance is present.
