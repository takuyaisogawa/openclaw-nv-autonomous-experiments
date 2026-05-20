Case: podmr_032_2026-05-16-201700

Sequence interpretation:
- Active sequence: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "1 level reference" block is skipped.
- Readout 1 is the initial polarized m_S = 0 reference detection after adj_polarize.
- Readout 2 is the detection after the single Rabi-modulated microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At 250 MS/s this is 13 samples, so rounding leaves it at 52 ns.
- do_adiabatic_inversion is true in the variable list, but the only active microwave operation in this sequence is the Rabi pulse; the adiabatic inversion code is inside the skipped full_expt block and commented alternatives.

Physical model calculation:
For this setup the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a rectangular pulse, the driven transition probability versus detuning is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * t)

with f_R = 10 MHz and t = 52 ns. On resonance:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected fractional darkening in the post-pulse readout on resonance is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean m_S = 0 reference readout is about 55.26 counts, so the expected on-resonance post-pulse readout would be

55.26 * (1 - 0.219) = 43.15 counts,

a drop of about 12.1 counts. The expected fractional darkening remains large near resonance: about 16.5% at +/-5 MHz detuning, 6.0% at +/-10 MHz, and 1.05% at +/-20 MHz.

Data comparison:
I used the normalized contrast c = (readout1 - readout2) / readout1, where a positive value is the expected pODMR darkening. Across the 21 scan points:

- mean c = -0.00043
- standard deviation c = 0.0275
- maximum positive c = 0.0418
- minimum c = -0.0729

The largest observed positive contrast is only about 4.2%, far below the expected 21.9% on-resonance contrast for this pulse. At 3.875 GHz, the contrast is negative, c = -0.0729, meaning readout 2 is brighter than the reference rather than darker. A grid comparison to the rectangular-pulse line shape also does not support a real pODMR feature: the fixed 22% physical-amplitude model has higher squared residual than a no-resonance baseline, and the best nonnegative fitted amplitude is only about 3.6% with an offset.

Decision:
The active pulse should produce an easily visible dark resonance if the scanned frequency crosses the transition. The measured post-pulse readout does not show the expected magnitude, sign, or line-shape behavior. I therefore decide that a pODMR resonance is absent.
