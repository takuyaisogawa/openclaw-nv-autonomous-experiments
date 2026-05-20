Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- readout 1 is the true m_S = 0 optical reference, acquired after laser polarization and before the microwave pulse.
- readout 2 is the signal readout after a modulated Rabi pulse.
- The m_S = +1 reference block is inactive because full_expt = 0, so no independent 1-level reference is acquired.

Pulse settings used for the decision:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s and therefore still 52 ns.
- With the provided setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance, so a real resonance should produce a large reduction in the signal readout relative to the 0 reference, on the order of the setup contrast scale of about 22%.

Data assessment:
The two combined raw readout traces both show a gradual upward drift across the scan. The post-pulse readout is not consistently or locally suppressed at a single frequency by anything close to the expected 22% contrast for a resonant pi pulse. Differences between readout 2 and readout 1 are small and change sign, and the per-average traces mainly show shared drift/tracking structure rather than a repeatable resonance feature. Since stored averages can reflect tracking cadence, the per-average overlay is not strong independent evidence for a resonance.

Decision: resonance_absent.
