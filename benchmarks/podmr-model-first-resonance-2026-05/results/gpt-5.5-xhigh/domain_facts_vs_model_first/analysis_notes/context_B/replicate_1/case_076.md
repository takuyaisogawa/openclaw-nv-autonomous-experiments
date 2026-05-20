Case: podmr_062_2026-05-17-063134

I used the provided Rabimodulated sequence XML and the raw numeric export. The active scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps, with 2 stored averages and 100000 repetitions. The active sequence is:

1. adj_polarize
2. detection
3. wait_for_awg
4. optional m_S=+1 reference block, skipped because full_expt = 0
5. rabi_pulse_mod_wait_time
6. detection
7. wait_for_awg

Therefore readout 1 is the bright m_S=0 reference after polarization, and readout 2 is the post-Rabi signal readout. There is no active dark-state reference readout in this run. The relevant pulse parameters are mod_depth = 1 and length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this pulse length is already on the 4 ns grid.

Quantitative expected-signal model:

For a driven two-level transition, I used

P_1(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

where f_R is the Rabi frequency in cycles/s, delta is detuning in Hz, and tau is the pulse duration. The supplied setup facts give f_R = 10 MHz at mod_depth = 1. With tau = 52 ns:

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996

The optical contrast scale between m_S=0 and m_S=+1 is about 22%, so the expected on-resonance fluorescence drop in readout 2 relative to readout 1 is:

0.22 * 0.996 = 0.219, or about 21.9%.

For a baseline near 50 raw counts, that would be an expected drop of about 11 counts, giving an on-resonance signal near 39 counts. The same model gives P_1(+/-5 MHz) = 0.749, so the expected neighboring-point drop is still about 16.5% for a resonance centered on a sampled point.

Observed normalized readout 2/readout 1:

- Mean ratio: 1.001
- Standard deviation across scan points: 0.025
- Minimum ratio: 0.937 at 3.920 GHz, a 6.3% drop
- Neighboring ratios around 3.920 GHz: 0.975 at 3.910 GHz, 1.001 at 3.915 GHz, 0.937 at 3.920 GHz, and 1.009 at 3.925 GHz

This does not match the expected resonant response. If the resonance were centered at 3.920 GHz, the model predicts ratios near 0.781 at 3.920 GHz and about 0.835 at both 3.915 GHz and 3.925 GHz before accounting for small baseline drift. The data instead show only an isolated modest low point, with adjacent points near or above unity.

I also fit the normalized ratio to a linear baseline plus the modeled resonance profile. With the physical contrast fixed at 22%, the best resonance fit was worse than a linear no-resonance baseline. Allowing the resonance amplitude to float gave only about a 3.3% fitted drop for a 3.920 GHz center, far below the 21.9% expected from the pulse parameters.

Decision: resonance_absent.
