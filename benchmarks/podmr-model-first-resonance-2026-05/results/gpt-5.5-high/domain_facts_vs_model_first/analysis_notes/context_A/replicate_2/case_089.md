Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The instructions have full_expt = 0, so the intermediate mS = +1 reference block is skipped. The two active detections are therefore:
- readout 1: true mS = 0 reference after optical polarization
- readout 2: signal after the Rabi-modulated microwave pulse

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. On resonance this should produce a large transfer from mS = 0 to mS = +1 and therefore a signal drop close to the setup contrast scale of about 22%.

The observed readout 2 minus readout 1 contrast is small and irregular across the scan, ranging only by a few percent and changing sign. The apparent dips near 3.830 and 3.900 GHz are about 4-5%, are not isolated clean resonance features, and are comparable to the scatter between the stored averages. The readouts mostly share slow drift rather than showing a strong microwave-induced contrast loss.

Decision: resonance_absent.
