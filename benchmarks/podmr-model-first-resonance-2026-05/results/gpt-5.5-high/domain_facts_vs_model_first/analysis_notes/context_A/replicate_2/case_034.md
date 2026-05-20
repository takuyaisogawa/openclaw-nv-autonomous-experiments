Case podmr_019_2026-05-16-164247.

Sequence interpretation:
- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML executes adj_polarize followed by detection first, so readout 1 is the bright m_S = 0 reference.
- full_expt is 0, so the optional m_S = +1 reference block is skipped.
- The second active detection occurs after rabi_pulse_mod_wait_time, so readout 2 is the microwave-pulsed pODMR signal.
- The provided sequence variables set mod_depth = 1 and length_rabi_pulse = 52 ns. At the 250 MHz sample rate this remains 52 ns.

Pulse/contrast expectation:
- With the stated setup Rabi frequency of about 10 MHz at mod_depth = 1, a 52 ns pulse is approximately a pi pulse on resonance.
- If a resonance is present, the pulsed readout should show a substantial fluorescence drop relative to the m_S = 0 reference, on the order of the setup's 22% contrast scale.

Observed readouts:
- Mean readout 1 is about 46.94 and mean readout 2 is about 46.13, only about a 1.7% average decrease.
- The largest pointwise decrease is at 3.895 GHz, where readout 2/readout 1 is about 0.929, a roughly 7.1% drop. This is far below the expected near-pi-pulse contrast and is not a clean resonance-shaped feature across neighboring points.
- Several points have readout 2 equal to or above readout 1, including the endpoint at 3.925 GHz.
- The per-average traces are dominated by baseline/tracking shifts, so they should not be treated as a strong independent repeatability test; they also do not rescue the weak combined signal as an obvious resonance.

Decision:
Given the active near-pi Rabimodulated pulse conditions, the scan should show a large and coherent pulsed-readout deficit if a pODMR resonance were present. The observed differences are small, irregular, and compatible with baseline drift/noise rather than a real resonance.
