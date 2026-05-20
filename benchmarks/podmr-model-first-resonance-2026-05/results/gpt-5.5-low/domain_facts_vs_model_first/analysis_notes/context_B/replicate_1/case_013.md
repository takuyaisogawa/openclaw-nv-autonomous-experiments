Case podmr_032_2026-05-14-161051

The sequence is Rabimodulated.xml. The active instruction path is:

1. adj_polarize followed by detection: this is the true m_S = 0 optical reference, corresponding to readout 1.
2. full_expt = 0, so the optional m_S = +1 reference block is skipped.
3. rabi_pulse_mod_wait_time followed by detection: this is the microwave-driven pODMR readout, corresponding to readout 2.

Relevant active parameters from the saved sequence/export:

- scanned variable: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps
- length_rabi_pulse: 52 ns
- mod_depth: 1
- setup Rabi frequency estimate: 10 MHz at mod_depth = 1
- contrast scale between m_S = 0 and m_S = +1: about 22%

Quantitative expected-signal model:

For a square resonant Rabi pulse, the population transfer probability is

P = sin^2(pi * f_Rabi * tau)

with f_Rabi = 10 MHz and tau = 52 ns. This gives:

P = sin^2(pi * 10e6 * 52e-9) = 0.996

The expected fluorescence ratio at resonance is therefore approximately

readout2 / readout1 = 1 - 0.22 * P = 0.781

At a typical readout-1 level of about 34 counts, the expected resonant drop is

34 * 0.22 * 0.996 = 7.45 counts.

Including detuning with

P(delta) = (f_Rabi^2 / (f_Rabi^2 + delta^2)) * sin^2(pi * tau * sqrt(f_Rabi^2 + delta^2))

predicts a narrow dip over the few scan points nearest resonance. For a center at 3.880 GHz, the expected readout2/readout1 ratios are approximately 0.835 at +/-5 MHz and 0.781 on resonance, rising toward about 0.94 by +/-10 MHz.

Measured combined readouts:

- mean readout 1: 34.055
- mean readout 2: 33.429
- minimum readout2/readout1 ratio: 0.822 at 3.880 GHz
- at 3.880 GHz: readout 1 = 35.654, readout 2 = 29.308, drop = -6.346 counts
- excluding the central candidate region, the readout2-readout1 difference has mean about -0.075 counts and standard deviation about 1.586 counts; the 3.880 GHz drop is about 4 sigma below this background difference scale.

The observed central drop at 3.880 GHz is close to the expected near-pi-pulse contrast for a real resonance. Adjacent points are noisy and stored averages mainly reflect tracking cadence, so I do not treat the per-average traces as a strong independent repeatability test. Still, the active sequence makes readout 2 the driven readout, and the measured central suppression has the correct sign, approximate magnitude, and frequency-localized character expected from the physical model.

Decision: resonance_present.
