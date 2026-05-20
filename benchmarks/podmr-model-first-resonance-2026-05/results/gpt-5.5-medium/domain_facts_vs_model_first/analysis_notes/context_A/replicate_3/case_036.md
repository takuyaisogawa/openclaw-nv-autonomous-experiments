Active sequence and roles:

The sequence is Rabimodulated.xml / Rabimodulated. It polarizes the NV, performs a detection readout for the true m_S = 0 reference, waits, then conditionally would acquire an m_S = 1 reference only if full_expt were nonzero. Here full_expt = 0, so that branch is inactive. The active measurement after the reference is a single rabi_pulse_mod_wait_time followed by detection. Thus readout 1 is the initial polarized reference readout and readout 2 is the post-Rabi-pulse signal readout.

Pulse settings used for the decision:

The exported variable values give length_rabi_pulse = 52 ns and mod_depth = 1. The sequence XML text contains a default mod_depth assignment, but the run variable values list mod_depth = 1, and the pulse call uses that variable. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, a 52 ns pulse is close to a pi pulse on resonance. A real resonance should therefore produce a substantial contrast change in the post-pulse signal relative to the polarized reference, on the order of the setup contrast scale, about 22% between m_S = 0 and m_S = +1.

Data assessment:

The combined raw readouts are both near 44 to 48 counts. There are small local readout differences, including a modest depression of readout 2 around the lower-middle part of the sweep, but the magnitude is only a few percent, far below the expected near-pi-pulse contrast for a single NV under these stated conditions. The per-average overlay shows large baseline/tracking changes between the two stored averages, so the stored averages do not provide strong independent repeatability evidence. The apparent structure is consistent with tracking drift and noise rather than a clear pODMR dip.

Decision:

pODMR resonance is absent.
