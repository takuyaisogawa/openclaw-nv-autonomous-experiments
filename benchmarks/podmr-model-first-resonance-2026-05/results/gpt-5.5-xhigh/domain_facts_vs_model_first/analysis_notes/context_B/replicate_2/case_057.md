I used the provided sequence XML and raw export only.

Active sequence and readout roles:

- Sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence first runs adj_polarize followed by detection. This first active detection is the bright m_S = 0 reference readout.
- full_expt = 0, so the optional "1 level reference" block is inactive; no adiabatic inversion or separate dark reference readout is acquired.
- The active pODMR manipulation is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, and switch_delay = 100 ns, followed by the second detection. This second active detection is the post-microwave signal readout.

Quantitative expected-signal calculation:

The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1. For a square microwave pulse with duration t = 52 ns, I used the standard driven two-level transition probability

P_flip(Delta) = f_R^2 / (f_R^2 + Delta^2) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

with f_R and Delta in cycles/s. On resonance this gives

P_flip(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated 22% contrast scale between m_S = 0 and m_S = +1, a resonant point should therefore reduce the post-pulse fluorescence by

0.22 * 0.996 = 0.219, or about 21.9% of the bright reference.

The measured bright reference mean is 47.11 counts, so the expected on-resonance post-pulse value is approximately

47.11 * (1 - 0.219) = 36.79 counts,

a drop of about 10.32 counts. Because the scan spacing is 5 MHz, even a resonance exactly halfway between sampled points would put the nearest sampled point only 2.5 MHz detuned. The same model gives P_flip(2.5 MHz) = 0.929, implying a still-large expected drop of about 20.4%, or about 9.63 counts.

Observed data comparison:

- Combined readout 1 mean: 47.11 counts.
- Combined readout 2 mean: 47.55 counts.
- readout2/readout1 ranges from 0.976 to 1.041, with mean 1.009.
- The largest observed negative readout2 - readout1 excursion is -1.19 counts, far smaller than the approximately 9.6 to 10.3 count drop expected for a resonant pi-like pulse.
- A fixed Rabi-line-shape least-squares comparison on readout2/readout1 gives a best unconstrained feature with positive sign, not a dip. The best constrained negative dip is about 4.8%, well below the approximately 22% physical expectation, and forcing the expected -22% dip substantially worsens the fit.

The stored averages differ in baseline as expected for tracking cadence, and I did not treat them as a strong independent repeatability test. They do not show a physically sized resonant decrease in the post-microwave readout either.

Decision: resonance_absent.
