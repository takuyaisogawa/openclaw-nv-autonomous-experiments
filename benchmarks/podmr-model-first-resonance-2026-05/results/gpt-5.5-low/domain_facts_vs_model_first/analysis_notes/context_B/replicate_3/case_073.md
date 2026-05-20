Case: podmr_059_2026-05-17-054846

Sequence identification:
- The saved scan uses SequenceName Rabimodulated.xml and varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active instructions first polarize and detect, then wait, then run one rabi_pulse_mod_wait_time pulse, then detect again.
- full_expt = 0, so the optional "1 level reference" block is inactive despite do_adiabatic_inversion being true. Therefore readout 1 is the optically polarized m_S = 0 reference and readout 2 is the signal after the microwave pulse.
- Active pulse duration is length_rabi_pulse = 52 ns. mod_depth = 1. switch_delay = 100 ns.

Quantitative physical expectation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and approximately linear scaling, the relevant Rabi frequency is f_R = 10 MHz.
- For a resonant square pulse, the transferred population is modeled as P = sin^2(pi f_R t).
- With t = 52 ns, f_R t = 0.52 cycles, so P = sin^2(pi * 0.52) = 0.996.
- The stated setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant pulse should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219 of the m_S = 0 reference.
- The observed mean readout 1 baseline is 42.67 raw units, so the expected resonant readout-2 drop is about 42.67 * 0.219 = 9.35 raw units at resonance.

Data comparison:
- Mean readout 1 = 42.67; mean readout 2 = 42.11.
- Mean difference readout2 - readout1 = -0.56 raw units.
- The largest observed drop is at 3.880 GHz: readout 1 = 44.54, readout 2 = 41.67, drop = 2.87 raw units, ratio = 0.936.
- This largest drop is only about 6.4% of the local reference and about 31% of the expected 9.35-unit resonant drop.
- Neighboring points do not show a coherent contrast-sized resonance feature; the readouts fluctuate at the few-unit level and stored averages mostly track slow baseline changes, which is not a strong independent repeatability test.

Decision:
The pulse should act almost as a pi pulse on resonance, so a true pODMR resonance should be a large approximately 22% readout-2 suppression relative to readout 1. The measured scan contains only small, inconsistent readout differences far below that quantitative expectation. I decide resonance_absent.
