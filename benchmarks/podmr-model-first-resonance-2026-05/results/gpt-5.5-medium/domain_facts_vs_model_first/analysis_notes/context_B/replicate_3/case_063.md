<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_063

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- SequenceName is Rabimodulated.xml.
- The active microwave drive is `rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)` followed by detection.
- `full_expt = 0`, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 is the true mS = 0 reference acquired immediately after optical polarization.
- Readout 2 is the driven measurement after the Rabi-modulated microwave pulse.
- Active parameters from the provided sequence/export values: `length_rabi_pulse = 52 ns`, `mod_depth = 1`, `sample_rate = 250 MHz`, and scan is `mw_freq` from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Quantitative physical model:

Given the supplied setup facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant rectangular pulse with duration T = 52 ns,

theta = 2*pi*f_Rabi*T = 2*pi*(10 MHz)*(52 ns) = 3.267 rad.

The resonant transfer probability is:

P_flip = sin^2(theta/2) = sin^2(1.6336) = 0.996.

The supplied contrast scale between mS = 0 and mS = +1 is about 22%, so a true resonance should make the driven readout lower than the mS = 0 reference by roughly:

0.22 * 0.996 = 0.219, or 21.9% of the reference level.

The mean reference readout is 49.856 counts, so the expected resonant dip in readout 2 relative to readout 1 is approximately:

49.856 * 0.219 = 10.93 counts.

Observed data check:

- Mean readout 1: 49.856 counts.
- Mean readout 2: 49.775 counts.
- Mean driven-reference difference: -0.082 counts.
- Median driven-reference difference: +0.173 counts.
- Most negative driven-reference difference: -2.615 counts at 3.850 GHz.
- Most negative residual relative to the median offset: -2.788 counts.
- Minimum readout-2/readout-1 ratio: 0.9487, only a 5.1% decrease.

The observed largest dip is about 2.8 counts after offset removal, far below the approximately 10.9-count dip expected for a resonant near-pi pulse under the stated contrast and Rabi-frequency model. The data also lack a clear isolated pODMR-shaped resonance feature; the deviations are comparable to point-to-point fluctuations and average-to-average baseline shifts. Stored averages are not treated as a strong independent repeatability test, per the prompt.

Decision: resonance_absent.
