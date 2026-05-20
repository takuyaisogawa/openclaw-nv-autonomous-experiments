Case podmr_006_2026-05-11-020739.

Sequence identification:
- The active sequence is Rabimodulated.xml, swept over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML sets full_expt = 0, so the "Acquire 1 level reference" block is inactive.
- The active readout roles are therefore:
  - readout 1: laser-polarized m_S = 0 reference, with no preceding microwave pulse.
  - readout 2: signal readout after one rabi_pulse_mod_wait_time pulse.
- The active microwave pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is 13 samples, so rounding leaves it at 52 ns.
- mod_depth = 1 in the provided sequence XML and exported variable values.

Quantitative model calculation:
- Given the supplied setup fact, f_Rabi is about 10 MHz at mod_depth = 1.
- For a rectangular pulse, the transition probability versus detuning is
  P(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * pulse_duration * sqrt(f_Rabi^2 + delta^2)),
  using cycle-frequency units for f_Rabi and delta.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With a 22% m_S = 0 to m_S = +1 contrast scale, a fully resonant pulse should therefore allow about
  0.22 * 0.996 = 0.219, or 21.9%, normalized readout contrast before allowing for background and imperfect collection.

Data reduction:
- I used the paired contrast y = (readout1 - readout2) / readout1 at each frequency.
- The largest contrasts are around 3.875 to 3.885 GHz:
  - 3.875 GHz: 0.089
  - 3.880 GHz: 0.154
  - 3.885 GHz: 0.130
- The two stored averages both show the strongest paired deficit near this region:
  - average 1 at 3.875/3.880/3.885 GHz: 0.136, 0.163, 0.163
  - average 2 at 3.875/3.880/3.885 GHz: 0.042, 0.146, 0.097
  These averages are not treated as a strong repeatability test because stored averages can reflect tracking cadence, but they are consistent with the combined feature.

Model fit:
- I fit y = baseline + amplitude * P(freq - f0), scanning f0 across the measured range and solving baseline/amplitude by least squares.
- Best center: f0 = 3.8796 GHz.
- Best baseline contrast: 0.0173.
- Best modeled resonant amplitude above baseline: 0.1228.
- Best peak modeled contrast: 0.1401, below the 0.219 ideal contrast but physically plausible for background dilution and imperfect contrast transfer.
- Sum of squared residuals for a flat contrast model: 0.05972.
- Sum of squared residuals for the finite-pulse Rabi model: 0.03479.
- The Rabi model reduces residual error by about 42% relative to a flat model.

Decision:
The paired readout contrast has a broad feature centered near 3.88 GHz with the width and scale expected for a 52 ns, mod_depth = 1 Rabi pulse. Because the active sequence compares an m_S = 0 reference against a post-microwave readout, and the observed feature quantitatively matches the finite-pulse response better than a flat model, I decide that a pODMR resonance is present.
