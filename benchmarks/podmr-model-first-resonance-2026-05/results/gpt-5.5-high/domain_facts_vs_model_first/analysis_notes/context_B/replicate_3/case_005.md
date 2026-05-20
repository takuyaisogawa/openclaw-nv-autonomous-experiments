Case podmr_008_2026-05-11-131831

Input used:
- Provided sequence XML: inputs/sequence.xml
- Raw readouts: inputs/raw_export.json

Active sequence and readout roles:
- Sequence: Rabimodulated.xml.
- The active variable scan is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is inactive.
- The first detection occurs immediately after optical polarization and is the bright mS = 0 reference readout.
- The second detection occurs after rabi_pulse_mod_wait_time and is the MW-pulse signal readout.
- mod_depth = 1 from the provided sequence XML and variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, the rounded pulse length remains 52 ns because it is 13 samples.

Physical model calculation:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1, the active pulse has f_R = 10 MHz.
- For a square pulse with detuning Delta, I used
  P1(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * sqrt(f_R^2 + Delta^2) * t),
  where t = 52 ns.
- On resonance, f_R * t = 0.52 cycles, so P1(0) = sin^2(pi * 0.52) = 0.996.
- With the stated mS = 0 to mS = +1 contrast scale of 22%, the expected resonant signal change is
  0.22 * 0.996 = 0.219, i.e. readout2/readout1 should fall to about 0.781 near resonance.
- Model contrast values are still large over nearby detunings: about 16.5% at 5 MHz detuning and 6.0% at 10 MHz detuning.

Data reduction:
- I evaluated the directly relevant contrast as (readout1 - readout2) / readout1.
- Across the 21 scan points, the measured contrast has mean 0.0122 and standard deviation 0.0566.
- The measured contrast ranges from -0.0615 to +0.1185.
- No point approaches the expected 21.9% resonant contrast for the active 52 ns, mod_depth 1 pulse.

Model comparison:
- A fixed 22% finite-pulse resonance model, allowing the resonance center to scan across the measured frequency range, gives best SSE 0.0841 in contrast units squared.
- A flat contrast model at the measured mean gives SSE 0.0642, better than the expected-resonance model.
- If the resonance model shape is allowed to fit an arbitrary positive amplitude and offset, the best amplitude is only 0.0833, about 38% of the expected 0.22 contrast scale, and the best center lands at the scan edge rather than producing a resolved in-band pODMR feature.

Decision:
- The active pulse should produce a large, easily visible pODMR dip if the resonance is present in the scan.
- The normalized readout contrast is small, sign-changing, and does not match the expected finite-pulse resonance response.
- I therefore classify this case as resonance_absent.
