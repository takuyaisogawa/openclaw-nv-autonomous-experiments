<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_020

Active sequence and readout roles:
- The provided sequence is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active pulse sequence first polarizes the NV and detects immediately. Because full_expt = 0, the optional separate m_S = +1 reference block is skipped. Therefore readout 1 is the bright/polarized reference for each scan point.
- The sequence then applies rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1, followed by detection. Therefore readout 2 is the post-microwave-pulse signal.
- The sample rate is 250 MHz, so 52 ns rounds to 13 samples and remains 52 ns.

Physical model calculation:
- Given setup facts: contrast between m_S = 0 and m_S = +1 is about 22%; Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- With mod_depth = 1, f_R = 10 MHz. For a resonant square pulse of duration t = 52 ns, the driven transfer probability is
  P = sin^2(pi f_R t) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The expected resonant PL drop in the post-pulse readout is therefore about 0.22 * 0.996 = 0.219, or 21.9%, relative to the bright readout baseline.
- Off resonance, using the detuned two-level square-pulse model
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  so the dip should be localized on the order of the 10 MHz Rabi frequency around the resonance, with oscillatory side response.

Data comparison:
- I used readout2/readout1 as the normalized signal because readout 1 is the same-cycle bright reference.
- The off-resonant baseline ratio from representative non-dip points is about 0.983.
- The minimum ratio is 0.748 at the 3.875 GHz scan point, with the adjacent 3.880 GHz point at 0.774. This corresponds to an observed dip of about 23.9% relative to baseline.
- A fixed-contrast Rabi model with contrast = 22%, f_R = 10 MHz, pulse length = 52 ns, and a fitted resonance center and multiplicative baseline gives best center about 3.8785 GHz and explains about 81% of the variance in the normalized ratios compared with a flat model.
- The deepest observed feature spans the expected resonance region and has the expected magnitude for a near-pi pulse. Stored averages are only two averages and may reflect tracking cadence, so I do not treat the per-average traces as a strong independent repeatability test, but both averages contribute to the same combined dip.

Decision:
The frequency-localized suppression of the post-pulse readout has the correct sign, location coherence over adjacent scan points, and quantitative amplitude for the 52 ns mod_depth = 1 Rabi pulse. A pODMR resonance is present.
