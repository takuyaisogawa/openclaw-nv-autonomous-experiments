Case: podmr_060_2026-05-17-060259

Sequence inspection:
- Active sequence: Rabimodulated.xml / Rabimodulated pODMR frequency scan.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional 1-level reference branch is inactive.
- Readout 1 role: true 0-level reference after optical polarization and before the Rabi pulse.
- Readout 2 role: signal readout after the modulated Rabi pulse.
- mod_depth = 1 from the provided sequence XML variable values.
- length_rabi_pulse = 52 ns, rounded at 250 MS/s but unchanged because 52 ns is 13 samples.

Physical model calculation:
- Given Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly with mod_depth.
- For a resonant square Rabi pulse, transition probability is P = sin^2(pi * f_Rabi * mod_depth * tau).
- With f_Rabi = 10 MHz, mod_depth = 1, and tau = 52 ns:
  P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between mS = 0 and mS = +1 is about 22%, so an on-resonance pODMR feature should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219, or roughly 21.9%.
- Around a 50-count raw-readout baseline, the expected on-resonance drop is about 10.96 counts in readout 2 relative to the 0-reference readout.

Data comparison:
- Combined readout 1 mean: 50.943.
- Combined readout 2 mean: 50.197.
- Mean paired difference readout2 - readout1: -0.746 counts.
- Standard deviation of paired differences across scan points: 1.507 counts.
- Largest paired drop is -3.635 counts at 3.875 GHz, corresponding to a readout2/readout1 ratio of 0.931.
- This largest observed drop is only about 7% of the local reference and far below the approximately 22% drop expected for a resonant 52 ns pi pulse.
- Neighboring points do not show a strong isolated pODMR-scale dip, and stored averages are only two averages, which mainly reflect tracking cadence rather than a strong repeatability test.

Decision:
The expected resonant signal from the active pulse sequence is large, about an 11-count drop, but the observed differences are small and comparable to point-to-point scatter. Therefore this dataset does not show a pODMR resonance.
