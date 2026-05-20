Case podmr_058_2026-05-17-053345

The provided sequence is Rabimodulated.xml with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect the true m_S = 0 level reference, then skip the optional m_S = 1 reference because full_expt = 0, then apply rabi_pulse_mod_wait_time and detect again. Therefore readout 1 is the m_S = 0 reference and readout 2 is the post-microwave signal readout.

The active values are mod_depth = 1 and length_rabi_pulse = 52 ns. With the supplied setup facts, mod_depth = 1 gives about a 10 MHz Rabi frequency, so 52 ns is essentially a pi pulse. On resonance this should transfer substantial population and produce a signal-readout fluorescence drop approaching the setup contrast scale of about 22% relative to the m_S = 0 reference.

The combined signal/reference ratios do not show that behavior. The largest adjacent low region around 3.885-3.890 GHz is only about a 6-7% drop, with other similarly sized isolated low points at 3.910 GHz and the scan edge. The raw readouts are dominated by small scatter and baseline changes between stored averages, and the stored averages mainly reflect tracking cadence rather than independent confirmation. Given the near-pi pulse condition, the absence of a strong, coherent contrast dip means this should be classified as no pODMR resonance.
