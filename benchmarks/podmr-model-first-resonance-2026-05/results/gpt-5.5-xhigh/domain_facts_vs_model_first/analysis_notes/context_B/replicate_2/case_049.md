Sequence interpretation:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and perform detection; this is readout 1, the true m_S = 0 reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection; this is readout 2, the pODMR signal readout after the microwave pulse.

Physical model calculation:

Using the provided setup facts, the Rabi frequency is approximately

    f_R = 10 MHz * mod_depth = 10 MHz.

For a rectangular resonant microwave pulse, the transition probability is

    P_1(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * tau * sqrt(f_R^2 + df^2)),

where tau = 52 ns and df is the detuning from resonance in Hz. On resonance,

    P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a true resonance should therefore produce a normalized readout-2 deficit of

    0.22 * 0.996 = 0.219,

or about an 11-count drop for a 50-count reference level. The expected contrast remains large near resonance: about 20.4% at 2.5 MHz detuning, 16.5% at 5 MHz detuning, and 6.0% at 10 MHz detuning.

Data comparison:

I normalized the data as readout2/readout1 because readout 1 is the immediate m_S = 0 reference. The observed contrast, 1 - readout2/readout1, has mean 0.0166, standard deviation 0.0205, maximum 0.0565, and minimum -0.0216. The largest observed deficit is therefore only about 5.7%, far below the approximately 21.9% on-resonance pi-pulse expectation. Around the central part of the scan the contrast remains small; for example at 3.880 GHz it is 0.0131.

I also compared a simple linear baseline in readout2/readout1 against the fixed physical resonance model above. The linear baseline has SSE = 0.00881 and RMSE = 0.0205. For a mod_depth = 1 resonance constrained to lie within the scanned band, the best fixed-amplitude physical model has f0 = 3.925 GHz, SSE = 0.0353, and RMSE = 0.0410, substantially worse than the baseline because it predicts a much deeper dip than observed. The per-average traces fluctuate and reflect tracking cadence, so I did not treat them as strong independent repeatability evidence.

Decision:

The sequence would make a real pODMR resonance a large readout-2 dip relative to readout 1, but the measured normalized deficits are small, scattered, and not consistent with the required fixed-amplitude Rabi response. I therefore classify this case as resonance_absent.
