Case podmr_016_2026-05-12-120649

I used only the provided XML/exported data in this isolated workspace.

Active sequence and readout roles:

- SequenceName is Rabimodulated.xml.
- The instruction block first polarizes and performs detection, giving the true m_S = 0 reference readout.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped. There is no independent m_S = +1 reference readout in the acquired data.
- The active pODMR signal is the detection after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-microwave-pulse signal.

Pulse settings used for the physical expectation:

- mod_depth = 1.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, this is already exactly 13 samples, so rounding leaves it at 52 ns.
- The setup Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth, so f_R = 10 MHz here.

Explicit model calculation:

For a resonant square Rabi pulse, the population transferred to m_S = +1 is

P = sin^2(pi f_R t).

With f_R = 10 MHz and t = 52 ns:

pi f_R t = pi * 10e6 * 52e-9 = 1.6336 rad
P = sin^2(1.6336) = 0.996.

The stated optical contrast scale between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pODMR signal should be lower than the m_S = 0 reference by approximately

0.22 * 0.996 = 0.219, or 21.9%.

At the observed count level near 26 counts, that is an expected resonant drop of about 5.7 counts in the signal readout relative to the m_S = 0 reference/baseline. The square pulse duration also implies a broad frequency response on the order of 1/t = 19 MHz, so a real resonance should affect multiple adjacent 5 MHz scan points, not appear as a single-point fluctuation.

Observed data comparison:

The combined readout 1 values are approximately 23.56 to 27.13 counts, and readout 2 values are approximately 23.94 to 28.04 counts. The readout2/readout1 ratios across the scan are:

1.0117, 1.0652, 1.0340, 1.0333, 1.0143, 1.0000, 1.0924, 1.0613, 1.0205, 1.0110, 0.9918, 1.0286, 1.0326, 1.0295, 0.9468, 0.9881, 1.0963, 0.9781, 0.9467, 0.9719, 1.0048.

These ratios are mostly at or above 1, rather than showing the expected approximately 0.78 ratio at resonance. The largest apparent negative excursions are only about 5.3%, far smaller than the expected 21.9% contrast, and they are isolated or embedded in a monotonic/tracking-like drift. Stored averages are not a strong independent repeatability test here, and their overlays show large cadence/drift changes rather than a stable frequency-localized dip.

Decision:

Given the active sequence and expected signal size, a real resonance under these pulse settings should produce a clear, broad, several-count reduction in readout 2 relative to the m_S = 0 reference. The observed data do not show that feature. I therefore decide that a pODMR resonance is absent.
