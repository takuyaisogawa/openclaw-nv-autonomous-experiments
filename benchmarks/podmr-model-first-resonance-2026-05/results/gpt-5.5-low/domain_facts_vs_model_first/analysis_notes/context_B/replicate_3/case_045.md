Case podmr_031_2026-05-16-195907

I used only the provided XML/raw export for this case. The active sequence is Rabimodulated.xml. The instructions first polarize and detect a true m_S = 0 reference, then skip the optional m_S = 1 reference because full_expt = 0, then apply a single rabi_pulse_mod_wait_time pulse and detect again. Thus the two stored readouts are the pre-pulse m_S = 0 reference and the post-pulse signal readout, not independent ODMR repeats. The pulse duration is length_rabi_pulse = 52 ns. The active parameter list records mod_depth = 1, so I used the stated setup calibration of about 10 MHz Rabi frequency at mod_depth = 1.

Quantitative expected-signal model:

For a square driven two-level pulse, using Rabi frequency Omega = 10 MHz in cycles/s and pulse length t = 52 ns,

P_1(delta) = Omega^2 / (Omega^2 + delta^2) * sin^2(pi * sqrt(Omega^2 + delta^2) * t).

At zero detuning, P_1 = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected resonant fluorescence is baseline * (1 - 0.22 * P_1). The measured combined baseline across the scan is 52.724 counts, so an on-resonance point should be about 41.171 counts, an expected dip of about 11.554 counts.

The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. For a resonance at the scanned endpoint/carrier value, the model predicts the largest drop at 3.925 GHz. The measured final point is readout 1 = 51.615 and readout 2 = 51.577, combined 51.596, which is within about 1.1 counts of the scan baseline rather than lower by about 11.6 counts. The observed combined minimum is 50.442 at 3.915 GHz, only 2.282 counts below baseline and not shaped like the calculated Rabi/ODMR response; it is comparable to the readout scatter (readout-difference noise estimate about 0.985 counts, combined-trace standard deviation about 0.911 counts).

Decision: the expected resonant signal for the active pulse would be a large, localized fluorescence dip, especially at/near the resonant endpoint, and it is not present in the measured readouts. I therefore classify this case as resonance_absent.
