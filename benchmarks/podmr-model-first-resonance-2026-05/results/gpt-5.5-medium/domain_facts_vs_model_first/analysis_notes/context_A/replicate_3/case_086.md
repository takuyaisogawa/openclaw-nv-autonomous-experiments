Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz. The instructions first polarize and detect a true mS=0 reference, then because full_expt = 0 they skip the mS=+1 reference branch, then apply rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1 followed by the signal detection. Thus readout 1 is the bright mS=0 reference and readout 2 is the post-Rabi signal.

With the provided domain calibration, mod_depth = 1 gives about 10 MHz Rabi frequency, so a 52 ns pulse is close to a pi pulse on resonance. For a single NV with about 22% contrast, a true resonance should produce a clear, localized drop of the post-pulse signal readout relative to the 0-reference, on the order of many counts compared with a ~50 count baseline if the pulse is effective.

The combined readouts do not show such a feature. Readout 2 is sometimes below and sometimes above readout 1, with signal-reference differences ranging only from about -2.44 to +1.17 counts and no coherent dip centered in the scan. The largest negative differences occur at isolated points including the scan edge, while neighboring points do not support a resonance-shaped depletion. The two stored averages also show broad tracking-like offsets and scatter rather than independent repeatability of a resonance.

Decision: resonance absent.
