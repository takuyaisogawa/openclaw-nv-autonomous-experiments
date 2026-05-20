Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles from the XML:
- The first detection follows adj_polarize and is the true mS = 0 fluorescence reference.
- full_expt = 0, so the optional mS = +1 reference block is skipped.
- The second detection follows rabi_pulse_mod_wait_time and is the microwave-driven readout.

Pulse settings:
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 in the provided sequence XML / variable values.
- With the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse on resonance.

Decision:
The driven readout shows a clear, localized fluorescence loss near 3.875-3.88 GHz while the mS = 0 reference remains near 30 counts. The minimum driven readout is about 24.15 counts versus a simultaneous reference of about 30.04 counts, a drop of roughly 19.6%, close to the expected 22% mS = 0 to mS = +1 contrast for a near-pi pulse. The feature is frequency-localized and recovers away from the dip, while the per-average traces mainly show tracking drift rather than independent repeatability. This supports a real pODMR resonance.
