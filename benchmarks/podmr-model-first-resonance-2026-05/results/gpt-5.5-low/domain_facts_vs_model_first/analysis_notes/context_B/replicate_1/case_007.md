Case podmr_011_2026-05-11-181506.

I used the provided sequence XML and raw export only. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The variables used for the saved run give length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, delay_wrt_1mus = 0.2 us, wait_time = 2 us, and pumping_time = 1 us.

Readout roles from the instructions:

- The first detection follows adj_polarize directly, so readout 1 is the optically polarized m_S = 0 reference.
- The "Acquire 1 level reference" block is disabled because full_expt = 0.
- The active swept measurement then applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection, so readout 2 is the post-microwave-pulse signal.

Physical model calculation:

Given the domain facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a resonant rectangular Rabi pulse, the transferred population is approximated by

P_transfer = sin^2(pi * f_Rabi * t_pulse).

With f_Rabi = 10 MHz and t_pulse = 52 ns,

pi * f_Rabi * t_pulse = pi * 10e6 * 52e-9 = 1.6336 rad,
P_transfer = sin^2(1.6336) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional fluorescence drop in the post-pulse readout relative to the polarized reference is

0.996 * 0.22 = 0.219, or about 21.9%.

Quantitative comparison to the combined readouts:

- At 3.880 GHz, readout 1 = 21.346 and readout 2 = 16.981.
- The ratio readout2/readout1 is 0.7955, corresponding to a 20.45% drop.
- This is close to the expected 21.9% resonant drop.
- Off the central feature, the edge-point mean ratio is about 0.994 with population-scale scatter about 0.034, while the central five points from 3.865 to 3.885 GHz average ratio about 0.874 and form a clear dip.
- The per-average overlays mainly show drifting/tracking cadence structure, so I did not treat the two averages as a strong independent repeatability test.

Decision: the post-pulse readout has a central dip with amplitude matching the explicit Rabi/contrast model for this pulse and modulation depth. A pODMR resonance is present.
