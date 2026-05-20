Case: podmr_068_2026-05-17-075825

I used the provided sequence XML, not any external labels or sibling cases. The active sequence is Rabimodulated.xml / Rabi-modulated pODMR while sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Active readout roles from the instruction order:

1. adj_polarize followed by detection: this is the true m_S = 0 reference readout, with no microwave pulse before it.
2. The "Acquire 1 level reference" block is inactive because full_expt = 0, so no independent m_S = +1 reference is acquired.
3. rabi_pulse_mod_wait_time followed by detection: this is the pODMR signal readout after the microwave pulse.

Pulse parameters from the XML:

- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns
- sample-rate rounded pulse length = round(52 ns * 250 MHz) / 250 MHz = 13 samples / 250 MHz = 52 ns
- mod_depth = 1

Quantitative expected-signal model:

The supplied Rabi-frequency scale is f_R = 10 MHz at mod_depth = 1, linear in mod_depth, so this case has f_R = 10 MHz. For a resonant square pulse, the transferred population is

P_1 = sin^2(pi * f_R * t).

With t = 52 ns:

P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a real on-resonance transition should produce a post-pulse signal decrease of

0.22 * 0.996 = 0.219, or about 21.9% relative to the reference readout.

Using the detuned Rabi model,

P_1(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz and Delta = 2*pi*detuning. If the resonance lies halfway between adjacent 5 MHz scan points, the nearest-point expected contrast is still 20.4%. At 5 MHz detuning it is still 16.5%. Thus a resonance inside the swept range should be a large paired drop of readout 2 versus readout 1 over one or more neighboring points.

Data comparison:

I compared the second readout against the first readout point by point using (readout2 - readout1) / readout1. The combined data have:

- mean paired contrast = -0.78%
- minimum paired contrast = -4.47% at 3.855 GHz
- maximum paired contrast = +3.99% at 3.835 GHz
- standard deviation of paired contrast = 1.98%

The two stored averages separately have minimum paired contrasts of -7.00% and -8.32%, but these minima occur at different scan points and the prompt notes that stored averages often reflect tracking cadence rather than a strong repeatability test. The raw readouts also share a common drop near the high-frequency end, which appears in both the reference and post-pulse readouts and is therefore not the sequence-defined pODMR contrast.

A least-squares scan of the detuned Rabi line shape against the paired contrast gives a best-fit effective contrast amplitude of only about 2.2%, far below the expected 22%. Forcing the physical 22% contrast model gives a much worse residual than a flat percent-level paired-difference model.

Decision: the expected physical signal for the active 52 ns, mod_depth 1 pulse is an approximately 20% reference-normalized drop, but the observed sequence-defined signal channel shows only percent-level nonrepeatable deviations. I therefore decide that a pODMR resonance is absent.
