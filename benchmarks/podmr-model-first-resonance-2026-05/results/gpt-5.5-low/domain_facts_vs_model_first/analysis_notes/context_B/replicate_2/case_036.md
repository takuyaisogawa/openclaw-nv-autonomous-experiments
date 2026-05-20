Case: podmr_021_2026-05-16-171244

I used only the provided sequence XML and raw export for this case.

Active sequence and readout roles:
- SequenceName: Rabimodulated.xml / provided sequence.xml.
- The active scan variable is mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- full_expt = 0, so the "Acquire 1 level reference" block is disabled.
- Readout 1 is the initial reference detection after adj_polarize, intended as the true m_S = 0 bright reference.
- Readout 2 is the detection after a single rabi_pulse_mod_wait_time pulse.
- mod_depth = 1 in the provided sequence XML variable values.
- length_rabi_pulse = 5.2e-08 s. At sample_rate = 250 MHz this is already exactly 13 samples, so rounding leaves 52 ns.

Physical model calculation:
- Given Rabi frequency f_R = 10 MHz at mod_depth = 1 and linear scaling with mod_depth, the active pulse has f_R = 10 MHz.
- For a resonant rectangular Rabi pulse, the transition probability is P = sin^2(pi * f_R * tau).
- With tau = 52 ns, f_R * tau = 0.52 cycles and P = sin^2(pi * 0.52) = 0.9961.
- With the setup contrast scale of about 22%, an on-resonance pODMR feature should reduce fluorescence by C * P = 0.22 * 0.9961 = 0.2191, or about 21.9% of the bright readout.
- The mean readout-1 bright reference is 46.49 raw counts, so the expected on-resonance depression is about 46.49 * 0.2191 = 10.19 raw-count units.

Quantitative comparison to data:
- Measured readout2 - readout1 values across the scan:
  [-0.08, -2.27, -0.06, -1.94, -1.37, -0.52, 1.40, 1.75, 0.40, 0.19, 1.52, -1.08, -1.19, -0.10, 0.71, 0.37, 1.62, -0.37, -1.37, -1.00, 1.81]
- The mean differential signal is -0.074 counts, with sample standard deviation 1.237 counts.
- The deepest observed differential value is -2.27 counts, far smaller than the approximately -10.19 counts expected for a resonant 52 ns pulse at mod_depth 1.
- Stored averages show large baseline drift/cadence structure, so I did not treat the two averages as an independent repeatability test. The combined differential readout is the relevant check against the sequence model.

Decision:
The expected resonant signal for the active pulse would be a large negative post-pulse fluorescence dip relative to the m_S = 0 reference. No such feature is present anywhere in the scanned frequency range. I therefore classify this case as resonance_absent.
