Case podmr_023_2026-05-16-174219

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect the true m_S = 0 reference, then wait, then apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detect again.
- full_expt = 0, so the conditional m_S = +1 reference block is inactive. The two combined readouts are therefore the true 0-level reference and the post-Rabi-pulse signal, not two independent ODMR repetitions.
- The provided XML/variable values give length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale, this is about a pi pulse at resonance because the Rabi frequency is about 10 MHz.

Expected signal:
- If a resonance is present, the post-pulse readout should drop relative to the true 0 reference near the resonant microwave frequency.
- At mod_depth = 1 and near-pi pulse length, the possible contrast scale is on the order of the stated 22% m_S = 0 to m_S = +1 contrast, not merely a tiny percent-level wiggle.

Observed data:
- The post-pulse minus reference difference changes sign across the scan.
- The largest apparent post-pulse reduction is about 5% near 3.835 GHz, while other nearby and later points show no coherent line shape, and some points show the post-pulse readout higher than the reference by comparable magnitude.
- The mean normalized difference is close to zero, with point-to-point scatter around a few percent.
- The stored two averages mainly show a large tracking/drift offset between average blocks, so they do not provide a strong independent repeatability check.

Decision:
No convincing pODMR resonance is present. The active pulse should have produced a clear post-pulse fluorescence dip if resonant, but the readout difference is small, sign-changing, and comparable to drift/noise rather than a coherent resonance feature.
