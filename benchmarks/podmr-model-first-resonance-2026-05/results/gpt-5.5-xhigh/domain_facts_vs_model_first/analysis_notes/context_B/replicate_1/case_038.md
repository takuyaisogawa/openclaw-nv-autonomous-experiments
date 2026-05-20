Case: podmr_023_2026-05-16-174219

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence interpretation:
- Active sequence: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_s = +1 reference block is skipped.
- Readout 1 is the first detection immediately after optical polarization, so it is the m_s = 0 fluorescence reference.
- Readout 2 is the detection after the active microwave pulse, so it is the pODMR signal readout.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. The 250 MHz sample rate gives a 4 ns sample period, and 52 ns is exactly 13 samples.

Expected signal model:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, use the two-level rectangular-pulse model.
- On resonance, transferred population P = sin^2(pi f_R t).
- For t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.9961.
- With the stated m_s = 0 to m_s = +1 contrast scale of 22%, the expected on-resonance fluorescence change is 0.22 * 0.9961 = 0.2191, i.e. about a 21.9% drop in readout 2 relative to readout 1.
- With the observed mean readout 1 of 47.55, this would correspond to an expected resonant readout 2 near 37.13, a raw drop of about 10.42 counts.
- The scan step is 5 MHz. Even if the resonance sits halfway between sampled frequencies, the detuned Rabi formula gives a sampled transfer of about 0.929, still implying about a 20.4% normalized dip at at least one sampled point.

Observed quantitative comparison:
- Mean readout 1 = 47.5513 and mean readout 2 = 47.6896, so the average ratio is 1.0029, not a depressed signal readout.
- The pointwise normalized contrast (readout1 - readout2) / readout1 has mean -0.0034 and standard deviation 0.0309.
- The largest observed positive normalized contrast is 0.0506 at 3.835 GHz, far below the expected approximately 0.219 resonant contrast.
- The minimum observed readout2/readout1 ratio is 0.9494, whereas the expected resonant ratio is about 0.7809.
- Fitting the rectangular-pulse response shape with a free amplitude gives a best amplitude of about 0.0536, while the expected physical amplitude is about 0.22. Holding the amplitude at 0.22 gives a worse fit than a no-resonance baseline.

Decision:
The active pulse should produce a large, near-pi-pulse pODMR dip if a resonance is present in the scanned range, and such a dip is absent from the normalized signal readout. The small fluctuations are consistent with tracking/noise-scale variation rather than the expected physical response.

Prediction: resonance_absent
