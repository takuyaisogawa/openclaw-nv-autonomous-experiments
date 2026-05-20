Case: podmr_080_2026-05-17-105113

Sequence and readout roles

The provided sequence is Rabimodulated.xml. The active instruction path is:

1. adj_polarize(...)
2. detection(...)
3. wait_for_awg(...)
4. skip the "Acquire 1 level reference" block because full_expt = 0
5. rabi_pulse_mod_wait_time(..., length_rabi_pulse, mod_depth, ...)
6. detection(...)

Therefore the two stored readouts are not independent ODMR channels. Readout 1 is the direct post-polarization optical readout, i.e. the bright m_S = 0 reference. Readout 2 is the readout after the active microwave Rabi pulse, i.e. the pODMR signal readout. The sequence includes code for an m_S = 1 reference, but it is inactive because full_expt is zero.

Relevant pulse settings

The active microwave pulse is length_rabi_pulse = 52 ns and mod_depth = 1. The scan variable is mw_freq, swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The setup Rabi frequency is approximately 10 MHz at mod_depth = 1, so the active pulse is approximately a pi pulse.

Explicit signal model

I model the driven NV spin transition as a two-level Rabi pulse with detuning Delta and on-resonance Rabi frequency f_R = 10 MHz. The transition probability after pulse duration tau is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * tau * sqrt(f_R^2 + Delta^2)).

At resonance, tau = 52 ns gives

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.

With the stated bright-to-dark contrast scale of about 22%, the expected resonant fractional fluorescence drop in the signal readout relative to the m_S = 0 readout is therefore

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout-1 level is 51.67 counts, so a resonant pi-pulse pODMR feature should produce an approximately 11.3 count drop in readout 2 relative to readout 1 near resonance, modulo slow tracking offsets.

Observed data comparison

Using readout2/readout1 as the reference-normalized signal, the mean ratio is 1.0007. The deepest observed normalized drop is at 3.895 GHz:

readout1 = 52.25
readout2 = 50.44
ratio = 0.9654
drop = 3.46%

This is far smaller than the 21.9% expected resonant drop. In count units, the largest signal-reference deficit is 1.81 counts, compared with the approximately 11.3 counts expected from the physical model.

I also compared a flat normalized signal to a resonance-dip model with the above Rabi response. A best unconstrained resonance-shaped least-squares fit prefers a negative contrast amplitude, meaning it fits a small peak rather than a dip. A model constrained to the physical 22% contrast gives a substantially worse residual than a flat trace. The stored per-average traces vary strongly with tracking cadence and do not provide a strong independent repeatability check, but the combined readouts themselves do not show the large, physically expected pODMR feature.

Decision

No pODMR resonance is present in this scan.
