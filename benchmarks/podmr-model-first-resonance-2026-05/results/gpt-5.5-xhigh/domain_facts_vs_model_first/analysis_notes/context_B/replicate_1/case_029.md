Case podmr_014_2026-05-16-124559.

I used the provided Rabimodulated.xml sequence rather than any case label. The active sequence polarizes the NV, performs a first detection, waits, skips the optional full_expt branch because full_expt = 0, applies one Rabi-modulated microwave pulse, then performs a second detection. Therefore readout 1 is the true m_S = 0 reference acquired before the microwave pulse, and readout 2 is the post-pulse pODMR signal. There is no active m_S = +1 reference readout in this run. The active pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns; with sample_rate = 250 MHz this is exactly 13 samples after rounding.

Physical model calculation:

For a rectangular microwave pulse, using frequency units in Hz,

P_transfer(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2)).

The given setup has f_R about 10 MHz at mod_depth = 1. With tau = 52 ns,

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant readout-2 suppression relative to the readout-1 reference is 0.22 * 0.996 = 0.219, or about 21.9%. For a local reference near 47 counts, the expected resonant readout is about 47 * (1 - 0.219) = 36.7 counts, before allowing for imperfect contrast, tracking drift, and noise. At +/-5 MHz detuning, the same pulse model predicts a transfer probability of about 0.75, so a dip spanning adjacent 5 MHz scan points is expected.

Observed data:

The combined arrays scan 3.825 to 3.925 GHz in 5 MHz steps. Readout 2 has a strong local depression from about 3.870 to 3.885 GHz. The minimum is at 3.875 GHz, where readout 1 = 48.538 and readout 2 = 39.115, giving readout2/readout1 = 0.806, i.e. a 19.4% suppression. The off-dip readout2/readout1 mean, excluding 3.870 through 3.885 GHz, is 0.998 with standard deviation 0.0246. The dip-window mean ratio is 0.866, with minimum 0.806.

I also fit the explicit finite-pulse model r2 = r1 * (1 - 0.22 * P_transfer(f - f0)), fitting only the resonance center. The best center was approximately 3.87836 GHz with SSE = 32.95. A no-resonance constant-ratio model r2 = q * r1 gave SSE = 170.97, so the fixed physical model improves SSE by a factor of 5.19. Letting the contrast amplitude float as a cross-check gives center approximately 3.87838 GHz and fitted contrast 18.4%, close to the expected 22% scale.

Decision:

The measured suppression magnitude and width are quantitatively consistent with a near-pi pulse pODMR resonance under the active sequence. The feature is too large and too pulse-shaped to treat as absent. I decide resonance_present.
