Case: podmr_044_2026-05-16-232730

Inputs used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, sibling cases, previous outputs, or external context.

Active pulse sequence and readout roles

The sequence is Rabimodulated.xml / Rabimodulated. The instructions first set the microwave source, then acquire a true m_S = 0 reference:

- adj_polarize(...)
- detection(...)
- wait_for_awg(...)

The optional m_S = +1 reference block is guarded by if abs(full_expt)>1e-12. Here full_expt = 0, so that block is inactive. Therefore only two readout roles are active in the stored ExperimentData: readout 1 is the pre-pulse m_S = 0 reference, and readout 2 is the post-microwave-pulse pODMR signal readout.

The active microwave pulse before readout 2 is:

- rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

The exported variable values give length_rabi_pulse = 5.2e-08 s = 52 ns and mod_depth = 1. The provided sequence XML file also has mod_depth = 1 and length_rabi_pulse = 52 ns. The exported embedded Sequence text contains a stale-looking mod_depth = 0.3 in its text block, but the explicit Variable_values and the provided XML both identify the active mod_depth as 1.

Quantitative expected signal model

Given the supplied domain facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1 and scales linearly with mod_depth. Thus:

- f_R = 10 MHz
- t_pulse = 52 ns
- transfer probability for an on-resonance square pulse = sin^2(pi f_R t)
- transfer probability = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional fluorescence reduction in the post-pulse readout is:

- expected contrast = 0.22 * 0.996 = 0.219, or about 21.9%

The mean readout 1 level is 48.56 counts, so the expected resonant drop is:

- expected drop = 48.56 * 0.219 = 10.64 counts

Measured data comparison

Using readout 2 minus readout 1 across the 21 scanned microwave frequencies:

- mean(readout 1) = 48.56
- mean(readout 2) = 48.69
- mean(readout 2 - readout 1) = +0.13 counts
- standard deviation of differences = 1.09 counts
- minimum difference = -2.42 counts
- maximum difference = +2.06 counts

The largest observed darkening of readout 2 relative to readout 1 is -2.42 counts at 3.865 GHz, only about 5.0% of the reference level and far smaller than the approximately -10.6 count, 21.9% drop expected from a resonant near-pi pulse. It is also a single-point-scale fluctuation comparable to the scatter of the difference trace, not a robust pODMR resonance feature. The scan endpoint near the nominal mw_freq = 3.925 GHz is brighter in readout 2 than readout 1, not darker.

Decision

The active pulse should produce a very large pODMR dip if it is on resonance. The observed readouts show no localized fluorescence reduction with the expected sign and magnitude. I decide resonance_absent.
