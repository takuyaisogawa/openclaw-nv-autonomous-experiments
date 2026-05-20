Case podmr_035_2026-05-16-210045.

The provided sequence is Rabimodulated.xml with mw_freq as the swept parameter from 3.825 to 3.925 GHz. The active instructions polarize the NV and take a detection readout first, then skip the "1 level reference" block because full_expt = 0, then apply one rabi_pulse_mod_wait_time pulse and take a second detection readout. Thus readout 1 is the bright m_S = 0 reference/tracking readout, and readout 2 is the signal after the microwave pulse.

The active pulse has length_rabi_pulse = 52 ns, rounded at 250 MS/s, and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If a transition were in the scan range, the post-pulse signal should show a localized drop approaching the setup contrast scale, about 22% between m_S = 0 and m_S = +1.

The raw readouts do not show that behavior. Readout 2 is only a few percent below readout 1 at scattered points, with substantial common drift across both readouts and only two stored averages. The largest apparent differences are not a clean localized resonance feature and are much smaller than expected for a near-pi pulse on resonance. Stored averages mainly reflect tracking cadence here, so the per-average overlay is not enough to rescue the weak structure as repeatable resonance evidence.

Decision: resonance absent.
