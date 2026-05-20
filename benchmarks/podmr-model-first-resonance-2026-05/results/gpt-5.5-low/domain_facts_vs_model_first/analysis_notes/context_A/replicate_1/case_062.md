Active sequence: Rabimodulated.xml / Rabimodulated sequence with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps.

The provided sequence first polarizes and detects the bright m_S = 0 reference, waits, then applies a modulated Rabi pulse and detects again. The full_expt variable is 0, so the conditional branch that would acquire a separate m_S = +1 reference is inactive. Thus readout 1 is the 0-level reference and readout 2 is the signal after the microwave pulse.

The active pulse uses length_rabi_pulse = 52 ns and mod_depth = 1 in the provided XML/variable values. With the supplied setup fact of about 10 MHz Rabi frequency at mod_depth = 1, this is near a pi-pulse duration. If the swept microwave crosses a true single-NV pODMR resonance, readout 2 should show a clear frequency-localized drop relative to readout 1 on the order of the setup contrast scale, not merely small noisy point-to-point variation.

The combined raw readouts show only modest fluctuations around 50 counts. Readout 2 is often slightly below readout 1, but the difference is broad and inconsistent rather than a localized resonance feature; the per-average overlays also vary substantially and look tracking/noise limited rather than repeatable. The largest deviations are only a few counts, much smaller and less coherent than expected for a near-pi pulse with about 22% contrast.

Decision: resonance_absent.
