Case: podmr_024_2026-05-16-175646

Sequence and readout roles

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active branch has full_expt = 0, so the "Acquire 1 level reference" block is skipped. The pulse sequence therefore records:

1. Readout 1: after optical polarization, before the scanned microwave pulse. This is the bright m_S = 0 reference/readout.
2. Readout 2: after a rabi_pulse_mod_wait_time pulse using length_rabi_pulse and mod_depth, then detection. This is the pODMR signal readout.

The relevant active microwave pulse has length_rabi_pulse = 52 ns and mod_depth = 1 in the provided sequence XML. At sample_rate = 250 MHz, the rounded pulse duration remains 52 ns.

Quantitative expected-signal model

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Thus the expected on-resonance driven population transfer for a square pulse is

P_transfer = sin^2(pi * f_Rabi * t)
           = sin^2(pi * 10e6 * 52e-9)
           = 0.996.

Using the stated optical contrast scale of 22% between m_S = 0 and m_S = +1, the expected resonant fluorescence change is

expected fractional dip = 0.22 * 0.996 = 0.219, about 21.9%.

The mean readout-1 level in the combined data is 53.86 raw units, so a resonant point should show readout 2 lower than readout 1 by about

53.86 * 0.219 = 11.80 raw units.

Observed data check

The observed combined readout difference d = readout2 - readout1 has:

mean d = +0.32 raw units
standard deviation d = 1.13 raw units
minimum d = -1.65 raw units
maximum d = +2.62 raw units

The most negative observed point is only a 3.1% decrease relative to readout 1, far smaller than the expected approximately 21.9% resonant dip. Many scan points have readout 2 above readout 1. The stored averages show cadence-level offsets and are not a strong independent repeatability test, so I do not treat the per-average separation as resonance evidence.

Decision

With the active sequence, a real resonance should produce a large negative readout2-readout1 feature near the transition frequency. The measured data do not contain a dip of the expected sign or magnitude. I therefore decide that a pODMR resonance is absent.
