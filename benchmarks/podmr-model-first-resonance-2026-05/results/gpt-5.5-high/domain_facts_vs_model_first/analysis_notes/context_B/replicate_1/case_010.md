Case podmr_017_2026-05-12-134151

Sequence inspection:
- Active sequence: Rabimodulated.xml, scanned mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and take a detection readout. This is the m_S = 0 reference readout.
- full_expt = 0, so the conditional +1 reference block is inactive even though do_adiabatic_inversion is true.
- The active microwave operation is one rabi_pulse_mod_wait_time before the second detection readout. Thus readout 1 is the pre-pulse bright reference and readout 2 is the post-pulse signal readout.
- Pulse duration: length_rabi_pulse = 52 ns after sample-rate rounding at 250 MHz.
- mod_depth: 1 in the provided sequence/variable values.

Physical model calculation:
The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi frequency is about 10 MHz at mod_depth = 1, so the expected resonant transfer probability for a 52 ns square pulse is

P_res = sin^2(pi * f_R * tau)
      = sin^2(pi * 10e6 * 52e-9)
      = 0.996.

Therefore an on-resonance pulse should reduce the post-pulse readout by about

contrast * P_res = 0.22 * 0.996 = 0.219,

or about 21.9% of the bright readout. With the observed readout level near 23 counts, this is an expected dip of about 5.0 counts in readout 2 relative to readout 1.

Including finite detuning for a square pulse,

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * tau * sqrt(Omega^2 + delta^2)),

with Omega = 10 MHz and tau = 52 ns. If a resonance were centered on a scan point, the expected fractional fluorescence dips at detunings 0, +/-5 MHz, and +/-10 MHz would be approximately 21.9%, 16.5%, and 6.0%, respectively. Thus a real resonance should be a large multi-point feature, not a single isolated noisy point.

Observed data comparison:
- Combined readout 1 mean: 22.70 counts.
- Combined readout 2 mean: 22.77 counts.
- The normalized dip (readout1 - readout2) / readout1 ranges from -10.3% to +8.7%.
- The largest positive dip is 8.7% at 3.855 GHz, but its adjacent points are -4.8% and -8.7%, opposite to the expected broad square-pulse lineshape.
- The largest observed dip corresponds to about 2.1 counts, much smaller than the about 5.0-count on-resonance expectation for this pulse.
- A linear no-resonance model for the normalized readout difference has RMS residual about 4.83%.
- A resonance model with the physically expected 22% contrast and a center constrained inside the scan range worsens the residuals relative to the no-resonance baseline.
- A free-amplitude resonance-shaped fit constrained inside the scan range prefers only about 8.9% peak contrast, far below the expected 21.9%, and mainly fits small fluctuations rather than the required multi-point feature.
- The two stored averages show large drift/tracking structure, so their similarity at any one point is not a strong independent repeatability test.

Decision:
Given the active pulse sequence, the expected resonant pODMR signal should be a large and broad reduction of readout 2 relative to readout 1. The measured readout-pair difference does not show that physical signature. I classify this case as resonance_absent.
