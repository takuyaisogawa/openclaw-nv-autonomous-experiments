Case: podmr_077_2026-05-17-100811

I used only the provided sequence XML and raw export for this case.

Active sequence and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive. The adiabatic inversion code is not active in this run.
- readout 1 is the true mS = 0 reference after optical polarization and before the microwave test pulse.
- readout 2 is the signal readout after rabi_pulse_mod_wait_time.
- mod_depth = 1 from the provided XML variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples, so rounding leaves it at 52 ns.

Quantitative model:
For mod_depth = 1, the stated setup calibration gives a Rabi frequency of about 10 MHz. For a square pulse of duration t = 52 ns, the driven population transfer probability at detuning delta is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * sqrt(f_R^2 + delta^2) * t),

where f_R and delta are in cycles/s. With f_R = 10 MHz:
- On resonance, P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- With the 22% mS = 0 to mS = +1 contrast scale, the expected on-resonance fluorescence reduction is 0.22 * 0.996 = 0.219, or about 21.9%.
- The mean readout 1 level is 50.94 counts, so an on-resonance readout 2 value should be around 50.94 * (1 - 0.219) = 39.77 counts, a drop of about 11.16 counts.
- Even if the resonance sat halfway between two 5 MHz scan points, the nearest measured point would have |delta| <= 2.5 MHz, giving P = 0.929 and an expected drop of about 20.4%, or about 10.4 counts from the observed reference level.

Observed data comparison:
- Mean readout 1: 50.94 counts.
- Mean readout 2: 50.77 counts.
- Mean readout 2 - readout 1: -0.17 counts.
- Standard deviation of readout 2 - readout 1 across scan points: 1.19 counts.
- Largest observed fractional readout 2 drop relative to readout 1: 4.2% at the first scan point, much smaller than the 20-22% expected near a resonance and not accompanied by a consistent resonance-shaped feature.
- The readout 2 - readout 1 difference changes sign across the scan, with positive excursions as well as negative excursions, which is consistent with scan/tracking fluctuation at the observed scale rather than a microwave resonance response.
- The stored per-average traces show large common offsets between averages; I do not treat those averages as an independent repeatability test because stored averages often reflect tracking cadence.

Decision:
The active pulse should produce a large post-pulse readout dip if a pODMR resonance were sampled. The observed contrast is far too small and not resonance-shaped. I decide that a pODMR resonance is absent.
