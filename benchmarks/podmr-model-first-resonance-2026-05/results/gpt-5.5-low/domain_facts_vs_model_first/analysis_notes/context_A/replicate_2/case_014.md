Active pulse sequence: Rabimodulated.xml / Rabimodulated, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects the true m_S = 0 / bright reference. The optional m_S = +1 reference block is disabled because full_expt = 0, so there is no independent dark-state reference in this run. After the reference readout, the sequence applies one modulated Rabi microwave pulse and then performs the signal detection. Thus readout 1 is the pre-pulse bright reference/tracking readout and readout 2 is the post-pulse pODMR signal readout.

Relevant pulse settings from the saved run are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi-scale pulse duration, so an on-resonance transition should produce a large signal reduction in the post-pulse readout. The expected m_S = 0 to m_S = +1 contrast scale is about 22%, so a real resonance can plausibly appear as a sizeable dip in readout 2 relative to the bright reference.

The combined raw readouts show readout 1 remaining fairly flat around 38-40 counts across the scan, while readout 2 has a pronounced localized dip near 3.875 GHz, dropping from the high-30s to about 28.8 counts and then recovering. The per-average traces both include the same frequency-localized reduction in the post-pulse readout, although the two stored averages should mainly be treated as tracking cadence rather than a strong repeatability test. The dip magnitude is in the expected contrast range for a pi-scale pODMR pulse and is not mirrored by the bright reference readout.

Decision: a pODMR resonance is present.
