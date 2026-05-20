case_id: podmr_049_2026-05-17-004217
timestamp: 2026-05-17-004217

Input files used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- The sequence is Rabimodulated.xml / Rabimodulated.
- The scan varies mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The sequence performs an initial adj_polarize followed by detection. This is the first readout and is the m_S = 0 fluorescence reference.
- full_expt = 0, so the optional m_S = +1 reference block is skipped.
- The sequence then applies rabi_pulse_mod_wait_time(length_rabi_pulse, mod_depth, switch_delay) followed by detection. This is the second readout and is the pODMR signal after the microwave pulse.
- Provided sequence parameters identify length_rabi_pulse = 52 ns and mod_depth = 1. The sample-rate rounding at 250 MS/s leaves 52 ns unchanged.

Physical model calculation:
- Given the setup Rabi frequency of about 10 MHz at mod_depth = 1, the pulse has Omega_R = 10 MHz.
- For a square pulse starting from m_S = 0, the driven population transfer probability versus detuning is
  P(detuning) = (Omega_R^2 / (Omega_R^2 + detuning^2)) * sin^2(pi * t * sqrt(Omega_R^2 + detuning^2)),
  using frequencies in cycles/s.
- On resonance, t = 52 ns gives P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of about 22%, an on-resonance post-pulse readout should dip by 0.22 * 0.996 = 0.219 of the reference fluorescence, about 11 counts for a 50 count reference.
- Because the scan step is 5 MHz, any resonance inside the scanned interval is at most 2.5 MHz from a sampled point. At 2.5 MHz detuning the model gives P = 0.929, so the nearest sampled readout ratio should still be about 1 - 0.22 * 0.929 = 0.796 or lower relative to the m_S = 0 reference.
- Explicit simulation over possible resonance centers in the scanned interval gives an expected minimum sampled post-pulse/reference ratio between 0.781 and 0.796 for a resonance present in the scan.

Observed quantitative comparison:
- The measured readout1 mean is 49.856 counts and readout2 mean is 49.775 counts.
- The measured readout2/readout1 ratio has mean 0.9986, standard deviation 0.0292, and minimum 0.9487 at 3.850 GHz.
- The largest measured post-pulse depression relative to the reference is only 2.62 counts, far smaller than the roughly 10 to 11 count dip expected for a resonance with this pulse.
- A fixed-contrast resonance model fitted over resonance center with a multiplicative baseline gives its best center near 3.8508 GHz but still predicts a minimum ratio of about 0.810 and has RSS 0.0601 on the ratio data, worse than the no-resonance flat-ratio RSS of 0.0179.

Decision:
The active sequence is a near-pi-pulse pODMR probe, so a true resonance in the scan should produce a large, sampled fluorescence dip. The observed variations are small, tracking-like fluctuations around unity and do not match the required square-pulse resonance response. I therefore decide that no pODMR resonance is present in this scan.
