Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The executed instructions first polarize and detect, so readout 1 is the bright mS=0 reference. Because full_expt is 0, the separate mS=1 reference block is skipped; readout 2 is the detection after a rabi_pulse_mod_wait_time pulse.

The provided sequence uses length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth 1, the pulse area is about 0.52 Rabi cycles, close to a pi pulse. Therefore an on-resonance microwave drive should substantially transfer population from mS=0 to mS=+1 and reduce fluorescence in readout 2 by a large fraction of the about 22% setup contrast.

The data show readout 1 staying near 47-50 counts without a matching deep feature, while readout 2 has a localized trough near 3.875-3.880 GHz, falling from the high-40 count baseline to about 39 counts. This is roughly a 18-20% drop relative to the local bright reference and is consistent with the expected contrast for a near-pi pODMR resonance. The two stored averages both show the same central depression in readout 2, but I treat that mainly as supportive because stored averages can reflect tracking cadence.

Decision: resonance_present.
