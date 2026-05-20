Case podmr_081_2026-05-17-110558

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional +1 reference block is skipped. do_adiabatic_inversion is set but is inside the skipped block and does not define the active measurement here.
- Readout 1 is the true m_S = 0 reference: adj_polarize followed directly by detection.
- Readout 2 is the signal readout after the active modulated Rabi pulse, followed by detection.
- The active pulse is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1. At a 250 MHz sample rate this pulse remains 13 samples, 52 ns.

Physics/context check:
- With the provided setup facts, mod_depth = 1 corresponds to about a 10 MHz Rabi frequency, so a 52 ns pulse is approximately a pi pulse and should give a substantial on-resonance transfer if the scan crosses a driven transition.
- The stated m_S = 0 to m_S = +1 contrast scale is about 22%, so a convincing resonance under this pulse condition should be much larger and more structured than a few-percent fluctuation.

Data assessment:
- The combined readouts both drift downward across the scan, consistent with tracking/baseline changes.
- Normalizing the signal readout against the 0-reference readout gives small, sign-changing contrast excursions. The combined (readout1 - readout2) / readout1 values span about -3.7% to +4.5%, with no coherent resonance-shaped dip or peak across adjacent frequency points.
- The largest apparent contrast points are isolated and alternate in sign with nearby points. The two stored averages are strongly offset in baseline, consistent with tracking cadence rather than a robust independent repeatability test.

Decision:
No pODMR resonance is present. The observed changes are too small compared with the expected contrast for a near-pi pulse at mod_depth = 1 and lack a coherent frequency-dependent resonance shape.
