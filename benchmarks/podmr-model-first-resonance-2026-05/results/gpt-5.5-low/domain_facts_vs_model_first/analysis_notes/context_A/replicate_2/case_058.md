Sequence interpretation:
- Active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional mS=+1 reference block is disabled.
- Readout 1 is the true mS=0 reference after optical polarization and detection.
- Readout 2 is the signal detection after the modulated Rabi microwave pulse.
- The active Rabi pulse is length_rabi_pulse = 52 ns with mod_depth = 1.

Domain-based expectation:
- At mod_depth = 1 the Rabi frequency is about 10 MHz, so a 52 ns pulse is approximately a pi pulse.
- For this setup a real resonance should therefore produce a sizeable decrease in the post-pulse signal relative to the mS=0 reference, on the order of the 22% contrast scale when well driven.

Data assessment:
- The two raw readout traces remain close together across the scan, and readout 2 is often comparable to or higher than readout 1 rather than showing a localized fluorescence dip.
- There is no robust dip at a plausible resonance frequency; the largest excursions are small, irregular, and comparable to baseline drift/noise.
- The two stored averages mainly show a common tracking offset between averages, so they should not be interpreted as strong independent repeatability evidence.

Decision:
No pODMR resonance is present in this scan.
