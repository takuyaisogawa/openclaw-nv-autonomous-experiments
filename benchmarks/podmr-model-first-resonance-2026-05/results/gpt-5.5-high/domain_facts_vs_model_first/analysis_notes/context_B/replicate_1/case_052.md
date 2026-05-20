Case podmr_038_2026-05-16-214551

Active sequence and readout roles:
- The saved scan sequence is Rabimodulated.xml with vary_prop = mw_freq, scanned from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The executed variables give length_rabi_pulse = 52 ns, mod_depth = 1, sample_rate = 250 MHz, full_expt = 0, and do_adiabatic_inversion = 1.
- Because full_expt = 0, the conditional "Acquire 1 level reference" block is skipped. The active readouts are therefore:
  1. readout 1: after adj_polarize and detection, a bright m_S = 0 reference.
  2. readout 2: after the modulated Rabi pulse and detection, the pODMR signal readout.

Physical model calculation:
- The setup Rabi frequency is about 10 MHz at mod_depth = 1.
- For a rectangular pulse, the transition probability versus detuning is modeled as
  P(delta) = (f_R^2 / (f_R^2 + delta^2)) * sin^2(pi * t * sqrt(f_R^2 + delta^2)),
  using f_R in cycles/s and t = 52 ns.
- On resonance this gives P(0) = sin^2(pi * 10 MHz * 52 ns) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, the expected normalized signal drop at resonance is 0.22 * 0.996 = 21.9%.
- At +/-5 MHz detuning, the same model gives P = 0.749 and an expected drop of 16.5%; at +/-10 MHz it gives an expected drop of 6.0%. Thus a real resonance inside the scan should produce a broad, multi-point dip in readout 2 relative to readout 1, with a deepest point near 22% below the local reference.

Measured comparison:
- I normalized the signal readout by the reference readout at each scan point: readout2/readout1.
- The measured ratios have mean 0.9930, standard deviation 0.0251, minimum 0.9401, and maximum 1.0399.
- The largest apparent drop is only 5.99% at 3.845 GHz, followed by 4.71% at 3.850 GHz; this is much smaller than the approximately 21.9% on-resonance drop expected for the active 52 ns, mod_depth 1 pulse.
- A fixed-contrast Rabi model q = A * (1 - 0.22 * P(delta)) was fit over candidate resonance frequencies. Its best sum of squared residuals was 0.06164, worse than the flat normalized model sum of squared residuals 0.01256.
- Allowing the dip amplitude to float gives a best fractional dip amplitude of only about 4.9% of baseline, far below the expected 22% physical contrast for this pulse.

Decision:
The data do not show the quantitatively expected pODMR response for the active pulse sequence. The small ratio variations are more consistent with noise and tracking-scale drift than with a true resonance driven by a near-pi pulse. I therefore classify this case as resonance_absent.
