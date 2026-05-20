Active sequence: Rabimodulated.xml, varying mw_freq across 3.825-3.925 GHz.

Sequence/readout interpretation:
- full_expt is 0, so the optional mS=+1 reference block is not active.
- The first detection occurs immediately after optical polarization and is the bright mS=0 reference readout.
- The second detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...), so it is the microwave-driven test readout.
- Active length_rabi_pulse is 52 ns. Active mod_depth is 1 from the provided variable values/sequence file.

Pulse-strength check:
- The given setup has about 10 MHz Rabi frequency at mod_depth=1, so a 52 ns pulse is close to a pi pulse.
- At resonance, this should transfer substantial population out of mS=0 and can produce close to the full ~22% bright-to-dark contrast.

Data assessment:
- Readout 1 stays roughly flat around 35-37 counts across the scan, consistent with a bright reference.
- Readout 2 has a clear, localized dip near 3.875-3.88 GHz, falling to about 28.2 counts while neighboring off-resonance values are around 35-37 counts.
- The drop is about 7-8 counts relative to the bright reference/off-resonance level, roughly 20-22%, matching the expected contrast scale for a near-pi pODMR pulse.
- The per-average traces show the same central depression despite only two stored averages; the averages mostly reflect tracking cadence, but the combined feature is large and spectrally localized.

Decision: resonance_present.
