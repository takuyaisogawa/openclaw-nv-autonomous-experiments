Case: podmr_019_2026-05-16-164247

Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The active instructions first polarize the NV, then perform a detection before any microwave pulse. Because full_expt = 0, the "Acquire 1 level reference" block is skipped, so there is no active m_S = +1 reference in this acquisition. The active Rabi-modulated microwave pulse is then applied and followed by a second detection. Therefore readout 1 is the pre-pulse bright m_S = 0 reference and readout 2 is the post-pulse signal readout.

Relevant pulse parameters from the provided sequence XML:

- length_rabi_pulse = 52 ns, rounded at 250 MS/s and unchanged.
- mod_depth = 1.
- mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the nominal 1-level reference pulse/readout block is inactive.

Explicit physical model

For a square resonant pulse, the population transferred from m_S = 0 to m_S = +1 is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t),

using cycle frequencies. The stated setup gives f_R = 10 MHz at mod_depth = 1, and t = 52 ns. On resonance:

theta = 2*pi*f_R*t = 2*pi*(10e6)*(52e-9) = 3.267 rad = 187.2 degrees.
P(0) = sin^2(theta/2) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, a resonance driven by this pulse should produce a fractional post-pulse readout reduction of about

0.22 * 0.996 = 0.219, or 21.9%,

relative to the bright reference, near the resonance frequency.

Data comparison

Using readout 1 as the bright reference and readout 2 as the post-pulse signal, the observed ratio readout2/readout1 has:

- mean ratio = 0.9830, equivalent to a mean reduction of 1.7%.
- minimum ratio = 0.9293 at 3.895 GHz, equivalent to a maximum single-point reduction of 7.1%.
- several points have readout2 >= readout1, including 3.835, 3.860, 3.865, 3.910, and 3.925 GHz.

I also fit the detuned Rabi response shape above to the normalized ratios with a free baseline and free dip amplitude over possible resonance centers in the scan range. The best apparent dip amplitude was about 0.0396, or 4.0%, compared with the 21.9% expected from the pulse and contrast scale. The flat-ratio SSE was 0.01597 and the best Rabi-shaped SSE was 0.01337, only a small improvement for a much smaller-than-expected feature.

Decision

The active pulse should create a large near-pi-pulse pODMR dip if a resonance is present in the scanned range. The observed data show only small, irregular readout differences that are far below the expected 22% contrast-scale signal and do not form a convincing Rabi-line response. Stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.

Prediction: resonance_absent.
