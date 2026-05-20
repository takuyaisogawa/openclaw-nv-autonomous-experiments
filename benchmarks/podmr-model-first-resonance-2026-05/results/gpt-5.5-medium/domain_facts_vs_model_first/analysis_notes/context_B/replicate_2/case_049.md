Case podmr_035_2026-05-16-210045 analysis

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active pulse sequence and readout roles:
- Sequence name in the export is Rabimodulated.xml.
- The instruction block first polarizes the NV and performs detection. This is the true m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = +1 reference branch is skipped.
- The active signal operation is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This second readout is therefore the signal readout after the Rabi pulse.
- The provided sequence XML sets length_rabi_pulse = 5.2e-08 s, mod_depth = 1, sample_rate = 250 MHz. The pulse length is already an integer number of 4 ns samples, so the rounded pulse duration remains 52 ns.

Physical model calculation:
- Given domain fact: Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For a resonant square Rabi pulse, transferred population to m_S = +1 is P1 = sin^2(pi * f_Rabi * t).
- With f_Rabi = 10 MHz and t = 52 ns:
  P1 = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The setup contrast scale between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance PL drop in the post-pulse signal readout is:
  0.22 * 0.996 = 0.219, or about 21.9%.
- For a typical 50-count readout, this corresponds to about 10.96 counts lower signal at resonance relative to the m_S = 0 reference.

Observed quantitative comparison:
- Combined readout 1 mean: 50.936.
- Combined readout 2 mean: 50.084.
- Mean readout2 - readout1: -0.852 counts, only about -1.7% of the readout level.
- Minimum observed readout2/readout1 ratio is 46.846 / 49.654 = 0.943 at 3.830 GHz, a 5.7% loss.
- Another local low ratio is 48.077 / 50.846 = 0.946 at 3.865 GHz, a 5.4% loss.
- No point approaches the model expectation of roughly a 21.9% PL drop, and the lows are isolated among comparable scatter and slow drift. The first reference readout itself drifts upward across the scan, so raw signal level changes are not a clean resonance feature.
- Stored averages are not treated as a strong independent repeatability test because they can reflect tracking cadence.

Decision:
The active 52 ns, mod_depth 1 Rabi pulse should produce an almost full contrast-scale dip if a pODMR resonance were present in the scanned range. The observed normalized changes are far smaller and not a coherent resonance-sized feature. I therefore decide that the pODMR resonance is absent.
