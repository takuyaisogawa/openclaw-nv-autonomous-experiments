Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence has full_expt = 0, so the conditional mS = +1 reference block is inactive. The two active detections are:
- readout 1: immediately after optical polarization, a true mS = 0 fluorescence reference.
- readout 2: after a single modulated Rabi microwave pulse, the pODMR signal readout.

The provided sequence XML sets mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If a resonance were present, readout 2 should show a large fluorescence decrease relative to readout 1, on the order of the stated 22% contrast scale for mS = 0 versus mS = +1.

The observed combined traces do not show that. The mean readout 1 level is about 42.67 and mean readout 2 is about 42.11, only about 0.56 counts lower, roughly 1.3% of the reference level. Individual scan points fluctuate, with some readout-2 dips and peaks, but they are small compared with the expected contrast and do not form a clean, reproducible pODMR resonance. The per-average overlay is dominated by baseline offsets between stored averages, which is consistent with tracking cadence rather than strong independent repeatability.

Decision: resonance absent.
