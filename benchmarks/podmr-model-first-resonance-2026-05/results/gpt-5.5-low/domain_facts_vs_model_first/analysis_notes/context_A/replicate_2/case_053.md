Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The executed readout roles are determined from the sequence instructions with full_expt = 0. The sequence first polarizes and detects immediately, giving readout 1 as the true m_S = 0 bright reference. The optional m_S = +1 reference block is skipped. Then it applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, giving readout 2 as the microwave-manipulated signal.

Using the stated setup scale, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If a pODMR resonance were being hit, readout 2 should be strongly reduced relative to the m_S = 0 reference, on the order of the setup contrast scale (~22%) near resonance.

The observed combined readouts do not show that. Readout 2 is often close to readout 1 and sometimes above it, with only modest downward deviations at the high-frequency end. The largest sustained readout-2 reduction is only a few counts on a ~49 count baseline, well below the expected contrast for a near-pi pulse, and the two stored averages differ enough that the shape is not a strong repeatability check. The scan therefore does not provide convincing evidence for a pODMR resonance.
