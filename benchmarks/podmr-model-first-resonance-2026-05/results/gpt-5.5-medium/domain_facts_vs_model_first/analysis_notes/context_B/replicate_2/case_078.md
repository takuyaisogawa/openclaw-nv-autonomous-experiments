Case podmr_064_2026-05-17-065956

Input used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The sequence is Rabimodulated.xml / 1DExp-seq-Rabimodulated-vary-mw_freq.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- readout 1 is the detection immediately after adj_polarize, i.e. the true m_S = 0 reference.
- readout 2 is the detection after the modulated Rabi pulse.
- No active m_S = +1 reference readout is acquired in this run.

Pulse parameters from the provided XML:
- length_rabi_pulse = 52 ns, rounded at sample_rate = 250 MHz; 52 ns is exactly 13 samples.
- mod_depth = 1.
- The setup Rabi frequency is about 10 MHz at mod_depth = 1, so f_R = 10 MHz for this pulse.

Quantitative model:
For a rectangular resonant microwave pulse, the transition probability is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

On resonance, t = 52 ns and f_R = 10 MHz, so the pulse area is f_R * t = 0.52 cycles and

P(0) = sin^2(pi * 0.52) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance point should reduce the post-pulse readout by

0.22 * 0.996 = 0.219

or about 21.9% relative to the m_S = 0 reference. At the observed count scale near 50, this is an expected drop of about 11 raw-count units in readout 2 relative to readout 1. The 52 ns pulse also has a linewidth on the order of tens of MHz, so such a feature should be visible across multiple 5 MHz scan points if the resonance lies in the scanned range.

Data comparison:
- Mean readout 1 = 50.973.
- Mean readout 2 = 50.921.
- Mean readout2/readout1 = 0.9993.
- Standard deviation of readout2/readout1 = 0.0268.
- Minimum readout2/readout1 = 0.9462, a 5.4% drop, much smaller than the expected 21.9% resonant drop.
- Largest raw difference readout2 - readout1 on the dip side is -2.85 counts, much smaller than the expected approximately -11 counts.

I also fit the explicit rectangular-pulse lineshape to the normalized ratio over possible resonance centers in the scan range. The best positive dip amplitude was about 0.031, while the physically expected amplitude is about 0.22. Forcing a 0.22 dip gives a poor match and predicts ratios near 0.82 at resonance, which are not present in the data.

Decision:
The active pulse should produce a large, broad post-pulse PL dip if a pODMR resonance were in the scanned range. The measured post-pulse/reference ratio remains near unity with only small tracking-scale fluctuations, so this case is classified as resonance_absent.
