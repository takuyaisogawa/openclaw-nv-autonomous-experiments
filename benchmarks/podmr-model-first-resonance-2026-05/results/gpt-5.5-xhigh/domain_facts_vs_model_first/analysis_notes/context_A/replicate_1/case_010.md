Active sequence and readout roles:

The sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect, producing the true m_S = 0 bright reference. The full_expt variable is 0, so the optional 1-level reference block is not active. The only active microwave-dependent measurement is then a rabi_pulse_mod_wait_time pulse followed by detection, so readout 1 is the polarized 0-reference and readout 2 is the post-Rabi signal.

Pulse settings:

The provided sequence XML has mod_depth = 1 and length_rabi_pulse = 5.2e-08 s. At the 250 MS/s sample rate this is already a 52 ns pulse. With the setup estimate of about 10 MHz Rabi frequency at mod_depth = 1, this is close to a pi pulse, so an on-resonance point should transfer population strongly and make readout 2 substantially lower than readout 1, on the order of the available 22% contrast scale if the resonance is well hit.

Data assessment:

The combined contrast estimate (readout1 - readout2) / readout1 is not a clear resonance. It reaches only about 8.7% at 3.855 GHz, has a mean near zero, and alternates sign across neighboring frequencies; the adjacent 3.850 and 3.860 GHz points have readout 2 higher than readout 1. That single-point positive difference is much smaller and narrower than expected for a 52 ns near-pi pulse, and is comparable to the jagged point-to-point variation in the raw traces. The per-average traces are dominated by opposite tracking drift across the sweep, and stored averages here should not be treated as a strong independent repeatability check.

Decision:

No reliable pODMR resonance is present in this scan.
