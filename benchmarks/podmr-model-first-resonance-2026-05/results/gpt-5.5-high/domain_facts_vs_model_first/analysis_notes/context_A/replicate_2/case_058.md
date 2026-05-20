The active sequence is the Rabimodulated mw_freq sweep. In the provided XML, full_expt is 0, so the optional m_S = +1 reference block is not executed. The active readouts are therefore:

- readout 1: polarized m_S = 0 reference, acquired immediately after adj_polarize and before the microwave pulse.
- readout 2: signal readout after the modulated Rabi microwave pulse.

The active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), with length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is approximately a pi pulse. If the swept microwave frequency crossed a pODMR resonance, the post-pulse signal readout should show a strong decrease relative to the m_S = 0 reference, on the order of the stated 22% contrast scale for a good spin flip.

The raw averaged readouts do not show that behavior. The signal/reference ratios remain close to unity across the sweep, roughly 0.95 to 1.04, and the largest negative excursion is only about 4.8%, far below the expected contrast scale. The per-average overlays mainly show common baseline and tracking shifts rather than a repeatable resonance-shaped dip in the post-pulse signal. Since stored averages can reflect tracking cadence, I do not treat the per-average separation as independent confirmation.

Decision: resonance absent.
