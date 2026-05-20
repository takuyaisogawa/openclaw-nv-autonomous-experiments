Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Sequence/readout interpretation:
- The sequence first performs optical polarization and detection, giving the true m_S = 0 / bright reference readout.
- full_expt = 0, so the optional m_S = +1 reference branch is disabled despite do_adiabatic_inversion being true.
- The active experimental readout is after rabi_pulse_mod_wait_time followed by detection.
- Therefore readout 1 is the bright reference and readout 2 is the post-microwave-pulse signal.

Pulse settings:
- mod_depth = 1 from the provided sequence XML / variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s.
- With about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is approximately a pi pulse, so a real resonance should produce a sizeable fluorescence reduction in the signal readout relative to the bright reference, potentially on the order of the setup contrast scale rather than a sub-percent effect.

Data assessment:
- The raw readouts fluctuate around 50 counts with only two stored averages.
- The signal/reference ratio ranges roughly from 0.96 to 1.05, with isolated negative excursions near 3.870, 3.905, and 3.925 GHz rather than a consistent resonance-shaped dip.
- The per-average traces show substantial offsets and point-to-point variation; the stored averages are mainly tracking-cadence evidence and do not independently confirm repeatability.
- There is no clear, localized, reproducible fluorescence loss of the expected magnitude for a near-pi pulse.

Decision: resonance_absent.
