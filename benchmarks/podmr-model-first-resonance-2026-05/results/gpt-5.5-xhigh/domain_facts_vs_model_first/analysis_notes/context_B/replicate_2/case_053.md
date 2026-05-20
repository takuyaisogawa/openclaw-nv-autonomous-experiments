Sequence identification and readout roles

The provided XML is Rabimodulated.xml. The active variables are sample_rate = 250 MHz, mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps, length_rabi_pulse = 52 ns, mod_depth = 1, and full_expt = 0. The pulse duration is unchanged by the sequence rounding because 52 ns is exactly 13 samples at 250 MHz.

Because full_expt = 0, the "Acquire 1 level reference" block is skipped. The two stored readouts are therefore:

1. readout 1: true mS = 0 fluorescence reference after optical polarization and before the microwave pulse.
2. readout 2: fluorescence after the active Rabi-modulated microwave pulse, followed by detection.

Quantitative expected-signal model

Using the stated setup facts, the Rabi frequency at mod_depth = 1 is about f_R = 10 MHz. For a rectangular resonant pulse with detuning Delta, I used the standard driven two-level transfer probability:

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

with t = 52 ns and Delta in cycles/s. On resonance,

P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The mean mS = 0 reference readout is 49.348 counts. With the stated 22% mS = 0 to mS = +1 contrast scale, a resonant pi-like pulse should lower the second readout by

49.348 * 0.22 * 0.996 = 10.814 counts,

giving an expected resonant readout near 38.53 counts, or a normalized dip of about 21.9% relative to readout 1.

The finite-detuning transfer is still large on the 5 MHz scan grid: P(2.5 MHz) = 0.929 and P(5 MHz) = 0.749, corresponding to expected drops of about 10.1 and 8.1 counts. Thus a resonance inside the scan range should produce a large localized negative feature in readout2 - readout1 even if centered between adjacent scan points.

Observed quantitative comparison

From the combined raw data, the mean readout 1 is 49.348 counts and the mean readout 2 is 49.194 counts, so the mean readout2 - readout1 difference is only -0.154 counts. The most negative point is -2.538 counts at 3.850 GHz, about -4.91% of the local reference. Another negative tail appears near 3.910 to 3.925 GHz, but it is also only a few counts. The largest positive deviation is +4.212 counts at 3.855 GHz. These point-to-point excursions are much smaller than the expected 10.8-count resonant drop and are not a clean localized pODMR dip.

I also fit the finite-detuning Rabi response template to readout2 - readout1. A no-resonance constant-difference model has SSE = 53.19. The best free-amplitude resonance-template fit prefers a negative drop amplitude, A = -2.54 counts in the model d = b - A P(Delta), meaning it fits a small positive bump rather than the expected PL decrease. Forcing the physically expected 10.8-count drop gives best SSE = 163.36, much worse than the no-resonance model, even with the resonance center allowed to vary across the scan.

Stored averages here are not treated as a strong repeatability test because they can reflect tracking cadence. They are consistent with the combined data showing several-count drift/noise, not with the large dip expected from the pulse model.

Decision

The active sequence should produce an easily visible negative pODMR feature if the scanned transition is resonant, but the observed readout2 - readout1 data do not show the required amplitude or template shape. I therefore classify this case as resonance_absent.
