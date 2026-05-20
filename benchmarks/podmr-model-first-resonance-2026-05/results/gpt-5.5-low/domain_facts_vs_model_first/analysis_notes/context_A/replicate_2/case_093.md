Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes the NV and performs a detection readout, giving the true m_S = 0 reference. Because full_expt = 0, the optional separate m_S = +1 reference branch is skipped. The only microwave-dependent branch is then a rabi_pulse_mod_wait_time pulse followed by detection, so readout 1 is the polarized reference and readout 2 is the post-pulse signal.

The provided sequence XML sets length_rabi_pulse = 52 ns and mod_depth = 1. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, 52 ns is approximately a pi pulse. If the sweep hit a real pODMR resonance, the post-pulse readout should show a sizable contrast-scale drop relative to the reference, potentially on the order of the 22% m_S = 0 to m_S = +1 contrast scale.

The measured combined readouts stay near 50 counts for both roles. The differences between readout 2 and readout 1 change sign and are only a few counts, with isolated spikes rather than a stable resonance-shaped feature. The per-average traces mostly show tracking/offset changes between averages and do not provide strong independent repeatability. There is no consistent microwave-frequency-dependent depletion of the post-pulse readout at the expected contrast scale.

Decision: resonance_absent.
