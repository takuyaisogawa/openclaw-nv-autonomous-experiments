Case: podmr_007_2026-05-16-013306

Sequence and readout roles:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the "true 0 level reference": optical polarization followed by detection before the microwave pulse.
- Readout 2 is the signal readout after the modulated Rabi microwave pulse.
- mod_depth = 1 from the provided XML/active variable values.
- length_rabi_pulse = 52 ns. At 250 MS/s this is already exactly 13 samples, so rounding does not change it.

Expected physical signal:
The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant rectangular pulse, the transfer probability is

P = sin^2(pi * f_Rabi * t)

Using f_Rabi = 10 MHz and t = 52 ns:

f_Rabi * t = 0.52 cycles
P = sin^2(pi * 0.52) = 0.996

With a 22% m_S=0 to m_S=+1 contrast scale, the expected resonant fluorescence factor is

1 - 0.22 * 0.996 = 0.781

Thus a real resonance should produce about a 21.9% dip in readout 2 relative to its off-resonant level. The off-resonant readout 2 mean, excluding the central 3.865-3.885 GHz region, is about 35.26 counts, so the expected resonant minimum is about 27.53 counts.

Observed quantitative comparison:
- Readout 1 remains approximately flat near 36 counts through the central feature, consistent with a reference channel rather than the driven signal.
- Readout 2 drops from an off-resonant level near 35-36 counts to 28.96 counts at 3.875 GHz and 28.21 counts at 3.880 GHz.
- Relative to readout 1, the observed contrast is 18.4% at 3.875 GHz and 23.6% at 3.880 GHz, matching the expected approximately 22% pi-pulse contrast.
- Both stored averages show their post-pulse readout minimum at 3.880 GHz, but the averages mainly reflect tracking cadence and are not treated as a strong independent repeatability test.

Explicit line-shape calculation:
I modeled the driven transition with the rectangular-pulse Rabi formula

P(f) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * t)

where Omega = 2*pi*10 MHz, Delta = 2*pi*(f - f0), and t = 52 ns. A linear-baseline fit of readout 2 minus a scaled P(f) term gives best center f0 = 3.8776 GHz, dip amplitude = 7.54 counts, and baseline = 35.62 counts. The fitted dip fraction is 7.54 / 35.62 = 21.2%, close to the expected 21.9%. The fit SSE improves from 125.8 for a linear baseline alone to 32.2 with the Rabi line shape.

Decision:
The central readout-2 dip has the amplitude, width, and channel role expected for a 52 ns near-pi pODMR pulse at mod_depth = 1. A pODMR resonance is present.
