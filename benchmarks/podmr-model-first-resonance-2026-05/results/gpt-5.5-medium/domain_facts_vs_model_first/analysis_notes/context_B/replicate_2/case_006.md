<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_006

Sequence interpretation

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided XML and exported variable values, length_rabi_pulse is 52 ns and mod_depth is 1. The pulse program first polarizes and detects a true mS=0 reference, then, because full_expt is 0, skips the explicit mS=+1 reference block. It then applies one rabi_pulse_mod_wait_time pulse of length_rabi_pulse at mod_depth and performs the second detection. Therefore readout 1 is the pre-microwave mS=0 reference and readout 2 is the post-pulse signal readout.

Physical model calculation

Use a two-level driven transition model for the post-pulse population:

P(f) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * t * sqrt(f_R^2 + df^2))

where f_R is the resonant Rabi frequency in cycles/s, df is frequency detuning, and t is pulse duration. The setup facts give f_R about 10 MHz at mod_depth = 1, approximately linear in mod_depth. For the active mod_depth = 1 and t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated mS=0 to mS=+1 contrast scale of 22 percent, the expected on-resonance readout drop is:

0.22 * 0.996 = 0.219, or about 22 percent.

At a typical raw reference level near 40 counts, this corresponds to about 8.8 counts. Because the Rabi frequency is 10 MHz, neighboring scan points should also be affected: at +/-5 MHz detuning the same model gives about 0.165 relative drop, still roughly 6.6 counts at a 40 count reference.

Observed quantitative check

Using readout 1 as the local reference and readout 2 as the signal, the largest observed signal drop is at 3.875 GHz:

readout1 = 42.1154, readout2 = 38.2500, relative drop = 9.18 percent.

The adjacent points are not consistent with the active-pulse resonance model:

3.870 GHz: observed drop = 6.46 percent
3.875 GHz: observed drop = 9.18 percent
3.880 GHz: observed drop = -0.28 percent

The maximum observed dip is much smaller than the 21.9 percent on-resonance expectation, and the expected broad response at neighboring points is absent, especially on the high-frequency side.

I also fit the normalized readout ratio to the fixed-amplitude two-level model while allowing an offset and linear baseline drift. For mod_depth = 1, the best model residual was worse than a null linear-drift baseline:

resonance model RSS = 0.0445
null linear baseline RSS = 0.0214

This means the expected active-pulse resonance shape is not supported by the data.

Note on sequence discrepancy

The raw_export embedded Sequence text contains a stale-looking mod_depth = 0.3 string, but the provided sequence XML and exported Variable_values both give mod_depth = 1. The decision uses the active provided XML/variable values as requested. Even if mod_depth = 0.3 were considered, the expected on-resonance contrast would be about 4.9 percent, but the apparent feature is not cleanly repeatable across the two stored averages, and stored averages may mainly reflect tracking cadence rather than independent repeatability.

Decision

No pODMR resonance is present. The observed readout differences are compatible with drift/tracking and noise, not with the expected 52 ns, mod_depth = 1 Rabi-pulse resonance.
