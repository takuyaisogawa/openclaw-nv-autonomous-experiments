Active sequence assessment:

The provided Rabimodulated.xml sequence sets full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive. The active readout order is:

1. adj_polarize followed by detection: this is the true mS=0 reference readout.
2. rabi_pulse_mod_wait_time followed by detection: this is the swept microwave pODMR readout.

The active microwave pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this rounds to 13 samples, still 52 ns. The active mod_depth value is 1.

Quantitative signal model:

Use the two-level square-pulse Rabi response

P_transfer(detuning) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),

with Omega = 2*pi*10 MHz at mod_depth = 1, Delta = 2*pi*detuning, tau = 52 ns, and fluorescence contrast C = 0.22 between mS=0 and mS=+1. The expected fractional readout depression is C * P_transfer.

At zero detuning, Omega*tau = 2*pi*10e6*52e-9 = 3.267 rad, giving P_transfer = 0.996 and expected readout depression = 0.219. For a typical reference readout near 42.7 counts, the expected on-resonance signal readout would be lower by about 9.3 counts. The model also predicts broad neighboring-point effects at the 5 MHz scan step: at 5 MHz detuning the expected drop is 0.165, and at 10 MHz detuning it is 0.060.

Observed data comparison:

The scan has 21 points from 3.825 GHz to 3.925 GHz in 5 MHz steps. Readout 1 has mean 42.67 counts and readout 2 has mean 42.11 counts. The observed fractional difference (readout1 - readout2) / readout1 has mean 0.0128, standard deviation 0.0247, and maximum 0.0643. The largest observed drop is at 3.880 GHz: readout1 = 44.538, readout2 = 41.673, fractional drop = 0.064. This is far below the expected roughly 0.219 on-resonance drop and is not accompanied by the strong multi-point dip expected from the 52 ns, 10 MHz Rabi pulse.

I also compared a fixed 22% Rabi-response model against a flat scaled readout baseline. The flat no-resonance model gives SSE = 23.81 counts^2. The best fixed-contrast resonance model over the sampled centers gives SSE = 121.26 counts^2, substantially worse. If the contrast amplitude is allowed to float freely, the best equivalent contrast is only about 4.2%, much smaller than the expected 22% setup contrast.

Decision:

The data do not show the quantitatively expected pODMR resonance response for the active pulse settings. The small readout differences are compatible with noise or drift rather than a resolved resonance.
