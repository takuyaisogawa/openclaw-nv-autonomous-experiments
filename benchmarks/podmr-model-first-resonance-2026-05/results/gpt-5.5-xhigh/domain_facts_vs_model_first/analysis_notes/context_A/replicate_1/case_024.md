Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence XML polarizes first, then performs a detection before any microwave pulse. Because full_expt = 0, the optional "Acquire 1 level reference" block is inactive. The active pulse sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by the second detection. Thus readout 1 is the polarized m_S = 0 reference for each scan point, while readout 2 is the post-microwave-pulse signal.

At mod_depth = 1 the setup Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse on resonance. If a resonance is present, readout 2 should drop relative to readout 1 by about the m_S = 0 to m_S = +1 contrast scale, roughly 22%.

The combined data show a localized dip in readout 2 relative to readout 1 around 3.875 to 3.885 GHz. The normalized deficits are about 22.7% at 3.875 GHz, 19.6% at 3.880 GHz, and 18.7% at 3.885 GHz, while most off-resonant points are much smaller and fluctuate near zero. The per-average traces have large tracking drift, so they are not a clean independent repeatability test, but the same local readout-2 deficit relative to readout 1 is visible in both stored averages near the same frequencies.

Decision: resonance_present.
