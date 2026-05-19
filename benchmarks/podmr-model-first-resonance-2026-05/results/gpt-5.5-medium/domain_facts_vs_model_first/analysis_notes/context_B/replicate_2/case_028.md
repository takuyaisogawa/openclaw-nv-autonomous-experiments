<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_028

I used the supplied sequence XML and raw export only. The active sequence is Rabimodulated.xml. The instruction block first performs adj_polarize followed by detection, so readout 1 is the true m_S = 0 fluorescence reference. The m_S = +1 reference block is inside if abs(full_expt)>1e-12, and full_expt is 0, so that block is inactive. The second active detection occurs after PSeq = rabi_pulse_mod_wait_time(PSeq,sample_rate,length_rabi_pulse,mod_depth,switch_delay,ch_on), so readout 2 is the signal after the Rabi-modulated microwave pulse.

Relevant pulse parameters from the provided XML/export variable values:
- length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth = 1 from inputs/sequence.xml and Variable_values.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.

Physical model calculation:
For a square driven two-level pulse with Rabi frequency f_R and detuning Delta, the excited-state transfer probability is

P(Delta) = (f_R^2 / (f_R^2 + Delta^2)) * sin^2(pi * t * sqrt(f_R^2 + Delta^2)).

The setup facts give f_R about 10 MHz at mod_depth = 1. With t = 52 ns, the resonant transfer is

P(0) = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.

Using the stated m_S = 0 to m_S = +1 contrast scale of 22%, the expected on-resonance normalized fluorescence dip is 0.22 * 0.996 = 0.219, or about 21.9%. For a baseline near 43 counts/readout, the expected resonant signal is about 43 * (1 - 0.219) = 33.6.

Observed quantitative comparison:
- Readout 2 baseline excluding the central dip points is 43.06 with standard deviation 1.16.
- The minimum readout 2 value is 34.08 at 3.880 GHz.
- The absolute dip is 8.98 counts, or 20.9% of the baseline.
- Normalized by readout 1, the deepest ratio contrast is 21.9% at 3.875 GHz, and the adjacent point at 3.880 GHz is 20.9%.
- A simple fit of readout2 = a - b * P(Delta) with mod_depth = 1 gives best center about 3.878 GHz, fitted fractional contrast b/a about 22.6%, and SSE 20.7 versus 179.8 for a flat model.

This matches the expected resonance amplitude, frequency-localized line shape, and contrast scale from the active pulse sequence. The two stored averages both show the same central dip qualitatively, but I treat that only as supporting context because stored averages can reflect tracking cadence rather than independent repeatability.

Decision: resonance_present.
