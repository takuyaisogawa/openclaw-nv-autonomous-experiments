Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz.

The sequence first polarizes and detects a true mS=0 reference, then waits. Because full_expt = 0, the optional mS=+1 reference branch is inactive, despite the adiabatic inversion boolean being set. The active microwave operation is a modulated Rabi pulse followed by detection, so the two combined readouts should be interpreted as the 0 reference and the post-pulse signal readout rather than two independent resonance traces.

From the provided sequence XML and exported variable values, the Rabi pulse duration is 52 ns. The XML file lists mod_depth = 1, and the exported variable values also report mod_depth = 1, while the embedded saved sequence text contains an older/default-looking mod_depth = 0.3. Taking the provided XML/exported active values, the expected Rabi frequency is about 10 MHz, so a 52 ns pulse is close to a pi pulse. On resonance, the post-pulse signal should move substantially toward the mS=+1 fluorescence level, with a contrast scale on the order of the stated 22% between mS=0 and mS=+1.

The combined readouts do not show a localized pODMR resonance feature with that behavior. Readout 2 is often above readout 1 at lower frequencies, crosses gradually, and is only modestly lower over parts of the high-frequency end. The per-average overlays mainly show large tracking-like baseline shifts between the two stored averages, consistent with the warning that averages reflect tracking cadence rather than strong repeatability. The apparent structure is broad drift/crossover rather than a repeatable resonance dip or peak tied to the microwave scan.

Decision: resonance absent.
