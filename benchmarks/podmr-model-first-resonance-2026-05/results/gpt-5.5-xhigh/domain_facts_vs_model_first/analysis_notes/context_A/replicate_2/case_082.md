I used the provided sequence XML and raw export for this case only.

Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles from the instructions:
- The first detection follows adj_polarize and is the true mS = 0 reference.
- full_expt = 0, so the optional mS = +1 reference block is inactive.
- The second detection follows rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so it is the pODMR signal readout after the microwave pulse.

Pulse settings:
- length_rabi_pulse = 52 ns.
- mod_depth = 1.
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse, so an on-resonance response should be a sizable suppression of the signal readout relative to the mS = 0 reference, potentially on the order of the setup contrast scale.

Data assessment:
- The two raw readouts are mostly close together, with signal-reference differences generally only a few percent.
- The large fall near the high-frequency end is present in both readouts, so it looks like common count/tracking drift rather than a microwave-specific resonance feature.
- The strongest negative paired differences are isolated or drift-correlated, not a clean localized pODMR dip, and they are much smaller than the expected contrast for a near-pi pulse on resonance.
- The per-average overlays do not provide a strong independent repeatability check here, and their largest deviations occur at different scan points.

Decision: resonance_absent.
