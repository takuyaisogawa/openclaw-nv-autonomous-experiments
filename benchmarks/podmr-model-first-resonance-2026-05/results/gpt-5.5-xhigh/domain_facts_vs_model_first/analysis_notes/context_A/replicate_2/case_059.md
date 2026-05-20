Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the optional m_S = +1 reference block is skipped. Each scan point has two detections: readout 1 is the polarized bright m_S = 0 reference after adj_polarize, and readout 2 is the signal after rabi_pulse_mod_wait_time followed by detection.

Sequence parameters relevant to the decision:
- mod_depth = 1
- length_rabi_pulse = 52 ns, already aligned to the 250 MHz sample clock
- With the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse.

If a pODMR resonance were present, readout 2 should show a clear fluorescence reduction relative to readout 1 near resonance, with a possible scale approaching the stated 22% contrast between m_S = 0 and m_S = +1. The combined readouts instead track each other within small point-to-point fluctuations, and the per-average traces do not show a reproducible frequency-localized dip in the microwave-pulse readout. The largest deviations are comparable to the scatter between the two stored averages, which likely reflects tracking cadence rather than strong repeatability.

Decision: resonance_absent.
