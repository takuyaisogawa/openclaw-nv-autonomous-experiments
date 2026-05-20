Case podmr_026_2026-05-16-182622

Sequence interpretation:

The provided XML is Rabimodulated.xml. The active microwave operation is:

PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on)

with length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and switch_delay = 100 ns. The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

The sequence first polarizes and detects before the microwave pulse. Because full_expt = 0, the optional "1 level reference" block is skipped. Therefore the two stored readouts are:

- readout 1: bright m_S = 0 reference after optical polarization, before the Rabi pulse.
- readout 2: post-microwave signal after the 52 ns modulated Rabi pulse.

Quantitative physical model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1. For a square pulse, the transferred population is modeled as

P_1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2))

using f_R and Delta in cycles/s. The fluorescence contrast expected from this transferred population is C(Delta) = 0.22 * P_1(Delta), using the stated 22% m_S = 0 to m_S = +1 contrast scale.

For f_R = 10 MHz and t = 52 ns:

- On resonance: P_1 = sin^2(pi * 10e6 * 52e-9) = 0.9961, so expected contrast = 0.2191, about a 21.9% drop in readout 2 relative to readout 1.
- At 2.5 MHz detuning, representative of the worst nearest-grid offset for a 5 MHz scan step, the expected contrast remains about 20%.
- At 5 MHz detuning, expected contrast is about 16.5%.
- At 10 MHz detuning, expected contrast is about 6.0%.

Thus a true resonance inside the swept range should produce a large readout-2 dip relative to readout 1 at at least one sampled frequency, normally around 20% on the nearest scan point.

Data comparison:

Using normalized contrast 1 - readout2/readout1 from the combined raw readouts:

- mean contrast = 0.00007
- standard deviation across scan points = 0.0296
- maximum positive contrast = 0.0594 at 3.835 GHz
- minimum contrast = -0.0654 at 3.830 GHz

The largest apparent dip is only about 5.9%, far below the approximately 20-22% dip expected for this pulse if a resonance were present in the scan. A least-squares matched line-shape comparison against the Rabi model gives a best-fit amplitude of only about 0.20 times the expected physical amplitude and is dominated by point-to-point noise rather than a coherent resonance profile. The two stored averages also do not provide a strong independent repeatability check here, and their largest contrast excursions occur at different points.

Decision:

Given the active sequence, readout roles, mod_depth = 1, and 52 ns pulse duration, the expected resonant pODMR signal is much larger than the observed readout-2/readout-1 variations. The data do not show a physically consistent pODMR resonance.
