Case: podmr_005_2026-05-16-010352

Sequence interpretation

The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The sequence first polarizes the NV, then performs detection before any microwave pulse; this first readout is therefore the bright m_S = 0 reference. Because full_expt = 0, the conditional "1 level reference" block is inactive, so there is no separate dark-state reference readout. The sequence then applies one rabi_pulse_mod_wait_time pulse and performs detection again; this second readout is the post-microwave pODMR signal.

The provided sequence XML and exported variable values give length_rabi_pulse = 52 ns and mod_depth = 1. The embedded XML string inside raw_export.json contains mod_depth = 0.3, but the file inputs/sequence.xml and Variable_values both indicate mod_depth = 1, so I use mod_depth = 1 for the decision as requested.

Physical model calculation

Use the two-level resonant Rabi model for the driven m_S = 0 to m_S = +1 transition:

P_transfer(on resonance) = sin^2(pi * f_R * tau)

For this setup, f_R is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. With mod_depth = 1 and tau = 52 ns:

f_R = 10 MHz
tau = 52 ns
P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996

The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so the expected fractional fluorescence drop on resonance is:

0.22 * 0.996 = 0.219, or about 21.9%

The off-resonance first-readout median is about 38.88 raw counts, giving an expected on-resonance drop of about:

38.88 * 0.219 = 8.52 raw counts

Observed data comparison

The first readout is mostly flat near 39 counts and does not show a comparable dip. The second readout has a strong localized dip:

- At 3.875 GHz: readout 1 = 40.96, readout 2 = 30.63, drop = 10.33 counts, fractional drop = 25.2%.
- At 3.880 GHz: readout 1 = 39.19, readout 2 = 30.33, drop = 8.87 counts, fractional drop = 22.6%.
- At 3.885 GHz: readout 1 = 39.06, readout 2 = 33.65, drop = 5.40 counts, fractional drop = 13.8%.

The strongest observed drop is the correct sign for microwave-driven population transfer out of m_S = 0, is localized in frequency, and has the expected size from the Rabi/contrast calculation. The two stored averages both show the dip around 3.875-3.880 GHz, but I treat those averages mainly as consistency with the tracking cadence rather than as a strong independent repeatability test.

Decision

A pODMR resonance is present.
