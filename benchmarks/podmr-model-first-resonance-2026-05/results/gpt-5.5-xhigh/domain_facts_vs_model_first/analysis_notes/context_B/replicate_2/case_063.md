Sequence and readout interpretation

The provided sequence XML is the active Rabimodulated sequence. It first polarizes the NV and immediately performs a detection, so readout 1 is the mS=0 reference. The `full_expt = 0` branch skips the explicit mS=+1 reference acquisition. The only active microwave manipulation before the final detection is:

`rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)`

followed by detection, so readout 2 is the pODMR signal after the microwave pulse. The active parameters from the provided XML are `mod_depth = 1`, `length_rabi_pulse = 5.2e-08 s`, and `sample_rate = 250 MHz`; the pulse is exactly 13 samples, so it remains 52 ns after rounding.

Quantitative expected signal model

Using the supplied setup calibration, the resonant Rabi frequency is approximately

`f_R = 10 MHz * mod_depth = 10 MHz`.

For a rectangular pulse starting in mS=0, the transfer probability versus detuning is

`P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2))`.

With `tau = 52 ns`, the on-resonance transfer is

`P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996`.

The setup contrast scale between mS=0 and mS=+1 is about 22%, so an on-resonance pODMR point should have

`readout2 / readout1 = 1 - 0.22 * 0.996 = 0.781`,

or about a 21.9% dip. With the observed reference level near 49.86 raw counts, that is an expected dip of about 10.9 raw counts. The scan step is 5 MHz; even if the resonance fell halfway between scan points, the nearest sampled detuning of 2.5 MHz gives `P = 0.929` and an expected ratio of 0.796. At 5 MHz detuning the expected ratio is still 0.835. A true resonance should therefore be a large, broad dip in readout 2 relative to readout 1.

Observed data comparison

The combined readout ratio `readout2 / readout1` has mean 0.9986, standard deviation 0.0299, minimum 0.9487 at 3.850 GHz, and maximum 1.0715 at 3.890 GHz. The largest observed combined dip is only 5.1%, or 2.62 raw counts, much smaller than the expected 21.9% / 10.9-count dip for this pulse.

I also fit the rectangular-pulse response to the normalized ratio with a floating linear baseline. The best positive dip-like component was only about 0.054 in ratio units, centered near 3.8507 GHz, far below the expected 0.219. Forcing the expected 22% contrast pulse response made the squared residual about 2.84 times worse than a no-resonance linear baseline. The unconstrained best response around 3.89 GHz is actually peak-like, not dip-like. The stored averages show baseline offsets consistent with tracking cadence and do not provide a strong independent repeatability test.

Decision

Given the active 52 ns, mod_depth=1 pulse, the physically expected pODMR resonance would be much larger than the observed normalized fluctuations. I therefore classify this case as resonance absent.
