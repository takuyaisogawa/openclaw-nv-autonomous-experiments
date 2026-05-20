Case: podmr_041_2026-05-16-224136

Sequence interpretation from inputs/sequence.xml:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional "Acquire 1 level reference" block is skipped.
- Readout 1 role: after adj_polarize and before the microwave pulse, a polarized m_S = 0 reference.
- Readout 2 role: after one rabi_pulse_mod_wait_time pulse, the pODMR signal readout.
- Active pulse: rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on).
- mod_depth = 1.
- length_rabi_pulse = 52 ns. At 250 MS/s this is already on the 4 ns sample grid.

Quantitative model:

The setup facts give f_Rabi ~= 10 MHz at mod_depth = 1. For a rectangular microwave pulse, the driven transition probability versus detuning delta is

P(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * t * sqrt(f_Rabi^2 + delta^2)).

With t = 52 ns and f_Rabi = 10 MHz:
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With 22% optical contrast between m_S = 0 and m_S = +1, the expected resonant readout-2/readout-1 dip is 0.22 * 0.996 = 0.219, about 21.9%.
- The mean readout-1 level is 46.35 counts, so the expected resonant raw drop is about 10.16 counts.

Data check:
- Mean readout 1 = 46.354 counts.
- Mean readout 2 = 46.142 counts.
- Mean readout2/readout1 = 0.9955.
- Minimum readout2/readout1 = 0.9437 at 3.895 GHz, a 5.6% dip from the local m_S = 0 reference.
- Minimum raw difference readout2 - readout1 = -2.596 counts, also at 3.895 GHz.

Model comparison on normalized ratios readout2/readout1:
- A flat null model has SSE = 0.01924.
- Fitting the rectangular-pulse detuning lineshape with free center and free dip amplitude gives best center 3.8902 GHz and fitted dip amplitude 0.0526, far below the expected 0.219.
- Forcing the physically expected 22% contrast scale and fitting only center and offset gives SSE = 0.06122, worse than the flat null model by 0.04199.

Decision:

The active XML pulse is effectively a pi pulse at the stated Rabi rate, so a real pODMR resonance should produce a deep, structured dip of roughly 10 counts. The observed fluctuations are only a few counts and the expected 22% lineshape is rejected by the data relative to a flat trace. I therefore classify this case as resonance_absent.
