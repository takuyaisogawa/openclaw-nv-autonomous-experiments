Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The active blocks are:

1. adj_polarize, then detection: this is the first measured readout and is explicitly the true m_S = 0 reference.
2. The "Acquire 1 level reference" block is inactive because full_expt = 0.
3. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), then detection: this is the second measured readout and is the post-microwave pODMR signal.

The relevant parameters from the XML are sample_rate = 250 MHz, length_rabi_pulse = 5.2e-08 s, and mod_depth = 1. The instruction rounds the pulse length to the sample clock; 52 ns * 250 MHz = 13 samples, so the active pulse remains 52 ns.

Quantitative expected signal model

Using the supplied setup facts, the Rabi frequency at mod_depth = 1 is about f_R = 10 MHz. For a square pulse, I used the two-level transition probability

P1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),

where delta is frequency detuning in Hz and t = 52 ns. The normalized signal readout expected from the second detection relative to the m_S = 0 reference is

readout2/readout1 = 1 - C * P1(delta),

with C = 0.22 from the stated m_S = 0 to m_S = +1 contrast scale.

At zero detuning, P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996, giving an expected normalized dip of 0.22 * 0.996 = 0.219 and an expected ratio of about 0.781. The scan step is 5 MHz, so if a resonance center were inside the scanned range, the nearest sampled point would be within 2.5 MHz. Evaluating the same model over possible center positions gives a minimum sampled transition probability of about 0.929, so an in-range resonance should produce at least about 0.22 * 0.929 = 0.204 normalized contrast at one sampled point.

Data comparison

The combined readout2/readout1 ratios have mean 0.9808 and standard deviation 0.0293. The strongest observed normalized drop is at 3.860 GHz:

readout1 = 53.4423, readout2 = 48.8462, readout2/readout1 = 0.9140, contrast = 0.0860.

This is much smaller than the roughly 0.204 to 0.219 contrast expected for an in-range resonance under the active pulse parameters. A least-squares fit of the square-pulse line shape with free baseline and free contrast amplitude gives an amplitude of about 0.035, far below the expected 0.22. Forcing the expected 0.22 contrast gives a worse fit than a flat ratio model.

Decision

The active sequence and physical model predict a large, sampled pODMR dip if a resonance is present in this scan. The observed readout ratio shows only small fluctuations and no dip of the expected size or line shape. I therefore classify this case as resonance_absent.
