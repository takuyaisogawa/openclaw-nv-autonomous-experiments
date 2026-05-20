Case podmr_040_2026-05-16-222642

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles

The provided XML is Rabimodulated.xml. The active path is:

1. adj_polarize
2. detection
3. wait_for_awg
4. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay)
5. detection
6. wait_for_awg(length_last_wait)

The "Acquire 1 level reference" block is inactive because full_expt = 0. The do_adiabatic_inversion flag is therefore not part of the active pulse path. Readout 1 is the true mS = 0 reference taken immediately after polarization. Readout 2 is the signal readout after the modulated Rabi pulse.

Pulse settings from the XML and exported variable values:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so 52 ns is exactly 13 samples after rounding
- scan: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps

Quantitative model

Given the domain facts, the Rabi frequency at mod_depth = 1 is about f_R = 10 MHz. For a square pulse, I used

P_transfer(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * T * sqrt(f_R^2 + df^2))

with T = 52 ns. The normalized fluorescence signal expected after the pulse is approximately

signal/reference = baseline * (1 - 0.22 * P_transfer(df)).

This gives:

- df = 0 MHz: P_transfer = 0.996, expected depletion = 21.9%
- df = 2.5 MHz: P_transfer = 0.929, expected depletion = 20.4%
- df = 5 MHz: P_transfer = 0.749, expected depletion = 16.5%
- df = 10 MHz: P_transfer = 0.273, expected depletion = 6.0%

Because the scan step is 5 MHz, any resonance inside the scanned range should be within at most 2.5 MHz of a measured point, so the nearest measured point should show roughly a 20% signal/reference dip. If the resonance lands exactly on a measured point, that point should be near 0.78 of the reference, with adjacent points still around a 16% depletion.

Observed normalized signal

I normalized readout 2 by readout 1 at each frequency. The ratio mean is 0.9892, point-to-point standard deviation is 0.0276, and the smallest ratio is 0.9237 at 3.885 GHz, corresponding to only a 7.6% depletion. The local ratios around that point are:

- 3.875 GHz: 0.9972
- 3.880 GHz: 0.9774
- 3.885 GHz: 0.9237
- 3.890 GHz: 0.9753
- 3.895 GHz: 1.0158

This is an isolated small fluctuation, not the broad near-pi-pulse depletion expected from the model. In absolute counts, the mean reference is 47.19 counts, so a resonant pi pulse at 22% contrast should reduce the signal by about 9.6 to 10.3 counts at the nearest sampled point. The largest observed negative readout2-readout1 difference is only 3.69 counts.

As an explicit model comparison, a constant no-resonance ratio has SSE = 0.01598 on the normalized data. The best fixed-contrast resonance model with a resonance constrained inside the scan gives a worse SSE = 0.06298, with the model requiring a minimum predicted ratio near 0.796 that is absent from the data.

Decision

The active pulse is strong enough that an in-range pODMR resonance should produce a large, sampled depletion. The measured readout-2/readout-1 ratios do not show that expected feature. I therefore classify this case as resonance_absent.
