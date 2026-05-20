Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true mS=0 reference, then because full_expt = 0 it skips the optional mS=1 reference branch and applies one modulated Rabi pulse followed by detection. Thus readout 1 is the mS=0 reference and readout 2 is the post-microwave signal.

The relevant active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is near a pi pulse, so an on-resonance point should transfer population toward mS=+1 and reduce the post-pulse fluorescence by roughly the setup contrast scale, about 22%, relative to the mS=0 reference.

The combined data show readout 1 remaining near 38-40 counts across the scan, while readout 2 has a pronounced dip around 3.875 GHz: readout 2 drops to about 28.8 counts while readout 1 is about 38.5 counts at that point, a decrease of roughly 25%. Neighboring points around 3.870-3.885 GHz are also depressed relative to the local baseline, giving a resonance-like feature rather than a single isolated readout swap. The two stored averages are consistent with the same dip structure, but I treat them mainly as tracking-cadence samples rather than a strong independent repeatability test.

Decision: a pODMR resonance is present.
