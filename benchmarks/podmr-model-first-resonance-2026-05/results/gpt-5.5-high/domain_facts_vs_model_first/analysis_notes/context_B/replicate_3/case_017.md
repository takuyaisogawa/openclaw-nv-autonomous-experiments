Free-form analysis note

Inputs used:
- sequence XML: inputs/sequence.xml
- raw data export: inputs/raw_export.json
- diagnostic plot: inputs/raw_readouts.png

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt is 0, so the optional "Acquire 1 level reference" block is skipped. do_adiabatic_inversion is therefore not used in the active path.
- Readout 1 is the first detection immediately after adj_polarize, so it is the bright m_S = 0 reference.
- Readout 2 is the detection after rabi_pulse_mod_wait_time, so it is the pODMR signal after the swept MW pulse.
- The provided sequence XML sets length_rabi_pulse = 52 ns and mod_depth = 1; raw_export Variable_values also reports mod_depth = 1.

Quantitative physical model:
- Setup contrast scale between m_S = 0 and m_S = +1: C = 0.22.
- Rabi frequency at mod_depth = 1: f_R = 10 MHz.
- Pulse duration: t = 52 ns.
- On-resonance transfer model: P_1(0) = sin^2(pi f_R t).
- Calculation: P_1(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- Expected on-resonance PL ratio, before allowing a small baseline scale factor, is 1 - C * P_1(0) = 1 - 0.22 * 0.996 = 0.781.
- For detuning delta, I used the square-pulse two-level response
  P_1(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * t * sqrt(f_R^2 + delta^2)).

Data comparison:
- The measured readout2/readout1 ratio has off-central mean 0.978 with standard deviation 0.048 when excluding indices 9 through 12.
- Around the feature:
  - 3.870 GHz: ratio 0.885
  - 3.875 GHz: ratio 0.763
  - 3.880 GHz: ratio 0.707
  - 3.885 GHz: ratio 0.901
- The deepest normalized dip is at 3.880 GHz: readout1 = 38.115, readout2 = 26.962, ratio = 0.707. Relative to the off-central ratio mean, this is a 0.271 absolute ratio drop.
- A fixed physical line model using f_R = 10 MHz, C = 0.22, and t = 52 ns, with only resonance frequency and a multiplicative baseline scale fitted, gives best f0 = 3.8774 GHz, baseline scale = 0.986, SSE = 0.0477.
- A constant no-resonance ratio model gives SSE = 0.1513, so the physical resonance model reduces SSE to 31.6 percent of the no-resonance model.
- Stored averages are not treated as an independent repeatability proof, but both averages show their deepest normalized suppression in the same central region: average 1 at 3.875 GHz and average 2 at 3.880 GHz.

Decision:
The observed central dip has the correct readout role, frequency-localized shape, and amplitude scale for the 52 ns, mod_depth = 1 pODMR pulse. Its depth is at least as large as the approximately 22 percent expected contrast-scale dip from the quantitative Rabi model, and it is much better explained by the physical resonance response than by a no-resonance baseline. I therefore decide that a pODMR resonance is present.
