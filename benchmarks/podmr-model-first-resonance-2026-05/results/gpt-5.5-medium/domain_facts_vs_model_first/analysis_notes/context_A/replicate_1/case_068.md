<!-- Model-generated analysis note. Not a ground-truth label. -->

Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles: full_expt is 0, so the sequence acquires a true bright m_S=0 reference first after optical polarization, skips the optional m_S=+1 reference block, then applies the microwave pulse and acquires the signal readout. Thus readout 1 is the bright reference and readout 2 is the post-microwave signal readout.

Pulse settings from the provided sequence XML: mod_depth is 1 and length_rabi_pulse is 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth 1, 52 ns is approximately a pi pulse. If the swept microwave frequency crossed the single-NV resonance, the post-pulse readout should show a substantial dip relative to the bright reference, on the order of the 22% contrast scale for an effective m_S=0 to m_S=+1 transfer.

The combined traces instead fluctuate around similar raw readout levels. The post-microwave signal is not consistently suppressed relative to the bright reference at any scan point, and the per-average overlays mainly show tracking/cadence offsets between averages rather than a repeatable resonance-shaped contrast feature. The apparent point-to-point variations are small and inconsistent compared with the expected pi-pulse contrast.

Decision: resonance_absent.
