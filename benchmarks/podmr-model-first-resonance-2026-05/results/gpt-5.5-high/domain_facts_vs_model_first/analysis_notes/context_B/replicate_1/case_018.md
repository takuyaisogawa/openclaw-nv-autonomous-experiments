Case: podmr_003_2026-05-16-003531

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml.
- The active instructions first polarize the NV and detect the polarized level. This is readout 1, the mS = 0 reference.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive. There is no independent mS = +1 reference readout in this run.
- The active experiment pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This is readout 2, the post-Rabi-pulse fluorescence.
- mod_depth = 1 from the provided sequence file and exported variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse length remains 13 samples = 52 ns.

Quantitative expected-signal model:
The stated setup has Rabi frequency about 10 MHz at mod_depth = 1, with approximately linear scaling. Therefore f_R = 10 MHz for this sequence. I modeled the square pulse transfer probability versus frequency detuning as:

P_{+1}(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * tau)

with tau = 52 ns. On resonance this gives:

P_{+1}(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996.

Using the stated mS = 0 to mS = +1 contrast scale of about 22%, the expected resonant readout-2 fluorescence loss is:

0.996 * 0.22 = 0.219, or about 21.9% of the local fluorescence level.

For a baseline of about 37 counts, the expected resonant dip is about:

37 * 0.219 = 8.1 counts.

The same model predicts a broad response over the 5 MHz scan spacing:
- Delta = 0 MHz: transfer 0.996, expected dip fraction 21.9%, about 8.1 counts.
- Delta = 5 MHz: transfer 0.749, expected dip fraction 16.5%, about 6.1 counts.
- Delta = 10 MHz: transfer 0.273, expected dip fraction 6.0%, about 2.2 counts.
- Delta = 15 MHz: transfer 0.012, expected dip fraction 0.3%, about 0.1 counts.

Observed data:
- Scan range: 3.825 to 3.925 GHz in 5 MHz steps.
- Readout 1 mean is 37.42 counts, with population-reference-like fluctuations but no sharp collapse at the dip center.
- Readout 2 off-resonance baseline, excluding 3.865 to 3.885 GHz, is 36.77 counts.
- Readout 2 minimum is 28.06 counts at 3.880 GHz.
- The observed dip depth is 36.77 - 28.06 = 8.72 counts, or 23.7% of the off-resonance readout-2 baseline.
- The minimum readout-2/readout-1 ratio is 0.702 at 3.880 GHz.

I also fit readout 2 to a linear fluorescence model y = a + b * P_{+1}(f - f0), scanning f0. The best center was about 3.878 GHz, with a = 37.28 counts, b = -8.92 counts, corresponding to an effective contrast of 23.9%. This is very close to the expected 22% contrast for a nearly resonant pi pulse. The model fit residual sum of squares was 42.1 versus 173.3 for a flat baseline, so the resonance-shaped model explains most of the structured variation.

Decision:
The post-pulse readout contains a dip with the expected sign, magnitude, and width for the active 52 ns modulated Rabi pulse. Because the sequence's readout 2 is the physical post-pulse measurement and the predicted contrast-scale signal is quantitatively present, I decide that a pODMR resonance is present.
