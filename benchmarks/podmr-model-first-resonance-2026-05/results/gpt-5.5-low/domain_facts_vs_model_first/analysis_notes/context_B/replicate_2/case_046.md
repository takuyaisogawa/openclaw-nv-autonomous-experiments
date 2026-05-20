Analysis note for podmr_032_2026-05-16-201700

Inputs used only from this isolated case:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png as a visual check of the same exported arrays

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, with vary_prop = mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect, then wait, then apply one Rabi pulse, then detect again.
- full_expt = 0, so the optional mS = +1 reference block is not executed.
- Therefore readout 1 is the optically polarized mS = 0 reference/readout before the swept pulse, and readout 2 is the post-Rabi-pulse pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already an integer number of samples after rounding.

Quantitative physical model:
- Setup contrast between mS = 0 and mS = +1 is given as about 22%.
- Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so f_Rabi = 10 MHz here.
- For a square pulse, the on-resonance transition probability is
  P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns and f_Rabi = 10 MHz:
  pi * f_Rabi * tau = pi * 0.52, so P = sin^2(1.6336) = 0.996.
- Expected resonant PL contrast is therefore 0.22 * 0.996 = 0.219, i.e. about a 21.9% reduction of the post-pulse readout relative to the mS = 0 reference at resonance.
- At the observed raw count scale near 55 counts, that corresponds to an expected resonant change of about 12.1 counts.
- The same square-pulse model versus detuning uses
  P(delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),
  with Omega = 2*pi*10 MHz and Delta = 2*pi*(mw_freq - f0). This predicts a frequency-localized feature with a width set by the 52 ns pulse, so a true resonance in the scanned window should be visible at multi-count to roughly 12-count scale.

Observed data summary:
- Combined readout 1 mean = 55.255, sample sd = 1.120, range = 53.365 to 57.442.
- Combined readout 2 mean = 55.262, sample sd = 1.240, range = 52.788 to 58.058.
- readout2 - readout1 mean = 0.006, sample sd = 1.510, range = -2.346 to 3.942.
- readout2/readout1 mean = 1.0004, sample sd = 0.0275, range = 0.958 to 1.073.

Model comparison check:
- A linear baseline fit to readout 2 has SSE = 27.33.
- A square-pulse resonance response fit, allowing the center frequency and amplitude to vary, gives best SSE = 11.34 and BIC improvement, but the best amplitude is only about -4.17 counts and is placed near the scan edge around 3.92 GHz.
- This fitted amplitude is far smaller than the approximately -12 count physical expectation for a near-pi pulse with 22% contrast. Its edge placement and the lack of a corresponding readout2/readout1 depression indicate it is fitting low-frequency drift/shape rather than a robust pODMR resonance.
- Stored averages differ by several counts in offset, consistent with tracking cadence/drift, and are not a strong independent repeatability test.

Decision:
The expected physical pODMR signal for this pulse should be a clear approximately 22% post-pulse readout decrease at resonance. The measured post-pulse readout remains essentially equal to the mS = 0 reference across the scan, with only small drift-scale variations. I therefore decide that a pODMR resonance is absent.
