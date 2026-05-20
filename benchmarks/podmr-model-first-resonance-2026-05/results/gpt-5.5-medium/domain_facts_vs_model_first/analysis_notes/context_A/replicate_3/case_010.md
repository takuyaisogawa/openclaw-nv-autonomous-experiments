Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided XML has full_expt = 0, so the active readouts are:
- readout 1: after adj_polarize and detection, a bright m_S = 0 reference.
- readout 2: after a single rabi_pulse_mod_wait_time and detection, the signal readout after microwave drive.

The optional m_S = 1 reference block is inactive because full_expt is zero. The adiabatic inversion flag is therefore not active in the executed readout path. The active microwave pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi-pulse duration, so a true on-resonance point should produce a substantial drop in the driven readout relative to the bright reference, on the order of the setup contrast scale.

The combined raw readouts do not show a coherent pODMR dip. The driven readout differs from the reference by only small, irregular point-to-point amounts, with the largest negative deviations appearing isolated rather than as a reproducible resonance feature across the sweep. The two stored averages mainly show opposite slow tracking trends, consistent with the warning that averages reflect tracking cadence rather than independent repeatability. After accounting for the readout roles and the expected pi-pulse contrast, the data do not support a present pODMR resonance.
