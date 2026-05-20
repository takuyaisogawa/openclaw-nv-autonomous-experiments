Sequence and readout interpretation

The active sequence is Rabimodulated.xml. It first polarizes the NV and performs a detection, then waits. Because full_expt = 0, the optional "1 level reference" block is inactive. The only microwave manipulation before the second detection is:

PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on);

Therefore readout 1 is the polarized m_S = 0 reference, and readout 2 is the post-Rabi-pulse pODMR signal. The scanned variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The relevant pulse parameters from the provided sequence/export values are mod_depth = 1 and length_rabi_pulse = 52 ns.

Expected quantitative signal model

Given the provided setup facts, the Rabi frequency is about 10 MHz at mod_depth = 1. Treating this as the on-resonance Rabi frequency in cycles/s, the resonant rotation angle is:

theta = 2*pi*(10 MHz)*(52 ns) = 3.267 rad = 187.2 deg.

The expected resonant population transferred from m_S = 0 to m_S = +1 is:

P(+1) = sin^2(theta/2) = sin^2(1.6336) = 0.996.

With a 22% m_S = 0 to m_S = +1 fluorescence contrast, the expected resonant readout-2 loss relative to readout 1 is:

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout-1 level is 46.76 counts, so the expected on-resonance drop is:

46.76 * 0.219 = 10.25 counts.

This is the relevant physical scale for deciding whether a resonance is present. A detuned Rabi model would broaden and reduce the response away from resonance, but at or near the resonance within this 5 MHz-spaced scan a near-pi 52 ns pulse should still produce a large local loss, not a one-to-three-count fluctuation.

Observed data check

The combined readout means are:

readout 1 mean = 46.76
readout 2 mean = 46.83
mean(readout2 - readout1) = +0.07 counts

The largest apparent loss is at 3.890 GHz:

readout 1 = 47.52
readout 2 = 44.25
loss = 3.27 counts = 6.88%

Other negative excursions are smaller, for example 4.91% at 3.850 GHz and 4.23% at 3.830 GHz. Positive excursions of comparable size are also present, including +4.97% at 3.885 GHz and +4.81% at 3.905 GHz. The standard deviation of readout2 - readout1 over scan points is 1.48 counts, while the expected resonant loss from the model is about 10.25 counts. The stored averages also show large tracking-like offsets between averages, so they do not constitute a strong independent repeatability test.

Decision

Using the active sequence and the quantitative near-pi-pulse model, a real pODMR resonance should create a large readout-2 fluorescence decrease relative to readout 1. The observed scan only has small, non-systematic readout differences with positive and negative excursions of similar size. I therefore decide that a pODMR resonance is absent in this case.
