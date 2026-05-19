<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_049

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence/readout roles

The sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instructions first polarize the NV, then take a detection readout before any microwave pulse. This is the m_S = 0 bright reference/readout 1. The full_expt variable is 0, so the optional second reference branch that would acquire an m_S = 1 reference is inactive. The sequence then applies one rabi_pulse_mod_wait_time pulse and takes a second detection readout; this readout 2 is the pODMR signal channel after the microwave pulse.

Relevant pulse parameters

The sequence variables used by the export are length_rabi_pulse = 52 ns and mod_depth = 1. The setup fact gives a Rabi frequency of about 10 MHz at mod_depth = 1. Therefore the pulse is approximately a pi pulse on resonance: f_R * t = 10 MHz * 52 ns = 0.52 cycles.

Quantitative model calculation

For a square pulse, the excited-state transfer probability versus detuning is

P(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t),

using f_R and Delta in cycles/s. At Delta = 0, P = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fractional drop of the post-pulse readout relative to the pre-pulse reference is about 0.22 * 0.996 = 0.219, i.e. readout 2 should be roughly 39.0 when readout 1 is 50.0.

The same model predicts sizable contrast over the 5 MHz sampling scale: at 2.5 MHz detuning the drop is about 20.4%, at 5 MHz about 16.5%, and at 10 MHz about 6.0%. Thus a true resonance in the scan should produce at least one or a few points with a clear, large readout-2 depression relative to readout 1.

Measured comparison

The combined readout 1 values have mean 50.94 and range 48.92 to 52.77. The combined readout 2 values have mean 50.08 and range 46.85 to 52.02. The fractional contrast (readout1 - readout2) / readout1 has mean 1.66%, maximum 5.65%, and minimum -2.16%. The largest observed combined drop occurs near 3.830 GHz and is only about one quarter of the expected on-resonance 22% drop, and it is not supported as a strong reproducible feature by the stored per-average traces. The data instead show a slow baseline drift and point-to-point scatter at the few-percent level.

Decision

Given the active pulse is effectively resonant-pi strength when on resonance, the expected physical pODMR signal is a large dip in readout 2 relative to readout 1. No such dip appears in the measured scan. I therefore decide that a pODMR resonance is absent in this case.
