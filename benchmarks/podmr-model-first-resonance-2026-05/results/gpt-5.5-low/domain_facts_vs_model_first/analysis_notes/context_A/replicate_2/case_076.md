Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps.

Readout roles from the XML:
- The first detection occurs immediately after adj_polarize, so readout 1 is the polarized m_S = 0 reference.
- full_expt is 0, so the optional explicit m_S = 1 reference block is inactive.
- The second active detection occurs after rabi_pulse_mod_wait_time, so readout 2 is the MW-driven pODMR signal readout.

Pulse parameters:
- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- Given the stated setup scale of about 10 MHz Rabi frequency at mod_depth = 1, this is near a pi pulse on resonance.

Decision:
At this pulse setting, an on-resonance transition should produce a large fluorescence change, on the order of the stated 22% m_S = 0 to m_S = +1 contrast if the pulse is effective. The measured driven readout stays near the reference level and shows only small point-to-point fluctuations of a few percent, with no clear isolated dip or peak relative to the reference and no reproducible resonance-shaped feature across the stored averages. The averages are only two and can reflect tracking cadence, so the weak variation is not strong independent evidence. I therefore judge that no pODMR resonance is present in this scan.
