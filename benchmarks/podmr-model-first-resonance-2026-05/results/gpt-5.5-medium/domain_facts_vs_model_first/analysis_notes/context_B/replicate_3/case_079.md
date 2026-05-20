Case podmr_065_2026-05-17-071421

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated pODMR with mw_freq swept from 3.825 to 3.925 GHz in 5 MHz steps.
- Readout 1 role: after adj_polarize and before any microwave pulse, so it is the optically polarized m_S = 0 fluorescence reference for each scan point.
- full_expt = 0, so the optional separate m_S = +1 reference block is skipped.
- Readout 2 role: fluorescence after rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay), so this is the microwave-pulse signal readout.
- Relevant pulse settings from the provided XML: length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz. The rounded pulse duration remains 52 ns because 52 ns * 250 MHz = 13 samples.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the active pulse has f_R = 10 MHz.
- For a square resonant pulse, transition probability P_1 = sin^2(pi * f_R * t).
- With t = 52 ns, P_1 = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- With a setup contrast scale of 22%, the expected on-resonance fluorescence reduction in readout 2 relative to readout 1 is 0.22 * 0.996 = 0.219, so the expected readout2/readout1 ratio at resonance is about 0.781 before allowing for baseline scaling.

Data comparison:
- Combined readout2/readout1 ratios across the scan are:
  0.967, 0.952, 0.958, 0.988, 0.975, 1.010, 1.043, 1.006, 1.008, 1.006, 1.007, 0.990, 1.039, 0.957, 0.966, 0.998, 0.985, 1.028, 0.997, 1.014, 0.989.
- The minimum observed ratio is 0.952, corresponding to only about a 4.8% reduction, far smaller than the approximately 21.9% reduction expected for this near-pi pulse on resonance.
- The ratio scatter is about 0.025 RMS and includes both positive and negative excursions, consistent with drift/tracking and noise rather than a resolved ODMR dip.
- A fixed-physics square-pulse resonance model with 22% contrast improves the residual sum of squares only modestly when placed outside or near the scan edge, and no scan point shows the expected large resonant depletion.

Decision:
No pODMR resonance is present in this scan under the active sequence and expected signal scale.
