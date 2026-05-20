Case podmr_075_2026-05-17-093901

I used the provided sequence XML before deciding. The active sequence is Rabimodulated.xml. With full_expt = 0, the optional m_S = +1 reference branch is skipped, so the two acquired detections are:

1. readout 1: after adj_polarize, the true m_S = 0 bright reference.
2. readout 2: after a single rabi_pulse_mod_wait_time pulse, the pODMR signal readout.

The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. I did not treat the stored two averages as a strong independent repeatability test, since they can reflect tracking cadence.

Quantitative expected-signal model:

For a rectangular driven two-level pulse, using the setup fact f_Rabi = 10 MHz at mod_depth = 1, the transition probability versus detuning delta is

P(delta) = f_Rabi^2 / (f_Rabi^2 + delta^2) * sin^2(pi * tau * sqrt(f_Rabi^2 + delta^2)).

Here tau = 52 ns and f_Rabi = 10 MHz. On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996. With the stated m_S = 0 to m_S = +1 contrast scale of about 22 percent, an on-resonance pulse should lower the signal readout by 0.22 * 0.996 = 21.9 percent of the bright readout. The bright readout mean is about 50.52 counts, so the expected on-resonance signal loss is about 11.1 counts.

The 5 MHz scan spacing is fine enough that a resonance within the scanned interval should still be sampled close to its center. At offsets of 0, 2.5, 5, 10, and 15 MHz, the model transition probabilities are approximately 0.996, 0.929, 0.749, 0.273, and 0.012. Even if the resonance center fell halfway between two sampled frequencies, the nearest sampled point should still show a loss of about 0.22 * 0.929 = 20.4 percent, or about 10.3 counts.

Observed comparison:

The combined readout means are readout 1 = 50.52 and readout 2 = 50.39. The measured readout2/readout1 ratios range from 0.951 to 1.048 with mean 0.998. The deepest observed low point is therefore only about a 4.6 percent depression relative to the mean ratio, roughly 2.3 counts, and there is no broad 10-count-scale dip.

I also compared the data to the explicit pulse model. A no-resonance scale model readout2 = b * readout1 gives b = 0.9972 and RMSE = 1.16 counts. For a fixed expected 22 percent contrast resonance, scanning the resonance center across the measured frequency span gives the best RMSE = 2.87 counts, worse than the no-resonance model, because it predicts a large localized depression that is not present. Allowing the contrast amplitude to float chooses a small negative amplitude of about -3.5 percent, not the expected positive 22 percent resonance contrast.

Decision: resonance absent.
