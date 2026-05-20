Case: podmr_080_2026-05-17-105113

Sequence identification:
- Sequence: Rabimodulated.xml / Rabimodulated active instructions.
- Vary parameter: mw_freq, 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 role: true m_S = 0 optical reference after polarization and detection, before the microwave pulse.
- Readout 2 role: signal readout after the modulated Rabi microwave pulse and detection.
- mod_depth = 1 from the provided sequence XML and exported variable values.
- Pulse duration: length_rabi_pulse = 52 ns, rounded at 250 MS/s; 52 ns is already exactly 13 samples.

Quantitative expected-signal model:
- Given setup Rabi frequency f_R = 10 MHz at mod_depth = 1.
- For a resonant square pulse, transferred population is P_1 = sin^2(theta/2), theta = 2*pi*f_R*t.
- With t = 52 ns: theta = 2*pi*10e6*52e-9 = 3.267 rad = 1.04*pi.
- P_1 = sin^2(3.267/2) = 0.996.
- Setup contrast between m_S = 0 and m_S = +1 is about 22%, so expected resonant fluorescence depletion is 0.22*0.996 = 0.219, or 21.9% of the reference readout.
- The measured readout 1 mean is 51.67 counts, so an on-resonance pODMR point should be near 51.67*(1 - 0.219) = 40.35 counts in readout 2, about 11.32 counts below readout 1.

Observed data comparison:
- Readout 1 mean: 51.67 counts.
- Readout 2 mean: 51.70 counts.
- Mean readout2 - readout1: +0.03 counts.
- Standard deviation of readout2 - readout1 across scan points: 0.88 counts.
- Minimum readout2 - readout1: -1.81 counts, far smaller than the expected about -11.3 count resonant depletion.
- The lowest readout 2 point is 50.17 counts at 3.915 GHz, but readout 1 there is 50.81 counts, only a 0.63 count relative drop.
- Stored averages show broad tracking offsets between averages, so they are not treated as independent confirmation. The combined readouts show no frequency-localized depletion with the expected sign and magnitude.

Decision:
The expected resonant response for the active pulse sequence is a large negative contrast in readout 2 relative to readout 1. The measured data are consistent with small noise/tracking fluctuations and do not contain a pODMR resonance.
