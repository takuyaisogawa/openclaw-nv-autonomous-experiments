Case podmr_071_2026-05-17-084118

I used only the provided inputs in this workspace. The active sequence is Rabimodulated.xml. In the XML, the pulse program first performs adj_polarize followed by detection, which is the bright m_S = 0 reference readout. Because full_expt = 0, the optional m_S = 1 reference block is skipped. The active measurement block then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on) and performs a second detection, so readout 2 is the post-microwave-pulse signal readout. The relevant parameters are length_rabi_pulse = 5.2e-08 s, sample_rate = 250 MHz, and mod_depth = 1 in inputs/sequence.xml.

Quantitative model:
For a rectangular microwave pulse, I used the two-level Rabi transition probability

P1(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * tau * sqrt(f_R^2 + df^2))

with tau = 52 ns and f_R = 10 MHz * mod_depth. With mod_depth = 1, f_R = 10 MHz and the on-resonance transfer is

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so an on-resonance pODMR feature should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219, or about 21.9% of the bright reference. The mean bright readout is about 49.46 counts, so the expected resonant dip is about 10.8 counts in readout2 relative to readout1.

Observed data:
The paired difference readout2 - readout1 has mean -0.011 counts, standard deviation 1.47 counts, minimum -2.79 counts, and maximum +2.71 counts. The normalized ratio readout2/readout1 - 1 has mean +0.00036 and standard deviation 0.030. There is no point or broad region with a negative dip close to the expected -0.219 normalized contrast. The strongest three-point averaged negative deviation is only about -0.0217, an order of magnitude smaller than expected for mod_depth = 1.

I also fit the measured normalized difference to the Rabi line shape across possible resonance centers. A free-amplitude fit prefers a positive slope versus transition probability, not the expected negative fluorescence contrast. A fixed physical-amplitude model with -22% contrast worsens the residual error substantially compared with a flat baseline. Even under a conservative alternative mod_depth = 0.3 check, the expected on-resonance dip would be about 4.9% or 2.4 counts, and the fixed physical-amplitude model still does not improve over a flat baseline.

Decision: resonance_absent. The readouts track slow baseline variation and noise, but they do not show the sign, magnitude, or Rabi-pulse line shape expected from a pODMR resonance.
