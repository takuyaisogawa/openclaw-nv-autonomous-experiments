Case podmr_043_2026-05-16-231159

Inputs used
- Active sequence: Rabimodulated.xml / Rabimodulated sequence, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- Sequence instructions: polarize, detect true mS=0 reference, wait; the mS=1 reference block is disabled because full_expt = 0; then apply rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth), detect, wait.
- Readout roles: readout 1 is the reference/readout after optical polarization to mS=0; readout 2 is the signal readout after the microwave Rabi pulse. Since full_expt = 0, there is no separate acquired mS=1 reference.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s to 52 ns.
- mod_depth: the provided sequence.xml lists mod_depth = 1. The embedded saved sequence text in raw_export.json lists mod_depth = 0.3, while Variable_values lists mod_depth = 1. I evaluated both; the weaker saved-sequence value is the conservative expected-signal case.

Physical model calculation
- Setup Rabi frequency scale: 10 MHz at mod_depth = 1, linear in mod_depth.
- For a resonant square pulse, transition probability P = sin^2(pi * f_Rabi * t), where f_Rabi is in cycles/s and a pi pulse occurs at t = 1/(2 f_Rabi).
- At mod_depth = 1: f_Rabi = 10 MHz, t = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996. With 22% mS=0 to mS=+1 contrast, the expected resonant PL reduction is 0.219 of the bright signal, about 10.3 raw-count units for a 47.1 count baseline.
- At mod_depth = 0.3: f_Rabi = 3 MHz, t = 52 ns, P = sin^2(pi * 3e6 * 52e-9) = 0.222. With 22% contrast, the expected resonant PL reduction is 0.0487 of the bright signal, about 2.3 raw-count units for a 47.1 count baseline.

Observed data check
- Combined readout 1: mean 47.11, standard deviation 0.74, min 45.90, max 49.12.
- Combined readout 2: mean 47.55, standard deviation 0.96, min 45.75, max 49.44.
- Signal-reference difference readout2 - readout1: mean +0.44, standard deviation 0.95, min -1.19, max +1.87.
- The strongest negative signal-reference point is only -1.19 counts, below even the conservative expected resonant dip magnitude of about -2.3 counts, and it is not a clean localized feature. Near several candidate frequencies the signal readout is higher than the reference, the opposite of the expected ODMR/Rabi transfer contrast.
- The per-average traces differ by offsets and tracking-like changes; stored averages are not treated as an independent repeatability test.

Decision
The quantitative model predicts a negative PL dip of about 2.3 counts even under the conservative mod_depth=0.3 interpretation, and much larger if mod_depth=1 is active. The measured readout pair does not show a localized negative dip of that sign and scale. I therefore classify this case as resonance_absent.
