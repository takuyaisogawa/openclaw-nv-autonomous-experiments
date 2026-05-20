Active sequence and readout roles

The provided sequence is Rabimodulated.xml. The instructions first polarize the NV and perform detection, which is the true m_S = 0 reference readout. The block that would acquire an m_S = 1 reference is guarded by full_expt, and full_expt = 0, so it is inactive. The active measurement then applies rabi_pulse_mod_wait_time followed by detection; this second readout is the pODMR signal after the microwave pulse.

Relevant pulse parameters

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s, rounded at 250 MS/s to 52 ns
- frequency scan: 3.825 GHz to 3.925 GHz in 5 MHz steps
- readout 1: m_S = 0 reference
- readout 2: post-Rabi-pulse signal

Quantitative physical expectation

Using the provided setup calibration, the Rabi frequency at mod_depth = 1 is about 10 MHz. For a resonant square pulse with duration t = 52 ns, the driven transition probability is

P = sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With an m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance point should reduce the signal readout by approximately

delta = baseline * 0.22 * P.

The observed readout-1 baseline mean is 42.670 counts, so the expected resonant drop is

42.670 * 0.22 * 0.996 = 9.35 counts,

giving an expected resonant readout-2 value near 33.32 counts. Even if the true resonance were halfway between scan points, with a 2.5 MHz detuning from the nearest sampled point, the square-pulse model gives P = 0.929 and an expected drop of 8.72 counts. At 5 MHz detuning the expected drop remains about 7.03 counts.

Observed data check

The measured combined readout statistics are:

- readout 1 mean = 42.670, sd = 0.852, min = 41.135, max = 44.750
- readout 2 mean = 42.108, sd = 0.720, min = 41.058, max = 43.538
- readout2 - readout1 mean = -0.562, sd = 1.100, min = -2.865, max = 1.519
- readout2 / readout1 mean = 0.987, sd = 0.025, min = 0.936

The lowest readout-2 point is 41.058 counts at 3.870 GHz, with readout-1 = 42.885 counts and a ratio of 0.957. This is only a small fluctuation relative to the expected resonant ratio near 0.781. No scan point shows the large 7-9 count suppression predicted by the active pulse model.

Decision

A pODMR resonance is absent in this scan. The active pulse would produce a large, easily visible dip if resonant within or near the sampled frequency range, but the observed readout-2 trace stays close to the m_S = 0 reference with only small count-level fluctuations.
