Active sequence: Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is rabi_pulse_mod_wait_time after the initial bright-state reference detection.

Readout roles from the XML: the first detection follows adj_polarize and is the true m_s = 0 bright reference. full_expt = 0, so the optional one-level reference branch is skipped. The second detection follows the Rabi-modulated microwave pulse and is the resonance-sensitive post-pulse signal.

Pulse settings: mod_depth = 1 and length_rabi_pulse = 52 ns. At the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. A real resonance should therefore produce a post-pulse fluorescence drop close to the stated m_s = 0 to m_s = +1 contrast scale, about 22%.

Observed data: the post-pulse readout is similar to the reference away from the center of the sweep, but it shows a localized trough near 3.875-3.885 GHz. The largest separation is at 3.880 GHz, where the bright reference is 21.346 and the post-pulse signal is 16.981, a 20.5% drop relative to the reference. This is close to the expected contrast for a near-pi pulse at full modulation depth.

The stored averages show strong tracking-like baseline drift, so they should not be treated as a strong independent repeatability test. Even with that caveat, the combined readouts and the expected pulse contrast scale support a real pODMR resonance.
