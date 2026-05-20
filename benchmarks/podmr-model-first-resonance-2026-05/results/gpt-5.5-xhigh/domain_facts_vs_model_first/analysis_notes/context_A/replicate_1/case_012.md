Sequence interpretation:

The active saved scan is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz. The sequence first polarizes the NV center and immediately detects, so readout 1 is the bright m_S = 0 reference. Because full_expt = 0, the optional separate 1-level reference block is skipped. The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection, so readout 2 is the microwave-driven signal readout.

Pulse-strength check:

With the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency. A 52 ns pulse is approximately 0.52 Rabi cycles, i.e. very close to a pi pulse, so an on-resonance transition should create nearly the full m_S = 0 to m_S = +1 contrast. With a 22% contrast scale and raw readouts near 27 to 29 counts, a strong resonance would be expected to lower the driven readout by roughly several counts relative to the bright reference at a localized frequency.

Data assessment:

The combined readout 2 trace does not show a stable localized dark dip relative to readout 1. The largest negative differences are only about 2.2 counts and occur at isolated frequencies, while neighboring points often move in the opposite direction and readout 2 is frequently brighter than readout 1. The two stored averages also show strong tracking/drift structure, so they are not good independent repeatability evidence for a resonance. Given the near-pi active pulse, the absence of a clear, localized, contrast-scale suppression in the driven readout supports resonance_absent.
