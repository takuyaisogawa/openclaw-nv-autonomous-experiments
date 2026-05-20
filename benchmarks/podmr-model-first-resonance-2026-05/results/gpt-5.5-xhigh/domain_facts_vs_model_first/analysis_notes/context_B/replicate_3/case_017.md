Active sequence and readout roles

The provided sequence XML is Rabimodulated.xml with the scan varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. The active instruction flow first polarizes optically and immediately performs detection, so readout 1 is the true m_S = 0 optical reference. The block labelled "Acquire 1 level reference" is inactive because full_expt = 0. After the reference, the sequence applies rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth, then performs detection, so readout 2 is the signal after the microwave Rabi pulse.

The relevant pulse settings from the provided XML are:
- sample_rate = 250 MHz
- length_rabi_pulse = 52 ns, already on a 4 ns sample grid
- mod_depth = 1
- no active adiabatic inversion or separate m_S = +1 reference readout

Expected signal model

Using the supplied setup facts, the Rabi frequency is approximately

f_R = 10 MHz * mod_depth = 10 MHz.

For a rectangular microwave pulse, the two-level transfer probability as a function of detuning delta is

P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

For t = 52 ns and f_R = 10 MHz, the on-resonance transfer is

P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence reduction is

0.22 * 0.996 = 0.219, or about a 22% drop relative to the 0-reference level.

Quantitative comparison to data

I normalized the signal readout by the reference readout at each scan point: q = readout2 / readout1. I then fit the fixed-physics model

q(f) = a * (1 - 0.22 * P_1(f - f0))

with only the off-resonant scale a and resonance frequency f0 free.

The best fit gave:
- f0 = 3.877415 GHz
- a = 0.9863
- model minimum ratio = 0.7838
- constant-ratio null model q = 0.9470
- null SSE = 0.1513
- Rabi-model SSE = 0.0477
- SSE reduction versus null = 68%

The observed normalized ratios around the fitted resonance are:
- 3.870 GHz: 0.8847
- 3.875 GHz: 0.7627
- 3.880 GHz: 0.7074
- 3.885 GHz: 0.9013

The minimum observed ratio is 0.7074 at 3.880 GHz. Relative to the off-feature median ratio, this is about a 28% dip. That is somewhat deeper than the nominal 22% contrast scale, but it is localized at the fitted resonance and has the width expected from a 52 ns near-pi pulse. Stored per-average traces are not treated as a strong independent repeatability test, but the combined readouts alone show a quantitatively compatible pODMR feature.

Decision

A pODMR resonance is present.
