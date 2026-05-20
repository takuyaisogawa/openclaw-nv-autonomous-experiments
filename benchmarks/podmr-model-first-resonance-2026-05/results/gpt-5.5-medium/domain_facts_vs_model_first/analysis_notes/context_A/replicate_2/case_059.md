Sequence inspected before deciding.

Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.
full_expt is 0, so the optional mS=+1 reference block is inactive. The active
readouts are:

- readout 1: detection immediately after optical polarization, the mS=0 bright
  reference.
- readout 2: detection after a modulated Rabi microwave pulse, the pODMR signal
  readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse =
52 ns and mod_depth = 1. Given the supplied setup facts, mod_depth = 1 implies
about 10 MHz Rabi frequency, so 52 ns is approximately a pi-pulse duration. If a
resonance were present in this scan, the post-pulse signal readout should show a
large fluorescence reduction relative to the mS=0 reference, on the order of the
setup contrast scale (about 22%) at resonance.

The combined raw readouts stay near 48-50 counts for both readouts across the
scan. readout 2 does not show a clear localized dip relative to readout 1 with a
contrast-scale amplitude. The readout differences are small, change sign, and
are comparable to the per-average scatter. Stored averages here are only two and
can reflect tracking cadence, so the per-average traces do not provide a strong
independent repeatability test; they also do not show a consistent resonance
feature.

Decision: no convincing pODMR resonance is present.
