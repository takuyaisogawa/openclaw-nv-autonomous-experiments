The active scan is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz with 5 MHz steps. The sequence has full_expt = 0, so the optional mS = +1 reference block is skipped. The acquired readouts are therefore:

- readout 1: true mS = 0 fluorescence reference after optical polarization and detection.
- readout 2: fluorescence after the Rabi-modulated microwave pulse, followed by detection.

The provided sequence XML and exported variable table give length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 corresponds to about 10 MHz Rabi frequency, so 52 ns is close to a pi pulse. If the frequency sweep crossed a real pODMR resonance, the post-pulse readout should show a substantial fluorescence reduction relative to the mS = 0 reference, potentially on the order of the known 22% contrast scale when the pulse is effective.

The combined raw readouts do not show that behavior. Readout 2 is sometimes above readout 1, sometimes below it, and the apparent differences are only a few counts around a baseline near 50. The larger downward excursions toward the high-frequency end are not a clean, localized resonance feature and are not consistently supported by the two stored averages; those averages mostly show noisy/tracking-cadence variation rather than a repeatable spectral dip. Because the expected near-pi-pulse contrast should be much more distinct than the observed readout fluctuations, I classify this case as no pODMR resonance present.
