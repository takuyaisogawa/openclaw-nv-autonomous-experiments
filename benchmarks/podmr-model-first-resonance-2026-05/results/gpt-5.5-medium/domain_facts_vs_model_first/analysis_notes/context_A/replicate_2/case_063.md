Active sequence assessment:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz. With full_expt = 0, the optional mS=+1 reference block is skipped. The two acquired readouts are therefore:

- readout 1: true mS=0 reference after optical polarization and detection
- readout 2: detection after the Rabi-modulated microwave pulse

The active pulse is rabi_pulse_mod_wait_time using length_rabi_pulse = 52 ns and mod_depth = 1. Given the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse on resonance. If a resonance were present, readout 2 should show a substantial darkening relative to the mS=0 reference, with the setup contrast scale allowing an effect up to about 22%.

The measured combined readouts do not show that behavior. The mean readout 2 level is essentially equal to readout 1, and the pointwise readout 2 minus readout 1 excursions are small compared with the expected contrast and change sign across the scan. There is a local negative difference around 3.84-3.855 GHz of only about 4-5%, while around 3.89 GHz readout 2 is brighter than the reference. The per-average overlays mainly show baseline/tracking shifts and do not establish a consistent resonance feature.

Decision: resonance_absent.
