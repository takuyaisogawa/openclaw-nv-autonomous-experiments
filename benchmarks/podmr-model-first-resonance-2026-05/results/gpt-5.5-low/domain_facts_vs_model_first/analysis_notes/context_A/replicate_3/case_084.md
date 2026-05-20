Case podmr_070_2026-05-17-082720.

I used only the provided XML/raw export and the raw readout plot. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz in 5 MHz steps. In the instructions, the first detection after adj_polarize is the true mS = 0 reference readout. The full_expt flag is 0, so the optional separate mS = 1 reference block is inactive. The measurement readout is the detection after rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.

Given the supplied setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. On resonance it should transfer population from mS = 0 toward mS = +1 and make the post-pulse readout substantially lower than the preceding reference readout, on the order of the 22% contrast scale for a strong response.

The two combined raw readouts mainly show a shared slow downward trend across the frequency scan rather than a localized resonance-shaped contrast feature. The post-pulse readout is sometimes lower than the reference but the separation is small, inconsistent in sign across the scan, and much smaller than the expected contrast for a near-pi pulse. The stored per-average traces are not a strong independent repeatability test here and also look dominated by drift/tracking cadence rather than a reproducible resonance dip.

Decision: resonance_absent.
