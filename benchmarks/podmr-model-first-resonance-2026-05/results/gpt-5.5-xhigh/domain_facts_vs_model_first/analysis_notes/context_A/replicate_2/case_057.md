Sequence/readout context:

The provided sequence is Rabimodulated.xml. The active branch first polarizes the NV and records a detection readout as the true mS = 0 reference. The optional "Acquire 1 level reference" branch is disabled because full_expt = 0, so there is no active mS = +1 reference readout. After the reference, the sequence applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, then records the second detection readout. Thus readout 1 is the bright mS = 0 reference and readout 2 is the post-microwave Rabi/readout signal.

At mod_depth = 1 the stated setup gives about a 10 MHz Rabi frequency, so a 52 ns pulse is essentially a pi pulse on resonance. With an mS = 0 to mS = +1 contrast scale near 22%, an on-resonance point should produce a clear post-pulse fluorescence reduction relative to the reference, on the order of a large fraction of that contrast.

The scan from 3.825 to 3.925 GHz does not show that behavior. The combined readout 1 mean is about 47.11 and readout 2 mean is about 47.55, so the post-pulse readout is slightly higher on average rather than lower. The largest negative readout2-readout1 difference is only about -1.19 counts, or -2.4%, far below the expected resonance-scale drop for a near-pi pulse. Other points fluctuate by comparable small amounts, and the per-average overlay is consistent with tracking/noise structure rather than a strong repeatability test or a coherent resonance feature.

Decision: pODMR resonance absent.
