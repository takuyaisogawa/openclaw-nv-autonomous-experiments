Active sequence: Rabimodulated microwave-frequency sweep. The active XML has full_expt = 0, so the "1 level reference" block is skipped even though its code is present. The executed sequence polarizes and reads out a true m_S = 0 reference, waits, applies a modulated Rabi pulse, then reads out the post-pulse signal.

Readout roles: readout 1 is the initial polarized reference before the Rabi pulse. Readout 2 is the fluorescence after the Rabi pulse at the swept microwave frequency.

Pulse settings used for the decision: mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so an on-resonance point should produce a strong reduction in the post-pulse readout relative to the reference, on the order of the available m_S = 0 to m_S = +1 contrast.

The combined data show only small, irregular readout-2 depressions of a few percent relative to readout 1, with comparable point-to-point fluctuations and no clean, isolated resonance feature across the sweep. The stored per-average traces mainly reflect baseline/tracking offsets, so I do not treat them as a strong independent repeatability test. Given the near-pi pulse condition and the expected contrast scale, the observed structure is too weak and inconsistent to call a pODMR resonance.

Decision: resonance absent.
