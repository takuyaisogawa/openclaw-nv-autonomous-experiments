Case: podmr_070_2026-05-17-082720

Inputs used:
- Sequence XML: inputs/sequence.xml
- Raw export: inputs/raw_export.json
- Raw readout plot: inputs/raw_readouts.png

Active sequence and readout roles:
- SequenceName in the raw export is Rabimodulated.xml.
- The active instruction path has full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- The first readout is acquired immediately after adj_polarize, before the swept microwave pulse. It is the bright m_S = 0 / true 0-level reference.
- The second readout is acquired after one rabi_pulse_mod_wait_time pulse, so it is the post-pulse signal readout.
- do_adiabatic_inversion is true in the variables, but no adiabatic inversion is executed because the only active post-reference manipulation is rabi_pulse_mod_wait_time.
- Provided sequence XML parameters: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The 52 ns pulse is unchanged by sample-rate rounding because 52 ns is exactly 13 samples at 250 MHz.

Physical model calculation:
- Given setup contrast between m_S = 0 and m_S = +1: C = 0.22.
- Given Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: tau = 52 ns.
- For a resonant rectangular Rabi pulse, transferred population is modeled as P_1 = sin^2(pi f_R tau).
- f_R tau = 10e6 * 52e-9 = 0.52 cycles.
- P_1 = sin^2(pi * 0.52) = 0.9961.
- Expected fractional fluorescence change on resonance is approximately -C * P_1 = -0.2191, or a 21.9% drop in the post-pulse readout relative to the m_S = 0 reference.
- The mean reference readout is 50.71 counts, so the expected on-resonance drop is 50.71 * 0.2191 = 11.11 counts.

Observed quantitative comparison:
- Scan: 3.825 GHz to 3.925 GHz in 5 MHz steps, 21 points.
- Mean reference readout: 50.71.
- Mean post-pulse readout: 50.23.
- Post-minus-reference differences: mean -0.48 counts, sample standard deviation 1.19 counts, minimum -1.96 counts, maximum +1.69 counts.
- Fractional post-minus-reference differences range from -3.87% to +3.28%.
- The largest observed reduction, -1.96 counts at 3.885 GHz, is only about 17.6% of the 11.11-count drop expected for a resonant 52 ns, mod_depth 1 pulse in this setup.
- The per-average traces show similar small, drifting variations; stored averages are not treated as an independent repeatability test because they can reflect tracking cadence.

Decision:
The active sequence should produce a large post-pulse fluorescence dip if a pODMR resonance is within the scanned range. The observed signal lacks a dip of the expected scale and instead shows only low-percent readout fluctuations comparable to point-to-point noise and drift. Therefore I decide that a pODMR resonance is absent.
