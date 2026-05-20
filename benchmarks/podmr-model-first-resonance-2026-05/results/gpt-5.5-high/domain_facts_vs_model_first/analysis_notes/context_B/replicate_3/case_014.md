Case: podmr_033_2026-05-15-233800

Sequence interpretation

The provided sequence XML is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

The relevant parameters are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, mod_depth = 1, mw_ampl = -5 dBm, ampIQ = 5 dBm, and freqIQ = 50 MHz. The pulse length is already an integer number of 250 MHz samples: 52 ns * 250 MHz = 13 samples.

Readout roles

Because full_expt = 0, the conditional "Acquire 1 level reference" block is inactive. Therefore there are two active detections per sequence cycle:

1. Readout 1: after adj_polarize, before the swept Rabi pulse. This is the true m_S = 0 reference.
2. Readout 2: after the swept Rabi-modulated microwave pulse. This is the pODMR signal readout.

There is no independently acquired m_S = +1 reference in this run.

Expected signal model

Given the supplied setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. For a rectangular pulse, the transition probability versus detuning is

P(delta) = Omega^2 / (Omega^2 + delta^2) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau),

with Omega = 2*pi*10 MHz, delta = 2*pi*(f - f0), and tau = 52 ns.

On resonance this gives

P(0) = sin^2(pi * 10 MHz * 52 ns) = sin^2(1.6336) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant optical depletion is

0.22 * 0.996 = 0.219,

so the expected readout2/readout1 ratio on resonance is about 0.781. The mean readout 1 level is 38.46 counts, so the expected resonant readout 2 level is about 30.03 counts, a drop of about 8.43 counts.

Observed data comparison

The combined readout2/readout1 ratios are:

3.825 GHz: 0.972
3.830 GHz: 0.974
3.835 GHz: 0.991
3.840 GHz: 0.995
3.845 GHz: 1.011
3.850 GHz: 0.988
3.855 GHz: 0.998
3.860 GHz: 1.001
3.865 GHz: 0.943
3.870 GHz: 0.897
3.875 GHz: 0.749
3.880 GHz: 0.820
3.885 GHz: 0.911
3.890 GHz: 0.944
3.895 GHz: 1.043
3.900 GHz: 0.964
3.905 GHz: 0.975
3.910 GHz: 0.950
3.915 GHz: 1.018
3.920 GHz: 0.980
3.925 GHz: 0.881

The deepest point is at 3.875 GHz, where readout 1 is 38.50 and readout 2 is 28.83, giving a depletion of 25.1%. This is close to the 21.9% depletion expected for a near-pi pulse on resonance. The off-resonant readout2/readout1 ratio excluding +/-15 MHz around 3.875 GHz is 0.981 +/- 0.036, so the central dip is far outside the off-resonant scatter.

A least-squares fit of ratio = baseline - depth * P(f - f0), using the detuned Rabi model above with free baseline, depth, and center, gives center = 3.8769 GHz, baseline = 0.991, and depth = 0.212. The fitted depth is consistent with the expected 0.219 contrast-scaled resonant signal. The model SSE is 0.022 versus 0.096 for a flat-ratio model, so the resonance model explains the spectrum substantially better.

The stored per-average traces also show the central depletion, but I do not treat that as a strong independent repeatability test because stored averages can reflect tracking cadence. The decision is based primarily on the sequence-derived expected signal size and the combined readout ratio spectrum.

Decision

A pODMR resonance is present.
