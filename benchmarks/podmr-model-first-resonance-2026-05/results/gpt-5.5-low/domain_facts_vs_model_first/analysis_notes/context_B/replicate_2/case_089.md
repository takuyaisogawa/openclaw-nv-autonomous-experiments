Case: podmr_075_2026-05-17-093901

I used only the provided sequence XML and raw export. The active sequence is Rabimodulated.xml with mw_freq swept from 3.825 GHz to 3.925 GHz in 5 MHz steps. The XML sequence first calls adj_polarize and detection, so readout 1 is the polarized m_S = 0 reference. Because full_expt = 0, the conditional explicit m_S = 1 reference block is skipped. The active signal operation is then one rabi_pulse_mod_wait_time call followed by detection, so readout 2 is the signal after the modulated microwave pulse.

Sequence parameters relevant to the model:
- length_rabi_pulse = 52 ns
- mod_depth = 1
- current contrast scale between m_S = 0 and m_S = +1: about 22%
- Rabi frequency at mod_depth = 1: about 10 MHz

Explicit expected-signal calculation:
For a resonant square Rabi pulse, the transferred population is modeled as

P_1 = sin^2(pi * f_Rabi * tau).

With f_Rabi = 10 MHz and tau = 52 ns,
f_Rabi * tau = 0.52 cycles, so
P_1 = sin^2(pi * 0.52) = 0.996.

The expected fractional optical change at resonance is therefore approximately
0.22 * 0.996 = 0.219, i.e. about a 21.9% decrease of the signal readout relative to the m_S = 0 reference if the microwave frequency is resonant with the addressed transition. The mean readout 1 level is 50.523 raw units, giving an expected resonant drop of about
50.523 * 0.219 = 11.07 raw units.

Observed readout comparison:
- mean(readout 1) = 50.523
- mean(readout 2) = 50.390
- mean(readout2 - readout1) = -0.133 raw units
- most negative readout2 - readout1 point = -2.442 raw units at 3.830 GHz
- scan-to-scan standard deviation of the combined differences = 1.187 raw units
- median per-average disagreement scale for the difference trace = about 1.061 raw units

The observed readout-2 darkening is far smaller than the approximately 11 raw-count drop expected from a near-pi pulse at mod_depth = 1. The largest negative excursion is only about 22% of the expected resonant signal and appears as an isolated fluctuation rather than a clear pODMR dip. Other points even show readout 2 brighter than readout 1. Stored averages are not treated as an independent repeatability test because they can reflect tracking cadence.

Decision: resonance_absent. The physical model predicts a large negative contrast feature for a true resonance under this pulse condition, and the measured data do not contain such a feature.
