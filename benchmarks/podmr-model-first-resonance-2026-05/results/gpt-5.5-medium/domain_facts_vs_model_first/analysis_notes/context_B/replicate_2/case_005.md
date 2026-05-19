<!-- Model-generated analysis note. Not a ground-truth label. -->

Case case_005

Inputs used: inputs/sequence.xml and inputs/raw_export.json only.

Active sequence and readout roles:
- Sequence: Rabimodulated.xml.
- The sequence first polarizes the NV, then calls detection before any microwave pulse. This is the bright m_S = 0 reference readout, so readout 1 is the reference.
- full_expt = 0, so the optional "1 level reference" block is skipped. do_adiabatic_inversion is therefore inactive for the recorded two-readout measurement.
- The active experimental pulse is rabi_pulse_mod_wait_time(PSeq, sample_rate, length_rabi_pulse, mod_depth, switch_delay, ch_on), followed by detection. This makes readout 2 the post-microwave-pulse signal readout.
- length_rabi_pulse = 5.2e-08 s = 52 ns.
- mod_depth = 1 from the provided sequence XML and the exported variable values.

Physical model:
- Given f_Rabi = 10 MHz at mod_depth = 1, the resonant Rabi frequency for this sequence is approximately 10 MHz.
- For a square pulse of duration t = 52 ns, the transition probability at detuning Delta is modeled as:
  P(Delta) = (f_Rabi^2 / (f_Rabi^2 + Delta^2)) * sin^2(pi * sqrt(f_Rabi^2 + Delta^2) * t),
  using frequencies in cycles per second.
- On resonance, P(0) = sin^2(pi * 10e6 * 52e-9) = 0.996.
- With the stated 22% bright/dark contrast, a real resonant response should reduce the post-pulse readout by about 0.22 * 0.996 = 0.219, i.e. about a 22% dip relative to the m_S = 0 reference.
- Representative expected normalized post-pulse signals 1 - 0.22 P(Delta):
  Delta = 0 MHz: 0.781
  Delta = +/-5 MHz: 0.835
  Delta = +/-10 MHz: 0.940
  Delta = +/-15 MHz: 0.997
  Delta = +/-20 MHz: 0.989

Observed comparison:
- I compared readout 2 to readout 1 using the ratio readout2/readout1 across the 3.825 to 3.925 GHz scan.
- The ratio mean is 0.988. The deepest point is 0.881 at 3.840 GHz, only an approximately 12% dip, and other negative excursions occur at several separated frequencies rather than as one resonance-shaped feature.
- A one-center fit of ratio = baseline - A * P(f - f0), allowing A to float, gives the best center at the scan edge, 3.925 GHz, with A = 0.083. This is far below the physically expected A near 0.22.
- A fixed 22% contrast model fits worse than a constant baseline: SSE = 0.0813 for the fixed physical model versus SSE = 0.0642 for a constant ratio.
- The per-average traces show strong opposite slow drift between stored averages, so the stored averages mainly reflect tracking cadence and do not provide a strong independent repeatability check.

Decision:
The expected resonance for the active 52 ns, mod_depth 1 pulse should be a large, localized approximately 22% post-pulse dip. The measured readout ratios show only smaller, scattered excursions and do not match the required quantitative line shape. I therefore classify this case as resonance_absent.
