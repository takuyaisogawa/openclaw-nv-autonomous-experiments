Case podmr_046_2026-05-16-235726

Sequence and readout roles

The provided sequence is Rabimodulated.xml. The active path has full_expt = 0, so the optional "1 level reference" block is skipped. The executed detection windows are:

1. adj_polarize for 1 us, then detection: readout 1 is the polarized m_S = 0 reference.
2. wait_for_awg for 2 us.
3. rabi_pulse_mod_wait_time with length_rabi_pulse and mod_depth.
4. detection: readout 2 is the post-Rabi-pulse signal.
5. wait_for_awg for 1 us.

The relevant pulse settings are sample_rate = 250 MHz, length_rabi_pulse = 52 ns, rounded to 13 samples, mod_depth = 1, switch_delay = 100 ns, and mw_freq is scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps. The adiabatic inversion setting is not active because the full_expt block is skipped.

Quantitative physical expectation

Using the supplied calibration, the Rabi frequency at mod_depth = 1 is f_R = 10 MHz. For a rectangular pulse, the driven transition probability versus detuning is

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

With t = 52 ns:

P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.

The supplied fluorescence contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance point should reduce the post-pulse fluorescence by about 0.22 * 0.996 = 21.9% relative to the readout-1 reference. Because the scan spacing is 5 MHz, a resonance centered halfway between two sampled points is at most 2.5 MHz from the nearest sampled point. The same model gives P(2.5 MHz) = 0.929, corresponding to an expected 20.4% dip. At 5 MHz detuning the expected dip is still 16.5%.

Data comparison

The combined raw means are:

readout 1 mean = 52.157
readout 2 mean = 51.123
readout 2 / readout 1 mean = 0.9808
minimum readout 2 / readout 1 = 0.9140 at 3.860 GHz

If a pODMR resonance were present anywhere on this 5 MHz grid with the active 52 ns, mod_depth = 1 pulse, the normalized ratio should reach roughly 0.76 to 0.78 at the nearest sampled point after allowing for the 22% contrast. The observed minimum ratio is only a 8.6% reduction, and the apparent dips are not repeatable across the two stored averages: the lowest point in average 1 occurs at 3.915 GHz, while the lowest point in average 2 occurs at 3.925 GHz. Since stored averages can track cadence drift, this is not an independent repeatability test, but it also does not support a stable resonance.

I also fit the normalized data to the same rectangular-pulse line shape. The best unconstrained fit preferred a negative contrast amplitude, meaning a peak rather than a dip, while forcing the expected 22% contrast made the residual substantially worse than a flat baseline. This is inconsistent with a real pODMR resonance under the active pulse conditions.

Decision

The expected resonant signal is a large, grid-robust fluorescence dip of about 20% to 22%, but the data show only small baseline-level fluctuations. I decide that a pODMR resonance is absent.
