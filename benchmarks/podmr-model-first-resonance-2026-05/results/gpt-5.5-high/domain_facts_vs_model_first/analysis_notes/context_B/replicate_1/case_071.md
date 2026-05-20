Case: podmr_057_2026-05-17-051839

Inputs used only from this isolated workspace:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png for visual cross-check only

Sequence identification:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional mS = +1 reference block is not executed.
- Readout 1 role: the first detection immediately after optical polarization, i.e. the mS = 0 bright reference for each frequency point.
- Readout 2 role: the detection after the microwave rabi_pulse_mod_wait_time block, i.e. the pODMR signal readout.
- mod_depth: actual run value is 1, consistent between inputs/sequence.xml and raw_export.json Variable_values. The sequence text embedded in raw_export.json contains an older default of 0.3, but the exported actual variable value is 1.
- Microwave pulse duration: length_rabi_pulse = 52 ns. At sample_rate = 250 MHz, the 4 ns clock rounding leaves 52 ns exactly.

Quantitative physical model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the 52 ns pulse is essentially a pi pulse because 1/(2 f_R) = 50 ns.
- For a square pulse, the transferred population versus detuning delta is modeled as:
  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2))
  using f_R and delta in cycles/s.
- With t = 52 ns and f_R = 10 MHz:
  - delta = 0 MHz: P = 0.996
  - delta = 5 MHz: P = 0.749
  - delta = 10 MHz: P = 0.273
- With the provided contrast scale of 22%, the expected fractional change in the post-pulse signal relative to the mS = 0 reference is -0.22 * P(delta).
- The mean readout-1 level is 45.455 counts, so the expected signal-reference change is about:
  - -9.96 counts on resonance
  - -7.49 counts at 5 MHz detuning
  - -2.73 counts at 10 MHz detuning
- Since the scan grid is 5 MHz, any resonance inside the scan range should put at least one sampled point very close to resonance, normally producing a large negative readout2-readout1 feature of order 7 to 10 counts.

Observed data:
- Mean readout 1 = 45.455 counts.
- Mean readout 2 = 45.420 counts.
- Mean readout2-readout1 = -0.035 counts.
- Standard deviation of readout2-readout1 across frequency points = 0.985 counts.
- Most negative combined point: -2.077 counts at 3.925 GHz, ratio readout2/readout1 = 0.955.
- This largest observed decrease is only about 4.5%, far below the expected about 22% on-resonance contrast for this pulse and mod_depth.
- The observed excursions also alternate in sign and do not show the broad coherent square-pulse response expected around a resonance.
- Stored averages were not treated as a strong repeatability test, consistent with the prompt; they were used only as secondary context.

Decision:
The expected pODMR resonance for the active 52 ns, mod_depth 1 pulse would be a large post-pulse readout suppression relative to the initial mS = 0 reference. The measured signal does not contain a suppression of the required amplitude or shape anywhere in the scanned frequency range. Therefore the pODMR resonance is absent.
