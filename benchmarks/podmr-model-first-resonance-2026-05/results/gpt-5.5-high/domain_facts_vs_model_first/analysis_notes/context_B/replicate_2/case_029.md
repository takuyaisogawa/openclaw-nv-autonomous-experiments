Sequence and readout interpretation

The provided XML is Rabimodulated.xml. It sets up optical polarization, then performs a detection before any microwave pulse. That first detection is the true m_S = 0 reference, so readout 1 is the bright reference. The block that would acquire an m_S = +1 reference is guarded by full_expt, and full_expt is 0, so it is inactive. The active pODMR signal readout is the detection after:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

The relevant active pulse settings are length_rabi_pulse = 52 ns and mod_depth = 1.

Quantitative model

For this setup, the Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. Thus f_R = 10 MHz for this measurement. For a rectangular resonant pulse starting in m_S = 0, the driven transfer probability is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

where Delta is the detuning in cycles/s. On resonance with t = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fluorescence drop in the signal readout is about:

0.22 * 0.996 = 0.219, or 21.9%

Data comparison

The first readout remains near 46-49 counts over the scan and does not show the large dip. The second readout has a clear depression near 3.870-3.885 GHz, with the minimum at 3.875 GHz:

- readout 1 at 3.875 GHz: 48.538
- readout 2 at 3.875 GHz: 39.115
- normalized ratio readout2/readout1: 0.8059

Using off-resonant points outside 3.865-3.885 GHz, the mean normalized ratio is 0.9991 with standard deviation 0.0258. The minimum ratio drop is therefore:

0.9991 - 0.8059 = 0.1932, or 19.3% of the off-resonant normalized baseline

This is close to the 21.9% expected from a near-pi pulse under the stated contrast scale. A detuned Rabi lineshape with f_R = 10 MHz, t = 52 ns, contrast = 22%, and a center near 3.878 GHz gives a matching broad dip over the same scan points. Stored averages are only two averages and may mainly reflect tracking cadence, but both averages show the same pronounced second-readout depression while the first readout is not similarly depressed.

Decision

The observed signal has the correct readout role, magnitude, and frequency-localized shape expected for a pODMR resonance from this pulse sequence. I classify the resonance as present.
