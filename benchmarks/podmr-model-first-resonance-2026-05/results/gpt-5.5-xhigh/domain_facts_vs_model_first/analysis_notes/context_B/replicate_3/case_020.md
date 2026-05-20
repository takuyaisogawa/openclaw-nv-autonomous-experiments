Case: podmr_005_2026-05-16-010352

I used only the provided XML sequence and the raw readout export in this isolated workspace.

Sequence interpretation:

- Active sequence: Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instruction flow is:
  1. adj_polarize
  2. detection
  3. wait
  4. rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth)
  5. detection
  6. final wait
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- Readout 1 is therefore the laser-polarized m_s = 0 reference readout with no preceding microwave pulse.
- Readout 2 is the signal readout after the Rabi-modulated microwave pulse.
- mod_depth = 1.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is exactly 13 samples after rounding.

Physical model calculation:

The provided setup facts give a Rabi frequency of about 10 MHz at mod_depth = 1, and the sequence uses mod_depth = 1, so f_R = 10 MHz. For a square microwave pulse of duration t = 52 ns, I modeled the transition probability versus detuning df as:

P(df) = f_R^2 / (f_R^2 + df^2) * sin^2(pi * t * sqrt(f_R^2 + df^2))

Using the provided contrast scale of 22%, the expected normalized signal readout is:

readout2/readout1 = 1 - 0.22 * P(df)

On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(0.52*pi) = 0.996. The expected on-resonance ratio is therefore 1 - 0.22 * 0.996 = 0.781, i.e. a 21.9% drop from the m_s = 0 reference.

Observed normalized signal:

- At 3.875 GHz: readout1 = 40.962, readout2 = 30.635, ratio = 0.748, drop = 25.2%.
- At 3.880 GHz: readout1 = 39.192, readout2 = 30.327, ratio = 0.774, drop = 22.6%.
- At 3.885 GHz: ratio = 0.862, drop = 13.8%.
- Away from the central dip, excluding 3.865 to 3.885 GHz, the mean ratio is 0.976 with standard deviation 0.036.

A grid fit of the same square-pulse model to the normalized readout found a best center near 3.8785 GHz, with fitted baseline 0.989 and fitted contrast scale 0.234. That fitted contrast is close to the expected 0.22 scale, and the fixed 22% model also places the best center at 3.8785 GHz.

The dip is also present in both stored averages: the two averages give 3.875 GHz contrasts of about 22.1% and 27.8%. I treat this as supportive only, since stored averages can reflect tracking cadence rather than an independent repeatability test.

Decision:

The active pulse is essentially a pi pulse at the expected Rabi rate, so a true pODMR resonance should produce a roughly 22% decrease in the post-pulse readout relative to the m_s = 0 reference. The measured readout2/readout1 dip near 3.875-3.880 GHz is 22-25%, localized in frequency, and quantitatively consistent with that model. I therefore decide that a pODMR resonance is present.
