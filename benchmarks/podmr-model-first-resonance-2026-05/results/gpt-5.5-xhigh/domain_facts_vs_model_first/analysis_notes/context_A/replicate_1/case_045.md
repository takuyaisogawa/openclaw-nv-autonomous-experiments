Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The provided XML has full_expt = 0, so the optional mS = +1 reference block is inactive. The two active detections are therefore:

- readout 1: true mS = 0 reference after polarization, before the microwave pulse.
- readout 2: pODMR signal after the modulated Rabi pulse.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At the stated setup calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so 52 ns is essentially a pi pulse. If the scanned microwave frequency hit the transition, the post-pulse signal readout should show a strong fluorescence loss relative to the mS = 0 reference, on the order of the setup contrast scale (about 22% for full mS = 0 to mS = +1 contrast).

The combined raw data do not show that behavior. The mean readouts are almost identical (readout 1 about 52.72, readout 2 about 52.73), and the post-pulse readout ranges only from about 51.08 to 54.50 counts rather than dropping toward the roughly 41 count level implied by a full 22% loss from the reference level. The largest normalized excursion is a single low ratio near 3.920 GHz, but that comes mainly from a high reference point rather than a clear signal-channel dip, and neighboring points do not form a convincing resonance line shape for a 52 ns pulse. The per-average overlay shows large baseline offsets between stored averages, consistent with tracking cadence, so those averages are not strong independent evidence of repeatable resonance structure.

Decision: resonance_absent.
