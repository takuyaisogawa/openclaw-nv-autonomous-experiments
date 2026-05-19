<!-- Model-generated analysis note. Not a ground-truth label. -->

Case: case_007

Input sequence inspection:

- Sequence file: Rabimodulated.xml.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active sequence first optically polarizes and detects the true mS = 0 level.
- full_expt = 0, so the optional mS = +1 reference block is skipped.
- The active signal operation is a single rabi_pulse_mod_wait_time call followed by detection.
- Therefore readout 1 is the mS = 0 optical reference/tracking readout, and readout 2 is the microwave-pulse pODMR signal readout.
- The active rabi pulse duration is length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is exactly 13 samples, so the rounded duration remains 52 ns.
- The provided sequence XML variable value is mod_depth = 1.

Quantitative physical model:

Use the given setup Rabi frequency of about 10 MHz at mod_depth = 1, with approximately linear scaling. For this sequence, mod_depth = 1, so f_R = 10 MHz. For a resonant square Rabi pulse of duration t, the transferred population is

    P(+1) = sin^2(pi * f_R * t).

With t = 52 ns:

    P(+1) = sin^2(pi * 10e6 * 52e-9) = 0.996.

The setup contrast scale between mS = 0 and mS = +1 is about 22%, so a resonant point should show about

    0.22 * 0.996 = 0.219

fractional reduction in the signal readout, essentially the full available contrast. Using the off-resonance readout-2 edge baseline from the combined data, mean(readout 2 at 3.825, 3.830, 3.835, 3.840, 3.915, 3.920 GHz) = 22.1506. The expected resonant drop is

    22.1506 * 0.219 = 4.8539

so the expected resonant minimum is about 17.30 raw-readout units.

Observed data:

- Readout 2 has its minimum at 3.880 GHz with value 16.9808, very close to the model expectation of about 17.30.
- The readout-2 edge baseline is 22.1506, while the mean over 3.865 to 3.885 GHz is 18.0269, a drop of 4.1237 units or 18.6%.
- The single-point deepest drop from the edge baseline is 5.1699 units or 23.3%, consistent with the expected near-full 22% contrast given noise and baseline/tracking drift.
- Readout 1, the reference/tracking readout, does not show an equivalent narrow full-contrast dip at the same frequency; its same center-window reduction is only 1.4064 units and is not the active pODMR signal channel.
- The per-average traces show strong drift/tracking cadence, so I treat them as tracking context rather than an independent repeatability test.

Decision:

The active pulse is a near-pi pulse at the stated mod_depth, so a real resonance should produce nearly the full setup contrast in readout 2. The observed readout-2 dip centered near 3.88 GHz has the expected magnitude and channel role. I decide that a pODMR resonance is present.
