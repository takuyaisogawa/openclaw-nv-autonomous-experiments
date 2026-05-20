Case podmr_042_2026-05-16-225623.

I used only the provided sequence XML and raw export for this case. The active sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions acquire an initial fluorescence readout after polarization, then because full_expt is 0 they skip the separate m_S=1 reference block, apply the active modulated Rabi pulse, and acquire the second detection. Thus readout 1 is the pre-pulse/0-reference-like readout and readout 2 is the post-Rabi-pulse readout.

From the provided sequence XML, mod_depth is 1 and length_rabi_pulse is 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth 1, the Rabi period is about 100 ns, so a 52 ns pulse is close to a pi pulse. If the microwave frequency is resonant, the post-pulse readout should be suppressed relative to the initial readout by a sizeable fraction of the available 22% contrast.

The combined readouts both show a slow downward drift across the scan, so common-mode level changes alone should not be treated as resonance. The important feature is a local differential suppression around 3.875 GHz: at that scan point readout 2 drops to about 43.54 while readout 1 is about 45.37, and neighboring readout 2 points are higher. This is a roughly 4% post-pulse suppression relative to readout 1. It is smaller than the full 22% setup contrast, but it occurs at a plausible resonance-like local minimum and is visible in both stored averages. The averages should not be over-weighted as independent repeatability because they may reflect tracking cadence, but they do not contradict the feature.

Decision: pODMR resonance present.
