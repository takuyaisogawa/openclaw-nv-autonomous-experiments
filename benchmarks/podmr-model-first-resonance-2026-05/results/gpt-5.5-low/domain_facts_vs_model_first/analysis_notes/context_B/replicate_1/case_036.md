Case: podmr_021_2026-05-16-171244

Inputs used:
- inputs/sequence.xml
- inputs/raw_export.json
- inputs/raw_readouts.png as a visual check only

Active sequence and readout roles:
- Sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the conditional "Acquire 1 level reference" block is inactive.
- The active detections are therefore:
  1. readout 1: pre-microwave bright m_S = 0 reference after optical polarization.
  2. readout 2: post-microwave signal after the Rabi-modulated pulse.
- mod_depth = 1 from the provided sequence/variable values.
- length_rabi_pulse = 52 ns. With sample_rate = 250 MHz, this is already on the 4 ns grid.

Physical model calculation:
- Given Rabi frequency about 10 MHz at mod_depth = 1 and linear scaling with mod_depth, use f_Rabi = 10 MHz.
- For a square resonant pulse, transferred population is P = sin^2(pi * f_Rabi * tau).
- With tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so an on-resonance post-pulse readout should be:
  readout2/readout1 = 1 - 0.22 * 0.996 = 0.781.
- Around the measured mean readout1 of 46.49 counts, this predicts an on-resonance dip of about 10.19 counts.

Observed data comparison:
- Mean readout1 = 46.49, mean readout2 = 46.41, mean ratio readout2/readout1 = 0.999.
- The lowest observed ratio is 0.953 at 3.830 GHz, corresponding to only a 2.27 count decrease.
- Ratios elsewhere are often above 1, and no scan point approaches the modeled resonance ratio near 0.781.
- Stored averages mainly show slow tracking/cadence changes, so they are not treated as independent resonance repeats.

Decision:
The active pODMR channel should show a large post-pulse fluorescence dip if resonance is present, but the measured post/pre ratio remains near unity with only small fluctuations. Therefore this case is resonance_absent.
