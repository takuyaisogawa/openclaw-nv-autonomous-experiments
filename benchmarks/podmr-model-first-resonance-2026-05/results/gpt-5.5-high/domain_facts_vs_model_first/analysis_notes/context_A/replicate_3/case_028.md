The provided sequence XML is Rabimodulated. The active acquisition has full_expt = 0, so the optional one-level reference block is skipped. The first detection follows adj_polarize and is the true ms=0/polarized reference readout. The second detection follows rabi_pulse_mod_wait_time and is the signal readout after the microwave pulse.

The active microwave pulse has length_rabi_pulse = 52 ns and mod_depth = 1. With the given setup scale of about 10 MHz Rabi frequency at mod_depth = 1, the Rabi period is about 100 ns, so a 52 ns pulse is close to a pi pulse. On resonance this should drive substantial population out of ms=0 and reduce the signal readout by up to the setup contrast scale, about 22%.

The data show readout 1 staying comparatively flat near the low-to-mid 40s while readout 2 has a localized, deep trough around 3.875 to 3.88 GHz, falling from a baseline near 43 to about 34. This is roughly a 20% drop and appears in both stored averages, although the averages should mainly be treated as tracking-cadence snapshots rather than an independent repeatability proof. The feature is localized to the post-pulse readout and matches the expected contrast and pulse condition for pODMR.

Decision: resonance_present.
