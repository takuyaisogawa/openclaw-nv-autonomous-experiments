Case: podmr_065_2026-05-17-071421

Sequence interpretation

The provided sequence is Rabimodulated.xml. The active instructions polarize the NV, perform a detection readout, wait, then apply one rabi_pulse_mod_wait_time pulse and perform a second detection readout. Since full_expt = 0, the optional m_s = +1 reference block is skipped. Therefore readout 1 is the true m_s = 0 reference after optical polarization, and readout 2 is the signal after the microwave pulse. The pulse duration is length_rabi_pulse = 52 ns. The provided sequence XML and exported variable values give mod_depth = 1, so I use mod_depth = 1 for the decision.

Expected quantitative signal model

For this setup the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the resonant transfer probability is

P = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10 MHz and tau = 52 ns. This gives

P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The stated contrast scale between m_s = 0 and m_s = +1 is about 22%, so on resonance the post-microwave readout should be lower than the m_s = 0 reference by about

0.22 * 0.996 = 0.219, or 21.9%.

The mean readout-1 level is 47.48 raw counts, so the expected resonant drop is about

47.48 * 0.219 = 10.4 raw counts.

I also compared the measured readout difference r2 - r1 against the square-pulse detuned model

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(0.5 * sqrt(Omega^2 + Delta^2) * tau),

where Omega = 2*pi*10 MHz and Delta is angular detuning from a tested resonance center. Allowing only a constant readout offset, the best fixed-amplitude resonance model over centers in the scanned range had SSE = 115.69, while a no-resonance constant-offset model had SSE = 30.24. Thus the expected physical resonance shape with the calibrated amplitude fits much worse than no resonance.

Observed data comparison

The scan runs from 3.825 GHz to 3.925 GHz in 5 MHz steps. The observed combined readout statistics are:

- readout 1 mean = 47.48, standard deviation = 1.26
- readout 2 mean = 47.21, standard deviation = 1.50
- r2 - r1 mean = -0.27 counts
- minimum r2 - r1 = -2.27 counts
- r2/r1 mean = 0.9945
- minimum r2/r1 = 0.9523

The largest observed deficit is only 2.27 counts, or 4.8%, far below the expected 10.4-count, 21.9% resonant suppression for the active pulse. The difference trace also changes sign repeatedly and has positive excursions, so the observed structure is consistent with drift/noise between readouts rather than a pODMR dip. The stored two averages mainly show tracking-level offsets between averages and are not a strong repeatability test.

Decision

No pODMR resonance is present in this scan under the active Rabimodulated sequence and the expected 52 ns, mod_depth = 1 pulse response.
