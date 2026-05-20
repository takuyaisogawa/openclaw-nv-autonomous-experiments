# pODMR analysis note

Case: podmr_016_2026-05-12-120649

I used only the provided XML, raw export, and raw readout plot for this decision.

Sequence and readout roles:

- Active sequence: `Rabimodulated.xml`, with `mw_freq` scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active parameters from `sequence.xml` and `raw_export.json`: `mod_depth = 1`, `length_rabi_pulse = 52 ns`, `sample_rate = 250 MHz`, `full_expt = 0`.
- Since `full_expt = 0`, the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is the polarized `m_S = 0` reference: `adj_polarize(...)`, then `detection(...)`, with no microwave pulse before it.
- Readout 2 is the pODMR signal readout after `rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)`, then `detection(...)`.

Physical model calculation:

For a two-level driven transition, using frequency units, the microwave transfer probability versus detuning is

`P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2))`.

The given setup facts imply `f_R = 10 MHz * mod_depth = 10 MHz`. With `t = 52 ns`,

`P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996`.

The expected fluorescence contrast at exact resonance is therefore about

`0.22 * 0.996 = 0.219`, or a 21.9 percent dip of readout 2 relative to the `m_S = 0` reference. At the observed readout level of about 26 counts, this is an expected dip of about 5.7 counts. The same model gives expected fractional dips of about 16.5 percent at +/-5 MHz and 6.0 percent at +/-10 MHz, so a real resonance sampled on the 5 MHz grid should make a broad, multi-point reduction in readout 2 relative to readout 1.

Observed normalized channel:

I evaluated the signal as `(readout1 - readout2) / readout1`, because readout 1 is the local `m_S = 0` reference. The largest positive combined contrasts are:

- 3.915 GHz: 0.053
- 3.895 GHz: 0.053
- 3.920 GHz: 0.028
- 3.910 GHz: 0.022
- 3.900 GHz: 0.012

Most other points are negative, meaning readout 2 is brighter than readout 1 rather than darker. The observed maximum dip is about 1.37 counts, far below the approximately 5.7 counts expected for the active 52 ns, mod_depth 1 near-pi pulse.

I also fit the normalized contrast to a smooth baseline plus the Rabi line-shape model above while scanning the possible resonance center. With a nonnegative resonance amplitude and a linear baseline, the best combined fit had an amplitude of about 0.065 at about 3.918 GHz, only about 30 percent of the expected 0.219. Allowing a quadratic baseline raised the fitted amplitude to about 0.091, still less than half the expected pi-pulse signal. The unconstrained linear-baseline fit preferred a negative-amplitude feature near 3.858 GHz, which is the wrong sign for the pODMR signal.

The two stored averages show strong tracking-related drift and are not an independent repeatability test. They also do not give a clean repeatable pODMR feature: one average prefers an opposite-sign feature, and the other has a smaller positive feature near the high-frequency end.

Decision:

The active pulse sequence should produce a large, broad, approximately 22 percent resonant dip in readout 2 relative to readout 1. The measured normalized data show only small, irregular few-percent features that do not match the expected amplitude or line shape. I therefore classify this case as resonance absent.
