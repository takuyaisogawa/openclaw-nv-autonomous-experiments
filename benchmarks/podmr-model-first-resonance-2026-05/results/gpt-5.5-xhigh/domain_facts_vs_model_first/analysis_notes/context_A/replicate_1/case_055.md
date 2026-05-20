Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The instructions first acquire a true 0-level reference: polarize, detect, then wait. Because full_expt = 0, the explicit 1-level reference block is skipped. The only microwave-driven measurement after that is a rabi_pulse_mod_wait_time followed by detection, so readout 1 is the mS = 0 reference and readout 2 is the post-MW signal readout.

The actual pulse settings are mod_depth = 1 and length_rabi_pulse = 52 ns. With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is close to a pi pulse. If the scan crossed a real pODMR resonance, the post-MW signal should approach the mS = +1 level and show a large decrease relative to the 0 reference, on the order of the stated 22% contrast scale.

The combined signal/reference ratio only reaches a largest dip of about 5.6% near 3.895 GHz, and the individual stored averages have differing baselines and modest, non-unique dips at several frequencies. The stored averages are affected by tracking cadence, and the raw signal does not show a clean, strong, frequency-localized transfer consistent with a near-pi pulse at this contrast scale.

Decision: resonance absent.
