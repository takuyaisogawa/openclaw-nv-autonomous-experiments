Active pulse sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

Sequence/readout roles:
- full_expt is 0, so the optional m_S=+1 reference block is skipped.
- readout 1 is acquired immediately after optical polarization and is the m_S=0/bright reference for each frequency point.
- readout 2 is acquired after a rabi_pulse_mod_wait_time pulse and is the microwave-driven pODMR signal readout.

Pulse settings used for the decision:
- mod_depth = 1 from the provided sequence variable values.
- length_rabi_pulse = 52 ns, rounded on a 250 MHz sample clock.
- With the stated setup scale, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If an addressed NV resonance were present, the driven readout should show a sizable fluorescence reduction approaching the setup contrast scale, about 22%, at resonance.

Data assessment:
The two stored averages are mainly tracking-cadence snapshots rather than strong repeatability evidence. The combined readout after the microwave pulse does not show a coherent, localized dip relative to the bright reference with the expected contrast. Several point-to-point excursions are comparable to fluctuations in the reference readout itself, and the largest apparent separation occurs where the reference readout has an isolated spike rather than a stable resonance-shaped feature. Across the frequency sweep, readout 2 remains broadly similar to readout 1 and lacks the pronounced normalized contrast expected for a near-pi pulse on resonance.

Decision: resonance_absent.
