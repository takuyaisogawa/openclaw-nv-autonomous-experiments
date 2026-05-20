Active sequence: Rabimodulated.xml / Rabimodulated sequence, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided XML has full_expt = 0, so the optional m_S = +1 reference branch is inactive. The executed readouts are therefore:
- readout 1: detection immediately after optical polarization, a true m_S = 0 / bright reference.
- readout 2: detection after the modulated microwave Rabi pulse, the pODMR signal readout.

The microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is approximately a pi pulse. On a real resonance, the signal readout should therefore show a substantial contrast change on the order of the setup contrast scale, about 22%, relative to the bright reference.

The combined raw readouts do not show that. The largest normalized readout-2 depressions relative to readout 1 are isolated points, about 6.2% near 3.865 GHz and about 4.6% near 3.910 GHz, with neighboring points returning to baseline or moving oppositely. The readout-1 reference itself fluctuates at a comparable scale, and the two stored averages mainly reflect a high/low tracking offset rather than a strong independent repeatability test.

Decision: resonance_absent. The data contain noisy point-to-point fluctuations but no robust pODMR resonance consistent with the active near-pi pulse sequence and expected contrast.
