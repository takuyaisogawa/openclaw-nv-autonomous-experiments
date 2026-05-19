<!-- Model-generated analysis note. Not a ground-truth label. -->

Active-sequence analysis for case_033

The provided sequence is Rabimodulated.xml. The active acquisition path is:

1. adj_polarize
2. detection
3. wait_for_awg
4. optional +1 reference block, skipped because full_expt = 0
5. rabi_pulse_mod_wait_time
6. detection
7. wait_for_awg

Thus readout 1 is the optically polarized m_S = 0 reference. Readout 2 is the signal after the microwave Rabi-modulated pulse. There is no active independent m_S = +1 reference in this run because full_expt is zero.

The sequence parameters used for the physical model are:

- mod_depth = 1
- length_rabi_pulse = 52 ns
- sample_rate = 250 MHz, so 52 ns is exactly 13 samples after rounding
- microwave scan = 3.825 to 3.925 GHz in 5 MHz steps

Physical signal model:

The setup Rabi frequency is about 10 MHz at mod_depth = 1, scaling linearly with mod_depth. For a square resonant pulse, the transferred population is modeled as

P_flip = sin^2(pi * f_Rabi * tau).

With f_Rabi = 10 MHz and tau = 52 ns:

P_flip = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected resonant fractional PL drop is

0.22 * 0.996 = 0.219, or about 21.9%.

The mean readout-1 level is 48.07 counts, so the expected resonant count drop is

48.07 * 0.219 = 10.53 counts.

Observed data calculation:

Using the fractional contrast C = (readout1 - readout2) / readout1 at each microwave frequency, the largest contrast is at 3.875 GHz:

- readout1 = 49.269
- readout2 = 39.769
- observed drop = 9.50 counts
- observed fractional contrast = 0.193

An off-resonant baseline estimated from the eight lowest-contrast scan points is -0.010, giving a peak excess contrast of 0.203.

A least-squares Lorentzian model

C(f) = baseline + amplitude / (1 + ((f - f0) / gamma)^2)

fits the contrast data with:

- baseline = 0.0048
- amplitude = 0.2047
- center = 3.8765 GHz
- gamma = 7.0 MHz
- R^2 versus a constant model = 0.736

Decision:

The expected resonant signal for the active pulse is a near-full contrast drop of about 21.9% or 10.5 counts. The observed readout-2 depression is localized near 3.875 to 3.88 GHz and has fitted amplitude about 20.5%, with a 9.5 count drop at the strongest point. This is quantitatively consistent with a pODMR resonance from the active pulse model, while the stored two averages are treated only as limited cadence information rather than a strong independent repeatability test.

Prediction: resonance_present.
