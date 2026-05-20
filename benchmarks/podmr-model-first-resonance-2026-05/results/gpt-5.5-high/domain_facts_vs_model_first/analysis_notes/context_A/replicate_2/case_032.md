Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence XML sets full_expt = 0, so the optional m_S = +1 reference block is skipped. The first detection is the "true 0 level reference" after optical polarization, and the second detection is after the microwave Rabi pulse. Therefore readout 1 is the m_S = 0 reference channel and readout 2 is the microwave-affected signal channel.

The active Rabi pulse is length_rabi_pulse = 52 ns. The provided XML uses mod_depth = 1. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is near a pi pulse, so on resonance it should drive strong population transfer and reduce fluorescence in the signal readout. The expected m_S = 0 to m_S = +1 contrast scale is about 22%.

The combined data show readout 1 staying near 44-46 counts across the scan, while readout 2 has a clear minimum of about 34.17 counts at the central point around 3.875 GHz. Relative to the local reference near 45.4 counts, this is roughly a 25% drop, consistent with the stated contrast scale for a near-pi pulse. The adjacent signal points also form a dip shape, and both stored averages show the central depression, though the two averages should not be over-interpreted as a strong independent repeatability test because stored averages can follow tracking cadence.

Decision: a pODMR resonance is present.
