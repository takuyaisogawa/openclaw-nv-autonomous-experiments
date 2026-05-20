Active sequence and readout roles

The provided XML is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active settings are:

- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is exactly 13 samples after rounding.
- mod_depth = 1.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped. The adiabatic inversion setting is therefore not active in the executed sequence.
- The first detection occurs immediately after adj_polarize and is the bright m_S = 0 reference readout.
- The second detection occurs after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), so it is the microwave-pulse signal readout.

Quantitative model

Using the stated setup calibration, the Rabi frequency is approximately

f_R = 10 MHz * mod_depth = 10 MHz.

For a rectangular resonant microwave pulse of duration tau = 52 ns, I used the two-level transition probability

P_+1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)),

with delta in Hz. The fluorescence model for readout 2 normalized by the bright reference is

F2/F0 = 1 - C * P_+1(delta),

with C = 0.22 from the setup contrast scale.

On resonance this gives

P_+1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996,
expected F2/F0 = 1 - 0.22 * 0.996 = 0.781.

Observed normalized data

Using readout2/readout1 from the combined raw data:

- Off-dip median ratio, excluding 3.870-3.890 GHz, is 0.981.
- At 3.875 GHz the ratio is 30.635 / 40.962 = 0.748, a 23.8% drop from the off-dip median.
- At 3.880 GHz the ratio is 30.327 / 39.192 = 0.774, a 21.1% drop from the off-dip median.
- The expected on-resonance ratio from the calibrated pulse model is 0.781, very close to the observed central dip.

A fixed-contrast grid fit of the above pulse model to readout2/readout1 gave a best center near 3.8785 GHz, baseline scale 0.986, and SSE 0.021. A constant-ratio null fit gives SSE 0.111. At that best center the model predicts ratios of about 0.798 at 3.875 GHz and 0.775 at 3.880 GHz, matching the measured two-point dip shape within the experimental scatter.

The two stored averages both have their strongest normalized dip at 3.875 GHz, but I treat this only as a cadence sanity check rather than a strong independent repeatability test.

Decision

The active sequence is a bright-reference plus post-Rabi-pulse pODMR scan. The post-pulse readout contains a frequency-selective dip with the amplitude expected for a 52 ns, mod_depth 1 near-pi pulse and the known 22% contrast scale. I therefore decide that a pODMR resonance is present.
