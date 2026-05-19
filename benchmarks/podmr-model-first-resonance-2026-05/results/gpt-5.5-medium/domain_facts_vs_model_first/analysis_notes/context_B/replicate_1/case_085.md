<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_085.

I used the supplied sequence XML and the raw readout export only.

Active sequence and readout roles:

- Sequence: Rabimodulated.xml / Rabimodulated pulse sequence, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- The first detection after adj_polarize is the true m_S = 0 reference readout.
- The second active detection is after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, ...), so it is the pODMR signal readout.
- length_rabi_pulse = 52 ns.
- mod_depth = 1.

Physical model calculation:

For resonant microwave driving, the transferred population after a square Rabi pulse is

P_flip = sin^2(pi * f_Rabi * tau).

Using the given setup calibration f_Rabi ~= 10 MHz at mod_depth = 1 and tau = 52 ns:

P_flip = sin^2(pi * 10e6 * 52e-9) = 0.996.

The expected fluorescence contrast for a fully driven m_S = 0 to m_S = +1 transition is therefore about

0.22 * 0.996 = 0.219, or 21.9%.

The mean raw readout level is about 49.45, so an on-resonance signal should change by about

49.45 * 0.219 = 10.84 raw-readout units

relative to the m_S = 0 reference, with the signal readout lower than the reference for a normal ODMR fluorescence contrast.

Observed data:

- Mean readout 1: 49.459.
- Mean readout 2: 49.448.
- Mean signal-reference difference readout2 - readout1: -0.011.
- Standard deviation of readout2 - readout1 across scan points: 1.505.
- Most negative point in readout2 - readout1: -2.788.
- Most positive point in readout2 - readout1: +2.712.

Thus the largest observed negative deviation is only about 5.6% of the readout level and about one quarter of the expected resonant pi-pulse contrast. There is no localized dip or contrast feature near the expected 22% scale. The two stored averages are not treated as independent proof because stored averages can reflect tracking cadence, but they also do not show a stable resonance-scale feature.

Decision: resonance_absent.
