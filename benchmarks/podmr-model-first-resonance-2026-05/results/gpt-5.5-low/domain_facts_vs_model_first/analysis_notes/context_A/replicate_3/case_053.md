Case podmr_039_2026-05-16-221215.

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 to 3.925 GHz in 5 MHz steps. The sequence first polarizes and detects a true m_S = 0 reference, then waits, then applies a modulated Rabi pulse and detects again. full_expt is 0, so the optional m_S = +1 reference branch is inactive. Thus readout 1 is the pre-microwave bright reference and readout 2 is the post-microwave signal readout.

The active parameters to use are mod_depth = 1 and length_rabi_pulse = 52 ns. With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, this is approximately a pi pulse, so a real resonance should be capable of producing a substantial signal change, on the order of the known m_S = 0 to m_S = +1 contrast scale, not just a small ambiguous fluctuation.

The combined readouts are noisy and drifting. The readout 2 / readout 1 ratio ranges roughly from 0.95 to 1.09, with isolated excursions and a mild low-ratio region at the high-frequency end, but there is no clean, localized ODMR dip or repeatable resonance-shaped feature. Both stored averages differ substantially, consistent with the warning that stored averages can reflect tracking cadence rather than strong independent repeatability. The high-frequency decrease in readout 2 is only a few percent relative to readout 1 and does not stand out as a robust pODMR contrast feature for a near-pi pulse at mod_depth 1.

Decision: resonance_absent.
