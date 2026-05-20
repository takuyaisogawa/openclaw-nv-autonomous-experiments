Case podmr_006_2026-05-16-011837.

I used the provided inputs/sequence.xml to identify the active sequence. The sequence is Rabimodulated-style pODMR with mw_freq scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The instruction block first optically polarizes and detects, so readout 1 is the bright m_S = 0 reference. full_expt = 0, so the optional m_S = +1 reference block is skipped. The active pODMR signal is readout 2, acquired after rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).

Pulse parameters from the provided sequence XML:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so the 52 ns pulse is exactly 13 samples and is not changed by the round(length_rabi_pulse*sample_rate)/sample_rate operation

Quantitative physical model:

The supplied setup scale gives Rabi frequency f_R = 10 MHz at mod_depth = 1. For a square pulse, the on-resonance spin-transfer probability is

P = sin^2(pi * f_R * t).

With f_R = 10e6 Hz and t = 52e-9 s:

pi * f_R * t = 1.6336 rad
P = sin^2(1.6336) = 0.9961

The expected fluorescence suppression on resonance is therefore approximately

0.22 * 0.9961 = 0.2191, or 21.9%.

Measured data check:

The off-resonance readout 2 baseline, excluding the central dip region, is about 38.61 counts. The minimum readout 2 is 30.79 counts at 3.880 GHz, giving a baseline-referenced drop of

(38.61 - 30.79) / 38.61 = 0.203, or 20.3%.

Using the bright reference around the dip, the mean readout 1 at 3.875 and 3.880 GHz is 41.00 counts and the mean readout 2 is 31.33 counts, giving

1 - 31.33 / 41.00 = 0.236, or 23.6%.

I also evaluated the detuned square-pulse two-level model

P(f) = (Omega^2 / (Omega^2 + delta^2)) * sin^2(0.5 * sqrt(Omega^2 + delta^2) * t),

with Omega = 2*pi*10 MHz, contrast fixed at 0.22, pulse length fixed at 52 ns, and only a readout scale plus resonance center fit to readout2/readout1. A grid search found the best center near 3.878 GHz. The resonance model reduced SSE from 0.1049 for a constant ratio model to 0.0164, an improvement factor of about 6.4. The model minimum ratio at sampled points was 0.785, close to the observed minimum ratio of 0.762.

Decision:

The central suppression near 3.875-3.880 GHz has the amplitude expected for an almost pi pulse at mod_depth = 1 and is much larger than baseline scatter. This is consistent with a pODMR resonance being present.
