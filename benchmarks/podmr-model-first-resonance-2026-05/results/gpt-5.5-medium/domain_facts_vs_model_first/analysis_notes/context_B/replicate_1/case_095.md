<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_095.

Sequence interpretation:
- Active sequence: Rabimodulated.xml, varying mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the optional m_S = +1 reference block is inactive.
- Readout 1 is the bright m_S = 0 reference acquired immediately after optical polarization.
- Readout 2 is the signal readout acquired after the modulated Rabi pulse.
- mod_depth = 1 from the active variable values.
- length_rabi_pulse = 52 ns. At sample_rate = 250 MHz this is 13 samples, so rounding leaves it at 52 ns.

Quantitative expected-signal model:
- Given the setup Rabi frequency is about 10 MHz at mod_depth = 1 and scales linearly, the active Rabi frequency is about 10 MHz.
- For a square resonant pulse, the transferred population is P = sin^2(pi * f_Rabi * tau).
- With f_Rabi = 10 MHz and tau = 52 ns, P = sin^2(pi * 10e6 * 52e-9) = sin^2(1.6336) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so a resonant point should reduce readout 2 relative to readout 1 by about 0.22 * 0.996 = 0.219, or about 21.9%.
- On a typical 47-count readout baseline this is an expected dip of about 10.3 raw-count units.

Data comparison:
- The observed fractional drop (readout1 - readout2) / readout1 has maximum value 4.52%, at 3.905 GHz.
- The observed readout2 - readout1 range is only -2.15 to +1.69 raw-count units.
- The mean fractional drop is 0.48% with a point-to-point standard deviation of 2.75%.
- Several adjacent points alternate in sign, and there is no feature approaching the expected 21.9% resonance contrast.
- Stored averages show a similar global tracking offset structure rather than a reproducible narrow pODMR dip, so they do not provide a strong independent repeatability check.

Decision:
The expected resonant response for the active 52 ns, mod_depth 1 Rabi pulse is much larger than the observed readout difference. The data do not show a pODMR resonance.
