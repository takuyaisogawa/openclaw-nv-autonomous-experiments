Case podmr_067_2026-05-17-074342.

I inspected the sequence and raw readouts before deciding. The active sequence is Rabimodulated.xml. With full_expt set to 0, the intermediate +1 reference block is skipped. The first detection after adj_polarize is therefore the true m_S = 0 reference readout, and the second detection follows the Rabi-modulated microwave pulse and is the signal readout to compare against that reference.

The provided active settings give length_rabi_pulse = 52 ns and mod_depth = 1. Using the stated setup calibration, mod_depth = 1 gives about a 10 MHz Rabi frequency, so 52 ns is very close to a pi pulse. On a real resonance this should transfer close to the full available m_S = 0 to m_S = +1 contrast scale, about 22%, producing a large localized drop in the post-pulse readout relative to the reference.

The combined data do not show that. The post-pulse readout differs from the reference by only a few percent, with the largest local negative differences around 3.88-3.90 GHz at roughly 4-5%. Similar-scale fluctuations and sign changes occur elsewhere, and the stored two averages should not be treated as a strong repeatability test because they may reflect tracking cadence. Given a near-pi pulse at mod_depth = 1, the observed feature is far below the expected contrast and is not sufficient evidence for a pODMR resonance.

Decision: resonance absent.
