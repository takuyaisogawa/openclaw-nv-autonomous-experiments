<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_003

Sequence interpretation

The active sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps. In the provided sequence XML, full_expt = 0, so the optional m_S = +1 reference block is skipped. The two recorded readouts therefore have these roles:

- readout 1: after adj_polarize and detection, a true m_S = 0 fluorescence reference.
- readout 2: after a Rabi-modulated microwave pulse and detection, the pODMR signal readout.

The active microwave pulse is:

- mod_depth = 1.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s, still 52 ns.
- The current setup Rabi frequency is about 10 MHz at mod_depth = 1.

Physical model calculation

For a square microwave pulse with Rabi frequency f_R = 10 MHz and pulse length t = 52 ns, the excited-state transfer probability versus detuning delta is:

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

On resonance this gives:

P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.

With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected resonant fractional fluorescence drop in readout 2 relative to readout 1 is:

0.22 * 0.996 = 0.219, or about 21.9%.

Data comparison

Using the combined raw readouts, the readout-2/readout-1 fractional drops are localized around 3.875 to 3.885 GHz:

- 3.875 GHz: readout 1 = 44.423, readout 2 = 40.462, drop = 8.9%.
- 3.880 GHz: readout 1 = 47.923, readout 2 = 40.538, drop = 15.4%.
- 3.885 GHz: readout 1 = 48.154, readout 2 = 41.885, drop = 13.0%.

The deepest point is at 3.880 GHz. A least-squares fit of the square-pulse detuning model to the ratio readout2/readout1, allowing baseline and amplitude to float, gives a best center near 3.8796 GHz and an effective contrast amplitude of about 12.5% relative to baseline. This is smaller than the ideal 21.9% but has the expected sign, location, and width for a near-pi pODMR pulse. The stored two averages show similar cadence-scale structure and are not treated as a strong independent repeatability test.

Decision

The quantitative square-pulse model predicts a resonance dip for this sequence, and the measured normalized data show a localized dip centered near 3.88 GHz with the correct sign and a substantial fraction of the expected contrast. I decide that a pODMR resonance is present.
