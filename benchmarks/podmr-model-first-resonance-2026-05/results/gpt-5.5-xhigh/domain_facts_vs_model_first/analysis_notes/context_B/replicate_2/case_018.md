Case: podmr_003_2026-05-16-003531

Sequence identification:
- SequenceName is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active blocks: polarize, detection, wait; optional full_expt block is inactive because full_expt = 0; then rabi_pulse_mod_wait_time, detection, wait.
- Readout 1 is the polarized mS = 0 reference detection before the microwave pulse.
- Readout 2 is the post-pulse detection after the scanned microwave Rabi pulse.
- mod_depth = 1.
- length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz, round(5.2e-08 * 250e6) = 13 samples, so the active pulse duration remains 13 / 250e6 = 52 ns.

Physical model calculation:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1, use a square-pulse two-level transition model.
- For detuning d in cycles/s and Rabi frequency fR = 10 MHz, the transition probability after pulse length tau = 52 ns is:
  P(d) = fR^2 / (fR^2 + d^2) * sin^2(pi * tau * sqrt(fR^2 + d^2)).
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, essentially a pi pulse.
- With the stated mS = 0 to mS = +1 contrast scale of 22%, the expected resonant fluorescence drop is 0.22 * 0.996 = 0.219, about 22%.
- Expected drop fractions from the same model are approximately 16.5% at 5 MHz detuning, 6.0% at 10 MHz detuning, and near zero to a few percent beyond about 15 MHz except for weak finite-pulse sidelobes.

Measured comparison:
- The normalized signal readout2/readout1 is near unity over most of the scan but falls strongly around 3.875-3.880 GHz.
- At 3.875 GHz: readout1 = 35.942, readout2 = 29.346, ratio = 0.816, drop = 18.4%.
- At 3.880 GHz: readout1 = 39.981, readout2 = 28.058, ratio = 0.702, drop = 29.8%.
- A fixed-contrast model y = b * (1 - 0.22 * P(f - f0)) fit to readout2/readout1 gives best center f0 = 3.8775 GHz and b = 0.9947. Its SSE is 0.0461 versus 0.1485 for a flat normalized baseline, a 69.0% variance reduction.
- Allowing the contrast amplitude to float gives f0 = 3.8775 GHz and contrast = 25.1%, close to the expected 22% scale given noise/tracking variation.

Decision:
The observed dip has the right sign, frequency-localized shape, and magnitude for a near-pi pODMR pulse at mod_depth = 1 and 52 ns. The average traces should not be treated as a strong independent repeatability test, but both stored averages show a dip near the same frequency region. I decide that a pODMR resonance is present.
