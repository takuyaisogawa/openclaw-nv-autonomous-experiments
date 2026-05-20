Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active readouts are:
- First detection: after optical polarization, before the microwave pulse. This is the bright mS = 0 reference.
- Second detection: after rabi_pulse_mod_wait_time and then optical detection. Since full_expt = 0, the separate mS = +1 reference block is skipped.

The provided sequence uses mod_depth = 1 and length_rabi_pulse = 52 ns. At the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so a resonant microwave frequency should strongly reduce the second readout relative to the bright reference.

The raw data show a pronounced localized depression in the post-pulse readout around 3.875-3.885 GHz, deepest at 3.880 GHz where the first readout is about 39.98 and the second readout is about 28.06. That ratio is about 0.70, a drop larger than the usual 22 percent contrast scale but in the expected direction for resonant transfer. The first readout does not show a matching dip there, so the feature is not just a common-mode fluorescence fluctuation. The two stored averages both contribute to the depression, though those averages mainly reflect tracking cadence rather than a strong repeatability test.

Decision: resonance_present.
