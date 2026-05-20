Case podmr_042_2026-05-16-225623

Input files used: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles:

- The provided XML is Rabimodulated.xml.
- The instruction block first polarizes the NV and calls detection before any Rabi pulse. This is the true m_S = 0 reference readout, corresponding to readout 1 in ExperimentData.
- full_expt is 0, so the optional explicit m_S = 1 reference block is skipped.
- The active experiment operation is then rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is the post-pulse experiment readout, corresponding to readout 2.
- The provided sequence variables give mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this pulse is exactly 13 samples, so the rounded pulse duration remains 52 ns.

Quantitative model:

Using the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant square pulse of duration t, the transition probability is P = sin^2(pi f_R t). With f_R = 10 MHz and t = 52 ns,

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a true on-resonance response should reduce the post-pulse experiment readout relative to the m_S = 0 reference by about 0.22 * 0.996 = 0.219, or 21.9% of the reference signal. The mean readout 1 level is 46.72 counts, so the expected on-resonance dip is approximately 10.24 counts.

Observed raw comparison:

- Mean readout 1 = 46.72 counts.
- Mean readout 2 = 46.86 counts.
- Mean readout 2 - readout 1 = +0.14 counts.
- Standard deviation of readout 2 - readout 1 across scan points = 1.43 counts.
- Most negative readout 2 - readout 1 value is -2.54 counts at 3.840 GHz.
- At 3.875 GHz, where a candidate dip appears in readout 2, readout 2 - readout 1 is only -1.83 counts, far smaller than the approximately -10.24 count modeled resonant dip. Readout 1 is also low there, so this point is not a clean experiment-minus-reference resonance signature.

Decision:

The physical model predicts a large near-pi-pulse contrast feature if the swept microwave frequency crosses an addressed transition. The measured post-pulse readout does not show a dip of the required size relative to the preceding m_S = 0 reference; the observed differences are at the noise/tracking-drift scale. I therefore decide that a pODMR resonance is absent in this case.
