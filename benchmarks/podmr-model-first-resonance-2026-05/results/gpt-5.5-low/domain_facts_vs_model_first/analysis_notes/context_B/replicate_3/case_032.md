Sequence and readout interpretation

The active sequence is Rabimodulated.xml from the saved scan. The sequence first applies adj_polarize and detection, which is the true m_S = 0 reference readout. Because full_expt = 0, the optional m_S = 1 reference block is skipped. The active measurement readout is then produced after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. Thus readout 1 is the reference readout and readout 2 is the microwave-pulsed signal readout.

Relevant sequence values

- varied parameter: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- mod_depth: 1
- length_rabi_pulse: 52 ns
- sample rate: 250 MHz, so 52 ns is already on the sample grid
- full_expt: 0, so no independent 1-level reference readout is acquired

Quantitative physical model

For a rectangular resonant Rabi pulse, the population transferred to m_S = +1 is approximately

P_flip = sin^2(pi * f_R * tau)

with f_R = 10 MHz * mod_depth. Here f_R = 10 MHz and tau = 52 ns, so

P_flip = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected fractional fluorescence dip on resonance is

0.22 * 0.996 = 0.219, or about 21.9%.

Using the reference readout median baseline of about 44.54 raw counts, the expected resonant dip magnitude is

44.54 * 0.219 = 9.76 raw counts.

Data comparison

Readout 2 has a clear minimum at 3.875 GHz with value 34.17. The off-feature median for readout 2, excluding nearby points, is about 43.57, giving an observed dip of 9.39 counts, or 21.6%. This agrees closely with the 21.9% dip predicted by the Rabi model for a near-pi pulse at mod_depth = 1.

Readout 1 does not show a corresponding dip at the same frequency: it is 45.40 at 3.875 GHz, close to its median baseline of 44.54. The two stored averages both show the readout 2 depression at the same point (32.73 and 35.62), while the readout 1 values remain near baseline (45.42 and 45.38). The stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence, but they are consistent with the combined result.

Decision

The expected on-resonance pODMR signal from the active pulse sequence is a roughly 22% dip in the pulsed readout relative to the reference/baseline. The observed feature has the right readout role, size, and frequency-localized shape. A pODMR resonance is present.
