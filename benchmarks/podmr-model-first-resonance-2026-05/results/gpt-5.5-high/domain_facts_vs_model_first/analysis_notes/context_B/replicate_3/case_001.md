Case: podmr_004_2026-05-10-171142

Sequence and readout roles

The provided sequence XML is Rabimodulated.xml. The scan varies mw_freq from
3.825 GHz to 3.925 GHz in 5 MHz steps. The active pulse sequence first performs
adj_polarize, then detection, then wait_for_awg. This first detection is the
true m_S = 0 optical reference, so readout 1 is the reference readout.

The sequence has full_expt = 0, so the conditional block that would acquire a
separate m_S = 1 reference is skipped. After the reference, the active sequence
applies rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse,
mod_depth, switch_delay, ch_on), then performs detection. Therefore readout 2 is
the signal readout after the microwave Rabi pulse.

From the provided sequence XML and exported variable values:

- mod_depth = 1
- length_rabi_pulse = 5.2e-08 s = 52 ns
- sample_rate = 250 MHz, so the pulse is already aligned to 13 samples

Quantitative expected-signal model

The setup contrast between m_S = 0 and m_S = +1 is about 22%. The Rabi
frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth,
so here f_R = 10 MHz. For a square resonant Rabi pulse, the transferred
population is

P1(Delta) = Omega^2 / (Omega^2 + delta^2)
            * sin^2(0.5 * sqrt(Omega^2 + delta^2) * tau)

where Omega = 2*pi*10 MHz, delta = 2*pi*Delta, and tau = 52 ns.

On resonance:

P1(0) = sin^2(pi * 10e6 * 52e-9) = 0.9961.

The expected fluorescence ratio at resonance is therefore approximately

R_signal / R_reference = 1 - 0.22 * 0.9961 = 0.7809,

before allowing for a smooth multiplicative baseline. With the measured
reference mean of 43.68 raw counts, the expected resonant loss is

0.22 * 0.9961 * 43.68 = 9.57 raw counts.

The finite pulse model also predicts a broad enough feature to affect adjacent
5 MHz bins. The calculated transfer probabilities are:

- Delta = 0 MHz: P1 = 0.996, expected loss = 21.9%
- Delta = 5 MHz: P1 = 0.749, expected loss = 16.5%
- Delta = 10 MHz: P1 = 0.273, expected loss = 6.0%
- Delta = 15 MHz: P1 = 0.0117, expected loss = 0.26%

Observed data check

Using readout 1 as the local reference, the observed readout2/readout1 ratios
have:

- mean = 1.0133
- standard deviation = 0.0393
- minimum = 0.9428 at 3.855 GHz
- maximum = 1.0924 at 3.915 GHz

The largest observed negative deviation is only about 5.7%, corresponding to
2.46 raw counts, far below the expected on-resonance loss of about 21.9% or
9.57 raw counts. It is also isolated rather than having the expected square-pulse
line shape across neighboring frequency bins.

I compared the observed ratios to the fixed-contrast square-pulse resonance
model with the resonance center scanned across the measured frequency range and
a free multiplicative baseline. The best fixed-contrast resonance model had
SSE = 0.0786, while a flat ratio model had SSE = 0.0325, so the physical
resonance model fits worse than no resonance. Allowing the resonance amplitude
to float gave the best feature near 3.912 GHz with fitted drop amplitude
A = -0.061, i.e. a peak rather than a dip, with magnitude only about 28% of the
expected contrast and the wrong sign for pODMR.

Stored averages were not treated as a strong repeatability test because they can
reflect tracking cadence. The combined data and explicit pulse model are enough:
for this pulse duration and mod_depth, a real pODMR resonance should produce a
large fluorescence decrease in readout 2 relative to readout 1. That expected
signature is absent.

Decision: resonance_absent.
