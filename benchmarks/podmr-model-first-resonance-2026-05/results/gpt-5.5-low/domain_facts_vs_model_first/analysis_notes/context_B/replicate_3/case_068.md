Sequence and roles

The active sequence is Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instructions first polarize and detect, giving the true mS = 0 reference readout. Because full_expt = 0, the intermediate mS = 1 reference block is inactive. The sequence then applies one rabi_pulse_mod_wait_time pulse and performs the second detection, so readout 1 is the bright reference and readout 2 is the post-Rabi pODMR signal readout.

Active pulse parameters from the saved run are mod_depth = 1 and length_rabi_pulse = 52 ns. With the supplied setup calibration, the Rabi frequency is approximately 10 MHz at mod_depth = 1. For a resonant driven two-level transition, the transfer probability after a square pulse is

P(ms=+1) = sin^2(pi * f_Rabi * t).

Using f_Rabi = 10 MHz and t = 52 ns gives pi * f_Rabi * t = 1.6336 rad and P = 0.996. The setup contrast between mS = 0 and mS = +1 is about 22%, so a true resonance should reduce the post-pulse readout relative to the bright reference by approximately 0.22 * 0.996 = 21.9%.

Observed quantitative comparison

The combined readout means are 42.52 for readout 1 and 42.27 for readout 2. Pointwise normalized contrast 1 - readout2/readout1 has mean 0.55%, standard deviation 2.76%, minimum -5.59%, and maximum +5.32%. The largest apparent drop is therefore only about 5.3%, roughly one quarter of the expected resonant signal, and it is isolated rather than a coherent resonance feature. The values near the nominal center are also not dip-like: at 3.875 GHz contrast is +1.45%, at 3.880 GHz it is -5.59%, at 3.885 GHz it is +2.44%, and at 3.890 GHz it is +0.31%.

The stored per-average overlays show substantial slow baseline drift between averages, consistent with tracking cadence rather than an independent repeatability test. This drift changes both readouts together and does not create a stable pODMR-sized contrast feature.

Decision

Given the active near-pi pulse, a real pODMR resonance should be a large approximately 22% reduction in the second readout relative to the mS = 0 reference. The measured normalized signal is centered near zero and never approaches the expected amplitude. I therefore decide that no pODMR resonance is present.
