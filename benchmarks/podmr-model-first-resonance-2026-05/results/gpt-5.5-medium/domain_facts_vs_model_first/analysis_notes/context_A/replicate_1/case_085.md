Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence has full_expt = 0, so the enabled measurement path is:
1. optical polarization followed by detection: true m_s = 0 / bright reference readout;
2. a modulated Rabi pulse followed by detection: post-pulse signal readout.

The m_s = +1 reference block is gated by full_expt and is inactive, so the two plotted readouts are not two independent resonance measurements. They are a bright reference and a post-microwave-pulse readout.

Pulse settings used for the decision:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns;
- mod_depth = 1 in the provided XML/variable values;
- with the stated setup calibration this is about a 10 MHz Rabi frequency, so the 52 ns pulse is approximately a pi pulse when on resonance.

For a single NV pODMR resonance under these conditions, I would expect the post-pulse readout to show a localized fluorescence decrease relative to the bright reference, with a scale that can approach the stated 22% contrast if the pulse is resonant and effective. Instead, both raw readouts share a gradual drift upward with scan point. The differential signal readout2 - readout1 fluctuates around zero with no stable localized dip: the ratio readout2/readout1 ranges roughly from 0.946 to 1.057 and alternates sign across neighboring points. The strongest negative points are isolated and comparable to positive excursions, and the per-average traces mainly show tracking/drift rather than a repeatable resonance feature.

Decision: resonance_absent.
