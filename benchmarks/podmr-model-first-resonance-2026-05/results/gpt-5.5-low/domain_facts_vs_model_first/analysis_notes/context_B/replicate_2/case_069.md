Case: podmr_055_2026-05-17-045046

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Sequence identification:
- SequenceName in the export is Rabimodulated.xml.
- The active instructions polarize, detect the bright m_S = 0 reference, wait, skip the nominal m_S = +1 reference block because full_expt = 0, apply one rabi_pulse_mod_wait_time pulse, then detect the post-microwave signal.
- Thus readout 1 is the m_S = 0 bright reference and readout 2 is the post-Rabi-pulse pODMR readout.
- Active pulse duration is length_rabi_pulse = 52 ns. With sample_rate = 250 MHz this is already an integer 13 samples, so rounding does not change it.
- mod_depth from the provided sequence XML and exported Variable_values is 1.

Physical model calculation:
- Given f_Rabi = 10 MHz at mod_depth = 1 and approximately linear scaling, the active Rabi frequency is 10 MHz.
- For a resonant square pulse, transferred population is P = sin^2(pi * f_Rabi * t).
- With t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance fractional fluorescence drop is 0.22 * 0.996 = 0.219, or 21.9%.
- The measured bright-reference level is about 43.81 raw-count units, so the expected resonant drop is about 43.81 * 0.219 = 9.60 raw-count units.

Observed quantitative comparison:
- Mean readout 1 = 43.81, mean readout 2 = 43.45.
- Mean readout2 - readout1 = -0.37 raw-count units.
- Standard deviation of the pointwise differences across the scan = 1.61 raw-count units.
- Deepest pointwise drop is -2.62 raw-count units, ratio 0.941, at 3.850 GHz; a similarly deep drop occurs at 3.880 GHz.
- Some frequencies show positive readout2 - readout1 differences up to +3.19 raw-count units.

Decision:
The expected resonant signature for the active 52 ns, mod_depth 1 pulse is a large approximately 22% drop, about 9.6 raw-count units. The observed changes are much smaller, fluctuate in both signs, and do not form a clear pODMR resonance. Stored averages are treated cautiously because they can reflect tracking cadence rather than an independent repeatability test. I therefore decide resonance_absent.
