Analysis note for podmr_013_2026-05-16-123121

I used the provided sequence XML and the raw readout arrays only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml / Rabimodulated pulse sequence.
- The active XML sets full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is therefore the optical readout immediately after polarization, i.e. the m_S = 0 reference.
- Readout 2 is the optical readout after the microwave Rabi pulse, i.e. the pODMR signal readout.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse is still 52 ns, exactly 13 samples.

Quantitative model:

For a square microwave pulse driving the m_S = 0 to m_S = +1 transition, using Rabi frequency f_R in cycles/s and detuning delta in Hz,

P_transfer(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

The stated setup gives f_R about 10 MHz at mod_depth = 1. For t = 52 ns,

P_transfer(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant readout-2 drop relative to the readout-1 reference is

0.22 * 0.9961 = 0.2191, or 21.9%.

Observed normalized contrast, computed as 1 - readout2/readout1:
- At 3.875 GHz: readout1 = 44.4038, readout2 = 34.6731, drop = 9.7308 counts, normalized drop = 0.21914.
- At 3.880 GHz: readout1 = 43.0577, readout2 = 34.0769, normalized drop = 0.20858.
- The largest observed normalized drop is 0.21914 at 3.875 GHz.

I also fit the square-pulse model over resonance center using the physical contrast amplitude fixed at 0.22. The best center was about 3.87788 GHz, with a small contrast offset of 0.0124. The fixed-amplitude Rabi model SSE was 0.01935 versus 0.09783 for a constant-contrast null model, about a 5.1x improvement. Model-predicted dip fractions near the fitted center are about 0.200 at 3.875 GHz and 0.208 at 3.880 GHz, matching the observed central dip scale.

The stored per-average traces have different absolute baselines, consistent with tracking cadence effects, so I do not treat them as a strong independent repeatability test. The decision is instead based on the active sequence readout role and the quantitative agreement between the expected pi-pulse pODMR contrast and the observed readout-2 dip.

Decision: resonance_present.
