Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML uses full_expt = 0, so the optional m_S = +1 reference branch is skipped. The first detection after polarization is the bright m_S = 0 reference readout, and the second detection follows a rabi_pulse_mod_wait_time pulse and is the pODMR signal readout.

The pulse is length_rabi_pulse = 52 ns with mod_depth = 1. Given the stated setup calibration, this is approximately a pi pulse at about 10 MHz Rabi frequency, so an on-resonance response should approach the current m_S = 0 to m_S = +1 contrast scale of about 22% if the transition is being driven well.

The combined readouts do not show that behavior. Readout 1 averages about 46.49 and readout 2 about 46.41, essentially equal overall. The largest readout-2 deficit relative to readout 1 is about 2.27 counts, roughly 4.7%, and the per-average traces show strong tracking/baseline changes rather than a reproducible narrow or broad depletion at one microwave frequency. There are local crossings and small fluctuations, but no contrast-sized dip in the post-pulse readout compared with the reference.

Decision: resonance absent.
