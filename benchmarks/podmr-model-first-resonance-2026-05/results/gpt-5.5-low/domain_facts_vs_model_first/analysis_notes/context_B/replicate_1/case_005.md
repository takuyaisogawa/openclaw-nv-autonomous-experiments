Case: podmr_008_2026-05-11-131831

Inputs used:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Active instructions with full_expt = 0 acquire only two detections: first after optical polarization, and second after the Rabi-modulated microwave pulse.
- Readout roles: readout 1 is the bright m_S = 0 reference; readout 2 is the post-microwave pODMR readout.
- Active pulse parameters from the saved experiment: mod_depth = 1, length_rabi_pulse = 52 ns, sample_rate = 250 MHz.

Physical model calculation:
- Given setup Rabi frequency at mod_depth = 1 is about 10 MHz, the resonant square-pulse transition probability is
  P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a true resonance should lower the pulsed readout by approximately 0.22 * 0.996 = 21.9% relative to the bright reference.
- Therefore the expected normalized pulsed/reference ratio on resonance is about 0.781, corresponding to a drop of about 4.38 counts for a 20-count bright readout.

Data check:
- Combined readout means are readout 1 = 20.079 and readout 2 = 19.791.
- The mean readout2/readout1 ratio is 0.988.
- The smallest combined ratio is 0.881 at 3.840 GHz, a 2.5-count drop, which is much smaller than the expected 4.38-count resonant drop and is isolated.
- Other low ratios occur at separated scan points and do not form a coherent pODMR line shape. Stored averages show strong tracking/drift structure, so they are not treated as an independent repeatability test.

Decision:
The active pulse should produce an almost full-contrast pODMR dip if a resonance is present in the scan window. The measured pulsed readout does not show the expected depth or a coherent resonance feature, so I decide resonance_absent.
