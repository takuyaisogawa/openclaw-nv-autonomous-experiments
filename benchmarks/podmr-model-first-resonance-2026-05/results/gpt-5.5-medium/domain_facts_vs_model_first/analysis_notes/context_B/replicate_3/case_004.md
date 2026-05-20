Case podmr_007_2026-05-11-064944

Sequence identification:
- The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence first polarizes the NV and detects the true m_S = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" branch is inactive even though the branch contains a nominal pi-pulse/readout reference.
- The active experimental readout is the detection after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay).
- Therefore readout 1 is the polarized m_S = 0 reference and readout 2 is the post-Rabi-pulse signal being tested for ODMR contrast.

Pulse parameters from the provided XML:
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1.
- setup Rabi frequency estimate at mod_depth = 1 is 10 MHz.
- setup m_S = 0 to m_S = +1 contrast scale is about 22%.

Explicit signal model:
I used the rectangular driven two-level pulse model

P(f, f0) = Omega^2 / (Omega^2 + Delta^2) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t),

with Omega = 2*pi*10 MHz, Delta = 2*pi*(f - f0), and t = 52 ns. The fluorescence model for the post-pulse readout is

S2(f) = S0 * (1 - C * P(f, f0)),

where C = 0.22 and S0 is the m_S = 0 readout level. On resonance, P = sin^2(pi * 10e6 * 52e-9) = 0.996. With the observed S0 level near 31.72 raw counts, the expected resonant drop is

31.72 * 0.22 * 0.996 = 6.95 raw counts,

so the expected on-resonance readout ratio is S2/S1 = 0.781.

Observed data check:
- Mean readout 1 = 31.72.
- Mean readout 2 = 31.55.
- Mean readout 2 - readout 1 = -0.18 raw counts.
- Standard deviation of pointwise readout 2 - readout 1 = 1.70 raw counts.
- The largest negative pointwise difference is -3.81 raw counts at 3.855 GHz, much smaller than the approximately -6.95 count resonant expectation and not supported by a model-shaped resonance.
- A least-squares fit of the model-shaped ratio S2/S1 = baseline - A*P over possible resonance centers gives best A = -0.076 at 3.915 GHz, i.e. the fitted feature has the opposite sign from the expected ODMR dip. The expected physical amplitude is A about +0.22.

Decision:
The active pulse should produce a large, broad ODMR dip if a resonance lies in the scan window, but the measured post-pulse readout does not show the expected 22% contrast-scale decrease. The data are consistent with tracking/noise-scale fluctuations rather than a pODMR resonance.
