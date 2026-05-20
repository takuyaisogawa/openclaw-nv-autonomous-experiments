Case podmr_020_2026-05-16-165809.

I used the provided sequence XML and the exported variable values, not any prior labels or sibling cases. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The code polarizes, performs a detection, waits, applies one modulated Rabi microwave pulse, and performs a second detection. The optional "Acquire 1 level reference" block is inactive because full_expt = 0, so do_adiabatic_inversion does not affect the active readouts.

Readout roles:
- readout 1 is the pre-microwave "true 0 level reference" after optical polarization.
- readout 2 is the post-microwave signal after the Rabi pulse.

Pulse parameters from the active XML/variables:
- mod_depth = 1.
- length_rabi_pulse = 52 ns.
- sample_rate = 250 MHz, so the pulse length is already exactly 13 samples and remains 52 ns after rounding.

Quantitative physical model:
For a rectangular driven two-level pulse I used

P1(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),

where Omega = 2*pi*10 MHz at mod_depth = 1, tau = 52 ns, and Delta = 2*pi*(f - f_res). On resonance this gives

P1(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

With the stated 22% mS=0 to mS=+1 contrast, the expected on-resonance fractional PL drop in readout 2 relative to readout 1 is

0.22 * 0.996 = 0.219.

At the observed reference level of about 45 counts, a resonance driven by this pulse should therefore produce a signal readout near 45 * (1 - 0.219) = 35.1 counts, i.e. a dip of about 9.9 counts relative to the reference readout.

Data comparison:
The combined normalized contrast y = (readout1 - readout2) / readout1 has mean 0.014 and maximum 0.0706 at 3.825 GHz. Several points around 3.905-3.915 GHz have the opposite sign, with readout 2 brighter than readout 1. Thus the largest observed drop is only about one third of the expected resonant pi-pulse response, and it is not a broad 52 ns Rabi lineshape.

I also fit the normalized contrast to the Rabi lineshape model while allowing a linear baseline drift versus frequency. A baseline-only linear model gave RMSE 0.0247. A fixed +22% physical resonance model gave worse RMSE 0.0420. Allowing a positive Rabi feature amplitude from 0 to 22% gave a best amplitude of only 4.55%, located at the scan edge, not a robust resonance-sized feature. If the feature amplitude is allowed to take either sign, the best fit is negative, about -6.3%, near 3.9075 GHz, meaning the data prefer a small brightening rather than the expected darkening.

The two stored averages show large tracking-like drifts and do not provide a strong independent repeatability check. They also do not recover the expected near-22% driven contrast.

Decision: resonance_absent. The active 52 ns, mod_depth 1 pulse should almost fully transfer population on resonance and create a roughly 22% readout-2 dip, but the measured signal only shows small drift-scale structure and no physically signed resonance-sized feature.
