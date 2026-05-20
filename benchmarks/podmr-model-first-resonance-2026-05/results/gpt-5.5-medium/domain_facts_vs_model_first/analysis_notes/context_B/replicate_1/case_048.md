Case: podmr_034_2026-05-16-204545

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:

- The provided XML is Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection.
- length_rabi_pulse is 5.2e-08 s. At sample_rate = 250 MHz this remains 52 ns after rounding.
- mod_depth in the provided sequence XML is 1.
- full_expt is 0, so the optional m_S = +1 reference block is inactive.
- Therefore readout 1 is the bright m_S = 0 reference after optical polarization and before the swept Rabi pulse. Readout 2 is the post-microwave readout that should dip at resonance if the pulse drives m_S = 0 to m_S = +1.

Physical signal model:

Given the domain facts, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a square pulse with detuning delta, I used

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau)

with f_R = 10 MHz and tau = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast between m_S = 0 and m_S = +1 is about 22 percent, so a resonant pulse should reduce the second readout by approximately

0.22 * 0.996 = 0.219

of the bright fluorescence. With the observed readout-1 baseline near 50.02 counts, the expected resonant dip is about 10.96 counts.

For reference, the same model gives expected count dips of about 10.22 counts at 2.5 MHz detuning, 8.24 counts at 5 MHz detuning, 3.00 counts at 10 MHz detuning, and 0.53 counts at 20 MHz detuning. With a 5 MHz scan step, a resonance inside the scanned range should normally create at least one very large depressed readout-2 point.

Observed data:

- mean(readout 1) = 50.016 counts.
- mean(readout 2) = 49.366 counts.
- mean(readout 2 - readout 1) = -0.649 counts.
- stdev(readout 2 - readout 1) = 1.286 counts.
- The most negative readout 2 - readout 1 value is -2.654 counts.
- The minimum readout 2 value is 47.538 counts at 3.905 GHz.

I also fit the measured readout difference to an offset plus the model-shaped resonance dip with free center and amplitude. The best-fit dip amplitude was about 1.53 counts, much smaller than the approximately 10.96 counts expected from the pulse parameters and contrast. A fixed expected-amplitude model fits much worse than a constant offset model.

Decision:

The expected pODMR signal for the active sequence is a large post-pulse fluorescence dip near resonance. The observed second readout does not contain a model-consistent dip of the required scale, and the small fluctuations are compatible with readout noise/tracking variation rather than a driven resonance. I therefore classify this case as resonance_absent.
