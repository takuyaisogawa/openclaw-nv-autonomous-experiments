Sequence and decision notes

The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The provided sequence sets full_expt = 0, so the "Acquire 1 level reference" branch is skipped. The acquisition therefore consists of a true mS = 0 reference detection after optical polarization, followed by a modulated Rabi pulse and a second detection. Thus readout 1 is the mS = 0 reference and readout 2 is the post-microwave-pulse readout.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At the stated setup scale, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse. If the microwave frequency is resonant, readout 2 should drop strongly relative to readout 1, with a scale comparable to the stated 22% mS = 0 to mS = +1 contrast.

The combined data show a pronounced readout-2-only dip near 3.875-3.880 GHz: readout 2 falls from the high-30s baseline to about 29.3 and 28.1, while readout 1 remains near 36-40 and actually peaks at about 40 at 3.880 GHz. This is roughly the expected contrast scale for a near-pi pulse. The per-average overlay indicates the dip is visible in the stored averages, although the averages mainly reflect tracking cadence and should not be treated as a strong repeatability test. The feature is nevertheless large, frequency-localized, and appears in the correct readout channel for this sequence.

Decision: resonance_present.
