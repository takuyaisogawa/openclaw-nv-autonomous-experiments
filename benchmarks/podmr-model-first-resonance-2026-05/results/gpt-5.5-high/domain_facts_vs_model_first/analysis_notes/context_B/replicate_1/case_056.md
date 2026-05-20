Sequence and readout interpretation

The provided sequence is Rabimodulated.xml. The active scan variable is mw_freq over 3.825 to 3.925 GHz with 21 points. The variable values in the supplied XML/export are length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, and full_expt = 0. Because full_expt is zero, the optional m_S = +1 reference block is inactive. The active readouts are therefore:

- readout 1: after adj_polarize and detection, a true m_S = 0 reference.
- readout 2: after the modulated Rabi pulse and detection, the pODMR signal readout.

Physical model calculation

Use a driven two-level square-pulse model. The setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, approximately linear in mod_depth, so here f_R = 10 MHz. For a pulse of duration tau = 52 ns, the on-resonance transition probability is

P1(0) = sin^2(pi f_R tau)
      = sin^2(pi * 10e6 * 52e-9)
      = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance pi-like pulse should reduce the Rabi-probed readout by

0.22 * 0.996 = 0.219,

or about 21.9% relative to the m_S = 0 reference. At the observed count level near 47 counts, that is roughly a 10-count dip in readout 2 relative to readout 1.

For finite detuning, I used

P1(df) = (f_R^2 / (f_R^2 + df^2)) * sin^2(pi * tau * sqrt(f_R^2 + df^2)).

If a resonance were centered at 3.875 GHz, this predicts readout2/readout1 = 0.781 at line center and about 0.835 at +/-5 MHz, with the side structure set by the 52 ns square pulse.

Data comparison

The measured normalized contrast y = (readout1 - readout2) / readout1 has:

- maximum positive dip: 0.052 at 3.840 GHz.
- value at 3.875 GHz: 0.040.
- mean contrast over the scan: -0.0035.
- minimum contrast: -0.063, where readout 2 is higher than readout 1.

The readout traces share a slow downward drift, so readout1 normalization is important. After normalization there is no feature approaching the 21.9% dip expected for a resonant 52 ns pulse at mod_depth = 1. A grid fit of the square-pulse line shape with free center and amplitude gives a best amplitude of only 0.021 fractional contrast, about 9.5% of the expected 0.22 contrast scale, and this fit is not materially better than a no-resonance/flat explanation. The stored averages both show the general tracking-like drift and do not provide a strong independent repeatability test.

Decision

The relevant physical model predicts a large pi-pulse ODMR dip if the scan crosses resonance, but the measured normalized readout difference contains only small percent-level fluctuations and common drift. I therefore decide that a pODMR resonance is absent.
