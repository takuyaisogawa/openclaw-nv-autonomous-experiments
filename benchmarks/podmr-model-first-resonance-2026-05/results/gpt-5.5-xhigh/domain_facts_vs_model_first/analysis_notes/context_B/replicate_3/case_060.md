Case: podmr_046_2026-05-16-235726

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- SequenceName is Rabimodulated.xml.
- The varied parameter is mw_freq, scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active sequence has full_expt = 0, so the conditional "Acquire 1 level reference" block is skipped.
- The executed readouts are:
  1. After adj_polarize and before any microwave pulse: true m_S = 0 reference.
  2. After rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on): pODMR signal readout after the microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1, a resonant square pulse of duration tau = 52 ns gives
  P_transfer(0) = sin^2(pi f_R tau) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fluorescence decrease is
  0.22 * 0.996 = 0.219, i.e. about 22%.
- Including detuning with the standard driven two-level square-pulse expression,
  P_transfer(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi tau sqrt(f_R^2 + delta^2)).
  Expected PL drops are about 20.4% at 2.5 MHz detuning, 16.5% at 5 MHz, 6.0% at 10 MHz, and near 1-2% beyond about 20-30 MHz. Therefore a resonance anywhere on or between the 5 MHz scan points should create a large one- or two-point dip in the post-pulse readout relative to the 0-reference.

Data calculation:
- I normalized the pODMR readout by the reference readout at each scan point: readout2/readout1.
- The normalized ratios have mean 0.9808 and point-to-point standard deviation 0.0293.
- The minimum normalized ratio is 0.9140 at 3.860 GHz, a decrease of only about 6.8 percentage points relative to the mean normalized baseline, far smaller than the expected about 22% resonant decrease.
- Other low points are similarly small: 0.9429 at 3.875 GHz, 0.9433 at 3.885 GHz, 0.9505 at 3.900 GHz, 0.9433 at 3.915 GHz, and 0.9534 at 3.925 GHz. These are scattered rather than forming the expected Rabi spectral response.
- A constrained model using the expected 22% contrast and the square-pulse Rabi detuning response was fit over candidate center frequencies with only a baseline scale free. Its best residual sum of squares was 0.01988, worse than a constant normalized baseline residual sum of squares of 0.01799.
- Allowing the dip amplitude to float gives a best effective contrast of only about 0.036, not the expected 0.22.

Decision:
The active pODMR readout does not show the quantitatively expected near-pi-pulse resonance signature. The observed dips are much smaller than the expected signal and do not improve a physically constrained resonance fit, so I decide resonance_absent.
