Case: podmr_020_2026-05-16-165809

Sequence/readout interpretation:
- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize and immediately detect. With full_expt = 0, this is the only reference before the driven pulse, so readout 1 is the polarized m_S = 0 reference.
- The optional m_S = +1 reference block is inactive because full_expt = 0.
- The active driven measurement is rabi_pulse_mod_wait_time followed by detection, so readout 2 is the post-microwave-pulse signal.
- Active pulse duration: length_rabi_pulse = 52 ns.
- Active mod_depth: mod_depth = 1 from the provided sequence and recorded variable values.

Quantitative physical model:
For a rectangular resonant Rabi pulse, using the supplied setup calibration f_R = 10 MHz at mod_depth = 1, the transition probability is

P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * T * sqrt(f_R^2 + delta^2)).

At resonance with T = 52 ns:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the supplied m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fluorescence drop in the post-pulse readout relative to the m_S = 0 reference is

0.22 * 0.996 = 0.219, or about 22%.

In raw counts near a reference level of about 45 counts, this corresponds to an expected resonant decrease of roughly 9.9 counts. The expected normalized signal/readout ratio at resonance is about 0.781. The pulse response is broad enough that nearby sampled points would still show substantial contrast: at detunings of 2.5, 5, 7.5, and 10 MHz, the expected fractional drops are approximately 20.4%, 16.5%, 11.2%, and 6.0%.

Data calculation:
Using readout2/readout1 as the normalized post-pulse signal:
- Minimum observed ratio: 0.929 at 3.825 GHz, a 7.1% deficit.
- Maximum observed ratio: 1.040 at 3.905 GHz.
- Mean ratio: 0.986.
- Standard deviation across scan points: 0.029.

The largest observed deficit is only about one third of the on-resonance 22% drop expected from the calibrated pulse, and it occurs at the scan edge rather than as a pulse-shaped resonance feature. Several points in the high-frequency half have readout 2 greater than readout 1, which is opposite the expected fluorescence decrease from population transfer to m_S = +1.

As an explicit model check, fitting the normalized ratio to a linear baseline plus the expected rectangular-pulse dip profile did not prefer a positive dip. The best unconstrained coefficient for the physical dip term was negative, i.e. a peak-like response, while a fixed 22% dip model required a large edge feature inconsistent with the observed data. Stored averages show strong drift/tracking structure and are not treated as independent repeatability evidence.

Decision:
The expected resonant signal for the active 52 ns, mod_depth = 1 Rabi pulse is large and should be directly visible in readout2/readout1. The observed data do not contain a physically scaled dip or matching line shape. I therefore decide that a pODMR resonance is absent.
