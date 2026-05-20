Case: podmr_006_2026-05-11-020739

Sequence interpretation

The supplied sequence is Rabimodulated.xml. It scans mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions polarize the NV, take one detection, wait, then apply one modulated Rabi pulse and take a second detection. The optional "Acquire 1 level reference" block is skipped because full_expt = 0, so do_adiabatic_inversion is not active in this run despite being true as a boolean variable.

Readout roles:
- readout 1: detection immediately after optical polarization, i.e. the bright m_S = 0 reference for each frequency point.
- readout 2: detection after the microwave Rabi pulse, i.e. the ODMR/pODMR signal channel.

Pulse parameters:
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is already exactly 13 samples, so rounding leaves it at 52 ns.
- The relevant pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).

Quantitative expected signal model

Use a square-pulse two-level Rabi model for population transfer from m_S = 0 to m_S = +1:

P_transfer(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * sqrt(Omega^2 + delta^2) * tau)

with frequencies in Hz. The provided setup facts give Omega = 10 MHz at mod_depth = 1, and tau = 52 ns. On resonance,

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With a 22% m_S = 0 to m_S = +1 contrast scale, the expected on-resonance fractional PL drop is about

0.22 * 0.996 = 0.219.

For a typical readout-1 level near 47.2 counts, this is about 10.35 counts. A real finite-SNR data set can show a smaller apparent contrast because the sampled point may miss the exact resonance center, the pulse is not ideal, and tracking/readout drift changes the baseline.

Observed data and model fit

I used normalized contrast y = 1 - readout2/readout1. The strongest feature is centered in the post-pulse readout around 3.875-3.885 GHz:

- 3.875 GHz: y = 0.089, count drop = 3.96
- 3.880 GHz: y = 0.154, count drop = 7.38
- 3.885 GHz: y = 0.130, count drop = 6.27

The maximum observed normalized contrast is 15.4% at 3.880 GHz. This is below the ideal 21.9% estimate but is in the same direction and on the same scale for a near-pi pulse.

I fit y to baseline + amplitude * P_transfer(f - f0), with Omega fixed at 10 MHz and tau fixed at 52 ns. The best fit has:

- f0 = 3.879584 GHz
- baseline = 0.0173
- fitted pulse-dependent amplitude = 0.1228
- peak fitted contrast = 0.140
- RSS for physical pulse model = 0.03479
- RSS for constant baseline = 0.05972
- RSS for linear trend baseline = 0.05843

Thus the known-pulse resonance model reduces residual error by about 0.0249 relative to a constant baseline and about 0.0236 relative to a linear trend, while placing the resonance center at the same frequency as the observed readout-2 dip. The per-average traces both show excess normalized contrast near 3.875-3.885 GHz, but I do not treat those stored averages as strong independent repeatability evidence because they can reflect tracking cadence.

Decision

The active sequence makes readout 2 the microwave-pulse response channel, and a 52 ns pulse at mod_depth = 1 should produce an order-10-count dip on resonance. The data show a localized 6-7 count post-pulse dip near 3.88 GHz, with a normalized contrast up to 15.4%, and the fixed-physics Rabi line model fits the feature better than no-resonance baselines. I therefore classify this case as resonance_present.
