Case podmr_052_2026-05-17-015447

I used inputs/sequence.xml as the sequence definition. The active sequence is Rabimodulated.xml. It first polarizes and detects the bright m_S = 0 reference, then waits, then applies a modulated Rabi microwave pulse, then detects the post-pulse signal. Because full_expt = 0, the optional m_S = +1 reference block is skipped. Therefore the two combined raw readouts are:

- readout 1: pre-microwave m_S = 0 optical reference
- readout 2: post-Rabi-pulse signal

Relevant pulse parameters from the provided sequence XML:

- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, rounded to 13 samples / 250 MHz = 52 ns
- mod_depth = 1
- freqIQ = 50 MHz

Quantitative model:

For a rectangular resonant Rabi pulse starting from m_S = 0, I used

P1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2))

with f_R = 10 MHz * mod_depth = 10 MHz and t = 52 ns. On resonance,

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected normalized post-pulse darkening on resonance is

0.22 * 0.996 = 0.219, about 22%.

The expected contrast from the same model at detunings of 0, 5, 10, and 15 MHz is approximately 21.9%, 16.5%, 6.0%, and 0.26%, respectively. Thus a resonance in the scan should produce a large, structured dip in readout 2 relative to readout 1 over adjacent frequency points, not just a single isolated excursion.

Observed normalized contrast, computed as 1 - readout2/readout1, ranges from -10.1% to +10.0%, with mean +1.5% and standard deviation about 3.9%. The largest positive contrast is at the high-frequency edge, but it is only about 10%, less than half the expected on-resonance signal for the active pulse. Neighboring points do not follow the expected resonant Rabi line shape: for example, a resonance centered at the last scan point would predict about 16.5% darkening one 5 MHz step away, while the observed neighboring point is -2.0%.

I also fit the explicit Rabi line-shape model to the normalized contrast. A constant baseline gives RMSE about 3.85%. Allowing a resonance center plus baseline with the physical 22% contrast only improves RMSE to about 3.39%, with the best center outside the scan near 3.934 GHz and driven mainly by the final edge point. That improvement is small relative to the observed point-to-point scatter and does not establish a resonance in the measured scan.

Decision: resonance_absent. The active 52 ns, mod_depth 1 pulse should give a near-full 22% pODMR darkening on resonance, but the measured readout ratio lacks a model-consistent resonant feature and is dominated by drift/scatter.
