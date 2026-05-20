Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is the detection immediately after adj_polarize, so it is the active m_S=0 / bright reference readout.
- Readout 2 is the detection after rabi_pulse_mod_wait_time, so it is the post-microwave-pulse readout used to look for population transfer.
- mod_depth = 1 and length_rabi_pulse = 52 ns.
- With the given setup scale of about 10 MHz Rabi frequency at mod_depth = 1, the 52 ns pulse is approximately a pi pulse, so an on-resonance point should drive population toward m_S=+1 and reduce readout 2 relative to readout 1 by up to roughly the 22% contrast scale.

Signal assessment:
The combined normalized contrast 1 - readout2/readout1 is near zero away from the feature, but has a clear local dip in readout 2 around 3.875-3.885 GHz: 11.8% at 3.870 GHz, 22.7% at 3.875 GHz, 19.6% at 3.880 GHz, 18.7% at 3.885 GHz, then recovering toward the baseline. This magnitude matches the expected contrast for a near-pi pulse.

The per-average traces show broad opposing trends consistent with tracking cadence, so they should not be treated as independent repeatability tests. Even so, within each stored average the same local suppression appears near the same frequency: average 1 reaches about 23.8% contrast at 3.875 GHz and 22.7% at 3.885 GHz, while average 2 reaches about 21.9% at 3.875 GHz and 21.5% at 3.880 GHz.

Decision: a pODMR resonance is present.
