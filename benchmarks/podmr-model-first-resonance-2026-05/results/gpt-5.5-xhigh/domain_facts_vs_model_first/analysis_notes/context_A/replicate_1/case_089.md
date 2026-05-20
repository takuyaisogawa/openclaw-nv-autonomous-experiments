Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and pulse settings:
- SequenceName is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active experiment has full_expt = 0, so the optional m_S = +1 reference block is skipped even though do_adiabatic_inversion is true.
- Readout 1 is the "true 0 level reference": laser polarization followed immediately by detection.
- Readout 2 is the pODMR signal readout: a microwave rabi_pulse_mod_wait_time pulse followed by detection.
- length_rabi_pulse is 5.2e-08 s. At 250 MS/s this is exactly 13 samples, so the applied pulse remains 52 ns.
- mod_depth is 1 in the provided sequence/variable values. With the stated 10 MHz per unit mod_depth scaling, this is approximately a near-pi pulse for this setup.

Decision reasoning:
For a single NV center with about 22% m_S = 0 to m_S = +1 contrast, a 52 ns near-pi pulse at mod_depth = 1 should produce a large negative pODMR feature in the signal readout relative to the reference if the sweep crosses resonance. The combined readout data do not show that. Readout 1 and readout 2 mostly share a slow upward drift across the scan. The signal/reference ratios only make shallow, isolated excursions, with the lowest points around 0.951 at 3.830 GHz and 0.958 at 3.900 GHz, and there is no coherent dip or line shape across adjacent frequency points. The two stored averages are not enough to treat isolated points as independent repeatability evidence, especially because stored averages often reflect tracking cadence.

Conclusion: resonance_absent.
