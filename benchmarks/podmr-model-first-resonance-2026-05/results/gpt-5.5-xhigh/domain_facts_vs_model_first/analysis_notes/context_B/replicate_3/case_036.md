Case: podmr_021_2026-05-16-171244

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- sample_rate = 250 MHz.
- length_rabi_pulse = 52 ns. The sequence rounds this to the sample grid; 52 ns is exactly 13 samples at 250 MHz.
- mod_depth = 1 from the provided sequence XML and exported variable values.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive even though it is present in the XML.
- Active instruction order is: polarize, detection, wait, Rabi pulse, detection, wait.
- Therefore readout 1 is the post-polarization true m_S = 0 bright reference, and readout 2 is the signal readout after the Rabi pulse. There is no active m_S = +1 reference readout.

Expected signal model:
I used the square-pulse two-level transition probability

P(Delta f) = f_R^2/(f_R^2 + Delta f^2) * sin^2(pi * t * sqrt(f_R^2 + Delta f^2)).

With the given setup scale, f_R = 10 MHz * mod_depth = 10 MHz. For t = 52 ns,
P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fluorescence dip in the post-pulse signal is
0.22 * 0.996 = 0.219, or about 21.9%.

Using the median readout 1 level of 46.44 counts, this predicts an on-resonance post-pulse signal near
46.44 * (1 - 0.219) = 36.27 counts, a drop of about 10.18 counts. Even if the resonance is halfway between two 5 MHz scan samples, the nearest sampled transition probability is 0.929, implying a sampled dip of about 20.4%.

Observed data comparison:
- Median readout 1 = 46.44 counts; median readout 2 = 46.63 counts.
- The readout2/readout1 ratio ranges from 0.953 to 1.040, with mean 0.999 and standard deviation 0.026.
- The largest downward residual of readout2/readout1 after a linear trend is about 0.036, much smaller than the expected about 0.20 to 0.22 resonance dip.
- The minimum absolute readout 2 value is 43.96 counts, still far above the about 36.3 counts expected for an on-resonance pulse at mod_depth = 1.
- A fixed-amplitude physical line-shape model with the expected contrast worsens the normalized-ratio fit relative to a line-only drift model (RSS 0.0335 versus 0.0131). A free-amplitude fit uses only about a 5.9% maximum decrement, far below the physical expectation for the active pulse.

Decision: resonance_absent. The measured variations are consistent with small drift/tracking-scale fluctuations rather than the large, broad square-pulse dip expected from a real pODMR resonance under these pulse parameters.
