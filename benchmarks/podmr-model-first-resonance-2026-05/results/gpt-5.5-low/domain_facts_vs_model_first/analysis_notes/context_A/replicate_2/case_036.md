Active sequence: Rabimodulated.xml / Rabimodulated sequence varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles: with full_expt = 0, the optional m_S = +1 reference block is skipped. The first detection after adj_polarize is the true m_S = 0 reference readout. The second detection follows the active rabi_pulse_mod_wait_time call and is the microwave-pulsed signal readout.

Pulse settings: length_rabi_pulse is 52 ns and mod_depth is 1 in the provided sequence/variable values. With the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1, this pulse is near a pi pulse, so a real resonance should be capable of producing a sizable contrast change relative to the about 22% m_S = 0 to m_S = +1 scale.

Data assessment: the signal/reference ratio changes only by a few percent and changes sign across the scan. The largest negative deviations are around 3.830 and 3.840 GHz, while the center of the scan near the nominal carrier does not show a coherent dip and nearby points include positive deviations. Both readouts also share slow baseline/tracking structure, and the stored averages mainly reflect tracking cadence rather than independent repeatability. Given a near-pi pulse, the lack of a stable, localized, spin-contrast-sized decrease in the pulsed readout argues against a pODMR resonance.

Decision: resonance_absent.
