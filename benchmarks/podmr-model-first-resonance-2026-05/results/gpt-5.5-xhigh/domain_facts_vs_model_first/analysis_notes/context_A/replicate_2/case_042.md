Sequence review:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the true m_S = 0 bright reference after adj_polarize and detection.
- Readout 2 is the detection after rabi_pulse_mod_wait_time.
- mod_depth = 1 and length_rabi_pulse = 52 ns, unchanged after rounding at 250 MHz sample rate. With the supplied setup calibration, this is essentially a near-pi pulse for a 10 MHz Rabi rate.

Data assessment:
The post-pulse readout is lower than the bright reference near 3.875-3.885 GHz, but only by about 3.7-5.5 percent in the combined readouts. For a near-pi pulse at mod_depth = 1, a real on-resonance response should be much closer to the available m_S = 0 to m_S = +1 contrast scale of about 22 percent. The small depression is also followed immediately by a comparable opposite excursion at 3.890 GHz, and the stored averages are not a strong independent repeatability test because they often track cadence. Overall this looks like drift/noise structure rather than a convincing pODMR resonance.

Decision: resonance_absent.
