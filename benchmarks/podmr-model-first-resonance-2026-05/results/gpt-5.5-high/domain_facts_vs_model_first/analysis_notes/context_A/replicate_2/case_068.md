Case podmr_054_2026-05-17-043636.

I used the provided sequence XML rather than labels or outside context. The active sequence is Rabimodulated.xml. With full_expt = 0, the enabled acquisitions are the initial polarized m_S = 0 reference detection followed by a modulated Rabi pulse and the final signal detection; the optional m_S = 1 reference block is skipped. Thus readout 1 is the m_S = 0 reference role and readout 2 is the post-pulse pODMR signal role.

The relevant pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. Given the stated setup, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so 52 ns is approximately a pi pulse on resonance. If a resonance were present and well addressed, the post-pulse signal readout should show a large fluorescence reduction on the order of the 22 percent m_S = 0 to m_S = +1 contrast scale near the resonant microwave frequency.

The combined readouts do not show such a feature. The mean readout-2/readout-1 ratio is close to unity, and the most negative combined ratio is only about 0.947, roughly a 5 percent drop, at an isolated point. Other nearby points do not form a coherent dip, and readout 2 is even above readout 1 at some scan points. The per-average overlay mainly shows broad average-to-average offsets and drift/tracking-cadence behavior rather than independent repeatable spectral structure.

Because the expected near-pi resonance response should be much larger and localized, while the observed differences are small, noisy, and not reproducible across the scan, I classify this case as resonance absent.
