Analysis note for podmr_040_2026-05-16-222642

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The provided XML is Rabimodulated.xml. The instructions first polarize the NV and run detection before any microwave pulse; since full_expt = 0, the optional "Acquire 1 level reference" block is skipped. Then the sequence applies one rabi_pulse_mod_wait_time pulse and detects again. Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-Rabi-pulse signal. The active microwave pulse is length_rabi_pulse = 5.2e-08 s, rounded at sample_rate = 250 MHz to exactly 13 samples = 52 ns. The active mod_depth from the provided XML and exported variable values is 1.

Quantitative physical expectation

Given the stated setup calibration, the Rabi frequency is about 10 MHz at mod_depth = 1. I used a two-level Rabi model for the population transferred by the pulse:

P1(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau)

with Omega = 2*pi*10 MHz and tau = 52 ns. On resonance this gives

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With a measured m_S = 0 to m_S = +1 contrast scale of about 22%, the expected fluorescence ratio for an on-resonance point is

readout2/readout1 ~= 1 - 0.22 * 0.996 = 0.781.

The mean readout 1 level is 47.19 counts, so the expected on-resonance drop is about 10.34 counts, giving an expected post-pulse readout near 36.85 counts if the scanned frequency hits the transition.

Observed data comparison

The combined data have mean readout 1 = 47.19 and mean readout 2 = 46.66, so the mean post-pulse difference is only -0.53 counts. The largest pointwise decrease of readout 2 relative to readout 1 is -3.69 counts at 3.885 GHz, corresponding to a ratio of 0.924, far shallower than the expected 0.781 resonant ratio.

I also fit the normalized ratio readout2/readout1 to the same Rabi lineshape over candidate resonance centers across the scan, allowing only a dip amplitude. The best fitted dip amplitude was about 0.039 in fractional contrast, whereas the expected resonant fractional dip from the calibrated model is about 0.219. The constant-ratio residual sum of squares was 0.01598 and the best dip-model residual was 0.01344, only a small improvement. Stored averages show large tracking-scale shifts: RMS half-difference between the two stored averages is about 3.38 counts for readout 1 and 3.10 counts for readout 2, so the shallow apparent dip is not a strong independent repeatability result.

Decision

Because the active 52 ns, mod_depth 1 pulse should produce an approximately 22% resonant drop, and the observed readout2/readout1 data show no dip close to that scale or a robust fitted resonance, I decide that a pODMR resonance is absent in this scan.
