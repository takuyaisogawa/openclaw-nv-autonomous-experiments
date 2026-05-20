Active sequence: Rabimodulated.xml with mw_freq scanned from 3.825 to 3.925 GHz in 5 MHz steps. The active instructions acquire a true mS=0 optical reference immediately after polarization, skip the mS=+1 reference block because full_expt = 0, then apply a modulated Rabi pulse and acquire the signal readout. Thus readout 1 is the reference and readout 2 is the post-microwave signal.

Using the provided sequence XML and exported active variable values, the Rabi pulse duration is 52 ns and mod_depth is 1. With the setup facts, this is near a pi pulse for a 10 MHz Rabi rate, so an on-resonance point should be capable of producing a substantial fraction of the approximately 22% mS=0 to mS=+1 contrast.

The combined readouts do not show a convincing pODMR resonance. The normalized signal/reference ratio has scattered depressions, with the largest at the high-frequency edge around 3.925 GHz, but this is not a clean local lineshape and nearby points do not form a coherent resonance feature. The per-average traces are dominated by strong opposite tracking trends, so they do not provide a strong independent repeatability check. Given the expected pulse sensitivity, the observed irregular and edge-weighted contrast is not sufficient evidence for a resonance.

Decision: resonance_absent.
