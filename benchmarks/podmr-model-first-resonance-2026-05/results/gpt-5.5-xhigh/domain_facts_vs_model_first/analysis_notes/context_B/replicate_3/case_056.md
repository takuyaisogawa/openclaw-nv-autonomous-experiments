Case: podmr_042_2026-05-16-225623

Input files used: inputs/sequence.xml and inputs/raw_export.json.

Active sequence and readout roles:
- The active sequence is Rabimodulated.xml, scanning mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- In the sequence, the first detection occurs immediately after polarization and is labeled as the true 0 level reference. This is readout 1.
- The conditional "Acquire 1 level reference" block is inactive because full_expt = 0, so it does not produce an active stored readout.
- The active microwave manipulation is then PSeq = rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This post-pulse signal is readout 2.
- mod_depth = 1. The pulse duration is length_rabi_pulse = 52 ns; at sample_rate = 250 MHz this is 13 samples, so the rounded duration remains 52 ns.

Physical model calculation:
- The given setup has Rabi frequency about 10 MHz at mod_depth = 1, and the active sequence uses mod_depth = 1, so f_R = 10 MHz.
- For a rectangular driven two-level pulse, the transition probability versus detuning is

  P(delta) = f_R^2 / (f_R^2 + delta^2) * sin^2(pi * tau * sqrt(f_R^2 + delta^2))

  with tau = 52 ns and frequencies in cycles/s.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- The setup contrast between m_S = 0 and m_S = +1 is about 22%, so the expected on-resonance normalized post-pulse readout is

  readout2 / readout1 = 1 - 0.22 * P(0) = 0.7809.

- With readout 1 near 46 to 47 counts, this is an expected raw drop of about 10 counts at resonance.
- Model ratios at representative detunings are:
  - delta = 0 MHz: 0.7809
  - delta = 5 MHz: 0.8353
  - delta = 10 MHz: 0.9400
  - delta = 15 MHz: 0.9974

Observed normalized data:
- The measured readout2/readout1 ratios have mean 1.0035 and standard deviation 0.0302.
- The minimum ratio in the combined data is 0.9479 at 3.840 GHz, corresponding to only a 5.2% apparent drop.
- At 3.875 GHz the ratio is 0.9597, a 4.0% apparent drop.
- The raw readouts both show a common downward drift with frequency, and the post/reference ratio does not show a resonance-sized dip.
- The per-average traces are not treated as a strong independent repeatability test because stored averages can reflect tracking cadence. They also do not show a stable near-22% post-pulse loss.

Decision:
An in-range pODMR resonance under this active pulse should produce a large post-pulse fluorescence reduction, roughly readout2/readout1 = 0.78 near the resonance and still a strong dip if the resonance falls between adjacent 5 MHz scan points. The observed normalized data never approach that level and are consistent with drift/noise-level variations rather than the expected near-pi-pulse response. Therefore I decide that a pODMR resonance is absent.
