Sequence and readout interpretation

The active pulse sequence is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and
detect, giving a true m_S = 0 reference readout. The optional m_S = +1
reference branch is inactive because full_expt = 0, despite
do_adiabatic_inversion = 1. The sequence then applies
rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1,
followed by the second detection. Therefore readout 1 is the pre-microwave
m_S = 0 reference and readout 2 is the post-Rabi-pulse signal readout.

Physical model calculation

Given the supplied calibration, the Rabi frequency is about 10 MHz at
mod_depth = 1. For a resonant rectangular pulse, the transferred population is
P = sin^2(pi f_R t). With f_R = 10 MHz and t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The mean reference readout is about 47.29 counts. With a setup contrast scale
of 22% between m_S = 0 and m_S = +1, the expected on-resonance depletion for a
near-pi pulse is:

0.22 * 0.996 * 47.29 = 10.36 counts.

Data comparison

Using readout1 - readout2 as the depletion metric, the central points near the
candidate resonance are:

3.875 GHz: 3.96 counts
3.880 GHz: 7.38 counts
3.885 GHz: 6.27 counts

Their mean depletion is 5.87 counts. Away from the 3.870-3.885 GHz feature,
the mean depletion is 1.12 counts with a standard deviation of about 2.06
counts. The central feature is therefore a localized additional depletion of
about 4.76 counts above the off-resonant offset, or roughly 2.3 off-window
standard deviations for individual points. The deepest point corresponds to a
15.4% contrast relative to readout 1, below the ideal 22% model value but
consistent with a real, imperfectly sampled or broadened resonance.

The two stored averages both show enhanced depletion around the same central
region, but I do not treat the averages as a strong repeatability test because
stored averages can reflect tracking cadence.

Decision

The observed localized post-pulse depletion near 3.88 GHz has the sign,
location, and approximate scale expected from the near-pi-pulse pODMR model.
It is smaller than the ideal 10.36-count depletion and the data are noisy, but
the quantitative comparison supports resonance_present rather than
resonance_absent.
