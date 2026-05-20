Sequence readout interpretation:

The active sequence is Rabimodulated.xml behavior: it polarizes the NV, performs an immediate detection as the true m_S = 0 reference, waits, skips the optional m_S = +1 reference because full_expt = 0, then applies one modulated Rabi pulse before the second detection. Thus readout 1 is the polarized reference and readout 2 is the post-pulse signal readout.

The provided sequence values for the active pulse are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is essentially a pi pulse, so an on-resonance point should produce a clear reduction of readout 2 relative to readout 1, potentially on the order of the 22% m_S = 0 to m_S = +1 contrast scale.

The combined raw readouts do not show that behavior. Signal minus reference ranges only from about -2.35 to +3.94 raw counts, approximately -4.2% to +7.3%, with an average difference near zero. The largest excursion is positive rather than a fluorescence loss, and the negative points are small and not a coherent frequency-localized dip. The stored per-average traces mainly show baseline/tracking changes, consistent with the note that stored averages are not a strong independent repeatability test.

Decision: resonance absent.
