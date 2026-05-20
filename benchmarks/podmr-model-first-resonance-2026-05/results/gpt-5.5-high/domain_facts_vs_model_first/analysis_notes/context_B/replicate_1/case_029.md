Case: podmr_014_2026-05-16-124559

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first performs optical polarization and detection. This is readout 1, the true m_S = 0 fluorescence reference.
- full_expt is zero, so the optional m_S = +1 reference block is inactive.
- The sequence then applies one modulated Rabi microwave pulse and performs detection. This is readout 2, the signal after the scanned microwave pulse.
- The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, round(52 ns * 250 MHz) = 13 samples, so the rounded duration remains 52 ns.
- The provided sequence XML and exported variable values give mod_depth = 1.

Quantitative physical model:

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse of duration t = 52 ns, the driven two-level transfer probability versus microwave detuning delta is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

where f_R = 10 MHz and delta is in Hz. On resonance this gives

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The m_S = 0 to m_S = +1 contrast scale is about 22%, so a fully resonant pulse should reduce the second readout by roughly 0.22 * P(0), approximately 21.9% of the local m_S = 0 fluorescence. Using the off-resonance readout-2 baseline estimated from points outside 3.865-3.885 GHz, B = 46.734 raw-count units, the expected on-resonance raw-count minimum is

B * (1 - 0.22 * 0.996) = 36.45,

an expected dip amplitude of about 10.28 counts. This is the maximum expected value for ideal contrast and exact calibration.

Observed data:

- readout 1 mean is 46.92 counts and does not show the narrow deep dip.
- readout 2 off-resonance baseline is about 46.73 counts.
- readout 2 has a minimum of 39.12 counts at 3.875 GHz, with 39.56 counts at 3.880 GHz.
- The observed dip amplitude is 46.73 - 39.12 = 7.62 counts, or 16.3% of baseline.
- The same feature appears in the two stored averages: average 1 has an 8.65 count dip near 3.880 GHz, and average 2 has a 7.32 count dip near 3.875 GHz. These averages are not treated as a strong independent repeatability test, but they are consistent with the same feature.

Model comparison:

- A fixed-contrast rectangular-pulse model with the 10 MHz, 52 ns pulse and 22% contrast gives the best center near 3.87742 GHz and reduces the readout-2 sum of squared residuals to 36.56, compared with 132.75 for a constant-baseline no-resonance model using the readout-2 mean.
- Allowing only the dip amplitude and baseline to fit while keeping the same finite-pulse lineshape gives center 3.87742 GHz, baseline 47.11, amplitude 8.30 counts, fractional contrast 17.6%, and sum of squared residuals 19.03.

Decision:

The pulse parameters predict a large finite-pulse pODMR dip if a transition lies in the scan. The observed readout-2-only dip near 3.875-3.880 GHz has the expected sign, approximate width, center behavior, and a physically plausible amplitude somewhat below the nominal contrast ceiling. I therefore decide that a pODMR resonance is present.
