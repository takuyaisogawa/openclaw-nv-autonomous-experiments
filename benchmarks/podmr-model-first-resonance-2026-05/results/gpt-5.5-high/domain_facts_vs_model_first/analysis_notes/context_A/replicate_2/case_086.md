Active sequence and roles:

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV and immediately performs detection, which is the bright m_S = 0 reference readout. Because full_expt = 0, the conditional +1 reference block is skipped. The sequence then applies one modulated Rabi microwave pulse and performs the second detection, so the second readout is the post-pulse pODMR signal.

Pulse settings:

The provided sequence XML and saved variable values set mod_depth = 1. The Rabi pulse duration is 52 ns; at the 250 MHz sample rate this is exactly 13 samples, so rounding does not materially change it. With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse, so an on-resonance transition should produce a sizable post-pulse PL decrease, on the order of the 22% bright-to-dark contrast scale if efficiently driven.

Data assessment:

The combined readouts stay near 50 counts. The post-pulse/reference ratio ranges only from about 0.95 to 1.02, with the deepest deficits around 3.840 GHz and 3.925 GHz at roughly 4.7% to 4.8%. Similar few-percent excursions occur at several separated frequencies, and some neighboring points reverse sign. The per-average traces show tracking-scale baseline shifts and noisy point-to-point variation rather than a clean, isolated resonance feature. Stored averages here should not be treated as a strong repeatability test because they can reflect tracking cadence.

Decision:

Given the near-pi pulse at full modulation depth, a real pODMR resonance should be substantially stronger and more coherent than the observed few-percent scattered dips. I therefore classify this case as resonance absent.
