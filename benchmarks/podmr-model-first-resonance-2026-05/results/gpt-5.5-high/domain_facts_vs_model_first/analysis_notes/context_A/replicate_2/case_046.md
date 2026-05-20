Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so only the true 0-level reference readout is acquired before the driven measurement readout. The conditional 1-level reference block is inactive. Thus readout 1 is the laser-polarized 0-state reference, and readout 2 is the readout after the microwave rabi_pulse_mod_wait_time pulse.

Pulse settings used for the decision: length_rabi_pulse = 52 ns and mod_depth = 1 from the provided sequence/variable values. With the stated setup, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If a pODMR resonance were present, the driven readout should show a substantial fluorescence reduction versus the 0-state reference, on the order of the stated 22% contrast scale at resonance.

The combined raw readouts do not show that behavior. Readout 2 is sometimes below readout 1 by a few percent and sometimes above it; around 3.875 GHz readout 2 is higher than readout 1, not lower. The per-average traces mainly show offset/tracking changes between the two stored averages rather than a stable resonant dip in the driven readout. Since stored averages can reflect tracking cadence, I do not treat their similar broad shapes as independent confirmation.

Decision: resonance_absent.
