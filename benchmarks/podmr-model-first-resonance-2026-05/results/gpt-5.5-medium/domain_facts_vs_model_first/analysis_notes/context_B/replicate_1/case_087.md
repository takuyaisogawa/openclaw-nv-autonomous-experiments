<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_087.

I used the provided sequence XML to identify the active experiment. The sequence is Rabimodulated.xml. The instruction path is:

1. adj_polarize for 1 us.
2. detection immediately after polarization: this is the true m_S = 0 reference readout.
3. The optional m_S = 1 reference branch is skipped because full_expt = 0.
4. rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
5. detection after the microwave pulse: this is the pODMR signal readout.

Thus readout 1 is the m_S = 0 reference and readout 2 is the microwave-pulse signal. The relevant physical signal is not an arbitrary line in either raw trace, but a dip of readout 2 relative to readout 1 when the microwave pulse is resonant.

Quantitative model:

For a square resonant Rabi pulse, the spin transfer probability is

P(delta) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(pi * t * sqrt(Omega^2 + delta^2)),

using Omega and delta in cycles/s. The setup facts give Omega approximately 10 MHz at mod_depth = 1, and the active pulse duration is t = 52 ns. On resonance,

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce the signal readout by about 0.22 * 0.996 = 21.9% relative to the m_S = 0 reference. With the observed reference mean near 50.17 raw counts, the expected resonant dip is about 10.99 raw counts, putting readout 2 near 39.2 counts at resonance.

Observed data:

The combined readout means are readout 1 = 50.17 and readout 2 = 50.04. The pointwise difference readout2 - readout1 has mean -0.12 counts and sample standard deviation 1.09 counts. The largest observed negative difference is -2.52 counts at 3.855 GHz, far smaller than the approximately -11 count dip expected for a resonant near-pi pulse. The normalized contrast (readout1 - readout2) / readout1 has mean 0.22%, sample standard deviation 2.17%, and maximum 4.96%, whereas the expected resonant contrast is about 21.9%.

I also fit the expected Rabi line shape across possible resonance centers within the scan. A free-amplitude fit gives a best amplitude of about 2.3% contrast, close to the noise scale and about one tenth of the expected 22% contrast. Forcing the physical 22% amplitude makes the residual much worse than a flat null model, so the data do not support the expected pODMR response.

Stored averages are not treated as a strong independent repeatability test here, but they also do not show a coherent 22% resonant dip. The small isolated raw excursions are compatible with tracking/noise-scale variation, not the active sequence's expected near-pi pODMR signal.

Decision: resonance_absent.
