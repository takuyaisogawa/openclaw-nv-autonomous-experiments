Analysis note for podmr_043_2026-05-16-231159

Input sequence identification:
- Sequence name in the export: Rabimodulated.xml.
- Active sequence behavior: full_expt = 0, so the optional "1 level reference" branch is skipped.
- Readout roles:
  - readout 1 is the initial polarized m_S = 0 bright reference after adj_polarize and detection.
  - readout 2 is the measurement after the Rabi-modulated microwave pulse and detection.
- Relevant pulse parameters from the provided workspace XML / variable values:
  - varied parameter: mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
  - mod_depth = 1.
  - length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
  - full_expt = 0, so there is no independent dark-state reference readout in this scan.

Quantitative physical model:
The setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth. For a resonant square pulse of duration t = 52 ns, the transferred population is modeled as

P_transfer = sin^2(pi * f_Rabi * t)

With f_Rabi = 10 MHz:

P_transfer = sin^2(pi * 10e6 * 52e-9) = 0.996

Using the stated m_S = 0 to m_S = +1 contrast scale of about 22%, a resonant point should reduce the signal readout relative to the m_S = 0 reference by

contrast * P_transfer = 0.22 * 0.996 = 0.219

So the expected resonant signal/reference ratio is about 0.781. The observed mean reference readout is 47.11 raw units, so the expected absolute resonant drop is about

47.11 * 0.219 = 10.32 raw units

Data comparison:
- Mean readout 1: 47.11.
- Mean readout 2: 47.55.
- Mean readout2/readout1 ratio: 1.009.
- Minimum readout2/readout1 ratio across the scan: 0.976 at 3.885 GHz.
- Ratio standard deviation across scan points: 0.020.
- The most negative readout2 - readout1 difference is -1.19 raw units, far smaller than the expected approximately -10.3 raw-unit resonant drop.
- At every scan point, readout 2 remains about 9.3 to 12.3 raw units above the modeled resonant signal level expected from the local readout 1 reference.

Decision:
The active sequence should produce a large darkening of readout 2 at resonance because the pulse is essentially a pi pulse at mod_depth = 1. The measured readout 2 does not show a 22% dip relative to the m_S = 0 reference; it stays near or above the reference with only small scatter. Therefore this scan does not contain a pODMR resonance.
