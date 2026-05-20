Case podmr_006_2026-05-11-020739

Sequence identification:
- Active sequence name in the export is Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The provided sequence XML has full_expt = 0, so the optional "Acquire 1 level reference" block is inactive despite do_adiabatic_inversion = 1. The active readouts are therefore:
  - readout 1: true m_S = 0 reference after laser polarization and detection.
  - readout 2: detection after one modulated Rabi microwave pulse.
- Active pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- length_rabi_pulse = 52 ns, sample_rate = 250 MHz, so rounding keeps 52 ns exactly.
- mod_depth = 1 in the provided XML variable values.

Explicit physical model calculation:
- Given setup Rabi frequency f_R approx 10 MHz at mod_depth = 1, and linear scaling with mod_depth, f_R = 10 MHz.
- For a resonant square pulse, excited-state transfer probability is modeled as P_1 = sin^2(pi f_R t), where f_R is the population oscillation frequency.
- With t = 52 ns: f_R t = 0.52 cycles and P_1 = sin^2(pi * 0.52) = 0.996.
- With setup m_S = 0 to m_S = +1 contrast scale about 22%, the expected resonant fluorescence reduction is 0.22 * 0.996 = 0.219, or about 21.9% of the readout-1 level. For readout levels around 47 counts, that corresponds to an ideal resonant drop of about 10.3 counts relative to the m_S = 0 reference.

Observed quantitative comparison:
- The combined data show readout 2 dipping near 3.875-3.885 GHz:
  - 3.875 GHz: readout1 = 44.423, readout2 = 40.462, normalized reduction = 8.9%.
  - 3.880 GHz: readout1 = 47.923, readout2 = 40.538, normalized reduction = 15.4%.
  - 3.885 GHz: readout1 = 48.154, readout2 = 41.885, normalized reduction = 13.0%.
- The average normalized reduction over those three points is 12.4%, while the other points average about 2.5% with a standard deviation of about 4.2%.
- The strongest observed reduction is smaller than the ideal 21.9% calculation, but a reduced apparent depth is plausible from detuning grid spacing, linewidth/power broadening, imperfect microwave coupling, tracking drift, and the fact that stored averages mostly reflect tracking cadence rather than independent repeatability.

Decision:
The active sequence should produce a negative pODMR feature in readout 2 relative to the m_S = 0 reference when the microwave frequency is resonant. The data contain a localized, multi-point normalized fluorescence loss centered around 3.88 GHz in the expected direction and with a magnitude compatible with a partial version of the modeled 21.9% ideal contrast. I therefore decide that a pODMR resonance is present.
