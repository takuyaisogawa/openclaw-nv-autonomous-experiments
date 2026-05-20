Case: podmr_036_2026-05-16-211536

Input files used: inputs/sequence.xml and inputs/raw_export.json. I did not use labels, previous outputs, sibling cases, or external context.

Active sequence and readout roles:

- Sequence: Rabimodulated.xml / Rabi-modulated pODMR scan with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instruction block first runs adj_polarize followed by detection, so readout 1 is the bright m_S = 0 polarized reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The active microwave operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection, so readout 2 is the post-microwave readout.
- From the provided sequence XML and exported variable values: mod_depth = 1 and length_rabi_pulse = 52 ns. sample_rate = 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns.

Quantitative expected-signal model:

Given the supplied domain facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse of duration t = 52 ns, the resonant transition probability is

P(Delta = 0) = sin^2(pi * f_Rabi * t)
             = sin^2(pi * 10e6 * 52e-9)
             = 0.996.

With the setup contrast scale C = 0.22 between m_S = 0 and m_S = +1, the expected resonant normalized drop in readout 2 relative to readout 1 is C * P = 0.219. The mean readout 1 level is 50.985 counts, so an on-resonance point should be lower by about 11.17 counts, giving an expected readout 2 value near 39.81 counts.

Using the detuned square-pulse model,

P(Delta) = (Omega^2 / (Omega^2 + Delta^2)) * sin^2(pi * t * sqrt(Omega^2 + Delta^2)),

with Omega = 10 MHz in cycles/s, the expected transition probabilities are approximately:

- Delta = 0 MHz: P = 0.996, expected drop = 21.9%.
- Delta = 2.5 MHz: P = 0.929, expected drop = 20.4%.
- Delta = 5 MHz: P = 0.749, expected drop = 16.5%.
- Delta = 10 MHz: P = 0.273, expected drop = 6.0%.
- Delta = 20 MHz: P = 0.048, expected drop = 1.1%.

Thus a real resonance within the swept range should make a broad, line-shaped depression in readout 2 relative to readout 1, not just one noisy point.

Observed data comparison:

The combined readouts have means:

- readout 1 mean = 50.985, population standard deviation across scan = 0.793.
- readout 2 mean = 50.476, population standard deviation across scan = 0.904.
- readout 2 - readout 1 mean = -0.509 counts, with standard deviation 1.327 counts.

The normalized contrast y = (readout1 - readout2) / readout1 has:

- mean = 0.0097.
- standard deviation = 0.0261.
- maximum apparent drop = 0.0539 at 3.920 GHz.

This maximum apparent drop is about 5.4%, far below the expected 21.9% resonant drop for mod_depth = 1 and a 52 ns pulse. In counts, the largest observed drop is 2.79 counts, whereas the expected resonant drop is about 11.17 counts. The neighboring points do not show the broad detuned-pulse line shape expected from a 10 MHz Rabi rate; for example the adjacent endpoint at 3.925 GHz is a 4.2% drop, while the rest of the scan fluctuates at similar positive and negative percent-level amplitudes.

I also compared the observed normalized contrast to the physical square-pulse model over possible resonance centers in the scan range. The physical model with fixed contrast C = 0.22 fits poorly: the best physical-model squared error is about 0.060, compared with about 0.014 for a flat mean model. A free-amplitude fit prefers a negative line amplitude near -0.041 plus a small offset, which is opposite the expected sign for a pODMR dip and only about 19% of the expected contrast magnitude.

Decision:

The sequence would produce a large, broad post-microwave readout drop if a resonance were present. The data show only small scan-to-scan fluctuations and no physically consistent resonant dip. I therefore classify this case as resonance_absent.
