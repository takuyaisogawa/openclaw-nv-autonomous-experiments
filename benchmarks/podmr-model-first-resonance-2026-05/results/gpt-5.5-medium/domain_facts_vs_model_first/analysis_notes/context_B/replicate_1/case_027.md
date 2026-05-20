Case: podmr_012_2026-05-16-121601

I used only the provided sequence XML and raw export values for this decision.

Active sequence and readout roles:

- SequenceName is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The XML sets full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The executed sequence is: optical polarization, detection, wait, one modulated Rabi pulse, detection, final wait.
- Therefore readout 1 is the optically polarized m_S = 0 reference, and readout 2 is the post-microwave Rabi-pulse readout. The relevant resonance signal is a reduction in readout 2 relative to readout 1.
- mod_depth = 1 in the provided XML and in the exported variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MS/s, this is 13 samples and remains 52 ns after rounding.

Physical model calculation:

The provided setup scale is Rabi frequency about 10 MHz at mod_depth = 1, approximately linear in mod_depth. For a resonant rectangular pulse, the transfer probability is

P = sin^2(pi * f_R * t).

With f_R = 10 MHz and t = 52 ns:

P = sin^2(pi * 10e6 * 52e-9) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance readout reduction is about 0.22 * 0.996 = 21.9% of the local bright readout. For a baseline around 41.75 counts, this is about 9.15 counts. This is the expected ideal contrast-scale signal for a near-pi pulse; a somewhat smaller observed amplitude is plausible from imperfect addressing, finite linewidth, detuning, and normalization/readout effects.

I also evaluated the finite-detuning Rabi response:

P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

Fitting readout difference d = readout1 - readout2 to offset + amplitude * P(delta) over center frequencies gave:

- Best center: 3.8785 GHz.
- Fitted amplitude: 6.93 counts.
- Ideal amplitude from 22% contrast and off-resonance readout2 baseline: 9.19 counts.
- Off-resonance delta mean: 0.56 counts.
- Off-resonance delta scatter: 1.06 counts.
- Dip-region delta mean from 3.870 to 3.885 GHz: 5.93 counts.
- Maximum delta: 7.31 counts at 3.880 GHz, or 17.7% of readout 1.
- The Rabi lineshape model reduced the delta residual sum of squares by about 82% relative to an offset-only null model.

The stored two averages are not treated as a strong independent repeatability test, since averages can reflect tracking cadence. They do, however, show the same qualitative depression in readout 2 near the same frequency region, so they do not contradict the combined-readout result.

Decision:

The active sequence is a single near-pi Rabi pulse followed by readout, and the observed 3.87-3.885 GHz reduction in readout 2 has the correct sign, frequency-localized shape, and magnitude expected from the Rabi contrast model. I decide that a pODMR resonance is present.
