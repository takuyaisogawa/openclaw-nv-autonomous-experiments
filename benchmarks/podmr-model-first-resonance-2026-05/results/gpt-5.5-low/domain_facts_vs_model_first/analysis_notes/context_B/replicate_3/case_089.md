Case podmr_075_2026-05-17-093901

I used only the provided isolated files. The sequence is Rabimodulated.xml. In the active instructions, the experiment first polarizes and detects the bright m_S = 0 reference, then because full_expt = 0 it skips the separate m_S = 1 reference block, then applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, followed by the second detection. Thus readout 1 is the true 0-level / bright reference and readout 2 is the post-microwave signal readout.

Relevant pulse parameters from the sequence/variable values:
- length_rabi_pulse = 52 ns
- mod_depth = 1
- mw_freq is swept from 3.825 GHz to 3.925 GHz in 5 MHz steps
- sample_rate = 250 MHz, so 52 ns rounds to 52 ns

Quantitative expected-signal model:
The setup Rabi frequency is approximately 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant square pulse, the transferred population is

P_transfer = sin^2(pi * f_Rabi * t)

With f_Rabi = 10 MHz and t = 52 ns:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996

The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should reduce the post-pulse signal readout by approximately

0.22 * 0.996 = 0.219, or 21.9% of the bright baseline.

At the observed baseline near 50 raw-count units, the expected resonant dip in readout 2 relative to readout 1 is therefore about 10.96 counts. This is a direct quantitative model calculation for the active pulse, not a qualitative expectation.

Observed data check:
- mean readout 1 = 50.523
- mean readout 2 = 50.390
- mean(readout2 - readout1) = -0.133 counts
- standard deviation of pointwise differences = 1.187 counts
- most negative pointwise difference = -2.442 counts at 3.830 GHz
- readout2/readout1 mean = 0.9975
- minimum readout2/readout1 = 0.9509 at 3.830 GHz

The largest negative fluctuation is only about 4.9% of the local reference and is about 2.1 standard deviations of the observed pointwise difference scatter. It is also far smaller than the approximately 22% / 11-count resonant signal expected from the active 52 ns, mod_depth 1 pulse. The scan instead shows slow baseline drift and small readout-to-readout fluctuations, with no coherent pODMR dip of the expected amplitude.

Decision: resonance_absent.
