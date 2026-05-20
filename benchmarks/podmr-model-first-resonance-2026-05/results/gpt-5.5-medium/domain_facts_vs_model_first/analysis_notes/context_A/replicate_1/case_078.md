Active sequence identification:

The provided sequence is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes and
detects a true m_S = 0 bright reference. The full_expt variable is 0, so the
optional m_S = 1 reference branch is skipped. The active measurement branch is
a rabi_pulse_mod_wait_time pulse followed by detection. Therefore readout 1 is
the bright reference and readout 2 is the post-microwave signal readout.

Pulse parameters:

The active pulse is length_rabi_pulse = 52 ns with mod_depth = 1. For the
given setup, the Rabi frequency at mod_depth = 1 is about 10 MHz, so a 52 ns
pulse is close to a pi pulse. If the scan crossed a real pODMR resonance, the
post-microwave readout should show a substantial contrast change relative to
the bright reference, on the order of the stated 22 percent scale.

Data assessment:

The combined readouts remain near 50 to 52 counts with no robust resonant
contrast feature in readout 2 relative to readout 1. The largest apparent
negative difference is narrow and is not a convincing reproducible dip across
the two stored averages; stored averages are also not a strong repeatability
test because they may reflect tracking cadence. The most prominent feature is
instead a positive spike in readout 2 near the high-frequency side, which is
opposite the expected pODMR depletion signature. Given the near-pi pulse, a
true resonance should be much clearer than the observed small, inconsistent
fluctuations.

Decision: resonance_absent.
