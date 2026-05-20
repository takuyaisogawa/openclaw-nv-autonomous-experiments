Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The active instruction path is:
- adj_polarize
- detection
- wait_for_awg
- skip the Acquire 1 level reference block because full_expt = 0
- rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay)
- detection

Readout roles:
- readout 1 is the direct post-polarization detection, so it is the bright m_S = 0 reference/tracking readout.
- readout 2 is the detection after the microwave Rabi pulse, so it is the pODMR signal readout.

Pulse settings from the provided XML:
- mod_depth = 1
- length_rabi_pulse = 52 ns

Using the stated setup facts, mod_depth = 1 gives about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse. If the scan crossed a strong resonance, readout 2 should be substantially suppressed relative to the m_S = 0 reference readout, with contrast on the order of the 22 percent m_S = 0 to m_S = +1 scale.

The combined raw readout ratio readout2/readout1 ranges only from about 0.969 to 1.040, with mean difference nearly zero. The largest apparent dips are only a few percent and are not a clean resonance-shaped suppression. The stored per-average traces also move substantially with tracking/cadence and do not provide a strong independent repeatability check.

Decision: resonance absent.
