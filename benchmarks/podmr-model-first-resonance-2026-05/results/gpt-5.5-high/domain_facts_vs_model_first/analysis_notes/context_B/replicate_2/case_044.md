Case: podmr_030_2026-05-16-194429

Sequence interpretation:
- The provided XML is Rabimodulated.xml, scanned over mw_freq from 3.825 GHz to 3.925 GHz in 5 MHz steps.
- The active microwave pulse before the signal readout is rabi_pulse_mod_wait_time with length_rabi_pulse = 52 ns and mod_depth = 1.
- full_expt = 0, so the optional "1 level reference" block is skipped.
- Readout 1 is the first detection immediately after optical polarization, so it is the m_S = 0 / no-pulse reference.
- Readout 2 is the detection after the 52 ns Rabi-modulated microwave pulse, so it is the pODMR signal channel.

Physical model calculation:
- Given the setup, the Rabi frequency is approximately 10 MHz at mod_depth = 1.
- For a rectangular resonant pulse, the transferred population is
  P(d) = (Omega^2 / (Omega^2 + d^2)) * sin^2(pi * sqrt(Omega^2 + d^2) * t),
  using Omega and detuning d in cycles/s.
- With Omega = 10 MHz and t = 52 ns, Omega*t = 0.52, so on resonance
  P(0) = sin^2(pi * 0.52) = 0.996.
- With the stated m_S = 0 to m_S = +1 contrast scale of 22%, an on-resonance signal readout should be lower than the readout-1 reference by 0.22 * 0.996 = 21.9%, giving readout2/readout1 = 0.781.
- Expected ratios at representative detunings are:
  - 0 MHz: transfer 0.996, expected ratio 0.781
  - 2.5 MHz: transfer 0.929, expected ratio 0.796
  - 5 MHz: transfer 0.749, expected ratio 0.835
  - 10 MHz: transfer 0.273, expected ratio 0.940

Observed data:
- The combined readout2/readout1 ratios have mean 0.9987 and standard deviation 0.0239.
- The minimum combined ratio is 0.9473 at 3.895 GHz, corresponding to only a 5.3% dip.
- The combined minimum difference is readout2 - readout1 = -2.77 counts at 3.895 GHz, while a resonant pi-pulse-scale feature would be about 0.219 * 52.6 = 11.5 counts at that fluorescence level.
- The two stored averages do not provide a strong independent repeatability test because they can reflect tracking cadence. Even so, their lowest local ratios are small and shifted: average 1 has its minimum ratio at 3.895 GHz, while average 2 has its minimum ratio at 3.885 GHz.

Decision:
The active pulse should produce a large, broad pODMR dip if a resonance is present within this scan. The observed feature is much smaller than the expected pi-pulse contrast and is not a stable model-matched resonance, so I classify this case as resonance_absent.
