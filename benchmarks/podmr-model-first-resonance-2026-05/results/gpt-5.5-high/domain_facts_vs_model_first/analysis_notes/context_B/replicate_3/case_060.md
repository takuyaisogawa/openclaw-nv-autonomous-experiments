Case: podmr_046_2026-05-16-235726

Sequence interpretation from inputs/sequence.xml:

- Active sequence: Rabimodulated.xml, sweeping mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 role: true m_S = 0 reference after optical polarization and before the microwave pulse.
- Readout 2 role: signal readout after the active microwave Rabi pulse.
- Active microwave pulse: rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns, mod_depth = 1, switch_delay = 100 ns.
- sample_rate = 250 MHz, so 52 ns is exactly 13 samples after rounding.

Physical model calculation:

The setup Rabi frequency is approximately 10 MHz at mod_depth = 1 and scales linearly with mod_depth, so the active pulse has f_R = 10 MHz. For a resonant rectangular Rabi pulse, the transferred population is

P(+1) = sin^2(pi * f_R * tau)

with tau = 52 ns. This gives

P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance point should therefore show a fractional PL/readout decrease of

0.22 * 0.996 = 0.219,

so readout2/readout1 should fall to about 0.781 at resonance. Including detuning with

P(+1, delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * sqrt(f_R^2 + delta^2) * tau),

the expected fractional drops are about 21.9% at zero detuning, 16.5% at 5 MHz detuning, and 6.0% at 10 MHz detuning. Because the scan step is 5 MHz, a resonance within the scanned span should normally produce a large, localized drop near at least one sampled frequency.

Observed normalized data:

- Mean readout1 = 52.16, mean readout2 = 51.12.
- Mean readout2/readout1 = 0.981.
- Minimum readout2/readout1 = 0.914 at 3.860 GHz, corresponding to an 8.6% drop.
- The largest observed deficit is far below the approximately 22% resonant expectation and does not form the expected Rabi detuned line shape.
- Several apparent dips coincide with readout1 baseline variation and the two stored averages show strong tracking-like drift, so the stored averages are not a strong independent repeatability test.

Decision:

No pODMR resonance is present in this scan. The active 52 ns, mod_depth 1 pulse should produce an almost full pi-pulse response and about a 22% normalized readout drop on resonance, but the observed normalized signal never approaches that scale and lacks the expected line shape.
