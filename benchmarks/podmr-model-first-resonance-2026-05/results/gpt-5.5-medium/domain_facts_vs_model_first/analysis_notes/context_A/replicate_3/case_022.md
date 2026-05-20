Active sequence: Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active readout structure is:
- Readout 1: true m_S = 0 level reference, acquired after optical polarization and before the microwave pulse.
- Readout 2: signal readout after the modulated Rabi pulse.

The optional m_S = +1 reference branch is inactive because full_expt = 0, so stored readouts are not a full three-role reference/signal set. The do_adiabatic_inversion flag is present, but that branch is not reached in the active instructions.

Pulse parameters from the provided sequence XML:
- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- sample_rate = 250 MHz, so the pulse length is already on the 4 ns grid

Using the domain facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. On resonance this should transfer population from m_S = 0 toward m_S = +1 and lower the post-pulse fluorescence by roughly the setup contrast scale, about 22%.

The data match that expectation. The reference readout stays comparatively flat near the mid-30s across the scan, while the post-pulse readout has a pronounced frequency-localized dip around 3.875-3.880 GHz, falling from a typical off-resonant level near 35-36 down to about 28.2. That is a roughly 20-22% reduction relative to the local off-resonant signal, consistent with a real pODMR transition under an approximately pi pulse. The per-average traces also show the same dip region, though the averages should not be overinterpreted as independent repeatability because they can reflect tracking cadence.

Decision: a pODMR resonance is present.
