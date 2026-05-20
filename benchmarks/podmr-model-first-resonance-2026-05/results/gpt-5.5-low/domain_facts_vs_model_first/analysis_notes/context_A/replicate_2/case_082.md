Sequence inspection:

The active sequence is Rabimodulated.xml while sweeping mw_freq from 3.825 GHz to 3.925 GHz. The executed order is polarize and detect first, then wait, then apply rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then detect again. Because full_expt is 0, the conditional "Acquire 1 level reference" block is inactive. Thus readout 1 is the true mS=0-like fluorescence reference before the microwave pulse, and readout 2 is the fluorescence after the microwave Rabi pulse at each microwave frequency.

The provided XML gives length_rabi_pulse = 5.2e-08 s, i.e. 52 ns, and mod_depth = 1. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth 1, this is approximately a pi pulse on resonance. A real resonance should therefore make the post-pulse readout substantially lower than the pre-pulse reference near resonance, with a possible contrast scale up to roughly the 22% mS=0 to mS=+1 contrast, though practical contrast may be smaller.

Data assessment:

The two readouts mostly track each other across the sweep. There is a broad downward drift toward the high-frequency end in both readouts, including the pre-pulse reference, which points to fluorescence/tracking variation rather than selective microwave-driven spin transfer. The largest separation near the final points is only a few percent and coincides with a simultaneous drop in the reference channel. Around the mid-sweep, the post-pulse readout is sometimes above the reference and sometimes below it, with no clean local dip in readout 2 relative to readout 1. The two stored averages differ enough that they mainly indicate tracking cadence and drift, not a stable repeated resonance feature.

Decision:

No convincing pODMR resonance is present in this scan. The expected near-pi-pulse resonance signature would be a selective depression of the post-pulse readout relative to the pre-pulse reference, but the observed structure is dominated by common-mode drift and average-to-average variation.
