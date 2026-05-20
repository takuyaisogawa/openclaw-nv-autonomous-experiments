Sequence interpretation:

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize the NV and take a detection readout, then skip the optional 1-level reference because full_expt = 0, then apply a rabi_pulse_mod_wait_time pulse and take the second detection readout. Therefore readout 1 is the bright m_S = 0 reference for each scan point, and readout 2 is the post-microwave-pulse signal readout, not an independent dark-state reference.

Pulse settings:

The provided sequence variables give mod_depth = 1 and length_rabi_pulse = 52 ns. With the provided setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is near a pi pulse on resonance, so a real transition should produce a substantial drop in the post-pulse signal relative to the 0-state reference, on the order of the stated 22% contrast scale.

Data assessment:

The combined readouts show a shared slow downward drift across frequency, also visible in the per-average overlays. The post-pulse signal is only about 0.95% lower than the reference on average, with pointwise signal/reference deviations generally within a few percent and changing sign at several frequencies. There is no localized, repeatable dip near the expected contrast scale, and the two stored averages should not be over-weighted as an independent repeatability test because stored averages may mostly reflect tracking cadence.

Decision:

No convincing pODMR resonance is present in this scan.
