Active sequence and roles

The provided sequence is Rabimodulated.xml. In the saved export, the actual run variables are mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps, length_rabi_pulse = 52 ns, mod_depth = 1, full_expt = 0, and delay_wrt_1mus = 0.2 us. Because full_expt is zero, the optional m_S = +1 reference block is inactive. The active readouts are therefore:

- readout 1: true m_S = 0 reference after optical polarization and detection.
- readout 2: pODMR measurement after the rabi_pulse_mod_wait_time microwave pulse and detection.

Quantitative physical expectation

Using the supplied setup fact, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a rectangular resonant pulse, the transfer probability from m_S = 0 to m_S = +1 is

P = sin^2(pi * f_R * t)

when a pi pulse occurs at t = 1 / (2 f_R). With f_R = 10 MHz and t = 52 ns,

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance pODMR feature should have fractional contrast

0.22 * 0.996 = 0.219.

The mean true-zero reference readout is 46.35 counts, so the expected resonant drop is approximately

46.35 * 0.219 = 10.16 counts.

Data check

The combined readout 1 mean is 46.35 counts with standard deviation 0.46 counts. The combined driven readout 2 mean is 46.14 counts with standard deviation 1.36 counts. The lowest driven point is 43.50 counts at 3.895 GHz. Using the readout 2 points excluding +/- 2 scan steps around that minimum as a local baseline gives 46.31 counts, so the largest observed depression is 2.81 counts, or about 6.1% of the m_S = 0 reference.

Simple fixed-width Gaussian dip fits to readout 2 give best dip amplitudes of about 1.8 counts for a 1-point sigma, 1.5 counts for 1.5-point sigma, 1.2 counts for 2-point sigma, and 0.75 counts for 3-point sigma. These amplitudes are well below the approximately 10-count drop expected from the near-pi pulse model.

Decision

Although readout 2 has a low point near 3.895 GHz, its amplitude is far smaller than the expected pODMR response for mod_depth = 1 and a 52 ns near-pi pulse. The stored averages mainly reflect tracking cadence and do not independently establish repeatability. Under the explicit model calculation, this scan does not show a credible pODMR resonance.
