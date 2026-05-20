Case: podmr_017_2026-05-12-134151

Sequence identification:
- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The instructions first polarize the NV and immediately detect: this is the bright m_S = 0 reference readout.
- full_expt = 0, so the optional m_S = 1 reference block is inactive.
- The active pODMR signal block applies rabi_pulse_mod_wait_time, then detects again: this second readout is the microwave-after-pulse signal readout.
- The provided sequence XML has length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns, and mod_depth = 1. The raw export also contains an embedded saved sequence text showing mod_depth = 0.3, while its Variable_values list and the provided sequence.xml show mod_depth = 1. I evaluated both drive depths; the decision does not rely on the discrepancy.

Quantitative model:
- Given the stated setup, Rabi frequency is approximately 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For a rectangular resonant pulse, the transition probability is P(Delta) = Omega^2/(Omega^2 + Delta^2) * sin^2(pi * t * sqrt(Omega^2 + Delta^2)), with Omega in cycles/s.
- At mod_depth = 1: Omega = 10 MHz, t = 52 ns, so Omega*t = 0.52 cycles and on-resonance P = sin^2(pi*0.52) = 0.996. With 22% m_S=0 to m_S=+1 contrast, the expected on-resonance fluorescence drop in the post-pulse readout is about 0.22*0.996 = 21.9%. At +/-5 MHz detuning the model still predicts P = 0.749 and a 16.5% drop, so the feature should cover multiple adjacent 5 MHz scan points.
- At mod_depth = 0.3, for the alternate embedded value, Omega = 3 MHz and P(0) = sin^2(pi*0.156) = 0.222, giving an expected drop of about 4.9%. At +/-5 MHz the expected drop remains about 3.9%, so even this weaker case should not appear as only one isolated point.

Data check:
- Combined readout means are readout 1 = 22.70 and readout 2 = 22.77; there is no overall post-pulse depletion.
- The readout2/readout1 ratio has mean 1.005 and standard deviation 0.048. The lowest ratio is 0.913 at 3.855 GHz, but the adjacent ratios are 1.048 and 1.087, opposite to the expected multi-point resonant dip.
- The post-pulse readout alone at that point is 21.92, only about 1.1 below a linear trend, while the mod_depth = 1 model expects a roughly 5-count depletion near line center and still a large depletion in neighboring bins. Other low points of comparable size occur elsewhere without a resonant line shape.
- The stored averages show similar tracking-scale slopes and are not treated as independent repeatability evidence. The apparent feature is a one-bin fluctuation superposed on drift, not the expected pODMR response.

Decision:
The expected quantitative pODMR signal for the active 52 ns pulse is not present in the measured readouts. I classify this case as resonance_absent.
