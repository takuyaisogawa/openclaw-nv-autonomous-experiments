Case: podmr_062_2026-05-17-063134

Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Readout roles from the sequence:
- The first detection happens immediately after adj_polarize, so readout 1 is the true m_S=0 fluorescence reference.
- full_expt is 0, so the optional m_S=+1 reference block is inactive.
- The active measurement then applies rabi_pulse_mod_wait_time followed by detection, so readout 2 is the post-microwave-pulse signal.

Pulse settings used for the decision:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s.
- With the provided setup scale of about 10 MHz Rabi frequency at mod_depth 1, 52 ns is approximately a pi pulse.
- A real resonance under this sequence should therefore drive a large drop in the post-pulse signal relative to the m_S=0 reference, on the order of the setup contrast scale rather than a small percent-level fluctuation.

Data assessment:
The combined readouts do not show a sustained signal/reference contrast feature. The normalized readout 2 minus readout 1 differences are centered near zero, with typical scatter of about 2.5 percent. The deepest combined negative point is around 3.920 GHz at about -6.3 percent, but it is not a broad or stable feature consistent with a 52 ns near-pi pulse, and the surrounding points return toward zero. The per-average traces vary substantially, which is consistent with tracking cadence and drift rather than an independent repeatability test.

Decision: resonance absent. There is no clear pODMR resonance feature at the expected contrast scale for this active sequence and pulse setting.
