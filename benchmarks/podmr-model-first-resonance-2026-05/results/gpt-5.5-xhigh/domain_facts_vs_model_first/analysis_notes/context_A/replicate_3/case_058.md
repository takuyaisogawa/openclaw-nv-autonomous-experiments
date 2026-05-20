Case podmr_044_2026-05-16-232730.

I used the provided sequence XML and the raw export values before deciding. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The executed path is:

1. adj_polarize for 1 us.
2. detection after delay_wrt_1mus = 0.2 us: this is readout 1, the true m_S = 0 reference.
3. wait_for_awg for 2 us.
4. The optional "1 level reference" branch is skipped because full_expt = 0.
5. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
6. detection after the same delay: this is readout 2, the post-microwave signal readout.
7. final wait_for_awg for 1 us.

At the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency. A 52 ns pulse is therefore essentially a pi pulse, so if a pODMR resonance were sampled well, the post-pulse readout should be strongly lower than the m_S = 0 reference, on the order of the setup contrast scale between m_S = 0 and m_S = +1 (about 22%).

The combined raw readouts do not show that behavior. The largest suppression of readout 2 relative to readout 1 is about 2.42 raw units at 3.865 GHz, or about 4.8%, and the mean readout difference is close to zero. Many scan points have readout 2 equal to or higher than readout 1, including the high-frequency end. The per-average traces mainly show a large tracking/baseline offset between averages, and the stored averages are not a strong independent repeatability test.

Decision: resonance absent. The data contain small fluctuations and drift but no physically convincing near-pi-pulse pODMR contrast feature.
