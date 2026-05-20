Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The provided sequence has full_expt = 0, so the optional mS=+1 reference block is inactive. The two stored readouts are therefore the initial polarized true mS=0 reference detection, followed by a detection after a single rabi_pulse_mod_wait_time pulse.

The active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1. Given the supplied setup facts, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, making 52 ns approximately a pi-scale pulse on resonance. With an mS=0 to mS=+1 contrast scale of about 22%, a resonance should show a clear frequency-localized reduction of the post-pulse readout relative to the mS=0 reference.

The combined data do not show that behavior. Readout 1 stays near 46 counts, while readout 2 fluctuates above and below readout 1 with isolated excursions. There are low points around several frequencies, but they are not a smooth or reproducible resonance-like dip, and stored per-average traces mainly show baseline offsets consistent with tracking cadence rather than independent confirmation. The size and pattern of deviations look like noise/drift rather than a contrast-scale pODMR feature.

Decision: resonance_absent.
